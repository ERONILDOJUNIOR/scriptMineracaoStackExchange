import requests
import json
import time
import re
from bs4 import BeautifulSoup

# Endpoint da API
url = "https://api.stackexchange.com/2.3/questions"

# Sua chave gerada em Stack Apps
API_KEY = "rl_Rzzb6ghSHRGYESZAr8ANM78QX"

params = {
    "site": "stackoverflow",
    "tagged": "dart;testing", # só perguntas com a tag Dart e testing
    "pagesize": 100,          # máximo por página
    "order": "desc",
    "sort": "creation",       # pode mudar para "votes"
    "filter": "withbody",     # traz o corpo da pergunta
    "key": API_KEY
}

all_results = []
page = 1

# Expressões típicas de testes Dart
padroes = re.compile(r"\b(expect|verify|test\s*\()", re.IGNORECASE)

while True:
    print(f"📥 Buscando página {page}...")
    params["page"] = page
    res = requests.get(url, params=params)
    data = res.json()

    if "items" not in data:
        print("⚠️ Erro:", data)
        break

    for item in data["items"]:
        corpo_html = item.get("body", "")
        soup = BeautifulSoup(corpo_html, "html.parser")

        # Extrair todos blocos <code>
        blocos_codigo = [code.get_text() for code in soup.find_all("code")]
        codigo_unido = "\n".join(blocos_codigo)

        # Verificar se contém padrões de teste
        if padroes.search(codigo_unido):
            resultado = {
                "titulo": item.get("title"),
                "score": item.get("score"),
                "views": item.get("view_count"),
                "respostas": item.get("answer_count"),
                "tags": item.get("tags"),
                "link": item.get("link"),
                "conteudo_html": corpo_html,
                "codigo": blocos_codigo
            }
            all_results.append(resultado)

    # Se não tem mais páginas, para
    if not data.get("has_more", False):
        break

    page += 1
    time.sleep(1.2)  # delay para respeitar rate limit

# Salvar em JSON
with open("posts_dart&testing_tests.json", "w", encoding="utf-8") as f:
    json.dump(all_results, f, indent=4, ensure_ascii=False)

print(f"\n✅ Total de {len(all_results)} perguntas salvas em posts_dart&testing_tests.json")
