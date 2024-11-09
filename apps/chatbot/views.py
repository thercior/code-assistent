from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from langchain_groq import ChatGroq
from markdown import markdown
from chatbot.models import Chat
from clients.agent import CodeAssistantAI


class ChatBotView(View):
    def __init__(self):
        self.code_assistant = CodeAssistantAI()

    def get(self, request, *args, **kwargs):
        chats = Chat.objects.all()
        return render(request, 'chatbot.html', {'chats': chats})

    def post(self, request, *args, **kwargs):
        chats = Chat.objects.all()
        context = self.code_assistant.get_chat_history(chats=chats)

        message = request.POST.get('message')

        response = self.code_assistant.ask_ai(
            context=context,
            message=message,
        )

        chat = Chat(
            message=message,
            response=response,
        )
        chat.save()

        return JsonResponse({
            'message': message,
            'response': response
        })
