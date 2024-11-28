from django.conf import settings
import requests


class Notify:

    def __init__(self):
        self.__base_url = settings.NOTIFY_URL

    def send_reset_password_event(self, data):
        response = requests.post(
            url=f'{self.__base_url}/password/reset/',
            json=data,
        )

        response.raise_for_status()

    def send_changed_password_event(self, data):
        requests.post(
            url=f'{self.__base_url}/password/changed/',
            json=data,
        )
