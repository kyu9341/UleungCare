from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import HomeInfo, AndroidRequested, Settings
from django.http import JsonResponse
from datetime import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.forms.models import model_to_dict

# Create your views here.

@csrf_exempt
def AndroidControl(request):

    if request.method == 'GET':
        androidrequested = AndroidRequested.objects.order_by('id').last()
        res_data={}
        res_data['success'] = androidrequested.airconOnOff


        return render(request, 'uleung/AndroidControl.html', res_data)

    elif request.method == 'POST':
        tvOnOff = request.POST.get('tvOnOff', None) # 템플릿에서 입력한 name필드에 있는 값을 키값으로 받아옴
        airconOnOff = request.POST.get('airconOnOff', None) # 받아온 키값에 값이 없는경우 None값으로 기본값으로 지정
        airconTempUpDown = request.POST.get('airconTempUpDown', None)
        tvVolUpDown = request.POST.get('tvVolUpDown', None)
        tvChUpDown = request.POST.get('tvChUpDown', None)

        #androidrequesteds = AndroidRequested.objects.all() #AndroidRequested에 있는 모든 객체를 불러와 androidrequesteds에 저장
        res_data = {} # 응답 메세지를 담을 변수(딕셔너리)

        ar = AndroidRequested.objects.order_by('id').last() # 가장 최근의 튜플을 가져옴

        res_data['kind'] = '' # 안드로이드에 응답 시 kind라는 키값에 어떠한 값이 변화했는지 알려줌
        if(int(tvVolUpDown) > 0):
            ar.tvVolUpDown += 1
            res_data['kind'] = 'volume-'
        elif(int(tvVolUpDown) < 0):
            ar.tvVolUpDown -= 1
            res_data['kind'] = 'volume+'

        if(int(tvChUpDown) > 0):
            ar.tvChUpDown += 1
            res_data['kind'] = 'channel-'
        elif(int(tvChUpDown) < 0):
            ar.tvChUpDown -= 1
            res_data['kind'] = 'channel+'

        if(int(airconTempUpDown) > 0):
            ar.airconTempUpDown += 1
            res_data['kind'] = 'temperature-'
        elif(int(airconTempUpDown) < 0):
            ar.airconTempUpDown -= 1
            res_data['kind'] = 'temperature+'


        if(int(tvOnOff) == 0): # TV를 끄면 음량 및 채널 값 초기화
            ar.tvVolUpDown = 0
            ar.tvChUpDown = 0
        if(int(airconOnOff) == 0): # 에어컨를 끄면 온도 값 초기화
            ar.airconTempUpDown = 0

        ar.tvOnOff = int(tvOnOff)
        ar.airconOnOff = int(airconOnOff)
        ar.save()

        res_data['success'] = True

        return JsonResponse(res_data)

 #       return HttpResponse(json.dumps(res_data), content_type="application/json")
   #     return JsonResponse({"success" : True}) #


def getHomeInfo(request):
    if request.method == 'GET':
        homeinfo = HomeInfo.objects.order_by('id').last()

        home_data = {} # HomeInfo 테이블의 데이터를 응답하기 위한 딕셔너리
        home_data['temperature'] = homeinfo.temperature
        home_data['registered_dttm'] = homeinfo.registered_dttm
        home_data['cctvURL'] = homeinfo.cctvURL

        return JsonResponse(home_data) # json으로 응답
        #return HttpResponse(json.dumps(home_data), content_type="application/json")
        #return render(request, 'uleung/getHomeInfo.html', json.dumps(home_data))
    elif request.method == 'POST':
        pass

@csrf_exempt
def raspberry(request):
    if request.method == 'GET':
        return HttpResponse("raspberry")

    elif request.method == 'POST':
        temperature = request.POST.get('temperature', None) # 라즈베리파이로부터 수신받은 데이터
        light = request.POST.get('light', None)
        cctvURL = request.POST.get('cctvURL', None)

        homeinfo = HomeInfo.objects.order_by('id').last() # 마지막 튜플을 가져와 업데이트
        homeinfo.temperature = float(temperature)
        homeinfo.light = float(light)
        homeinfo.registered_dttm = datetime.now()
        homeinfo.cctvURL = cctvURL
        homeinfo.save() # 데이터베이스에 저장

        res_data = {}
        ar = AndroidRequested.objects.order_by('id').last()
        res_data['tvOnOff'] = ar.tvOnOff # 기본값 : 0 (꺼짐상태), 1이면 TV on
        res_data['airconOnOff'] = ar.airconOnOff # 기본값 : 0 (꺼짐상태), 1이면 에어컨 on
        res_data['tvChUpDown'] = ar.tvChUpDown # 기본값 : 0, 정수형, + or - 만큼 up or down
        res_data['tvVolUpDown'] = ar.tvVolUpDown # 기본값 : 0, 정수형, + or - 만큼 up or down
        res_data['airconTempUpDown'] = ar.airconTempUpDown # 기본값 : 0, 정수형, + or - 만큼 up or down
        res_data['powerOnOff'] = ar.powerOnOff # 기본값 : 0, 우렁케어 종료 : 1

        ar.tvChUpDown = 0 # 전송 후 UpDown데이터는 초기화, OnOff데이터는 유지
        ar.tvVolUpDown = 0
        ar.airconTempUpDown = 0
        ar.powerOnOff = 0
        if ar.tvOnOff == 999:
            ar.tvOnOff = 0
        if ar.airconOnOff == 999:
            ar.airconOnOff = 0
        ar.save()

        sett = Settings.objects.order_by('id').last() # 가장 최근의 튜플을 가져옴
        res_data['ledRed'] = sett.ledRed
        res_data['ledGreen'] = sett.ledGreen
        res_data['ledBlue'] = sett.ledBlue
        res_data['ledThreshold'] = sett.ledThreshold
        res_data['airconThreshold'] = sett.airconThreshold


        return JsonResponse(res_data) # 안드로이드에 응답

@csrf_exempt
def settings(request):
    if request.method == 'GET':
        settings_data = {}
        sett = Settings.objects.order_by('id').last() # 가장 최근의 튜플을 가져옴
        settings_data['ledRed'] = sett.ledRed

        return JsonResponse(settings_data)

    elif request.method == 'POST':
        andset = Settings.objects.order_by('id').last() # 가장 최근의 튜플을 가져옴

        andset.ledRed = request.POST.get('ledRed', None) # 각 데이터 업데이트
        andset.ledGreen = request.POST.get('ledGreen', None)
        andset.ledBlue = request.POST.get('ledBlue', None)
        andset.ledThreshold = request.POST.get('ledThreshold', None)
        andset.airconThreshold = request.POST.get('airconThreshold', None)

        andset.save() # 데이터베이스에 저장
        res_data = {}
        res_data['success'] = True
        return JsonResponse(res_data) # 안드로이드에 정상적으로 처리되었음을 응답


@csrf_exempt
def IRregister(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        tvOnOff = request.POST.get('tvOnOff', None) # 템플릿에서 입력한 name필드에 있는 값을 키값으로 받아옴
        airconOnOff = request.POST.get('airconOnOff', None) # 받아온 키값에 값이 없는경우 None값으로 기본값으로 지정
        airconTempUpDown = request.POST.get('airconTempUpDown', None)
        tvVolUpDown = request.POST.get('tvVolUpDown', None)
        tvChUpDown = request.POST.get('tvChUpDown', None)

        #androidrequesteds = AndroidRequested.objects.all() #AndroidRequested에 있는 모든 객체를 불러와 androidrequesteds에 저장
        res_data = {} # 응답 메세지를 담을 변수(딕셔너리)

        ar = AndroidRequested.objects.order_by('id').last() # 가장 최근의 튜플을 가져옴

        ar.tvVolUpDown = int(tvVolUpDown)
        ar.tvChUpDown = int(tvChUpDown)
        ar.airconTempUpDown = int(airconTempUpDown)
        ar.tvOnOff = int(tvOnOff)
        ar.airconOnOff = int(airconOnOff)
        ar.save()

        res_data['success'] = True

        return JsonResponse(res_data)


@csrf_exempt
def raspOnOff(request):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        powerOnOff = request.POST.get('powerOnOff', None)

        res_data = {}

        ar = AndroidRequested.objects.order_by('id').last()
        ar.powerOnOff = int(powerOnOff)
        ar.save()

        res_data['success'] = True

        return JsonResponse(res_data)











