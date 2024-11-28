from django.contrib.auth.tokens import default_token_generator
from django.core.signals import Signal
from django.dispatch import receiver
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from datetime import datetime
from services.Notify.notify import Notify


# Sinal customizado para solicitação de senha
password_reset_signal = Signal()
password_changed_signal = Signal()


@receiver(password_reset_signal)
def password_reset_notify(sender, user, request, **kwargs):
    try:
        token = default_token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        reset_link = request.build_absolute_uri(
            reverse('Accounts:password_reset_confirm', kwargs={'uidb64': uid, 'token': token})
        )

        data = {
            'event_type': 'password_reset_request',
            'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'user_email': user.email,
            'username': user.username,
            'user': f'{user.first_name} {user.last_name}',
            'reset_link': reset_link,
        }

        notify = Notify()
        notify.send_reset_password_event(data)
    except Exception as e:
        print(f'Não foi possível enviar o e-mail de resetar senha. Contate o administrador. Erro {e}')


@receiver(password_changed_signal)
def password_changed_signal_notify(sender, user, **kwargs):
    try:
        data = {
            'event_type': 'password_changed',
            'timestamp': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'user_email': user.email,
            'username': user.username,
            'user': f'{user.first_name} {user.last_name}'
        }

        notify = Notify()
        notify.send_changed_password_event(data)
    except Exception as e:
        print(f'Não foi possível enviar o e-mail de confirmação de alteração de senha. Contate o administrador. erro {e}')
