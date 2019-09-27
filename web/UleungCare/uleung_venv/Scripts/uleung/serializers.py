from rest_framework import serializers
from .models import AndroidRequested, HomeInfo


class AndroidRequestedSerializer(serializers.ModelSerializer):
    tvOnOff = serializers.IntegerField()
    airconOnOff = serializers.IntegerField()
    airconTempUpDown = serializers.IntegerField()
    tvChUpDown = serializers.IntegerField()
    tvVolUpDown = serializers.IntegerField()
