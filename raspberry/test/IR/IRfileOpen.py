
def IR_fileOpen(data):
	# IRlist = ['tvOn', 'utf-8', 'ABC123']
	f = open('RemoteController.txt', 'a', encoding="utf8")

	for i in data:
		f.write(i+'\t')
	f.write('\n')
	f.close()



data =['tvonoff','7','E0E040BF']
IR_fileOpen(data)
