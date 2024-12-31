from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
#from django.contrib.auth import logout
from .models import User 
#from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            messages.success(request, 'Login successful')
            return redirect('profile')
        else:
            if not User.objects.filter(username=username).exists():
                messages.error(request, "User does not exist.")
            else:
                messages.error(request, "Incorrect password. Please try again.")

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        email=request.POST.get('email')
        full_name=request.POST.get('full_name')
        if not User.objects.filter(username=username).exists():
            User.objects.create(
                username=username,
                password=password,
                email=email,
                full_name=full_name,
            )
            messages.success(request, 'registration successfull')
            return redirect('login')
        else:
            messages.error(request, "error")
    return render(request, 'register.html')

"""
def about(request):
    return render(request, 'dashboard/about.html')

"""