from django.contrib.auth import get_user_model, views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import FormView
from django.views.generic.edit import CreateView, UpdateView
from accounts.forms import CustomUserCreationForm, UserProfileForm, AccountsUserPasswordResetForm
from accounts.signals import password_reset_signal, password_changed_signal
from chatbot.models import ConversationChat
from config.permission import UserPermissionMixin



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


class AccountsUserPasswordResetView(FormView):
    template_name = 'Accounts/password_reset_form.html'
    success_url = reverse_lazy('Accounts:password_reset_done')
    form_class = AccountsUserPasswordResetForm

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')

        try:
            user = get_user_model().objects.get(email=email)
            password_reset_signal.send(sender=self.__class__, user=user, request=self.request)
            self.request.session['user_email'] = email
        except get_user_model().DoesNotExist:
            pass

        return response


class AccountsUserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'Accounts/password_reset_done.html'

    def context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_email'] = self.request.session.get('user_email', '')

        if 'user_email' in self.request.session:
            del self.request.session['user_email']
        return context


class AccountsUserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'Accounts/password_reset_confirm.html'
    success_url = reverse_lazy('Accounts:password_reset_complete')

    def dispatch(self, *args, **kwargs):
        self.validlink = False

        try:
            uid = force_str(urlsafe_base64_decode(self.kwargs['uidb64']))
            user = get_user_model().objects.get(pk=uid)
            token = self.kwargs['token']

            if default_token_generator.check_token(user, token):
                self.validlink = True
                self.user = user
        except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
            pass

        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['validlink'] = self.validlink

        return context

    def form_valid(self, form):

        if self.validlink:
            response = super().form_valid(form)
            password_changed_signal.send(sender=self.__class__, user=self.user)

            return response
        return super().form_invalid(form)


class AccountsUserPasswordChangeView(UserPermissionMixin, auth_views.PasswordChangeView):
    template_name = 'Accounts/password_change.html'
    success_url = reverse_lazy('Accounts:password_change_done')

    def get_object(self):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['has_permission'] = self.request.user.is_superuser or self.request.user.pk == self.get_object().pk

        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        password_changed_signal.send(sender=self.__class__, user=self.request.user)

        return response
