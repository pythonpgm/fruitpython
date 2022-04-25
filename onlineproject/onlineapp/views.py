from django.http import HttpResponse
from . models import fruit
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    fruit1=fruit.objects.all()
    context={'fruit_list':fruit1}
    return render(request,'index.html',context)
def detail(request,fruit_id):
    fruit2=fruit.objects.get(id=fruit_id)
    # return HttpResponse('this is movie number %s' % movie_id)
    return render(request,'detail.html',{'fruit1':fruit2})
def index2(request):
    return render(request,'order.html')






def add_fruit(request):
    if request.method=='POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)

        img=request.FILES['img']
        fruit1=fruit(name=name,desc=desc,img=img)
        fruit1.save()
    return render(request,'add.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        Cpassword = request.POST['password1']

        if password==Cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')

            else:

                user=User.objects.create_user(username=username,password=password)
                user.save();
                print('user created')
                return redirect('login')
            print('user created')
        else:
            messages.info(request,'Incorrect password')
            return redirect('register')
        return redirect('/')
    return render(request,'registration.html')

def logout(request):
    auth.logout(request)
    return redirect('/')




def order(request):
    if request.method=='POST':
        username=request.POST['username']
        Phonenumber=request.POST['Phonenumber']

        user=auth.authenticate(username=username,Phonenumber=Phonenumber)
        if order is not None:
            auth.user(request,order)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('order')

    return render(request,'cart.html')