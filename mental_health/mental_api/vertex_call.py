from vertexai.preview.generative_models import GenerativeModel
import os
import subprocess

# Ustawienie zmiennej środowiskowej
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

# Opis obrazu oraz kontekstu w formie tekstowego prompta
text_prompt = """
nie mam jezyka, ucieli mi go co moge zrobic ?
"""

# Inicjowanie modelu generatywnego
model = GenerativeModel("gemini-pro-vision")

# Generowanie treści na podstawie tekstowego prompta
response = model.generate_content([text_prompt])

# Wyświetlenie wyniku
print(response.candidates[0].content.parts[0].text)