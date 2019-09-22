from django.contrib import admin
from django.urls import path
from .models import HomeInfo, AndroidRequested

urlpatterns = [
    path('admin/', admin.site.urls)
]

class HomeInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'humidity', 'registered_dttm') # user list 사용자명과 비밀번호를 확인할 수 있도록 구성

class AndroidRequestedAdmin(admin.ModelAdmin):
    list_display = ('id', 'tvOnOff', 'airconOnOff', 'airconTempUp', 'airconTempDown') # user list 사용자명과 비밀번호를 확인할 수 있도록 구성


admin.site.register(HomeInfo, HomeInfoAdmin) # 등록
admin.site.register(AndroidRequested, AndroidRequestedAdmin) # 등록

