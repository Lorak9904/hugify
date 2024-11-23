
from django.shortcuts import render
from rest_framework import serializers, viewsets
# from .models import UserInput
from google.cloud import aiplatform
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import EmotionForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import MoodLog
from .forms import MoodLogForm
from google.cloud import aiplatform
from decouple import config




from .endpoint import analyze_emotion  

# class UserInputSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserInput
#         fields = '__all__'

# class UserInputViewSet(viewsets.ModelViewSet):
#     queryset = UserInput.objects.all()
#     serializer_class = UserInputSerializer

#     def perform_create(self, serializer):
#         input_text = self.request.data.get('text')
#         emotion = self.get_emotion_from_ai(input_text)
#         serializer.save(emotion=emotion)

#     def get_emotion_from_ai(self, text):
#         aiplatform.init(project='your-project-id', location='us-central1')
#         endpoint = aiplatform.Endpoint('projects/your-project-id/locations/us-central1/endpoints/endpoint-id')
#         response = endpoint.predict([text])
#         return response.predictions[0]['emotion']



def analyze_text(request):
    result = None
    if request.method == 'POST':
        form = EmotionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            result = analyze_emotion(text)  # Call the Vertex AI function
    else:
        form = EmotionForm()
    
    return render(request, 'analyze.html', {'form': form, 'result': result})







# Initialize Vertex AI
aiplatform.init(
    project=config("PROJECT_ID"),
    location=config("REGION")
)

# Define endpoint for emotion detection
def analyze_emotion(text):
    endpoint = aiplatform.Endpoint(endpoint_name=config("ENDPOINT"))
    response = endpoint.predict(instances=[text])
    if response.predictions:
        return response.predictions[0]
    else:
        return "Error: No prediction returned"

# Home view for displaying chat and mood log
def home(request):
    chat_response = None
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        # Send text to AI for emotion analysis
        chat_response = analyze_emotion(user_input)
    
    return render(request, 'home.html', {'chat_response': chat_response})

# Log mood view
def log_mood(request):
    if request.method == "POST":
        selected_mood = request.POST.get("mood")
        # Save mood log in the database
        MoodLog.objects.create(mood=selected_mood)
        return redirect('home')  # Redirect to home after logging mood
    
    return redirect('home')


def log_mood(request):
    if request.method == "POST":
        mood = request.POST.get("mood")
        notes = request.POST.get("notes", "")
        MoodLog.objects.create(user=request.user, mood=mood)
        # Save the data (this could be a database save in a real app)
        messages.success(request, f"Mood '{mood}' logged successfully!")
        return redirect("home")
    return render(request, "mood_tracker.html")


def mood_tracker(request):
    mood_entries = MoodLog.objects.filter(user=request.user).order_by('-date')
    return render(request, 'mood_tracker.html', {'mood_entries': mood_entries})

def mental_health_education(request):
    return render(request, "mental_health_education.html")


def dashboard(request):
    return render(request, "dashboard.html")

def ai_support(request):
    chat_response = None
    if request.method == "POST":
        user_input = request.POST.get("user_input")
        chat_response = analyze_emotion(user_input)  # Use your Vertex AI function here
    return render(request, "ai_support.html", {"chat_response": chat_response})


def resource_hub(request):
    resources = [
        {"title": "Understanding Anxiety", "url": "https://example.com/anxiety"},
        {"title": "Stress Management Techniques", "url": "https://example.com/stress"},
        {"title": "Building Emotional Resilience", "url": "https://example.com/resilience"},
    ]
    return render(request, 'resource_hub.html', {'resources': resources})


# mental_api/views.py
from datetime import date, timedelta

def dashboard(request):
    last_week = date.today() - timedelta(days=7)
    mood_entries = MoodLog.objects.filter(user=request.user, date__gte=last_week)

    mood_summary = {
        "happy": mood_entries.filter(mood="happy").count(),
        "sad": mood_entries.filter(mood="sad").count(),
        "stressed": mood_entries.filter(mood="stressed").count(),
        "neutral": mood_entries.filter(mood="neutral").count(),
    }
    return render(request, 'dashboard.html', {'mood_summary': mood_summary})
