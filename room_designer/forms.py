from django import forms

class RoomDesignForm(forms.Form):
    image = forms.ImageField(label="Upload a picture of your room")
    prompt = forms.CharField(
        label="Design Prompt",
        max_length=500,
        widget=forms.Textarea(attrs={"placeholder": "E.g., Add modern furniture and a green rug"}),
        required=False,
    )
