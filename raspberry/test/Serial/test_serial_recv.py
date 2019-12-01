
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
count = 0

decode_type_list = list()
IR_data_list = list()

while True:
	data = ser.readline().decode()

	data = data.split(',')

	decode_type_list.append(data[0])
	IR_data_list.append(data[1])

	print(data[0])
	print(data[1])

	count=count+1

	if(count > 20):
		break


how_many = 0

for i in decode_type_list:
	if(how_many < decode_type_list.count(i)):
		how_many = decode_type_list.count(i)
		decode_type = i

how_many = 0

for i in IR_data_list:
	if(how_many < IR_data_list.count(i)):
		how_many = IR_data_list.count(i)
		IR_data = i

print("decode type : ",decode_type,'IR data : ',IR_data)
