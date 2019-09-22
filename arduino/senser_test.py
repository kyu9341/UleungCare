
import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

ser.flushInput()

while True:
        try:
                line = ser.readline()
                print(line)

        except KyboardInterrupt:
                break

