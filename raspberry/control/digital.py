from pyfirmata import Arduino, util
import time
from find_device import find_dev

board = Arduino('/dev/ttyUSB0')
ledon = board.get_pin('d:13:o')
it = util.Iterator(board)

it.start()

while True:
	ledon.write(True)
	print("on")
	time.sleep(1)
	ledon.write(False)
	print("off")
	time.sleep(1)


