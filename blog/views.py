from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    # posts: QuerySet의 이름
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # request: 사용자가 요청하는 모든 것
    # 'blog/post_list.html': 템플릿
    # {}: 템플릿을 사용하기 위해 이곳에 매개변수를 추가
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})