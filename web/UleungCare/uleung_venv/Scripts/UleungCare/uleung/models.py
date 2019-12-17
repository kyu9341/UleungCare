from django.db import models

class HomeInfo(models.Model):
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='온도')
    light = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='조도')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='측정시간')
    cctvURL = models.TextField(verbose_name="CCTV URL")

    airconTem = models.IntegerField(verbose_name='현재 에어컨 설정 온도')


    class Meta:
        db_table = 'Uleung_HomeInfo' # 테이블명 지정
        verbose_name = '스마트 홈 데이터'
        verbose_name_plural = '스마트 홈 데이터' # 복수형 표현도 설정

class AndroidRequested(models.Model):
    tvOnOff = models.IntegerField(verbose_name='TV on off')
    airconOnOff = models.IntegerField(verbose_name='AirConditioner on off')
    airconTempUpDown = models.IntegerField(verbose_name='AirConditioner Temperature Up Down')
    tvChUpDown = models.IntegerField(verbose_name='TV Channel Up Down')
    tvVolUpDown = models.IntegerField(verbose_name='TV Volume Up Down')
    powerOnOff = models.IntegerField(verbose_name='RaspberryPi Power On Off')

    class Meta:
        db_table = 'Uleung_androidRequested' # 테이블명 지정
        verbose_name = '안드로이드 요청 데이터'
        verbose_name_plural = '안드로이드 요청 데이터' # 복수형 표현도 설정

class Settings(models.Model):
    ledRed = models.IntegerField(verbose_name='led Red value') # LED RGB값
    ledGreen = models.IntegerField(verbose_name='led green value')
    ledBlue = models.IntegerField(verbose_name='led blue value')
    airconThreshold = models.IntegerField(verbose_name='AirConditioner Temperature setting') # 에어컨 자동 온도 설정값
    ledThreshold = models.IntegerField(verbose_name='LED light setting') # LED 자동 켜짐 조도 설정값

    class Meta:
        db_table = 'Uleung_settings' # 테이블명 지정
        verbose_name = '안드로이드 setting 데이터'
        verbose_name_plural = '안드로이드 setting 데이터' # 복수형 표현도 설정
