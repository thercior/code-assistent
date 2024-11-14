from django.urls import path, include
from accounts.views import LoginView, LogoutView, RegisterView, UpdateRegisterView


app_name = 'Accounts'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/cadastro/', RegisterView.as_view(), name='register'),
    path('accounts/editar_perfil/<int:pk>', UpdateRegisterView.as_view(), name='update_profile')
]
