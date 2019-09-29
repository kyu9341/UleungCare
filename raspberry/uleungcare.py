import get_sensor as sensor
import control_device as condev
import requests



class Home_info():
    def __init__(self,temperature,light):
        self.temperature = temperature
        self.light = light

    def set_temperature(slef,input_data):
        self.temperature = input_data

    def set_light(self,input_data):
        self.light = input_data

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

class Led():
    def __init__(self,thleshold,R,G,B):
        self.red = R
        self.green = G
        self.blue = B

    def set_rgb(self,rgb):
        red,green,blue = rgb

    def get_rgb(self):
        rgb=(red,green,blue)
        return rgb


#remote_data = {'tvOnOff':0,'airconOnOff':0,'tvChUpDown':0,'tvVolUpDown':0,'airconTempUpDown':0,'airconThleshold':0,'ledRed':0,'ledGreen':0,'ledBlue':0,'ledThleshold':0}

def main():
	while True:
		ser = sensor.set_dev()
		data = sensor.get_data(ser) ## temperature, light
		home_obj = Home_info(data[0],data[1])

		home_data = {'temperature':home_obj.get_temperature(),'light':home_obj.get_light()}
		#re = requests.get('http://127.0.0.1:8000',data=home_data)

		if int(data[1]) > 600:
			condev.set_led(ser,'a')
			print("so dark ")
		else:
                        condev.set_led(ser,'c')
                        print('no matter')

		if float(data[0]) > 36:
			condev.set_led(ser,'b')
			print("so hot")


main()
