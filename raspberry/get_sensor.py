import serial
import time

def set_dev(): # return serial data what raspberry connect with arduino
	device_number = 0
	while True:
		try:
			print('connect ttyACM'+str(device_number))
			ser = serial.Serial('/dev/ttyACM'+str(device_number),9600) #device name

			ser.flushInput()
			print('connect success')
			time.sleep(2) # delay duaring connected
			return ser
		except: # if device name uncorrect
			device_number += 1
			if device_number > 5:
				return 0
			time.sleep(1)


def get_data(ser): # return sensor data
	ser.write('3'.encode())
	line = ser.readline().decode()
	line = line.replace('\n','')
	line = line.replace('\r','')
	data = line.split(',')
	print(data)
	return data
