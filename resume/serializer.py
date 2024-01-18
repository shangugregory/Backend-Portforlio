from rest_framework import serializers
from . models import *

class EducSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('education_id', 'institution_name', 'year_joined', 'year_Ended', 'grade_attained', 'certificate_earned',)


class IntrestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intrests
        fields = ('intersts_id', 'intrests_name', 'intrests_description')

class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = ('language_id', 'language_name', 'percentage_coverage')

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('work_id', 'company', 'work_title', 'start_date', 'end_date')
        