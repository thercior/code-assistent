from django.contrib import admin
from chatbot.models import ConversationChat, Chat
from import_export.admin import ImportExportMixin


@admin.register(Chat)
class ChatAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('conversation__title', 'message', 'response', 'created_at')


@admin.register(ConversationChat)
class ConversationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('user__username', 'title', 'created_at')
