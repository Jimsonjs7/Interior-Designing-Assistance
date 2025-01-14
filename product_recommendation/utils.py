from ultralytics import YOLO
import os

def detect_objects(image_path):
    # Load the YOLO model
    model = YOLO('yolov8n')  # Choose a YOLO model (e.g., yolov8n.pt for nano version)

    # Perform object detection
    results = model(image_path)  # This returns a list of results

    # Get detected objects
    detections = []
    for result in results:  # Iterate over the results list
        for box in result.boxes:
            label = box.cls  # Class ID
            confidence = box.conf  # Confidence
            detections.append({
                'label': model.names[int(label)],
                'confidence': float(confidence),
                'coordinates': box.xywh.tolist()  # Bounding box (x, y, width, height)
            })

    # Save annotated image (using the first result object in the list)
    annotated_image_path = os.path.join(os.path.dirname(image_path), 'annotated_' + os.path.basename(image_path))

    # Fixing the issue: Access the first result object in the list and save the image
    if isinstance(results, list) and len(results) > 0:
        # Accessing the first result object (assuming it contains the annotations)
        results[0].save(annotated_image_path)  # Save the annotated image directly

    return detections, annotated_image_path
