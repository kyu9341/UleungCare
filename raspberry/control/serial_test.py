import serial
ser = serial.Serial("/dev/ttyACM1",9600)
print(ser.portstr)
while True:
	ser.write("5")
