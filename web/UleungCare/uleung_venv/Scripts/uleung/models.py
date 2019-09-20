
from django.db import models

# Create your models here.

class HomeInfo(models.Model):
    temperature = models.DecimalField(max_digits=10, decimal_places=10, verbose_name='온도')
    humidity = models.DecimalField(max_digits=10, decimal_places=10,verbose_name='습도')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='측정시간')

    class Meta:
        db_table = 'Uleung_HomeInfo' # 테이블명 지정
        verbose_name = '스마트 홈 데이터'
        verbose_name_plural = '스마트 홈 데이터' # 복수형 표현도 설정

class AndroidRequested(models.Model):
    tvOnOff = models.IntegerField(verbose_name='TV on off')
    airconOnOff = models.IntegerField(verbose_name='AirConditioner on off')
    airconTempUp = models.IntegerField(verbose_name='AirConditioner Temperature Up')
    airconTempDown = models.IntegerField(verbose_name='AirConditioner Temperature Down')

    class Meta:
        db_table = 'Uleung_androidRequested' # 테이블명 지정
        verbose_name = '안드로이드 요청 데이터'
        verbose_name_plural = '안드로이드 요청 데이터' # 복수형 표현도 설정
