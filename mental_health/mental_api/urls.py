from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from mental_api.views import UserInputViewSet
from . import views

router = DefaultRouter()
# router.register(r'inputs', UserInputViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('analyze/', views.analyze_text, name='analyze'),
    path('', views.home, name='home'),
]