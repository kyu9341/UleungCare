import get_sensor as sensor  #communication with arduino

import requests
import json

import time
from datetime import datetime

class Home_info(): # home data class
	def __init__(self,temperature,light):
		self.temperature = temperature
		self.light = light
	def set_data(self,data1,data2):
		self.temperature = data1
		self.light = data2

	def set_temperature(slef,input_data):
		self.temperature = input_data

	def set_light(self,input_data):
		self.light = input_data

	def get_data(self):
		return self.temperature,self.light

	def get_temperature(self):
		return self.temperature

	def get_light(self):
		return self.light


class Remote_info(): # remote data super class
	def __init__(self,onoff,updown):
		self.onoff = onoff
		self.updown = updown

	def set_onoff(self,data):
		self.onoff = data

	def set_updown(self,data):
		self.updown = data

	def get_onoff(self):
		return self.onoff

	def get_updown(self):
		return self.updown

class Tv(Remote_info):
	def __init__(self,OnOff,ChUpDown,VolUpDown):
		super().__init__(OnOff,ChUpDown)
		self.VolUpDown = VolUpDown
	def set_VolUpDown(self,data):
		self.VolUpDown = data

	def get_VolUpDown(self):
		return self.VolUpDown

class aircon(Remote_info):
	def __init__(self,thleshold,OnOff,UpDown):
		super().__init__(OnOff,UpDown)
		self.thleshold = thleshold

class Led():
	def __init__(self,thleshold,R,G,B):
		self.red = R
		self.green = G
		self.blue = B
		self.thleshold = thleshold


	def set_rgb(self,rgb):
		red,green,blue = rgb

	def get_rgb(self):
		rgb=[self.red,self.green,self.blue]
		return rgb

	def set_thleshold(self,thleshold):
		self.thleshold = thleshold

	def get_thleshold(self):
		return self.thleshold


#remote_data = {'tvOnOff':0,'airconOnOff':0,'tvChUpDown':0,'tvVolUpDown':0,'airconTempUpDown':0,'airconThleshold':0,'ledRed':0,'ledGreen':0,'ledBlue':0,'ledThleshold':0}

def rgb_control(ser,rgb_led):
	for i in range(0,3):
		ser.write(str(rgb_led[i]))
		ser.write('\n')

def remote_control(ser,order):
	ser.write(str(order))
	ser.write('\n')



def main():

	while True: ## wait arduino when can't connect 
		try:
			ser = sensor.set_dev()
			break
		except:
			print('no device')
			time.sleep(1)

	home_obj = Home_info(0,0) ## home data obj
	past_remote_data = {} #if change data

	while True: ## wait arduino delay
		now = datetime.now()
		data = sensor.get_data(ser) ## temperature, light

		try:
			home_obj.set_data(data[0],data[1])
		except:
			print('wait arduino')
			continue

		home_data = {'temperature':home_obj.get_temperature(),'light':home_obj.get_light(),'cctvURL':'http://192.168.0.146:8091'} # send home_data set to server

		rs = requests.post('http://kyu9341.pythonanywhere.com/uleung/raspberry/',data=home_data) # target server 
		new_remote_data  = rs.json() # rs



		new_rgb_led = Led(new_remote_data['ledThreshold'],new_remote_data["ledRed"],new_remote_data["ledGreen"],new_remote_data["ledBlue"])

		print('time : ',now)

		try:

			if new_remote_data == past_remote_data: ## if remote_data did't change don't work
	        	        print("same")
			else:
				print('data change')
				if(new_rgb_led.get_rgb() != past_rgb_led.get_rgb()): ## LED control
					print("led change")
					ser.write('1\n')
					rgb_control(ser,new_rgb_led.get_rgb())

				if(new_remote_data["tvOnOff"] != past_remote_data["tvOnOff"]): ## TV control
					print("tv on off")
					ser.write('2\n')
					remote_control(ser,1)

				if(new_remote_data["airconOnOff"] != past_remote_data["airconOnOff"]):
					print("air on off")
					ser.write('2\n')
					remote_control(ser,6)

				if(new_remote_data["tvChUpDown"] != past_remote_data["tvChUpDown"]):
					print("tv ch up down")
					ser.write('2\n')
					if new_remote_data["tvChUpDown"] > 0:
						print("up")
						remote_control(ser,4)
					elif new_remote_data["tvChUpDown"] <0:
						print("down")
						remote_control(ser,5)
				if(new_remote_data["tvVolUpDown"] != past_remote_data["tvVolUpDown"]):
					print("tv vol")
					ser.write('2\n')
					if new_remote_data["tvVolUpDown"] > 0:
						print("up")
						remote_control(ser,2)
				elif new_remote_data["tvVolUpDown"] <0:
						print("down")
						remote_control(ser,3)

				if(new_remote_data["airconTempUpDown"] != past_remote_data["airconTempUpDown"]): ## aircon control
					print("aircon temp up down")
					ser.write('2\n')
					if new_remote_data["airconTempUpDown"] > 0:
						print("up")
						remote_control(ser,7)
					elif new_remote_data["airconTempUpDown"] <0:
						print("down")
						remote_control(ser,8)


			#'temperature':home_obj.get_temperature(),'light':home_obj.get_light()

				if(new_remote_data["ledThreshold"] != 0 ): ## use light data
					if((new_remote_data["ledThreshold"] == 1) and (home_obj.get_light()<800)):
						ser.write('1\n')
						rgb_control(ser,[0,0,0])

					elif((new_remote_data["ledThreshold"] == 2) and (home_obj.get_light()<650)):
						ser.write('1\n')
						rgb_control(ser,[0,0,0])

					elif((new_remote_data["ledThreshold"] == 3) and (home_obj.get_light()<500)):
						ser.write('1\n')
						rgb_control(ser,[0,0,0])

					elif((new_remote_data["ledThreshold"] == 4) and (home_obj.get_light()<350)):
						ser.write('1\n')
						rgb_control(ser,[0,0,0])

					elif((new_remote_data["ledThreshold"] == 5) and (home_obj.get_light()<200)):
						ser.write('1\n')
						rgb_control(ser,[0,0,0])




				if(new_remote_data["airconThreshold"] != 0 ): ## auto temperature control
					if(home_obj.get_temperature()>new_remote_data["airconThreshold"]):
						remote_control(ser,7)
					elif(home_obj.get_temperature()<new_remote_data["airconThreshold"]):
						remote_control(ser,8)

		except:
			print("no data")




		# remote_data format
		#'tvOnOff' 'airconOnOff' 'tvChUpDown'
		#'tvVolUpDown' 'airconTempUpDown' 'ledRed'
		#'ledGreen' 'ledBlue' 'ledThreshold'
		#'airconThreshold'

		for data in new_remote_data.items():
			print(data)


		past_remote_data = new_remote_data ## data sync
		past_rgb_led = new_rgb_led


main()
