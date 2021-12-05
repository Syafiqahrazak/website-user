from . import views
from django.urls import path

urlpatterns = [
    path('', views.loginuser, name='loginuser'),
    path('index', views.index, name='index'),
]