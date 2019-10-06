## 개요
파이썬 웹 프레임 워크인 Django를 사용하여 구동되며 안드로이드와 라즈베리파이를 연결해주는 역할을 수행.
사용자가 안드로이드에서 리모컨기능을 사용하여 TV 또는 에어컨 등을 제어하는 요청을 보내면 
mysql의 AndroidRequested테이블의 값이 변경되며 라즈베리파이에서 Polling하며 변경된 값을 확인하고 디바이스를 제어.
또한 라즈베리파이에서 Polling하며 전송하는 HomeData를 HomeInfo 테이블에 저장하며 안드로이드에 응답을 수행.

## 사용 환경
테스트 서버 os : 윈도우 10
배포 서버 os : 우분투 18.04 

## 설치 및 실행
pythonanywhere서버를 호스팅 받아 우분투 리눅스환경에서 동작중

### MySQL

### 데이터베이스에 저장되는 데이터

**AndroidRequested**
- integer(TV on off 설정) 꺼짐 : 0, 켜짐 : 1, 기본값 : 2
- integer(에어컨 on off 설정) 꺼짐 : 0, 켜짐 : 1, 기본값 : 2 
- integer(에어컨 온도 up down)
- integer(TV 음량 up down)
- integer(TV 채널 up down)

**HomeInfo**

- float(조도 센서 값)
- float(온도 센서 값)
- text(cctvURL 주소) : cctvURL
- 측정시간

**Setting**

- integer(LED rgb 값) : ledRed, ledGreen, ledBlue
- integer(에어컨 설정온도) : airconThreshold
- integer(LED 조도 기준 설정) : ledThreshold


