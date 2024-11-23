
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
        chat_response = """
1. Practice Gratitude
Write down three things you're grateful for, even if they're small. It could be something as simple as the warmth of your blanket or a good cup of coffee. Focusing on positive things can shift your mindset.

2. Move Your Body
Physical movement, even just a short walk, can release endorphins and improve your mood. If you can, try to get outside and breathe in some fresh air, even if it’s for just five minutes.

3. Listen to Uplifting Music
Music has a powerful impact on our emotions. Find a playlist of songs that make you feel good or are calming. Sometimes, music can speak when words fall short.

4. Limit Social Media
Sometimes, scrolling can make us feel worse. Try taking a short break from social media or setting a time limit. This can help reduce feelings of comparison or anxiety.

5. Be Kind to Yourself
When we’re feeling low, we can be really hard on ourselves. Remind yourself that it’s okay to feel sad sometimes, and that you're doing the best you can. Self-compassion can make a huge difference.

6. Do Something Creative
Whether it's doodling, journaling, cooking, or even organizing something in your space, creative activities can help get your mind off things and give you a sense of accomplishment.

7. Connect with a Friend or Loved One
Even a brief chat with someone you trust can help you feel more connected and supported. Sometimes sharing how you're feeling, even if it's just a little, can lighten the load.

8. Practice Deep Breathing or Meditation
Take five deep breaths, breathing in for a count of four and exhaling for a count of six. This can help lower stress levels and give your mind a reset. You could also try a short guided meditation to help calm your thoughts.

9. Focus on What You Can Control
When things feel overwhelming, focus on small, manageable tasks that are in your control. It can help you regain a sense of agency and accomplishment.

10. Give Yourself a Break
If you've been pushing yourself hard, it might be time for a pause. Take a few minutes (or more) to just rest and recharge—guilt-free. Your well-being matters.

I hope some of these resonate with you! You don’t have to feel positive all the time, but even tiny steps can help lift you up. If you want to talk more, I’m here!

"""
    
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
        chat_response = """
1. Practice Gratitude
Write down three things you're grateful for, even if they're small. It could be something as simple as the warmth of your blanket or a good cup of coffee. Focusing on positive things can shift your mindset.

2. Move Your Body
Physical movement, even just a short walk, can release endorphins and improve your mood. If you can, try to get outside and breathe in some fresh air, even if it’s for just five minutes.

3. Listen to Uplifting Music
Music has a powerful impact on our emotions. Find a playlist of songs that make you feel good or are calming. Sometimes, music can speak when words fall short.

4. Limit Social Media
Sometimes, scrolling can make us feel worse. Try taking a short break from social media or setting a time limit. This can help reduce feelings of comparison or anxiety.

5. Be Kind to Yourself
When we’re feeling low, we can be really hard on ourselves. Remind yourself that it’s okay to feel sad sometimes, and that you're doing the best you can. Self-compassion can make a huge difference.

6. Do Something Creative
Whether it's doodling, journaling, cooking, or even organizing something in your space, creative activities can help get your mind off things and give you a sense of accomplishment.

7. Connect with a Friend or Loved One
Even a brief chat with someone you trust can help you feel more connected and supported. Sometimes sharing how you're feeling, even if it's just a little, can lighten the load.

8. Practice Deep Breathing or Meditation
Take five deep breaths, breathing in for a count of four and exhaling for a count of six. This can help lower stress levels and give your mind a reset. You could also try a short guided meditation to help calm your thoughts.

9. Focus on What You Can Control
When things feel overwhelming, focus on small, manageable tasks that are in your control. It can help you regain a sense of agency and accomplishment.

10. Give Yourself a Break
If you've been pushing yourself hard, it might be time for a pause. Take a few minutes (or more) to just rest and recharge—guilt-free. Your well-being matters.

I hope some of these resonate with you! You don’t have to feel positive all the time, but even tiny steps can help lift you up. If you want to talk more, I’m here!

i very bat at this point


"""
          
        
        
        
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
