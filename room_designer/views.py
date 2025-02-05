import requests
from django.shortcuts import render
from django.conf import settings
from .forms import RoomDesignForm  # Import the form
from dotenv import load_dotenv
import os
import requests
from django.conf import settings

STABILITY_API_KEY = settings.STABILITY_API_KEY

# Load environment variables from the .env file
load_dotenv()

# Get the API key from the environment variable
STABILITY_API_KEY = os.getenv("STABILITY_API_KEY")

def results(request):
    """
    Renders the offline recommendation page.
    """
    return render(request, 'results.html')

def ai_room_designer(request):
    """Render the main AI Room Designer page."""
    form = RoomDesignForm()
    return render(request, "ai_room_designer.html", {"form": form})



def generate_image(request):
    """Handles image generation with Stability AI."""
    if request.method == "POST":
        form = RoomDesignForm(request.POST)  # Handle form submission

        if form.is_valid():  # Ensure form input is valid
            prompt = form.cleaned_data['prompt']

            headers = {
                "Authorization": f"Bearer {settings.STABILITY_API_KEY}",
                "Accept": "application/json",  # We expect JSON response
            }

            # Prepare the payload and files for multipart/form-data
            files = {
                'prompt': (None, prompt, 'text/plain'),  # Send the prompt as a plain text file
                'steps': (None, '50'),
                'width': (None, '1024'),
                'height': (None, '1024'),
                'cfg_scale': (None, '7.5')
            }

            # Send the POST request with 'multipart/form-data' encoding
            response = requests.post(
                "https://api.stability.ai/v2beta/stable-image/generate/sd3",
                headers=headers,
                files=files
            )

            # Print the entire response for debugging
            print(f"Status Code: {response.status_code}")
            response_data = response.json()

            # Log the complete structure of the response
            print("Full Response:", response_data)

            # Check if the 'image' key contains the generated image
            image_data = response_data.get('image', None)

            if image_data:
                # If the image is in base64 format, create a data URL for the image
                image_data_url = f"data:image/png;base64,{image_data}"
                return render(request, "results.html", {"image_data_url": image_data_url})
            else:
                error_msg = response_data.get("error", "Image generation failed. No image returned.")
                return render(request, "ai_room_designer.html", {"form": form, "error": error_msg})

        else:
            return render(request, "ai_room_designer.html", {"form": form, "error": "Invalid input. Please try again."})

    return render(request, "ai_room_designer.html", {"form": RoomDesignForm()})
