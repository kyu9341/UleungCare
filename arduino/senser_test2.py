import serial
import time

ser = serial.Serial ('/dev/ttyUSB1',9600)
# arduino serial port name
#ls /sys/bus/usb-serial/devices/ | sed "s/^/\/dev\//g"

inputPin = 5
inputPinStr = str(inputPin)
inputPinStrBytes = inputPinStr.encode()

ser.write(inputPinStrBytes)
ser.flushInput()
while True:
	try:
		lineBytes = ser.readline()
		line = lineBytes.decode('utf-8')
		print(line)
		

	except KeyboardInterrupt:
		break


