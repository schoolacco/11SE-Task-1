import requests
import webbrowser
import webview
import os
# NASA API Base URL
APOD_URL = "https://api.nasa.gov/planetary/apod"
EARTH_URL = "https://api.nasa.gov/planetary/earth/assets"
API_KEY = "qKn4WWrU3fuG9OuhcOOsGo7aFHvIfBC7XLqnqCpH"
class apod:
  #running = False
  def get_apod(date):
      """Fetch NASA's Astronomy Picture of the Day (APOD)."""
      try:
        params = {"api_key": API_KEY, "date": date, "thumbs": True} # nessecary parameters
        response = requests.get(APOD_URL, params=params) # Refers to the APOD
        if response.status_code == 200: #If it gets a response
            data = response.json()
            try: # Usual scenario
             return {
                "title": data["title"],
                "date": data["date"],
                "explanation": data["explanation"],
                "image_url": data["url"]
             }
            except KeyError: #For if there is no image url
               return {
                "title": data["title"],
                "date": data["date"],
                "explanation": data["explanation"],
               }
        else:
            os.system('cls')
            print("The API_Key has been temporarily rate limited, please try again soon")
            print("Or you entered an invalid input (remember that NASA is a day behind)")
            return None #Explaining possible errors
      except requests.exceptions.HTTPError as errh:
          return "An Http Error occurred:" + repr(errh)
      except requests.exceptions.ConnectionError as errc:
          return "An Error Connecting to the API occurred:" + repr(errc)
      except requests.exceptions.Timeout as errt:
          return "A Timeout Error occurred:" + repr(errt)
      except requests.exceptions.RequestException as err:
          return "An Unknown Error occurred" + repr(err) #This error handling was taken from online
  def open_url(date):
    """Open up the APOD's url in the user's default browser"""
    try:
        params = {"api_key": API_KEY, "date": date, "thumbs": True}
        response = requests.get(APOD_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            try:
              return webbrowser.open(data["url"]) #This opens to the image
            except KeyError:
               return webbrowser.open("https://apod.nasa.gov/apod/astropix.html") # In the case that there is no image link it opens directly towards the current APOD
    except NameError:
       print("Unable to retrive Image URL, likely due to rate limits or the APOD does not exist")
       pass #Error handling
  def return_explanation(date):
     """Specifically return the explanation of the APOD from the given date"""
     try:
        params = {"api_key": API_KEY, "date": date} #Taken from the get apod function
        response = requests.get(APOD_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            return data["explanation"]
     except NameError:
       return "Unable to retrieve explanation"
     except requests.exceptions.HTTPError as errh:
          return "An Http Error occurred:" + repr(errh)
     except requests.exceptions.ConnectionError as errc:
         return "An Error Connecting to the API occurred:" + repr(errc)
     except requests.exceptions.Timeout as errt:
         return "A Timeout Error occurred:" + repr(errt)
     except requests.exceptions.RequestException as err:
         return "An Unknown Error occurred" + repr(err)
class Earth:
     def open_image(lat, lon, dim, date):
      """Fetch an Earth picture and open it in a GUI window with pywebview."""
      try:
        params = {"api_key": API_KEY, "lat": lat, "lon": lon, "dim": dim, "date": date}
        response = requests.get(EARTH_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            window = webview.create_window(data["date"], data["url"]) #Opens the image url in a GUI with the title of the image
            webview.start() #Open the GUI
            return window
        else:
            print("Failed to fetch requested image.") #Error handling
            return None
      except NameError:
       pass #Invalid inputs
     def open_url(lat, lon, dim, date):
       """Same as APOD's open url but for earth images"""
       try:
           params = {"api_key": API_KEY, "lat": lat, "lon": lon, "dim": dim, "date": date}
           response = requests.get(EARTH_URL, params=params)
           if response.status_code == 200:
               data = response.json()
               return webbrowser.open(data["url"])
       except NameError:
          print("Unable to access image URL")
          pass   