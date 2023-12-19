from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import QuerySet
# Create your views here.
def index(request):
    tutorials = Tutorial.objects.all()
    category = Category.objects.all()
    blogs = Blog.objects.all()[:5]
    
    return render(request,"index.html",{'tutorials':tutorials,'category':category,'blogs':blogs})

def contact(request):
    if request.method=="POST":
        name = request.POST.get('username')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name)
        query = Contact(name=name,email=email,subject=subject,message=message)
        query.save()

        subject = 'THANK YOU FOR CONTACTING ME '
        message = f'Hi {name}, Thank you so much for reaching out to me. Your message brightened my day! '
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )

        
        subject1 = 'HELLOW SIR YOU GOT A NEW MAIL'
        message = f'Hi k satyanarayana chary,  Some one contacted you details are:- \n username - {name},\n  email - {email},\n subject - {subject},\n message - {message} \n'
        email_from = settings.EMAIL_HOST_USER
        recipient_list1 = ['charysatheesh4@gmail.com', ]
        send_mail( subject1, message, email_from, recipient_list1 )

        messages.success(request,"Thanks for contacting me ,I will look forward to utilize this oppertunity.....")
        return redirect('/contact/')
    return render(request,"contact.html")   

def about(request):
    return render(request,"about.html") 

def blogs(request):
    category = Category.objects.all()
    return render(request,"blogs.html",{'category':category})

def tutorials(request):
    tutorials = Tutorial.objects.all()
    return render(request,"tutorials.html",{'tutorials':tutorials})

def category(request,url):
    category = Category.objects.get(url=url)
    blogs = Blog.objects.filter(category=category)
    return render(request,"categories.html",{ 'category':category,'blogs': blogs})

def blogSingle(request,url):
    blogs=Blog.objects.get(url=url)
    category = Category.objects.all()
    return render(request,"singleBlog.html",{'blogs':blogs,'category':category})

def tutorialsPage(request,url):
    tutorial = Tutorial.objects.get(url=url)
    posts = Post.objects.filter(tutorial=tutorial)
    return render(request,"tutorialsPage.html",{'tutorial':tutorial,'posts':posts})

def singleTutorial(request,url):
    posts = Post.objects.get(url=url)
    tutorial = Tutorial.objects.all()
    return render(request,"singleTutorial.html",{'posts':posts,'tutorial':tutorial})

def searchresult(request):
    return render(request, 'searchresult.html',)

def search(request):
    query = request.GET.get('q', '')  # Get the search query from the URL parameters
    data = Blog.objects.filter(blog_title__icontains=query)
    posts = Post.objects.filter(post_title__icontains=query)
    return render(request,"search.html", {'data':data,'query':query,'posts':posts})