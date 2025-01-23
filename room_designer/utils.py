import openai  # For OpenAI's GPT and DALL·E API
import os
from PIL import Image
from io import BytesIO

openai.api_key = "api"  # Replace with your API key

def design_room_with_prompt(image_path, prompt):
    """
    Generate an updated room design based on the uploaded image and user prompt.
    
    Args:
        image_path (str): Path to the uploaded room image.
        prompt (str): User-provided prompt for the design.

    Returns:
        str: Path to the generated design image.
    """
    try:
        # Load the original image
        with open(image_path, "rb") as f:
            original_image = f.read()

        # Combine the image and prompt for OpenAI's API
        description = f"Based on this room image, {prompt}"
        print(f"AI prompt: {description}")

        # Generate a new design using OpenAI's DALL·E
        response = openai.Image.create(
            prompt=description,
            n=1,
            size="1024x1024",
        )

        # Download the generated image
        generated_image_url = response["data"][0]["url"]
        response = requests.get(generated_image_url)
        response.raise_for_status()

        # Save the generated image locally
        generated_image_path = os.path.join("media", "generated_design.png")
        with open(generated_image_path, "wb") as f:
            f.write(response.content)

        print(f"Generated design saved at: {generated_image_path}")
        return generated_image_path

    except Exception as e:
        print(f"Error generating room design: {e}")
        return None
