import serial
import os
from find_device import find_dev

dev = '/dev/' + find_dev() 
ser = serial.Serial (dev,9600)
# arduino serial port name
#ls /sys/bus/usb-serial/devices/ | sed "s/^/\/dev\//g"
value = ['','','','','','']
inputPin = 0
ser.flushInput()
while True:
	try:
		lineBytes = ser.readline()
		line = lineBytes.decode('utf-8')
		data = line.split(":")
		if(len(data)==2):
			inputpin = data[0]
			value[inputPin] = data[1]
			os.system('clear')
			for i in range(0,6):
				print("input pin {} has value {} ".format(i,value[i]))

		inputPin = inputPin+1
		if(inputPin > 5 ):
			inputPin = 0
		ser.write(str(inputPin).encode())

	except KeyboardInterrupt:
		break

