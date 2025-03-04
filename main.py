import requests

# NASA API Base URL
APOD_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "WEIouyu7zWA7RuTEsuAJPVYTcaKeNyhIGr6Fn6bV"  # Replace with your own API key from https://api.nasa.gov/

# Dictionary to store favorite celestial objects
favorites = {}

def get_apod():
    """Fetch NASA's Astronomy Picture of the Day (APOD)."""
    params = {"api_key": API_KEY}
    response = requests.get(APOD_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return {
            "title": data["title"],
            "date": data["date"],
            "explanation": data["explanation"],
            "image_url": data["url"]
        }
    else:
        print("Failed to fetch APOD.")
        return None

def add_favorite(name, details):
    """Store a celestial object in the favorites collection."""
    favorites[name] = details
dict = get_apod()
add_favorite(dict["title"], dict["image_url"])
print(favorites)