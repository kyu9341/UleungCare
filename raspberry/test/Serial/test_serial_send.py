import serial
def set_dev():
	try:
		ser = serial.Serial('/dev/ttyACM0',9600)
		ser.flushInput()
		return ser
	except:
		print('change dev name')
		ser = serial.Serial('/dev/ttyACM1',9600)
		ser.flushInput()

	return ser


ser = set_dev()
while True:
	#line = ser.readline()
	#line = line.replace('\n','')
	#print(line)

	pi_say = input('input data : ')
	pi_say = str(pi_say)
	ser.write(pi_say.encode())
	print(ser.readline().decode())
	print(ser.readline().decode())
	print(ser.readline().decode())
	print(ser.readline().decode())

	#print(ser.readline())
	#print('send{}'.format(b[a]))
	#print('recv')
	#print(ser.readline())

