
from django.shortcuts import render
from rest_framework import serializers, viewsets
# from .models import UserInput
from google.cloud import aiplatform

from .forms import EmotionForm
from django.http import HttpResponse



# from .vertex_ai_utils import analyze_emotion  

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

def home(request):
    # return HttpResponse('Hello, World!')
    return render(request, 'home.html')


def analyze_text(request):
    result = None
    if request.method == 'POST':
        form = EmotionForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            result = analyze_emotion(text)  # Call the Vertex AI function
    else:
        form = EmotionForm()
    
    return render(request, 'templates/analyze.html', {'form': form, 'result': result})
