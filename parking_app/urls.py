from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pushRequest/<str:registry>', views.addPendingRequest, name='addPendingRequest'),
    path('processQueue/',views.processQueue,name='process_queue'),
    path('testajax/',views.testajax, name='testajax'),
    path('match_cars/',views.match_cars, name='match_cars'),
    path('administration/',views.administration, name='administration'),
    path('allow_capture/', views.allow_capture, name='allow_capture'),
    path('clear_queue/', views.clear_queue, name='clear_queue'),
    path('get_state/<str:registry>/',views.get_state,name='get_state'),
    path('get_capture/',views.get_capture,name='get_capture'),
]
