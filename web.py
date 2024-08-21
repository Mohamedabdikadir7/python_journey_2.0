import requests
from requests.exceptions import ConnectionError, Timeout

url = "https://www.garissauniversity.ac.ke/"

try:
    response = requests.get(url, timeout=10)  # 10 seconds timeout
    print(f"Response Status Code: {response.status_code}")
except ConnectionError as e:
    print(f"Connection error: {e}")
except Timeout as e:
    print(f"Request timed out: {e}")
