from django.shortcuts import render
from .models import Post

# Create your views here.
def post_list(request):
	post = Post.objects.all()
	return render(request, 'blog/index.html', {
		'post':post,
		})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'blog/post_detail.html',
		{
		'post':post,
		})