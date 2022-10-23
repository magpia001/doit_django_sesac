from django.urls import path
from . import views

urlpatterns = [
    # 도메인/
    path('aboutme/', views.about_me),     # /aboutme/
    path('potpolio/', views.potpolio),    # /potpolio/
    path('', views.landing),              # /
]