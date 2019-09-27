from pyfirmata import Arduino, util


board = Arduino('/dev/ttyUSB0')
while True:
	board.digital[11].write(True)
	board.digital[9].write(True)
