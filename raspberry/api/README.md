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
### 3-1 파이썬 설치

$ sudo apt-get update
$ sudo apt-get install python3-dev python3-venv # Use python3.4-venv if the package cannot be found.
$ python3 -m venv env
$ env/bin/python -m pip install --upgrade pip setuptools wheel
$ source env/bin/activate

> 위의 명령어를 사용하여 차례대로 설치한다.









