from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.
# def index(request):
#     # 내림차순 정렬
#     posts = Post.objects.all().order_by('-pk')

#     return render(request,'blog/index.html', {'posts':posts})
class PostList(ListView):
    model = Post
    # template_name = 'blog/index.html' 파일이름 post_list.html로 변경
    ordering = '-pk'


def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(request, 'blog/single_post_page.html', {'post':post})