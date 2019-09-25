# 라즈베리파이 세팅  

## 라즈비안 설치  
- 라즈비안  
https://www.raspberrypi.org/downloads/raspbian/  

- Flash OS images to SD cards & USB drives, safely and easily  
https://www.balena.io/etcher/  

## Configuration  
- Camera, SSH, VNC : Enable  

## Git  
- sudo apt-get install git-core  
- sudo git clone https://github.com/wjrmffldrhrl/UleungCare.git
- sudo git config --global user.name "본인 계정 입력"
- sudo git config --global user.email "본인 메일 주소 입력"
- sudo git config --global color.ui "auto"




# 카메라 제어 및 온습도, IR모듈 제어  

## Camera  

카메라 연결 후 재부팅 하여 사용 할 것  

- mjpg streamer  
http://www.3demp.com/community/boardDetails.php?cbID=234  

## IR  

- IR reciver  
http://ozzmaker.com/how-to-control-the-gpio-on-a-raspberry-pi-with-an-ir-remote/  

## Mic  

- usb mic  
https://www.youtube.com/watch?v=MjjbFLiFq2Y  

##   

https://poppy-leni.tistory.com/entry/Python-%EC%99%B8%EB%B6%80-%EC%8B%A4%ED%96%89-%EA%B2%B0%EA%B3%BC-%EB%B3%80%EC%88%98%EB%A1%9C-%EC%A0%80%EC%9E%A5%ED%95%98%EA%B8%B0  
라즈베리 파이와 아두이노간의 Serial communication을 위해 USB로 라즈베리파이와 아두이노를 연결한 상태이다.  
이때 라즈베리 파이에서 어떤 USB로 연결 되어있는지 확인하기 위해 기기명을 찾아야 한다.  

pi@raspberryppi:~/ $ ls /sys/bus/usb-serial/devices/ | sed "s/^/\/dev\//g"  
/dev/ttyUSB0  

~~출력되는 기기값을 라즈베리파이 코드에서 수정~~  

~~~  
ser = serial.Serial('/dev/ttyUSB0',9600)
~~~  

코드 내부에서 기기를 검색하고 직접 수정하도록 변경  

```{.python}  
import subprocess

def find_dev():
        cmd = ['ls', '/sys/bus/usb-serial/devices/']
        #ls /sys/bus/usb-serial/devices/ | sed "s/^/\/dev\//g" 기존 명령어

        fd_popen = subprocess.Popen(cmd,stdout=subprocess.PIPE).stdout
        data = fd_popen.read().strip()
        fd_popen.close()

        print(data.decode('utf-8'))
        return(data.decode('utf-8')) # 앞부분에 문자 'b'가 포함되는 현상 디코더로 제거

```

