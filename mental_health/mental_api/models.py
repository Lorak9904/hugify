from django.db import models

# class UserInput(models.Model):
#     text = models.TextField()
#     emotion = models.CharField(max_length=50, null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)


from django.db import models
from django.contrib.auth.models import User

class MoodLog(models.Model):
    MOOD_CHOICES = [
        ('happy', 'Happy'),
        ('sad', 'Sad'),
        ('stressed', 'Stressed'),
        ('neutral', 'Neutral')
    ]
    
    mood = models.CharField(max_length=10, choices=MOOD_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        return f'{self.mood} - {self.timestamp}'
    


    

    