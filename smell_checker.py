import json
import google.generativeai as genai
import os
import time

# Configurar Gemini API
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# Arquivos e smell
JSON_FILE = "posts_dart&testing_tests.json"
MD_FILE = "assertion-roulette.md"
SMELL_NAME = "Assertion Roulette"

# Carregar definição do smell
with open(MD_FILE, "r", encoding="utf-8") as f:
    smell_definition = f.read()

# Carregar JSON
with open(JSON_FILE, "r", encoding="utf-8") as f:
    posts = json.load(f)

# Batch control
REQS_PER_MINUTE = 15
req_count = 0
batch_start_time = time.time()

def check_smell(code, smell_definition, smell_name):
    global req_count, batch_start_time

    # Se atingir limite de 15 requisições, esperar
    if req_count >= REQS_PER_MINUTE:
        elapsed = time.time() - batch_start_time
        if elapsed < 60:
            wait = 60 - elapsed
            print(f"⏱ Limite atingido. Aguardando {wait:.1f}s...")
            time.sleep(wait)
        req_count = 0
        batch_start_time = time.time()

    prompt = f"""
Você é um analisador de código de testes em Dart.

Definição do smell a ser identificado:
{smell_definition}

Código de teste em Dart a ser analisado:
{code}

Pergunta: Este código contém o smell **{smell_name}**?
Responda apenas "SIM" ou "NÃO".
"""
    response = model.generate_content(prompt)
    req_count += 1

    return "SIM" in response.text.strip().upper()

# Percorrer posts
for post in posts:
    if "codigo" in post:
        for snippet in post["codigo"]:
            if check_smell(snippet, smell_definition, SMELL_NAME):
                if "smells" not in post:
                    post["smells"] = []
                if SMELL_NAME not in post["smells"]:
                    post["smells"].append(SMELL_NAME)

# Salvar JSON atualizado
with open(JSON_FILE, "w", encoding="utf-8") as f:
    json.dump(posts, f, indent=4, ensure_ascii=False)

print(f"✅ JSON atualizado com smells '{SMELL_NAME}'.")
