from django.urls import path#路径

from . import views

urlpatterns = [
    path('', views.index, name='index'),#index函数
]