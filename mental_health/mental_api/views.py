
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
import random




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
        chat_response = [
    "I'm really sorry that you're feeling this way right now. Please remember that it's completely okay to not feel okay sometimes. Life can be incredibly overwhelming, and it's natural to go through tough periods. Just take things one step at a time, and don't hesitate to reach out if you need someone to talk to. You're not alone in this, and it's okay to lean on others for support.",
    
    "I'm truly sorry you're going through such a difficult time. Please know that it's okay to feel the way you're feeling. Sometimes our minds and hearts need time to heal, and it's important to give yourself the space to do that. You're incredibly strong for acknowledging how you're feeling, and I hope you can find comfort in knowing that this tough time will eventually pass. Please be kind to yourself and take it one day at a time.",
    
    "I'm really sorry that you're struggling. I want you to know that feeling like this doesn't mean you're weak or failing in any way. It's just a part of being human. Everyone goes through difficult moments, and it's okay to experience pain. You deserve to take care of yourself during this time, and it's okay to not have all the answers right now. You're doing the best you can, and that is enough.",
    
    "It sounds like you're carrying a heavy load right now, and I want to remind you that it's okay to feel how you feel. You don't have to push through everything on your own. It's okay to ask for help when you're ready, and you are worthy of care and support. Please take time for yourself, even if it's just in small ways, and know that there are people who care about you and want to help you get through this.",
    
    "I’m so sorry you're feeling this way, but please remember that these tough moments don’t define you. They’re just a chapter in your life, and though it feels impossible right now, things can get better. You're not alone in this, and there are so many people who have gone through similar struggles and found light at the end of the tunnel. Take one step at a time, and don't forget to be gentle with yourself. You deserve peace and healing.",
    
    "I'm really sorry to hear you're struggling right now. It's okay to not feel okay, and it’s important to honor your feelings rather than push them aside. Your mental health matters, and you deserve to feel better. Don't be too hard on yourself, and remember that even small steps toward healing count. You've faced challenges before, and you have the strength to get through this one too. Take your time and know that better days are ahead.",
    
    "I'm so sorry you're feeling like this. Please remember that your emotions are valid, and you're allowed to take a break from everything when you need to. Life can feel really heavy at times, but these feelings will not last forever. You deserve to give yourself grace and patience during this time. If you're able, try to talk to someone you trust or a professional who can help guide you through this. You're doing the best you can, and that’s enough.",
    
    "I'm really sorry that you're going through this, but please know that it’s okay to not be okay. Sometimes life gets so overwhelming that it feels like there's no way out, but that's not the truth. There is hope, and you are worthy of healing. It's important to allow yourself to feel everything you're going through without guilt. Just take one step at a time, and remember that people care about you and are here to support you in whatever way you need.",
    
    "I'm so sorry you're feeling this way, and I want to remind you that it's okay to feel overwhelmed. It's part of being human, and it doesn’t mean you’re failing. It’s okay to have hard days. Please try to be gentle with yourself. Healing takes time, and there's no rush. You are doing your best, and that is enough. It’s important to take breaks and practice self-care, even if it’s just for a few moments each day. Better days are ahead, even if it doesn't feel like it right now.",
    
    "I'm really sorry you're feeling this way, but I want to remind you that you're not alone, even though it might feel like it. It's okay to feel down, and it's okay to ask for help when you need it. Your feelings are valid, and it's important to take care of yourself during difficult times. Please don't hesitate to reach out to someone, whether it's a friend, family member, or a professional. You deserve support, and you deserve to feel better. Take things one step at a time, and know that you're stronger than you think."
]
        chat_response = random.choice(chat_response)
    
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
        MoodLog.objects.create(mood=mood)
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
        chat_response = [
    "I'm really sorry that you're feeling this way right now. Please remember that it's completely okay to not feel okay sometimes. Life can be incredibly overwhelming, and it's natural to go through tough periods. Just take things one step at a time, and don't hesitate to reach out if you need someone to talk to. You're not alone in this, and it's okay to lean on others for support.",
    
    "I'm truly sorry you're going through such a difficult time. Please know that it's okay to feel the way you're feeling. Sometimes our minds and hearts need time to heal, and it's important to give yourself the space to do that. You're incredibly strong for acknowledging how you're feeling, and I hope you can find comfort in knowing that this tough time will eventually pass. Please be kind to yourself and take it one day at a time.",
    
    "I'm really sorry that you're struggling. I want you to know that feeling like this doesn't mean you're weak or failing in any way. It's just a part of being human. Everyone goes through difficult moments, and it's okay to experience pain. You deserve to take care of yourself during this time, and it's okay to not have all the answers right now. You're doing the best you can, and that is enough.",
    
    "It sounds like you're carrying a heavy load right now, and I want to remind you that it's okay to feel how you feel. You don't have to push through everything on your own. It's okay to ask for help when you're ready, and you are worthy of care and support. Please take time for yourself, even if it's just in small ways, and know that there are people who care about you and want to help you get through this.",
    
    "I’m so sorry you're feeling this way, but please remember that these tough moments don’t define you. They’re just a chapter in your life, and though it feels impossible right now, things can get better. You're not alone in this, and there are so many people who have gone through similar struggles and found light at the end of the tunnel. Take one step at a time, and don't forget to be gentle with yourself. You deserve peace and healing.",
    
    "I'm really sorry to hear you're struggling right now. It's okay to not feel okay, and it’s important to honor your feelings rather than push them aside. Your mental health matters, and you deserve to feel better. Don't be too hard on yourself, and remember that even small steps toward healing count. You've faced challenges before, and you have the strength to get through this one too. Take your time and know that better days are ahead.",
    
    "I'm so sorry you're feeling like this. Please remember that your emotions are valid, and you're allowed to take a break from everything when you need to. Life can feel really heavy at times, but these feelings will not last forever. You deserve to give yourself grace and patience during this time. If you're able, try to talk to someone you trust or a professional who can help guide you through this. You're doing the best you can, and that’s enough.",
    
    "I'm really sorry that you're going through this, but please know that it’s okay to not be okay. Sometimes life gets so overwhelming that it feels like there's no way out, but that's not the truth. There is hope, and you are worthy of healing. It's important to allow yourself to feel everything you're going through without guilt. Just take one step at a time, and remember that people care about you and are here to support you in whatever way you need.",
    
    "I'm so sorry you're feeling this way, and I want to remind you that it's okay to feel overwhelmed. It's part of being human, and it doesn’t mean you’re failing. It’s okay to have hard days. Please try to be gentle with yourself. Healing takes time, and there's no rush. You are doing your best, and that is enough. It’s important to take breaks and practice self-care, even if it’s just for a few moments each day. Better days are ahead, even if it doesn't feel like it right now.",
    
    "I'm really sorry you're feeling this way, but I want to remind you that you're not alone, even though it might feel like it. It's okay to feel down, and it's okay to ask for help when you need it. Your feelings are valid, and it's important to take care of yourself during difficult times. Please don't hesitate to reach out to someone, whether it's a friend, family member, or a professional. You deserve support, and you deserve to feel better. Take things one step at a time, and know that you're stronger than you think."
]
        chat_response = random.choice(chat_response)
          
        
        
        
          # Use your Vertex AI function here
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
