라즈베리파이 음성인식 
=============


## 1.라즈베리파이 마이크 사용하기

### 1-1 사용한 h/w

- 라즈베리파이3(라즈비안)
- USB 마이크

### 1-2 마이크 연결하는법
> 라즈베리 파이에 마이크를 연결한다.



$ sudo nano /usr/share/alsa/alsa.conf

> 위의 코드를 사용하여 아래의 내용을 바꾸어 준다. (3~4정도 페이지를 스킵하면 내용을 찾을수있다.)

defaults.ctl.card 0  ->  defaults.ctl.card 1

defaults.pcm.card 0  ->  defaults.pcm.card 1


$ nano .asoundrc
> 위의 명령어를 사용하여 아래와 같이 작성한다.
<pre><code>
 pcm.!default {
        type hw
        card 1
    }

    ctl.!default {
        type hw
        card 1
    }
    
</code></pre>

> 저장하고 닫는다.



$ arecord --format=S16_LE --duration=5 --rate=16000 --file-type=raw out.raw

> 위의 코드를 사용하여 녹음한다. (5초동안 녹음되는 코드)

aplay --format=S16_LE --rate=16000 out.raw

> 위의 코드를 사용하여 녹음이 되었는지 확인한다.


----------------

$ alsamixer

> 위의 명령어를 통해 음량을 조절한다.

----------------

## 2.구글 API사용
> 구글 api를 활용하기 위해 구글에 새로운 프로젝트를 만들어 구글 어시스턴스를 추가한다.


참고 https://m.blog.naver.com/skyshin0304/221291601237


----------------

## 3.파이썬 환경설정
### 3-1 파이썬 및 패키지 설치

$ sudo apt-get update

$ sudo apt-get install python3-dev python3-venv # Use python3.4-venv if the package cannot be found.

$ python3 -m venv env

$ env/bin/python -m pip install --upgrade pip setuptools wheel

> 위의 명령어를 차례대로 실행하여 설치를 진행한다.

$ source env/bin/activate

> 위의 명령어를 사용하면 파이썬 가상환경이 생성된다.

(env) $ python -m pip install --upgrade google-assistant-sdk[samples]
(env) $ python -m pip install --upgrade google-auth-oauthlib[tool]

> 위의 명령어를 사용해 구글 어시스턴트 패키지를 설치한다.

### 3-2 구글 API 환경구축

> 위의 과정에서 다운받은 .json 파일을 라즈베리파이 디렉토리 안에 넣고 진행합니다.

(env) $ google-oauthlib-tool --scope https://www.googleapis.com/auth/assistant-sdk-prototype --save --headless --client-secrets /경로/---/&&&&.com.json 

> 명령을 실행시키면 주소가 나오는데 주소로 들어가서 계정에 엑세스를 허용한다.
> 허용을 하면 나오는 코드를 복사하여 Enter the authorization code: 에 붙여넣어주면 된다.

============================

## 4 구글 API 실행해보기

(env) $ googlesamples-assistant-pushtotalk --project-id 프로젝트ID --device-model-id 모델ID

> enter를 누르며 대화하는 방식

(env) $ googlesamples-assistant-hotword --device_model_id 모델ID

> hotword로 대화하는 방식

*단,위의 방법은 한글은 지원하지 않습니다.

(env) $ googlesamples-assistant-pushtotalk  --lang ko-KR

> 위의 명령어를 사용하여 한글로 pushtotalk를 실행할수있습니다.







