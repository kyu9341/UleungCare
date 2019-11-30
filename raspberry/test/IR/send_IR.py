import serial
import requests
import json

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


def get_data(ser):
        line = ser.readline()
        line = line.replace('\n','')
        data = line.split(',')
        print(data)
        return data

##ser.write(order)
def main():

	ser = set_dev()

	while True:

		choice = int(input("choice : "))

		if choice == 1:
			print('send 1')
			ser.write('1\n')
			time.sleep(1)

		elif choice == 2:
			print('send 2')
			ser.write('2\n')
			time.sleep(1)

		elif choice == 3:
			print('send 3')
			ser.write('3\n')
			time.sleep(1)

main()
