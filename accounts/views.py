from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password1']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html',{'error': 'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',{'error': 'Password must match'})
               
    else:
         
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username= request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'Username or Password is incorrect.'})

    else:
        
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method =='POST':
        auth.logout(request)
        return redirect ('home')
    return render(request, 'accounts/signup.html')
