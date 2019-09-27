from pyfirmata import Arduino, util
import time

port = '/dev/ttyUSB0'

board = Arduino(port)
time.sleep(1)

board.get_pin('d:13:o')

iterater = util.Iterator(board)
iterater.start()

while(True):
	board.digital[13].write(1)
	print("on")
	time.sleep(0.5)
	board.digital[13].write(1)
	print("off")
	time.sleep(0.5)


