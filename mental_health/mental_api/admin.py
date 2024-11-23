from django.contrib import admin

# Register your models here.
#add model
from .models import MoodLog

admin.site.register(MoodLog)