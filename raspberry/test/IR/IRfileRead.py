
def IR_fileRead(command):

	f = open('RemoteController.txt', 'r', encoding="utf8")
	#command = 'tvonoff'
	IRlist = list()
	while True:
		line = f.readline()
		if not line:
			break
		if command in line:
			line = line.replace('\n', '')
			print(line)
			print('This Line!!')
			IRlist = list(line.split('\t'))
		print(line)

	print(IRlist)
	f.close()

	return IRlist[2]


IR_data = IR_fileRead('tvOnOff')
print(IR_data)
