import serial
from find_device import find_dev

dev = '/dev/' + find_dev() 
ser = serial.Serial (dev,9600)
# arduino serial port name
#ls /sys/bus/usb-serial/devices/ | sed "s/^/\/dev\//g"

inputPin = 0
ser.flushInput()
while True:
	try:
		lineBytes = ser.readline()
		line = lineBytes.decode('utf-8')
		data = line.split(":")
		if(len(data)==2):
			inputpin = data[0]
			value = data[1]
			print("input pin {} has value {}".format(inputpin,value))

		inputPin = inputPin+1
		if(inputPin > 5 ):
			inputPin = 0
		ser.write(str(inputPin).encode())

	except KeyboardInterrupt:
		break

