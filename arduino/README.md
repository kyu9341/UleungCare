# 아두이노  

## 목적  

각종 센서의 활용이 약간은 어려운 라즈베리파이의 단점을 보완하기 위해 아두이노를 활용하여 센서로 받아온 데이터를 라즈베리 파이로 전송한다.  

## 참고  

라즈베리 파이와 아두이노간의 Serial communication을 위해 USB로 라즈베리파이와 아두이노를 연결한 상태이다.  
이때 라즈베리 파이에서 어떤 USB로 연결 되어있는지 확인하기 위해 기기명을 찾아야 한다.  

pi@raspberryppi:~/ $ ls /sys/bus/usb-serial/devices/ | sed "s/^/\/dev\//g"  
/dev/ttyUSB0  

출력되는 기기값을 라즈베리파이 코드에서 수정  

~~~  
ser = serial.Serial('/dev/ttyUSB0',9600)
~~~  

