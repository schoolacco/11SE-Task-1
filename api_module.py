import requests
import webbrowser
import webview
# NASA API Base URL
APOD_URL = "https://api.nasa.gov/planetary/apod"
EARTH_URL = "https://api.nasa.gov/planetary/earth/assets"
API_KEY = "WEIouyu7zWA7RuTEsuAJPVYTcaKeNyhIGr6Fn6bV"
# Dictionary to store favorite celestial objects
favorites = {}
class apod:
  #running = False
  def get_apod(date):
      """Fetch NASA's Astronomy Picture of the Day (APOD)."""
      params = {"api_key": API_KEY, "date": date}
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
  def open_image(date):
    try:
        params = {"api_key": API_KEY, "date": date} #The parameters of the APOD, including the API key and the date retrived
        response = requests.get(APOD_URL, params=params) #Retriving from the APi
        if response.status_code == 200: #Checking if everything is working as intended
            data = response.json() #Converts data to json
            window = webview.create_window(data["title"], data["url"]) #Opens the image url in a GUI with the title of the image
            webview.start() #Open the GUI
            return window
    except NameError:
       pass #For invalid inputs
  def open_url(date):
    try:
        params = {"api_key": API_KEY, "date": date}
        response = requests.get(APOD_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return webbrowser.open(data["url"])
    except NameError:
       print("Unable to retrive Image URL")
       pass
  def return_explanation(date):
     try:
        params = {"api_key": API_KEY, "date": date}
        response = requests.get(APOD_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return data["explanation"]
     except NameError:
       return "Unable to retrieve explanation"
class Earth:
     def open_image(lat, lon, dim, date):
      """Fetch an Earth picture."""
      try:
        params = {"api_key": API_KEY, "lat": lat, "lon": lon, "dim": dim, "date": date}
        response = requests.get(EARTH_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            window = webview.create_window(data["date"], data["url"]) #Opens the image url in a GUI with the title of the image
            webview.start() #Open the GUI
            return window
        else:
            print("Failed to fetch requested image.")
            return None
      except NameError:
       pass
     def open_url(lat, lon, dim, date):
       try:
           params = {"api_key": API_KEY, "lat": lat, "lon": lon, "dim": dim, "date": date}
           response = requests.get(EARTH_URL, params=params)
           if response.status_code == 200:
               data = response.json()
               return webbrowser.open(data["url"])
       except NameError:
          print("Unable to access image URL")
          pass   