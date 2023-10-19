from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        username=request.POST.get('username')
        pswd=request.POST.get('pswd')
        email=request.POST.get('email')

        if(User.objects.filter(username=username)):
            messages.error(request,"Username already exists !")
            return redirect('signup')
        if(User.objects.filter(email=email)):
            messages.error(request,"Email already exists !")
            return redirect('signup')
        myuser=User.objects.create_user(username,email,pswd)
        myuser.save()
        messages.success(request,"Your Account has been successfully created.")
        return redirect('/')
    
    return render(request,'taskdb/Signup.html')


def signin(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method == 'POST':
        username=request.POST.get('username')
        pswd=request.POST.get('pswd')
        user=authenticate(username=username,password=pswd)
        if user is not None:
            login(request,user)
            messages.success(request,"You are Successfully signed in !")
            return redirect('homepage')
        else:
            messages.error(request,"Username or password is incorrect")
            return redirect('/')
    return render(request,'taskdb/Signin.html')

@login_required(login_url='signin')
def homepage(request):
    user = request.user
    return render(request, 'taskdb/homepage.html', {'user': user})

def user_logout(request):
    logout(request)
    messages.success(request,"Successfully Logged Out!")
    return redirect('/')
# Create your views here.
