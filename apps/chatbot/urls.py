from django.urls import path, include
from chatbot.views import ChatBotView, ConversationListView, NewConversationView


app_name = 'Chatbot'

urlpatterns = [
    path('chats/', ConversationListView.as_view(), name='conversation_list'),
    path('chats/novo/', NewConversationView.as_view(), name='new_conversation'),
    path('chats/<int:conversation_id>/', ChatBotView.as_view(), name='chat_view'),
]
