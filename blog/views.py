from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts=Post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts})
def jm (request):   
    return render(request,'blog/jm.html',{})

def post_details(request,pk):
   post = get_object_or_404(Post, pk=pk)
   return render(request,'blog/post_details.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
       form = PostForm()
       return render(request, 'blog/post_edit.html', {'form': form})



def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
