from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import HomeInfo, AndroidRequested
from django.http import JsonResponse
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

        ar = AndroidRequested.objects.order_by('id').last() #

        if(int(tvVolUpDown) == 1):
            tvVolUpDown = ar.tvVolUpDown + 1
        if(int(tvVolUpDown) == -1):
            tvVolUpDown = ar.tvVolUpDown - 1

        if(int(tvChUpDown) == 1):
            tvChUpDown = ar.tvChUpDown + 1
        if(int(tvChUpDown) == -1):
            tvChUpDown = ar.tvChUpDown - 1

        if(int(airconTempUpDown) == 1):
            airconTempUpDown = ar.airconTempUpDown + 1
        if(int(airconTempUpDown) == -1):
            airconTempUpDown = ar.airconTempUpDown - 1

#        ar = AndroidRequested.objects.order_by('id').last()
        ar.tvOnOff = int(tvOnOff)
        ar.airconOnOff = int(airconOnOff)
        ar.airconTempUpDown = int(airconTempUpDown)
        ar.tvVolUpDown = int(tvVolUpDown)
        ar.tvChUpDown = int(tvChUpDown)




        ar.save()

        res_data = {} # 응답 메세지를 담을 변수(딕셔너리)


        res_data['success'] = True

   #     return JsonResponse({"success" : True}) #
    #    return render(request, 'uleung/AndroidControl.html', res_data) # res_data가 html코드로 전달이 됨

        return JsonResponse(res_data)

 #       return HttpResponse(json.dumps(res_data), content_type="application/json")

'''

        androidrequested = AndroidRequested( # 모델에서 생성한 클래스를 가져와 객체를 생성
            tvOnOff=int(tvOnOff),
            airconOnOff=int(airconOnOff),
            airconTempUpDown=int(airconTempUpDown),
            tvVolUpDown=int(tvVolUpDown),
            tvChUpDown=int(tvChUpDown),

        )

        androidrequested.save() # 데이터베이스에 저장'''

def getHomeInfo(request):
    if request.method == 'GET':
        homeinfo = HomeInfo.objects.order_by('id').last()

        home_data = {}
        home_data['temperature'] = homeinfo.temperature
        home_data['humidity'] = homeinfo.humidity
        home_data['registered_dttm'] = homeinfo.registered_dttm
        home_data['airconTem'] = homeinfo.airconTem


        return JsonResponse(home_data)
        #return HttpResponse(json.dumps(home_data), content_type="application/json")
        #return render(request, 'uleung/getHomeInfo.html', json.dumps(home_data))
    elif request.method == 'POST':
        pass



