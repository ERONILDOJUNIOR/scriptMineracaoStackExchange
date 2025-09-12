import requests
import json

# Endpoint para pegar perguntas
url = "https://api.stackexchange.com/2.3/questions"

# Parâmetros da requisição
params = {
    "site": "stackoverflow",  # site da rede
    "tagged": "microservices;testing",      # a tag que você quer filtrar
    "pagesize": 5,            # pegar só os 5 primeiros resultados
    "order": "desc",
    "sort": "votes"           # ordenar pelos mais votados
}

res = requests.get(url, params=params)
data = res.json()

# Montar lista de resultados simplificados
resultados = []
for item in data.get("items", []):
    resultado = {
        "titulo": item["title"],
        "score": item["score"],
        "views": item["view_count"],
        "respostas": item["answer_count"],
        "tags": item["tags"],
        "link": item["link"]
    }
    resultados.append(resultado)

# Exibir no console
for r in resultados:
    print(r)

# Salvar em JSON
with open("posts_testing.json", "w", encoding="utf-8") as f:
    json.dump(resultados, f, indent=4, ensure_ascii=False)

print("\nResultados salvos em posts_testing.json ✅")
