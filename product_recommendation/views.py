from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import requests
from .serializers import JdoodleCompileSerializer

from flask import request, render_template, redirect, url_for 
from werkzeug.utils import secure_filename 
import os


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


