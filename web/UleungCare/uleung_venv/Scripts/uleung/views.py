from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import HomeInfo, AndroidRequested
# Create your views here.

@csrf_exempt
def androidControl(request):
    if request.method == 'GET':
        return render(request, 'uleung/androidControl.html')
    elif request.method == 'POST':
        tvOnOff = request.POST.get('tvOnOff', None) # 템플릿에서 입력한 name필드에 있는 값을 키값으로 받아옴
        airconOnOff = request.POST.get('airconOnOff', None) # 받아온 키값에 값이 없는경우 None값으로 기본값으로 지정
        airconTempUp = request.POST.get('re-airconTempUp', None)
        airconTempDown = request.POST.get('airconTempDown', None)

        res_data = {} # 응답 메세지를 담을 변수(딕셔너리)

        androidrequested = AndroidRequested( # 모델에서 생성한 클래스를 가져와 객체를 생성
            tvOnOff=tvOnOff,
            airconOnOff=airconOnOff,
            airconTempUp=airconTempUp,
            airconTempDown=airconTempDown,
        )

        androidrequested.save() # 데이터베이스에 저장

        return HttpResponse({"success" : True}) #