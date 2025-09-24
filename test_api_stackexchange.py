import requests

url = "https://api.stackexchange.com/2.3/info"
params = {
    "site": "stackoverflow"
}

res = requests.get(url, params=params)
if res.status_code == 200:
    print("API está disponível ✅")
    print("Quota restante:", res.json().get("quota_remaining"))
else:
    print("Problema de acesso ❌", res.status_code)
