from django.urls import path
from pasaportes import views


urlpatterns = [
path('', views.index),
path('', views.index, name='index'),
path('login', views.login, name='login'),
path('tramitepresencial', views.tramitepresencial, name='tramitepresencial'),
path('subirarchivos', views.subirarchivos, name='subirarchivos'),
]
