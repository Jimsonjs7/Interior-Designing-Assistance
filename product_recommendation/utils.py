from ultralytics import YOLO
import os
from PIL import Image
import matplotlib.pyplot as plt

def detect_objects(image_path):
    """
    Detect objects in an image using YOLO, save the annotated image, 
    and display the detections under the image.

    Args:
        image_path (str): Path to the input image.

    Returns:
        tuple: A list of detected objects and the path to the annotated image.
    """
    # Load the YOLO model
    model = YOLO('yolov8n')  # Use YOLOv8 nano version
    model.conf = 0.25  # Set confidence threshold (default is 0.25)

    # Perform object detection
    results = model(image_path)  # Detect objects in the image

    # Extract detected objects
    detections = []
    for result in results:
        for box in result.boxes:
            label = box.cls  # Class ID
            confidence = box.conf  # Confidence score
            detections.append({
                'label': model.names[int(label)],
                'confidence': float(confidence),
                'coordinates': box.xywh.tolist()  # Bounding box (x, y, width, height)
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

    # Display the annotated image and the detected products
    try:
        img = Image.open(annotated_image_path)
        plt.figure(figsize=(10, 8))

        # Display annotated image
        plt.subplot(2, 1, 1)  # Two rows, one column, first plot
        plt.imshow(img)
        plt.axis('off')
        plt.title("Annotated Image")

        # Display detected products
        plt.subplot(2, 1, 2)  # Two rows, one column, second plot
        product_texts = "\n".join(
            [f"{det['label']} (Confidence: {det['confidence']:.2f})" for det in detections]
        )
        plt.text(0.5, 0.5, product_texts, fontsize=12, ha='center', va='center', wrap=True)
        plt.axis('off')
        plt.title("Detected Products")

        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Could not display the annotated image or detections: {e}")

    return detections, annotated_image_path
