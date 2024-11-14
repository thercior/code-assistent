from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from accounts.forms import CustomUserCreationForm, UserProfileForm
from chatbot.models import ConversationChat



class LoginView(LoginView):
    template_name = 'Accounts/login.html'
    success_url = reverse_lazy('Chatbot:conversation_list')
    redirect_authenticated_user = True

    def get_access_url(self):
        return self.success_url


class LogoutView(LogoutView):
    next_page = reverse_lazy('Accounts:login')


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'Accounts/register.html'
    success_url = reverse_lazy('Accounts:login')

    def form_valid(self, form):
        return super().form_valid(form)


class UpdateRegisterView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'Accounts/edit_profile.html'
    success_url = reverse_lazy('Chatbot:conversation_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['conversations'] = self.request.user.conversations_chat.all()
        return context
