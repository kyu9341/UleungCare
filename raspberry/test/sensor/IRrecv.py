import serial
import os

ser = serial.Serial('/dev/ttyACM0', 9600)

ser.flushInput()


def recv(ser):
	f = open('remote_data.txt','a')
	for i in range(0,5):
		line = ser.readline()
	        #line = line.replace('\r\n','')
	        #line = line.split(',')
	        print(line)

		f.write(line)

	f.close()

recv(ser)
