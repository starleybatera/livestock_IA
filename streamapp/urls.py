from django.urls import path, include
from streamapp import views


urlpatterns = [
    path('', views.index, name='index'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
  
    ]
