import get_sensor as sensor # communication with arduino

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

		new_rgb_led = {'ledThreshold':new_remote_data['ledThreshold'],'red':new_remote_data['ledRed'],'green':new_remote_data['ledGreen'],'blue':new_remote_data['ledBlue']}

		print('time :',now)


		try:
			print('control...') # control code is here

			# if data didn't change pass this part
			if new_remote_data == past_remote_data:
				print('same data')

			else:
				print('data change')
		except:
			print('no data')



		for data in new_remote_data.items(): # print remote data
			print(data)

		past_remote_data = new_remote_data # data sync
		past_rgb_led = new_rgb_led

main()
