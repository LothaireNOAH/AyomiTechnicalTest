import requests

url = "http://localhost:8000/calculate"
expression = "8 5 *"
payload = {"expression": expression}
response = requests.post(url, json=payload)
if response.status_code == 200:
    result = response.json()
    print("NPI:", result)
else:
    print("Erreur API:", response.text)

