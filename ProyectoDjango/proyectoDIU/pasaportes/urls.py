from re import template
from django.urls import path
from pasaportes import views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
path('', views.index),
path('', views.index, name='index'),
path('login', LoginView.as_view(template_name='login.html'), name='login'),
path('registro', views.registro, name='registro'),
path('tramitepresencial', views.tramitepresencial, name='tramitepresencial'),
path('subirarchivos', views.subirarchivos, name='subirarchivos'),
path('tramitenacional', views.tramitenacional, name='tramitenacional'),
path('tramiteinternacional', views.tramiteinternacional, name='tramiteinternacional'),
path('pago',views.pago,name='pago')
]
