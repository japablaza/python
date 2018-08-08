import requests json

estado = requests.get("http://api.open-notify.org/iss-now.json")

print(estado.status_code)
