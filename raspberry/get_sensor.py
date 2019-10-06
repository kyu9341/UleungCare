import serial

def set_dev(): #라즈베리파이와 연결된 아두이노 시리얼 통신값 반환
	try:
		ser = serial.Serial('/dev/ttyACM0',9600)
		ser.flushInput()
		return ser
	except:
		ser = serial.Serial('/dev/ttyACM1',9600)
		ser.flushInput()
        return ser


def get_data(ser): # 연결된 아두이노의 센서값 수신후 반환
	line = ser.readline()
        line = line.replace('\n','')
        data = line.split(',')
        print(data)
	return data
