import os
import requests
from PIL import Image
from io import BytesIO
from colorthief import ColorThief
from ultralytics import YOLO



def detect_objects(image_content_or_url):
    """
    Detect objects in an image using YOLO.
    """
    print("Starting object detection...")
    image_path = None

    # Handle local file paths
    if isinstance(image_content_or_url, str) and os.path.exists(image_content_or_url):
        image_path = image_content_or_url
        print(f"Using local image file: {image_path}")
    elif isinstance(image_content_or_url, bytes):
        image = Image.open(BytesIO(image_content_or_url))
        image_path = "/tmp/temp_image.jpg"
        image.save(image_path)
        print(f"Image saved from bytes to: {image_path}")
    elif isinstance(image_content_or_url, str) and image_content_or_url.startswith("http"):
        try:
            response = requests.get(image_content_or_url)
            response.raise_for_status()
            image = Image.open(BytesIO(response.content))
            image_path = "/tmp/temp_image.jpg"
            image.save(image_path)
            print(f"Image downloaded and saved to: {image_path}")
        except requests.RequestException as e:
            print(f"Error fetching image from URL: {e}")
            return [], None
    else:
        raise ValueError("Invalid input: Provide image content (bytes) or a valid image URL (str).")

    # Proceed with YOLO detection
    ...

    # Load the YOLO model
    print("Loading YOLO model...")
    model = YOLO("yolov8n.pt")  # Ensure the model file is in the correct location
    model.conf = 0.25  # Set confidence threshold

    # Perform object detection
    print(f"Performing object detection on: {image_path}")
    results = model(image_path)
    print(f"YOLO results: {results}")

    # Extract detected objects
    detections = []
    for result in results:
        for box in result.boxes:
            label = box.cls  # Class ID
            confidence = box.conf  # Confidence score

            print(f"Detected: {model.names[int(label)]} with confidence {confidence}")

            # Extract bounding box coordinates
            xyxy = box.xyxy.tolist()[0]  # [x1, y1, x2, y2]

            # Crop the detected object
            img = Image.open(image_path)
            cropped_img = img.crop((xyxy[0], xyxy[1], xyxy[2], xyxy[3]))
            cropped_img_path = os.path.join(
                os.path.dirname(image_path), f"cropped_{model.names[int(label)]}.jpg"
            )
            cropped_img.save(cropped_img_path)
            print(f"Cropped image saved to: {cropped_img_path}")

            # Extract the dominant color using ColorThief
            try:
                color_thief = ColorThief(cropped_img_path)
                dominant_color = color_thief.get_color(quality=1)  # RGB tuple
                print(f"Dominant color: {dominant_color}")
            except Exception as e:
                print(f"Error extracting dominant color: {e}")
                dominant_color = (0, 0, 0)  # Fallback color

            # Create a color-based Google Shopping query
            color_query = f"{dominant_color[0]},{dominant_color[1]},{dominant_color[2]}"
            search_url = f"https://www.google.com/search?q={model.names[int(label)]}+color+{color_query}&tbm=shop"

            # Add detection details
            detections.append({
                "label": model.names[int(label)],
                "confidence": float(confidence),
                "coordinates": box.xywh.tolist(),  # Bounding box (x, y, width, height)
                "search_url": search_url,
                "dominant_color": f"rgb({dominant_color[0]}, {dominant_color[1]}, {dominant_color[2]})"
            })

    # Define the path to save the annotated image
    annotated_image_path = os.path.join(
        os.path.dirname(image_path),
        "annotated_" + os.path.basename(image_path)
    )

    # Save the annotated image
    if results and len(results) > 0:
        print("Saving annotated image...")
        results[0].save(annotated_image_path)
        print(f"Annotated image saved to: {annotated_image_path}")

    return detections, annotated_image_path


def get_dominant_color(image_content):
    """
    Extract the dominant color from image content.
    Args:
        image_content (bytes): Binary content of the image.
    Returns:
        tuple: RGB values of the dominant color.
    """
    try:
        color_thief = ColorThief(BytesIO(image_content))
        return color_thief.get_color(quality=1)
    except Exception as e:
        print(f"Error extracting dominant color: {e}")
        return None


def get_recommendations(detected_products, dominant_color):
    """
    Create recommendations based on detected products and their dominant colors.

    Args:
        detected_products (list): List of detected products.
        dominant_color (tuple): RGB values of the dominant color.

    Returns:
        list: Recommendations with links, names, and confidence scores.
    """
    print("Generating recommendations...")
    recommendations = []
    for product in detected_products:
        recommendations.append({
            "name": product["label"],
            "confidence": product["confidence"],
            "color": f"rgb({dominant_color[0]}, {dominant_color[1]}, {dominant_color[2]})" if dominant_color else "Unknown",
            "link": f"https://www.google.com/search?q={product['label']}&tbm=shop",
        })
    print("Recommendations generated:", recommendations)
    return recommendations
