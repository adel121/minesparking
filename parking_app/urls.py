from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pushRequest/<str:registry>', views.addPendingRequest, name='addPendingRequest'),
    path('processQueue/',views.processQueue,name='process_queue'),
    path('testajax/',views.testajax, name='testajax'),
    path('match_cars/',views.match_cars, name='match_cars'),
    path('administration/',views.administration, name='administration')
    
]
