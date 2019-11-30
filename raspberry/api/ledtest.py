# -*- coding: utf-8 -*-
import gspeech
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

def main():
	gsp = gspeech.Gspeech()
	print("start program")
	while True:
		# 음성 인식 될때까지 대기 한다.
		stt = gsp.getText()
		if stt is None:
			break
		print(stt)
		time.sleep(0.01)
		if('불 켜' in stt):
			GPIO.output(21, True)
		if('불 꺼' in stt):
			GPIO.output(21, False)
		if('끝' in stt):
			GPIO.cleanup()
			break
	
if __name__ == '__main__':
    main()
