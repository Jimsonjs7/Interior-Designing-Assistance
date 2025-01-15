from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .forms import ImageUploadForm
from .utils import detect_objects
import os
import requests

def online_recommendation(request):
    """
    Handles the online recommendation process by uploading an image,
    running object detection, and displaying the results with links.
    """
    uploaded_file_url = None
    predictions = {}
    annotated_image_url = None

    # Ensure the media directory exists
    media_directory = os.path.join(settings.MEDIA_ROOT)
    if not os.path.exists(media_directory):
        os.makedirs(media_directory)

    # Initialize the image upload form
    form = ImageUploadForm()

    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']

            # Save the uploaded image to the media directory
            file_path = os.path.join(settings.MEDIA_ROOT, image.name)
            with open(file_path, 'wb+') as destination:
                for chunk in image.chunks():
                    destination.write(chunk)

            # Generate URL for the uploaded image
            uploaded_file_url = os.path.join(settings.MEDIA_URL, image.name)

            # Perform object detection
            predictions, annotated_image_path = detect_objects(file_path)

            # Generate a URL for the annotated image
            annotated_image_url = os.path.join(settings.MEDIA_URL, os.path.basename(annotated_image_path))

    return render(request, 'online_recommendation.html', {
        'form': form,
        'uploaded_file_url': uploaded_file_url,
        'annotated_image_url': annotated_image_url,
        'predictions': predictions,
    })


def offline_recommendation(request):
    """
    Renders the offline recommendation page.
    """
    return render(request, 'offline_recommendation.html')


def offline_map_recommendation(request):
    """
    Renders the offline map-based recommendation page.
    """
    return render(request, 'offline_map_recommendation.html')


def upload_image(request):
    """
    Handles image upload and sends the file to a Flask service for predictions.
    """
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image.name, image)
        uploaded_file_url = fs.url(filename)

        # Send the image to a Flask app for predictions
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


def results(request):
    """
    Renders the results page.
    """
    return render(request, 'results.html')


def upload_image_with_detections(request):
    """
    Handles image upload and runs YOLO object detection, saving results to the database (optional).
    """
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save uploaded image
            uploaded_image = form.save()

            # Perform object detection
            detections, annotated_image_path = detect_objects(uploaded_image.image.path)

            # Save detections (optional, if using a model to store detected objects)
            uploaded_image.detected_objects = str(detections)
            uploaded_image.save()

            return render(request, 'results.html', {
                'image_url': uploaded_image.image.url,
                'annotated_image_url': os.path.join(settings.MEDIA_URL, os.path.basename(annotated_image_path)),
                'detections': detections
            })

    else:
        form = ImageUploadForm()

    return render(request, 'recommendation.html', {'form': form})
