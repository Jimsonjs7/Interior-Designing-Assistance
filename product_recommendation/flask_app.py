from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained model
model = tf.keras.models.load_model('product_recognition_model.h5')

# Define product-to-URL mapping
product_urls = {
    "product1": "https://example.com/product1",
    "product2": "https://example.com/product2",
    "product3": "https://example.com/product3",
}

# Preprocess the image
def preprocess_image(image):
    image = image.resize((224, 224))  # Adjust size according to your model
    image = np.array(image) / 255.0  # Normalize to [0, 1]
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Define the API endpoint
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']
    try:
        # Load and preprocess the image
        image = Image.open(file)
        processed_image = preprocess_image(image)

        # Make predictions
        predictions = model.predict(processed_image)
        predicted_class = np.argmax(predictions, axis=1)[0]

        # Get the corresponding URL
        product_name = list(product_urls.keys())[predicted_class]
        product_url = product_urls[product_name]

        return jsonify({"product": product_name, "url": product_url})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
