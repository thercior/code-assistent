from django.urls import path, include
from chatbot.views import chatbotview


app_name = 'Chatbot'

urlpatterns = [
    path('', chatbotview, name='chatbot')
]
