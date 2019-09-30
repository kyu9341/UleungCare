
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

ser.flushInput()

while True:
	line = ser.readline()
	line = line.replace('\r\n','')
	line = line.split(',')
	print(line)



