# Django 프레임 워크를 이용한 서버 구축




# Pythonanywhere 호스팅 서버 사용



# MySQL

## 데이터베이스에 저장될 데이터

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

