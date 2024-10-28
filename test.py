import requests
import time
import random
while True:
    try : 
        response = requests.get('http://localhost:8000')
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")
    
    
    #print(f"Time sleep {i}")
    time.sleep(random.uniform(0.1, 2))
        