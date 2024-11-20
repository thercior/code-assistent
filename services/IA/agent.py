from django.conf import settings
from langchain_groq import ChatGroq
from markdown import markdown
from services.IA.system_prompt_message import system_message


class CodeAssistantAI:

    def __init__(self):
        self.__model = ChatGroq(model='llama-3.2-90b-vision-preview')
        self.__system_message = (
            'Você é um assistente de código, responsável por tirar dúvidas sobre programação da Linguagem Python, Django, JavaScript/TypeScript, HTML/CSS, React, Tailwind/Boostrap, Docker, git e GithubActions.'
            'Seu nome é Code Assistant, carinhosamente apelidada de CA'
            'Responda em formato markdown e sempre em português brasileiro.'
        )

    def get_chat_history(self, chats):
        chat_history = []

        for chat in chats:
            chat_history.append(('human', chat.message,))
            chat_history.append(('ai', chat.response,))

        return chat_history

    def ask_ai(self, context, message):
        messages = [
            ('system', self.__system_message)
        ]
        messages.extend(context)
        messages.append(('human', message,))

        response = self.__model.invoke(messages)

        return markdown(response.content, output_format='html')

    def summarize_title(self, initial_message):
        prompt = f"Resuma esta mensagem em um título curto: '{initial_message}'"
        response = self.ask_ai(context="", message=prompt)
        return response.strip()
