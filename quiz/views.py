from django.shortcuts import render
from django.http import JsonResponse

def quiz_home(request):
    """Render the quiz homepage."""
    return render(request, 'quiz_home.html')

def quiz_result(request):
    """Process quiz results and return design suggestions."""
    if request.method == 'POST':
        # Fetch answers from the POST request
        answers = request.POST

        # Initialize style score counters
        style_scores = {
            "modern": 0,
            "classic": 0,
            "minimalist": 0,
            "bohemian": 0
        }

        # Count the votes for each style
        for key, value in answers.items():
            if value in style_scores:
                style_scores[value] += 1

        # Determine the highest-scoring style
        result = max(style_scores, key=style_scores.get)

        # Design suggestions for each style
        suggestions = {
            "modern": "Your style is Modern! Sleek furniture, clean lines, and neutral tones are your go-to elements.",
            "classic": "Your style is Classic! Elegant and timeless designs with bold and bright colors suit you best.",
            "minimalist": "Your style is Minimalist! Simple, clutter-free, and soft pastels define your ideal space.",
            "bohemian": "Your style is Bohemian! Cozy, eclectic, and earthy tones reflect your unique personality."
        }

        # Return the result as JSON for rendering on the frontend
        return JsonResponse({
            "result": result,
            "suggestion": suggestions[result]
        })
    else:
        return JsonResponse({"error": "Invalid request"}, status=400)
