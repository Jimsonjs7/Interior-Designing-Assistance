from ultralytics import YOLO
import os
from PIL import Image
from colorthief import ColorThief
import matplotlib.pyplot as plt

def detect_objects(image_path):
    """
    Detect objects in an image using YOLO, extract dominant colors for each detected object,
    and generate shopping links for Amazon, Flipkart, and Google Shopping.

    Args:
        image_path (str): Path to the input image.

    Returns:
        tuple: A list of detected objects with shopping links, and the path to the annotated image.
    """
    # Load the YOLO model
    model = YOLO('yolov8n')  # YOLOv8 nano version
    model.conf = 0.25  # Set confidence threshold

    # Perform object detection
    results = model(image_path)

    # Extract detected objects
    detections = []
    for result in results:
        for box in result.boxes:
            label = box.cls  # Class ID
            confidence = box.conf  # Confidence score

            # Extract bounding box coordinates
            xyxy = box.xyxy.tolist()[0]

            # Open the image and crop based on the bounding box
            img = Image.open(image_path)
            cropped_img = img.crop((xyxy[0], xyxy[1], xyxy[2], xyxy[3]))
            cropped_img_path = os.path.join(
                os.path.dirname(image_path), f"cropped_{model.names[int(label)]}.jpg"
            )
            cropped_img.save(cropped_img_path)

            # Extract the dominant color using ColorThief
            color_thief = ColorThief(cropped_img_path)
            dominant_color = color_thief.get_color(quality=1)  # RGB tuple

            # Generate shopping URLs
            search_term = f"{model.names[int(label)]} color {dominant_color[0]},{dominant_color[1]},{dominant_color[2]}"
            amazon_url = f"https://www.amazon.in/s?k={search_term.replace(' ', '+')}"
            flipkart_url = f"https://www.flipkart.com/search?q={search_term.replace(' ', '+')}"
            google_shopping_url = f"https://www.google.com/search?tbm=shop&q={search_term.replace(' ', '+')}"

            # Add detection details
            detections.append({
                'label': model.names[int(label)],
                'confidence': float(confidence),
                'coordinates': box.xywh.tolist(),  # Bounding box (x, y, width, height)
                'amazon_url': amazon_url,
                'flipkart_url': flipkart_url,
                'google_shopping_url': google_shopping_url,
                'dominant_color': f"rgb({dominant_color[0]}, {dominant_color[1]}, {dominant_color[2]})"
            })

    # Define the path to save the annotated image
    annotated_image_path = os.path.join(
        os.path.dirname(image_path),
        'annotated_' + os.path.basename(image_path)
    )

    # Save the annotated image if results are available
    if isinstance(results, list) and len(results) > 0:
        results[0].save(annotated_image_path)  # Save the first result with annotations

    return detections, annotated_image_path
