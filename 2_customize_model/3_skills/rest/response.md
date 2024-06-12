```python
import requests

url = "https://petstore.swagger.io/v2/store/order"

payload = {
    "id": 0,
    "petId": 0,
    "quantity": 1,
    "shipDate": "2024-06-12T12:34:56.789Z",
    "status": "placed",
    "complete": True
}
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
```
