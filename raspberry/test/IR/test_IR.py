import serial
import time
from datetime import datetime



def set_dev():
        try:
                ser = serial.Serial('/dev/ttyACM0',9600)
                ser.flushInput()
                return ser
        except:
                ser = serial.Serial('/dev/ttyACM1',9600)
                ser.flushInput()
        return ser


while True:



	ser = serial.Serial('/dev/ttyACM0',9600)
  	ser.flushInput()


	line = ser.readline()
	print(line)
