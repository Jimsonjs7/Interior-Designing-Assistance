from django.shortcuts import render, redirect 
from django.core.files.storage import FileSystemStorage

def online_recommendation(request):
    return render(request,'online_recommendation.html')
def offline_recommendation(request):
    return render(request,'offline_recommendation.html')
def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image'] 
        fs = FileSystemStorage() 
        filename = fs.save(image.name, image) 
        uploaded_file_url = fs.url(filename) 
        return render(request, 'online_recommendation.html', 
            { 'uploaded_file_url': uploaded_file_url 
            }) 
    return redirect('online_recommendation.html')