from django.urls import path
from . import views

urlpatterns = [
    # 도메인/blog/
    # path('', views.index),
    path('', views.PostList.as_view()),
    
    # 도메인/blog/1/
    # path('<int:pk>/', views.single_post_page),
    path('<int:pk>/', views.PostDetail.as_view()),

    
    # 도메인/about_me/
]

