from django.contrib.auth import views as auth_views
from django.urls import path, include
from accounts.views import LoginView, LogoutView, RegisterView, UpdateRegisterView, AccountsUserPasswordResetView, AccountsUserPasswordChangeView, AccountsUserPasswordResetConfirmView, AccountsUserPasswordResetDoneView, AccountsUserPasswordChangeView


app_name = 'Accounts'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/cadastro/', RegisterView.as_view(), name='register'),
    path('accounts/editar_perfil/<int:pk>', UpdateRegisterView.as_view(), name='update_profile'),

    # Rotas para procedimento de reset de senha
    path('accounts/password_reset/', AccountsUserPasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done', AccountsUserPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/password_reset/<uidb64>/<token>/', AccountsUserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Accounts/password_reset_complete.html'), name='password_reset_complete'),

    # Rotas para procedimento de alteração de senha
    path('accounts/password_change/', AccountsUserPasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done', auth_views.PasswordChangeDoneView.as_view(template_name='Accounts/password_change_done.html'), name='password_change_done'),
]
