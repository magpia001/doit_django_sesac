from django.urls import path
from . import views

urlpatterns = [
    # 도메인/
    path('about_me/', views.about_me),
    path('', views.landing),
]