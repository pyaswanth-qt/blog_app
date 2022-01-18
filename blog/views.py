from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
from sqlalchemy.engine import create_engine
from .models import Post,User
from operator import itemgetter
import mysql.connector
from sqlalchemy.orm import sessionmaker
# Create your views here.


engine=create_engine("mysql+mysqlconnector://root:root@localhost:3306/blog",echo=True)
session_maker=sessionmaker()
session_maker.configure(bind=engine)
session=session_maker()

def home(request):
    posts=Post.objects.all()[:11]
    data={
        'posts':posts
    }
    return render(request,'home.html',data)

def post(request,url):
    post=Post.objects.get(post_id=url)
    return render(request,'posts.html',{'post':post})

def login(request):
    
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['pass']
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        user=User()
        user.email=request.POST['email']
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.password=request.POST['pass']
        user.save()
    return render(request,'register.html')

def upload(request):
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        load=Post(title=title,content=content)
        load.save()
    return render(request,'upload.html') 