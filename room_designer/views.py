from django.shortcuts import render
from .forms import RoomDesignForm
from .utils import design_room_with_prompt
import os

def ai_room_designer(request):
    uploaded_image_url = None
    generated_design_url = None

    if request.method == "POST":
        form = RoomDesignForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image
            image = form.cleaned_data["image"]
            prompt = form.cleaned_data["prompt"]
            image_path = f"media/{image.name}"
            with open(image_path, "wb+") as f:
                for chunk in image.chunks():
                    f.write(chunk)

            uploaded_image_url = f"/media/{image.name}"

            # Use AI to generate the design based on the prompt
            generated_design_path = design_room_with_prompt(image_path, prompt)
            if generated_design_path:
                generated_design_url = f"/media/{os.path.basename(generated_design_path)}"

    else:
        form = RoomDesignForm()

    return render(request, "ai_room_designer.html", {
        "form": form,
        "uploaded_image_url": uploaded_image_url,
        "generated_design_url": generated_design_url,
    })
