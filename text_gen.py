import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("API_KEY")

genai.configure(api_key = API_KEY)

model = genai.GenerativeModel("gemini-1.5-pro")
response = model.generate_content("Write a story about a magic backpack in Turkish.")

file = open("text.txt", 'w', encoding='utf-8')
file.write("-" * 30 + "\n")
file.write(response.text)
file.close()