import get_sensor as sensor
import control_device as condev
import requests
import json
import time

class Home_info():
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


class Remote_info():
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
        rgb=(red,green,blue)
        return rgb


#remote_data = {'tvOnOff':0,'airconOnOff':0,'tvChUpDown':0,'tvVolUpDown':0,'airconTempUpDown':0,'airconThleshold':0,'ledRed':0,'ledGreen':0,'ledBlue':0,'ledThleshold':0}

def rgb_control(ser,rgb_led):
	for i in range(0,3):
		ser.write(str(rgb_led[i]))
		ser.write('\n')

def remote_control(ser,order):
	ser.write(str(order))
	ser.write('\n')



def main():
	while True:
		try:
			ser = sensor.set_dev()
			break
		except:
			print('no device')
			time.sleep(1)
	home_obj = Home_info(0,0) ## home data obj 
	past_remote_data = {}

	while True:
		data = sensor.get_data(ser) ## temperature, light
		try:
			home_obj.set_data(data[0],data[1])
		except:
			print('wait arduino')
			continue

		home_data = {'temperature':home_obj.get_temperature(),'light':home_obj.get_light(),'cctvURL':'http://192.168.0.1'}

		rs = requests.post('http://kyu9341.pythonanywhere.com/uleung/raspberry/',data=home_data)
		new_remote_data  = rs.json()

		rgb_led = [new_remote_data["ledRed"],new_remote_data["ledGreen"],new_remote_data["ledBlue"]]

		try:

			if new_remote_data == past_remote_data:
	                        print("same")
	                else:
				print('data change')
				ser.write('1\n')
				rgb_control(ser,rgb_led)

				if(new_remote_data["tvOnOff"] != past_remote_data["tvOnOff"]):
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
						remote_control(ser,4)
					elif new_remote_data["tvChUpDown"] <0:
						remote_control(ser,5)

				if(new_remote_data["tvVolUpDown"] != past_remote_data["tvVolUpDown"]):
					print("tv vol up down")
					ser.write('2\n')
					if new_remote_data["tvVolUpDown"] > 0:
                                                remote_control(ser,2)
                                        elif new_remote_data["tvVolUpDown"] <0:
                                                remote_control(ser,3)

				if(new_remote_data["airconTempUpDown"] != past_remote_data["airconTempUpDown"]):
					print("aircon temp up down")
					ser.write('2\n')
					if new_remote_data["airconTempUpDown"] > 0:
                                                remote_control(ser,7)
                                        elif new_remote_data["airconTempUpDown"] <0:
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


		past_remote_data = new_remote_data



main()