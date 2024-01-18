from rest_framework import serializers
from . models import *

class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'name', 'mydesc', 'pic')