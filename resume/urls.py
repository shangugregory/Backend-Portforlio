from django.urls import path
from .views import *

urlpatterns = [
    path("education/", EducationFetch),
    path('intrests/', IntrestsFetch),
    path('work/', WorkFetch),
    path('language/', ProgrammingFetch)
]