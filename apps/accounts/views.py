from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class LoginView(LoginView):
    template_name = 'Accounts/login.html'
    success_url = reverse_lazy('Chatbot:conversation_list')
    redirect_authenticated_user = True

    def get_access_url(self):
        return self.success_url


class LogoutView(LogoutView):
    next_page = reverse_lazy('Accounts:login')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'Accounts/register.html'
    success_url = reverse_lazy('Accounts:login')
