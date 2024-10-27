import requests
import time

for i in range(100000000):
    response = requests.get('http://localhost:8000/')
    print(response.text)
    if i%10 == 0 :
        print(f"Time sleep {i}")
        time.sleep(0.2)