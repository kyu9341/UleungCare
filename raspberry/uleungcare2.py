import get_sensor as sensor # communication with arduino
import sys
import requests #communication with web server
import json

import time #delay
from datetime import datetime

def rgb_control(ser,rgb_led):
	for i in range(0,3):
		ser.write(str(order)+'\n')

def remote_control(ser,order):
	ser.write(str(order)+'\n')


def main():
	print('connect arduino')
	while True: # wait arduino when didn't connected
		try:
			ser = sensor.set_dev()
			break
		except:
			print('no device')
			time.sleep(1)

	home_data = [0,0] # home data [temperature,light]
	past_remote_data = {} # check data chage
	past_rgb_led ={'ledThreshold':0,'red':0,'green':0,'blue':0}
	while True: # start main code

		print('get home data')
		now = datetime.now()
		data = sensor.get_data(ser) # get temperature & light

		try: # input data for trans to web server
			home_data = {'temperature':data[0],'light':data[1]}

		except: # wait arduino when home data didn't recive
			print('wait arduino')
			time.sleep(1)
			continue


		rs = requests.post('http://kyu9341.pythonanywhere.com/uleung/raspberry/',data=home_data)

		new_remote_data = rs.json() # recive new data
		#('tvOnOff', 0)
		#('airconOnOff', 0)
		#('tvChUpDown', 0)
		#('tvVolUpDown', 0)
		#('airconTempUpDown', 0)
		#('ledRed', 0)
		#('ledGreen', 0)
		#('ledBlue', 255)
		#('ledThreshold', 1)
		#('airconThreshold', 0)

		new_rgb_led = {'ledThreshold':new_remote_data['ledThreshold'],'red':new_remote_data['ledRed'],'green':new_remote_data['ledGreen'],'blue':new_remote_data['ledBlue']}

		print('time :',now)

		try:

		# if data didn't change pass this part
			if new_remote_data == past_remote_data:
				print('same data')

			else:
				print('data change')
				print('control...') # control code is here

				if new_rgb_led != past_rgb_led:
					print("led data change")
					order = '1 '+str(new_rgb_led['red'])+' '+str(new_rgb_led['green'])+' '+str(new_rgb_led['blue'])
					ser.write(order.encode())
				if(new_remote_data['tvOnOff'] != past_remote_data['tvOnOff']): 
					print('tv on off')

		except:
			es = sys.exc_info()[0]
			print('no data',es)



		for data in new_remote_data.items(): # print remote data
			print(data)

		past_remote_data = new_remote_data # data sync
		past_rgb_led = new_rgb_led
		print('\n')

main()
