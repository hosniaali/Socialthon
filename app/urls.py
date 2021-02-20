# from django.contrib.auth import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .api import *
from .views import index

urlpatterns = [
                  path('', index, name='index'),
                  path('app/api/chatbot', ChatbotAPI.as_view()),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
