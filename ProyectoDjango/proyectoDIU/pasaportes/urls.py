from django.urls import path
from pasaportes import views


urlpatterns = [
path('', views.index),
path('', views.index, name='index'),
]
