from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
#from django.contrib.auth import logout
from .models import User 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


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
            return redirect('viewprofile')
        else:
            if not User.objects.filter(username=username).exists():
                messages.error(request, "User does not exist.")
            else:
                messages.error(request, "Incorrect password. Please try again.")

    return render(request, 'login.html')
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        if not User.objects.filter(username=username).exists():
            User.objects.create(
                username=username,
                password=make_password(password),  # Hash the password
                email=email,
                full_name=full_name,  # Assuming full_name is stored in first_name
            )
            messages.success(request, 'Registration successful')
            return redirect('login')
        else:
            messages.error(request, "Username already exists")
    return render(request, 'register.html')


@login_required
def viewprofile(request):
    user = request.user  # Fetch the currently logged-in user
    context = {
        'username': user.username,
        'email': user.email,
        'full_name': user.get_full_name(),  # If using the default User model's full name method
    }
    return render(request, 'viewprofile.html', context)

"""
def about(request):
    return render(request, 'dashboard/about.html')

"""