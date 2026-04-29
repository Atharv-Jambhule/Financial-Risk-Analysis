import requests
url = "http://13.51.204.143:5000/predict"
data = {
    "AbsoluteQuantity": 200,
    "UnitPrice": 100,
    "Year": 2011,
    "MonthNumber": 12,
    "Quarter": 4,
    "Country_United Kingdom": 1
}
response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Raw Response:", response.text)  # 👈 IMPORTANT