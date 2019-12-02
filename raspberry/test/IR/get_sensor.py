import serial
def set_dev(): # return serial data what raspberry connect with arduino
	try:
		ser = serial.Serial('/dev/ttyACM0',9600)
		ser.flushInput()
		return ser
	except:
		ser = serial.Serial('/dev/ttyACM1',9600)
		ser.flushInput()
	return ser



