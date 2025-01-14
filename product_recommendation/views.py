from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import requests
#from flask import request, render_template, redirect, url_for 
from werkzeug.utils import secure_filename 
import os
from django.conf import settings
from django.shortcuts import render
from .forms import ImageUploadForm
from .utils import detect_objects  # Your YOLO integration

import os
from django.conf import settings

def online_recommendation(request):
    uploaded_file_url = None
    predictions = {}

    # Check if the media directory exists; if not, create it
    media_directory = os.path.join(settings.MEDIA_ROOT)
    if not os.path.exists(media_directory):
        os.makedirs(media_directory)

    # Initialize the form before any conditions
    form = ImageUploadForm()

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            # Define the file path where the image will be saved
            file_path = os.path.join(settings.MEDIA_ROOT, image.name)

            # Save the uploaded image
            with open(file_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            uploaded_file_url = os.path.join(settings.MEDIA_URL, image.name)
            
            # Perform object detection
            predictions, annotated_image_path = detect_objects(file_path)  # Now it returns detections and annotated image path

    return render(request, 'online_recommendation.html', {
        'form': form,
        'uploaded_file_url': uploaded_file_url,
        'predictions': predictions,
    })

def offline_recommendation(request):
    return render(request,'offline_recommendation.html')
def offline_map_recommendation(request):
    return render(request,'offline_map _recommendation.html')

def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)
        
        # Send image to Flask app for predictions
        with open(fs.path(filename), 'rb') as f:
            response = requests.post('http://127.0.0.1:5000/predict', files={'file': f})
        
        if response.status_code == 200:
            predictions = response.json()
        else:
            predictions = {}

        return render(request, 'recommendation.html', {
            'uploaded_file_url': uploaded_file_url,
            'predictions': predictions
        })
    return render(request, 'recommendation.html')
'''
from django.shortcuts import render
from .forms import ImageUploadForm
from .models import UploadedImage
from .utils import detect_objects

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            detections, annotated_image_path = detect_objects(uploaded_image.image.path)

            # Save detections to the model (optional)
            uploaded_image.detected_objects = str(detections)
            uploaded_image.save()

            return render(request, 'results.html', {
                'image_url': uploaded_image.image.url,
                'annotated_image_url': annotated_image_path,
                'detections': detections
            })
    else:
        form = ImageUploadForm()

    return render(request, 'recommendation.html', {'form': form})

'''