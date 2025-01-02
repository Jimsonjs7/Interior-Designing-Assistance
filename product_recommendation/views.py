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
        return render(request, 'online_recommendation.html', 
            { 'uploaded_file_url': uploaded_file_url 
            }) 
    return redirect('online_recommendation.html')

class JdoodleCompileView(APIView):
    """
    API endpoint for compiling code using the Jdoodle compiler.
    """

    def post(self, request):
        serializer = JdoodleCompileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)  # Raise exception for invalid data

        # Extract data from the validated serializer
        script = serializer.validated_data['script']
        language = serializer.validated_data['language']
        stdin = serializer.validated_data.get('stdin', '')  # Optional stdin input
        versionIndex = serializer.validated_data.get('versionIndex', 0)  # Optional version index

        # Replace with your Jdoodle API credentials (ensure they are not exposed in code)
        client_id = 'e1c065ada7c8aec19af3d1c0a3c7d12e'
        client_secret = 'd60c123ec622fd0e5978db72fb489f1769947b2dd0604a2980601131635673c3'

        # Construct the Jdoodle API request URL
        url = 'https://api.jdoodle.com/v1/execute'

        # Prepare request data
        data = {
            'script': script,
            'stdin': stdin,
            'language': language,
            'versionIndex': versionIndex,
            'clientId': client_id,
            'clientSecret': client_secret,
        }

        try:
            # Make the POST request to Jdoodle API
            response = requests.post(url, json=data)
            response.raise_for_status()  # Raise exception for non-200 status codes

            # Handle successful response
            jdoodle_response = response.json()
            return Response(jdoodle_response, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            # Handle errors during API request
            return Response({'error': f'Error calling Jdoodle API: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            # Handle unexpected errors
            return Response({'error': f'Unexpected error: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
def compile_code(self, request):
    serializer = JdoodleCompileSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)  # Raise exception for invalid data

    # Extract data from the validated serializer (same as before)
    # ... your existing code for extracting script, language, etc. ...

    # ... rest of your Jdoodle API request and response handling logic ...