from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    # check if logging in

    if request.method == 'POST':
            username = request.POST['user']
            password = request.POST['password']

            #check

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Login successful!")
                return redirect('home')
            else:
                messages.success(request, "Login Error!")
                return redirect('home')
    else:
         return render(request, 'home.html', {})



# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "Logout successful!")
    return redirect('home')
    
def register_user(request):
       return render(request, 'register.html', {})
     
