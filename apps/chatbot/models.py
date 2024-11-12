from django.contrib.auth.models import User
from django.db import models
from clients.agent import CodeAssistantAI


class ConversationChat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversations_chat', db_column='conversa_chat', verbose_name='Conversa de chat')
    title = models.CharField(max_length=255, default='', blank=True, db_column='título', verbose_name='título')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversa: {self.title} ({self.user.username})"

    def generate_title(self, initial_message):
        code_assistant = CodeAssistantAI()
        self.title = code_assistant.summarize_title(initial_message)
        self.save()


class Chat(models.Model):
    conversation = models.ForeignKey(ConversationChat, on_delete=models.CASCADE, related_name='chats', db_column='chat', verbose_name='chat')
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Mensagem de {self.conversation.user.username}: {self.message[:50]}'
