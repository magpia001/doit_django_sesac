from django.views.generic import ListView, DetailView
from .models import Post, Category

# Create your views here.
# def index(request):
#     # 내림차순 정렬
#     posts = Post.objects.all().order_by('-pk')

#     return render(request,'blog/index.html', {'posts':posts})
class PostList(ListView):
    model = Post
    # template_name = 'blog/index.html' 파일이름 post_list.html로 변경
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()

        return context


# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/single_post_page.html', {'post':post})
class PostDetail(DetailView):
    model = Post