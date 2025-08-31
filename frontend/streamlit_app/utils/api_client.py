import requests

BACKEND_URL = "http://localhost:8000"

def get_hello():
    try:
        r = requests.get(f"{BACKEND_URL}/hello")
        if r.status_code == 200:
            return r.json()
        return {"error": "Failed to fetch"}
    except Exception as e:
        return {"error": str(e)}
