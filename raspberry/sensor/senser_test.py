
import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

ser.flushInput()

while True:
	line = ser.readline()
	line = line.replace('\n','')
	data =line.split(',')
	print(data)
	order = 'a'

	if int(data[1])>600:
		ser.write(order)
	else:
		ser.write(0)
	#data = (0,0)


