from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import CartModel
import re


def login_(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        pasw = request.POST['pasw']

        user = authenticate(username=uname, password=pasw)
        if user:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'login_.html', {'error': True})

    return render(request, 'login_.html',{'login_nav':True})

def valid_pasw(pasw):
    pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'
    return re.match(pattern,pasw)



def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        uname = request.POST['uname']
        pasw = request.POST['pasw']
        try:
            user=User.objects.get(username=uname)
            return render(request, 'register.html', {'error': True})
        
        except:
            pass

        if not valid_pasw(pasw):
            return render(request, 'register.html', {'error': 'Password must be at least 8 characters and include uppercase, lowercase, number and special character'})

        

        user = User.objects.create_user(
            first_name=fname,
            last_name=lname,
            email=email,
            username=uname,
            password=pasw
        )

        return redirect('login_')

    return render(request, 'register.html',{'profile_nav':True})


@login_required
def profile(request):
    cartproductscount = CartModel.objects.filter(host=request.user).count()
    return render(request, 'profile.html', {'cartcount': cartproductscount})


@login_required
def logout_(request):
    logout(request)
    return render(request, 'logout_.html')


@login_required
def change_password(request):
    if request.method == 'POST':
        old = request.POST['old_password']
        new = request.POST['new_password']

        user = request.user
        if user.check_password(old):
            user.set_password(new)
            user.save()
            return redirect('login_')
        else:
            return render(request, 'change_password.html', {'error': True})

    return render(request, 'change_password.html',{'login_nav':True})


def forgot_password(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        new = request.POST['new_password']

        try:
            user = User.objects.get(username=uname)
            user.set_password(new)
            user.save()
            return redirect('login_')
        except User.DoesNotExist:
            return render(request, 'forgot_password.html', {'error': True})

    return render(request, 'forgot_password.html',{'login_nav':True})

@login_required
def updatedetails(request, pk):
    user = User.objects.get(id=pk)

    if request.method == 'POST':
        user.first_name = request.POST['fname']
        user.last_name = request.POST['lname']
        user.email = request.POST['email']
        user.save()
        return redirect('profile')

    return render(request, 'updatedetails.html', {'user': user,'login_nav':True})

