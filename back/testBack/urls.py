from django.urls import path
from . import views


urlpatterns = [
    path('GPT/', views.MessageAPIView.as_view(), name='message_api'),
    path('voiture/', views.VoitureAPIView.as_view())
]