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
    
home_obj = Home_info(36.6,128)
    
home_data={'temperature':home_obj.get_temperature(),'light':home_obj.get_light()}

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
    def __init__(self,OnOff,UpDown):
        super().__init__(OnOff,UpDown)
    

remote_data = {'tvOnOff':0,'airconOnOff':0,'tvChUpDown':0,'tvVolUpDown':0,'airconTempUpDown':0}

rs = requests.post('http://127.0.0.1:8000/uleung/raspberry/',data=home_data)

remote_data = rs.json()


