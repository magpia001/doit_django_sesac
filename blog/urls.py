from django.urls import path
from . import views

urlpatterns = [
    # 도메인/blog/
    path('', views.index),
    # 도메인/blog/1/
    # 도메인/about_me/
]

