import requests
BASE_URL =  "https://jsonplaceholder.typicode.com"

def fetch_posts():
    url = f"{BASE_URL}/posts"
    response = requests.get(url, timeout=30)
    response.raise_for_status()
    return response.json()

def fetch_users():
    url=f"{BASE_URL}/users"
    response = requests.get(url,timeout=30)
    response.raise_for_status()
    return response.json()