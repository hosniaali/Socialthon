from django.contrib.auth import views
from django.urls import path
from .api import *


urlpatterns = [
    path('app/api/chatbot', ChatbotAPI.as_view()),

]
