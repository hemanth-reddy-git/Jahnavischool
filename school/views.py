from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    username = request.user.username
    return render(request,"home.html",{'username':username})
def signin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(request,username=username,password=password)
        if user is not None:
            print("working")
            login(request, user)
            return redirect("home")
        else:
            print("not working")
            messages.info(request,"Bad cred")
            return redirect("signin")
    else:
        return render(request,"signin.html")
    
    
def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1 == pass2:
            user = User.objects.create_user(username=username,email=email,password=pass1,first_name=first_name,last_name=last_name)
            user.save()
            messages.success(request,"Your account Is successfully creadted")
            return redirect('signin')
        else:
            messages.info(request,"the password is not matching")
            return redirect('signup')
    else:
        return render(request,"signup.html")

    