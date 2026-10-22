"""
Маршруты приложения news.
Согласно методичке: все маршруты приложения хранятся здесь
и подключаются через include в корневом urls.py.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),       # /news/
    path('test/', views.test, name='test'),    # /news/test/
]
