from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from chatbot.models import Chat, ConversationChat
from services.IA.agent import CodeAssistantAI


class ConversationListView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        conversations = request.user.conversations_chat.all().order_by('-created_at')
        return render(request, 'Chatbot/conversations_list.html', {'conversations': conversations})


class NewConversationView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        conversation = ConversationChat.objects.create(
            user=request.user,
            title='',
        )
        return redirect('Chatbot:chat_view', conversation_id=conversation.id)


class ChatBotView(LoginRequiredMixin, View):
    def __init__(self):
        self.code_assistant = CodeAssistantAI()

    def get(self, request, conversation_id, *args, **kwargs):
        conversations = request.user.conversations_chat.all().order_by('-created_at')
        conversation = get_object_or_404(ConversationChat, id=conversation_id, user=request.user)
        chats = conversation.chats.all().order_by('-created_at')
        return render(
            request,
            'Chatbot/chatbot.html',
            {
                'chats': chats,
                'conversation': conversation,
                'conversation_selected': conversation_id,
                'conversations': conversations
            }
        )

    def post(self, request, conversation_id, *args, **kwargs):
        conversation = get_object_or_404(ConversationChat, id=conversation_id, user=request.user)
        message = request.POST.get('message')

        chats = conversation.chats.all().order_by('-created_at')
        context = self.code_assistant.get_chat_history(chats=chats)

        response = self.code_assistant.ask_ai(
            context=context,
            message=message,
        )

        chat = Chat(
            conversation=conversation,
            message=message,
            response=response,
        )
        chat.save()

        if not conversation.title:
            conversation.generate_title(initial_message=message)

        return JsonResponse({
            'message': message,
            'response': response
        })
