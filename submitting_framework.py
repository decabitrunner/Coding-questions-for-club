#Getting the inputs
import requests
response = requests.get('http://127.0.0.1:8000/q3')
d = response.json()
model, real_life = list(d['model']),list(d['actual'])
print(model, real_life)