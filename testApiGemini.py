import os
import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Diga 'olá mundo' em Dart")
print(response.text)
