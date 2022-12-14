from django.urls import path
from . import views

urlpatterns = [
    # 도메인/blog/
    # path('', views.index),
    path('', views.PostList.as_view()),
    # 도메인/blog/1/
    # path('<int:pk>/', views.single_post_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    # create_post/
    path('create_post/', views.PostCreate.as_view()),
    # update_post/
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),

    path('category/<str:slug>/', views.category_page),
    path('tag/<str:slug>/', views.tag_page),
    
    # 도메인/about_me/
]

