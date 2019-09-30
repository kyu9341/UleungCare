import serial

def set_dev():
	ser = serial.Serial('/dev/ttyACM0',9600)
	ser.flushInput()
	return ser

def get_data(ser):
	line = ser.readline()
        line = line.replace('\n','')
        data = line.split(',')
        print(data)
	return data
