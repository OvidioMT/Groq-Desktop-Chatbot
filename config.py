import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

PERSONALIDADES = {
    "Amigable": "Eres un chatbot amigable y servicial.",
    "Serio": "Eres un chatbot serio y profesional.",
    "Sarcástico": "Eres un chatbot sarcástico y bromista.",
    "Motivador": "Eres un chatbot motivador y positivo.",
    "No amigable": "Eres un chatbot no amigable."
}
