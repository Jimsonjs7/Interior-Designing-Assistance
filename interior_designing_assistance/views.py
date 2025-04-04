from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import User 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home.html',{
        'user': request.user
    })

@login_required
def homeloggedin(request):
    user_id = request.session.get('user_id')
    if user_id:
        user = User.objects.get(id=user_id)
        return render(request, 'homeloggedin.html', {
            'user': user
        })
    else:
        messages.error(request, 'You need to log in first.')
        return redirect('login')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password).first()
        if user:
            request.session['user_id'] = user.id
            messages.success(request, 'Login successful')
            return redirect('home')  # Updated redirect to 'home'
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
                password=password,  # Hash the password
                email=email,
                full_name=full_name,  # Assuming full_name is stored in first_name
            )
            messages.success(request, 'Registration successful')
            return redirect('login')
        else:
            messages.error(request, "Username already exists")
    return render(request, 'register.html')

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
        del request.session['username']
        messages.success(request, 'You have been logged out')
    return redirect('login')  # Redirect to login page



@login_required
def viewprofile(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to the login page if not authenticated
    
    user = request.user  # Fetch the currently logged-in user

    context = {
        'username': user.username,
        'email': user.email,
        'full_name': user.get_full_name(),  # If using the default User model's full name method
    }
    return render(request, 'viewprofile.html', context)



@login_required
def updateprofile(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        full_name = request.POST.get('full_name')
        
        user = request.user
        user.username = username
        user.email = email
        user.first_name, user.last_name = full_name.split(' ', 1)
        user.save()
        
        messages.success(request, 'Profile updated successfully!')
        return redirect('viewprofile')
    
    return render(request, 'updateprofile.html', {
        'username': request.user.username,
        'email': request.user.email,
        'full_name': request.user.get_full_name(),
    })


"""
def about(request):
    return render(request, 'dashboard/about.html')

"""