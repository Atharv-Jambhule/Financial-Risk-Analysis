import requests

url = "http://51.21.196.62:5000/predict"

data = {
    "product": "Chair",
    "unit_price": 50,
    "sales": 20000
}

response = requests.post(url, json=data)

print(response.json())