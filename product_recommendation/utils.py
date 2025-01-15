from ultralytics import YOLO
import os
from PIL import Image
from colorthief import ColorThief
import matplotlib.pyplot as plt

def detect_objects(image_path):
    """
    Detect objects in an image using YOLO, extract dominant colors for each detected object,
    and generate Google Shopping links with color similarity.

    Args:
        image_path (str): Path to the input image.

    Returns:
        tuple: A list of detected objects with Google Shopping links including color similarity,
               and the path to the annotated image.
    """
    # Load the YOLO model
    model = YOLO('yolov8n')  # Use YOLOv8 nano version
    model.conf = 0.25  # Set confidence threshold (default is 0.25)

    # Perform object detection
    results = model(image_path)

    # Extract detected objects
    detections = []
    for result in results:
        for box in result.boxes:
            label = box.cls  # Class ID
            confidence = box.conf  # Confidence score

            # Extract bounding box coordinates
            xyxy = box.xyxy.tolist()[0]  # [x1, y1, x2, y2]

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

            # Create a color-based Google Shopping query
            color_query = f"{dominant_color[0]},{dominant_color[1]},{dominant_color[2]}"
            search_url = f"https://www.google.com/search?q={model.names[int(label)]}+color+{color_query}&tbm=shop"

            # Add detection details
            detections.append({
                'label': model.names[int(label)],
                'confidence': float(confidence),
                'coordinates': box.xywh.tolist(),  # Bounding box (x, y, width, height)
                'search_url': search_url,
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
        if os.path.exists(annotated_image_path):
            print(f"Annotated image saved at: {annotated_image_path}")
        else:
            print("Failed to save the annotated image!")
    else:
        print("No results to save.")

    return detections, annotated_image_path
