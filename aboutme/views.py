from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import *
from . serializer import *


@api_view(['GET'])
def getData(request):
    app = About.objects.all()
    serializer = MeSerializer(app, many=True)
    return Response(serializer.data)