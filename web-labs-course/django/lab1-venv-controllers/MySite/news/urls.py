"""
Маршруты приложения news.
Подключаются в корневом urls.py через include('news.urls').
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),       # /news/
    path('test/', views.test, name='test'),    # /news/test/
]
