from django import forms

class RoomDesignForm(forms.Form):
    prompt = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={'placeholder': 'e.g., Modern living room with wooden flooring', 'class': 'form-control'}),
        label='Room Design Prompt'
    )
