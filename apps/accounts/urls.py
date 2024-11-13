from django.urls import path, include
from accounts.views import LoginView, LogoutView, RegisterView


app_name = 'Chatbot'

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/cadastro/', RegisterView.as_view(), name='register'),
]
