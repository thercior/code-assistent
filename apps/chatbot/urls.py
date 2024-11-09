from django.urls import path, include
from chatbot.views import ChatBotView


app_name = 'Chatbot'

urlpatterns = [
    path('', ChatBotView.as_view(), name='chatbot')
]
