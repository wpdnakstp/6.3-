from django.shortcuts import render, redirect, get_object_or_404
from .forms import BlogPost
# Create your views here.
from django.utils import timezone
from datetime import datetime
from .models import Blog, Pictures
from django.http import HttpResponse


def index(request):
    return HttpResponse("hello, world. You're at the polls index")
def home(request):
    blogs = Pictures.objects
    blog = Blog.objects
    return render(request, 'home.html', {'blog':blog, 'picture':blogs})

def blogpost(request):
    if request.method =='POST':
        #POST방식으로 요청이 들어왔을 때 실행할 코드 - form에 입력받은 데이터를 저장하기
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form' : form})
       # GET방식으로 요청이 들어왔을 때 실행할 코드 - form을 보여주기

    

def new(request):
    form = BlogPost()
    return render(request, 'new.html',{'form':form})