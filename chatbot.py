from groq import Groq
from config import API_KEY, PERSONALIDADES

class Chatbot:
    def __init__(self, personalidad):
        self.client = Groq(api_key=API_KEY)
        self.personalidad = personalidad
        self.messages = [{"role": "system", "content": PERSONALIDADES[self.personalidad]}]

    def set_personalidad(self, personalidad):
        self.personalidad = personalidad
        self.messages = [{"role": "system", "content": PERSONALIDADES[self.personalidad]}]

    def add_user_message(self, content):
        self.messages.append({"role": "user", "content": content})

    def get_response(self):
        completion = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=self.messages
        )
        respuesta = completion.choices[0].message.content
        self.messages.append({"role": "assistant", "content": respuesta})
        return respuesta

    def clear(self):
        self.messages = [{"role": "system", "content": PERSONALIDADES[self.personalidad]}]
