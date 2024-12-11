from django.shortcuts import render
def home(request):
    return render(request,'home.html')
"""
def contact(request):
    return render(request, 'dashboard/contact.html')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def about(request):
    return render(request, 'dashboard/about.html')

"""