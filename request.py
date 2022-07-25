import requests

test_data = 8 # must be an integer
url = 'http://127.0.0.1:5000/predict_api'
r = requests.post(url,json={"experience":test_data})

print(r.json()) 