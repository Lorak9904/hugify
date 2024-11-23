from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from mental_api.views import UserInputViewSet
from . import views

# router = DefaultRouter()
# router.register(r'inputs', UserInputViewSet)

urlpatterns = [
    # path('api/', include(router.urls)),
    path('analyze/', views.analyze_text, name='analyze'),
    path('', views.home, name='home'),
    path('log_mood/', views.log_mood, name='log_mood'),
    path('ai-support/', views.ai_support, name='ai_support'),
    path('education/', views.mental_health_education, name='mental_health_education'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('stress-relief/', views.resource_hub, name='stress_relief'),
    path('resources/', views.resource_hub, name='resource_hub'),
]