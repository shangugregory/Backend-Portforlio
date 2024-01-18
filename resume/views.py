from rest_framework.response import Response
from rest_framework.decorators import api_view
from . serializer import *
from . models import *

@api_view(['GET'])
def EducationFetch(request):
    my_education = Education.objects.all()
    serializer = EducSerializer(my_education, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def IntrestsFetch(request):
    my_intrets = Intrests.objects.all()
    serializer = IntrestsSerializer(my_intrets, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def ProgrammingFetch(request):
    myLanguage = ProgrammingLanguage.objects.all()
    serializer = ProgrammingLanguageSerializer(myLanguage, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def WorkFetch(request):
    mywork = Work.objects.all()
    serializer = WorkSerializer(mywork, many = True)
    return Response(serializer.data)