from django.contrib import admin
from django.urls import path
from .models import HomeInfo, AndroidRequested, Settings

urlpatterns = [
    path('admin/', admin.site.urls)
]

class HomeInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'temperature', 'light', 'registered_dttm') # user list 사용자명과 비밀번호를 확인할 수 있도록 구성

class AndroidRequestedAdmin(admin.ModelAdmin):
    list_display = ('id', 'tvOnOff', 'airconOnOff', 'airconTempUpDown', 'tvChUpDown', 'tvVolUpDown') # user list 사용자명과 비밀번호를 확인할 수 있도록 구성

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('ledRed', 'ledGreen', 'ledBlue', 'ledThreshold', 'airconThreshold')
#
admin.site.register(Settings, SettingsAdmin)
admin.site.register(HomeInfo, HomeInfoAdmin) # 등록
admin.site.register(AndroidRequested, AndroidRequestedAdmin) # 등록

