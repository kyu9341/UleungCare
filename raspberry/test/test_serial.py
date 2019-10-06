import get_sensor as sensor

ser = sensor.set_dev()
a=0
#b = (4450,4550,500,1750,500,1750,500,1750,500,600,500,650,450,650,500,650,450,650,500,1750,450,1800,450,1750,500,650,500,600,500,650,450,650,500,600,500,650,500,1750,450,1800,450,1750,500,650,450,650,500,650,450,650,500,1750,500,600,500,650,450,650,500,1750,500,1750,450,1800,450,1750,500,0)
b = (4450,4550,500,1750,500,0)
while True:
	#line = ser.readline()
	#line = line.replace('\n','')
	#print(line)

	if b[a] == 0:
		print('end')
		ser.write(str(b[a]))
		print(ser.readline())
	else:
		#print('send{}'.format(b[a]))
		ser.write(b[a])
		#print('recv')
		#print(ser.readline())
		a = a+1

