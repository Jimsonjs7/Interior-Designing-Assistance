from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.shortcuts import render
import requests
from PIL import Image
from io import BytesIO
from .utils import detect_objects, get_dominant_color, get_recommendations
import os


def modern(request):
    return render(request, 'modern.html')


def modern_living_room_designs(request):
    return render(request, 'modern_living_room_designs.html')

def modern_bedroom(request):
    return render(request, 'modern_bedroom.html')

def modern_kitchen(request):
    return render(request, 'modern_kitchen.html')

def modern_bathroom(request):
    return render(request, 'modern_bathroom.html')


def classic(request):
    return render(request, 'classic.html')


def classic_livingroom(request):
    return render(request, 'classic_livingroom.html')

def classic_bedroom(request):
    return render(request, 'classic_bedroom.html')

def classic_kitchen(request):
    return render(request, 'classic_kitchen.html')

def classic_bathroom(request):
    return render(request, 'classic_bathroom.html')


from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.shortcuts import render
import requests
from PIL import Image
from io import BytesIO
import os
from .utils import detect_objects, get_dominant_color, get_recommendations  # Make sure these functions are correctly imported

def product_recommendation(request, product_name=None):
    """
    Handle product recommendation by detecting objects in the provided image URL.
    """
    # Get the image URL from the query parameters
    image_url = request.GET.get('image_url', None)
    detected_products = []
    dominant_color = None
    annotated_image_url = None

    # Set a default product name if none is provided
    if not product_name:
        product_name = "Default Product"

    if image_url:
        try:
            # Validate the URL
            validator = URLValidator()
            validator(image_url)

            # Fetch the image from the URL
            response = requests.get(image_url)
            response.raise_for_status()

            # Save the image to a temporary file
            img = Image.open(BytesIO(response.content))
            original_image_path = "media/original_image.jpg"
            img.save(original_image_path)

            # Perform object detection
            detected_products, annotated_image_path = detect_objects(original_image_path)

            # Prepare the URL for the annotated image
            if annotated_image_path:
                annotated_image_url = f"/media/{os.path.basename(annotated_image_path)}"

            # Extract the dominant color
            dominant_color = get_dominant_color(response.content)

        except ValidationError:
            print("Invalid URL provided.")
        except requests.RequestException as e:
            print(f"Error fetching the image: {e}")
        except Exception as e:
            print(f"Error processing image: {e}")

    # Add product images and search URLs for Flipkart, Amazon, and Google Shopping
    product_image_mapping = {
        "chair": "/static/images/products/chair.jpg",
        "potted plant": "/static/images/products/potted_plant.jpg",
        "clock": "/static/images/products/clock.jpg",
    }

    for product in detected_products:
        # Assign image URLs
        product["image_url"] = product_image_mapping.get(
            product["label"], "/static/images/products/default.jpg"
        )

        # Dynamically generate shopping URLs
        search_query = product["label"].replace(" ", "+")  # Replace spaces with '+'
        dominant_color_query = f"+{dominant_color[0]},{dominant_color[1]},{dominant_color[2]}" if dominant_color else ""
        product["search_urls"] = {
            "flipkart": f"https://www.flipkart.com/search?q={search_query}{dominant_color_query}",
            "amazon": f"https://www.amazon.in/s?k={search_query}{dominant_color_query}",
            "google_shopping": f"https://www.google.com/search?tbm=shop&q={search_query}{dominant_color_query}",
        }

    # Prepare the context for rendering the template
    context = {
        "product_name": product_name,
        "image_url": image_url,
        "annotated_image_url": annotated_image_url,
        "detected_products": detected_products,
        "dominant_color": f"rgb({dominant_color[0]}, {dominant_color[1]}, {dominant_color[2]})" if dominant_color else None,
    }

    return render(request, "product_recommendation.html", context)
