import requests
import webbrowser
import webview
import urllib.request
import os
# NASA API Base URL
APOD_URL = "https://api.nasa.gov/planetary/apod"
EARTH_URL = "https://api.nasa.gov/planetary/earth/assets"
API_KEY = "WEIouyu7zWA7RuTEsuAJPVYTcaKeNyhIGr6Fn6bV"
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
            pass
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
       pass
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
  def save_APOD(date):
    '''Saves the APOD permanently via files'''
    try:
        params = {"api_key": API_KEY, "date": date} #Taken from the get apod function
        response = requests.get(APOD_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            if not os.path.exists("Images"): #If the directory does not exist
                os.makedirs("Images") #Create the directroy
            if not os.path.exists(f"Images/{data["title"]}.png"): #If the directory does not exist
              urllib.request.urlretrieve(data["url"], f"Images/{data["title"]}.png") #Grab the image from the site and store it
            else:
               print("Image already exists") #Error handling
    except NameError:
      return "Unable to retrieve image"
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
            pass
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
          pass
     def save_Image(lat,lon,dim,date):
       try:
           params = {"api_key": API_KEY, "lat": lat, "lon": lon, "dim": dim, "date": date} #Refer to the save_APOD function
           response = requests.get(EARTH_URL, params=params)
           if response.status_code == 200:
               data = response.json()
               if not os.path.exists("Images"):
                   os.makedirs("Images")
               n = 0
               if not os.path.exists("Images/Earth_Image.png"):
                 urllib.request.urlretrieve(data["url"], "Images/Earth_Image.png")
               while os.path.exists(f"Images/Earth_image{n}.png"):
                 n+=1
                 if os.path.exists(f"Images/Earth_image{n}.png"):
                   urllib.request.urlretrieve(data["url"], f"Images/Earth_Image{n}.png")
       except NameError:
         return "Unable to retrieve image"
       except requests.exceptions.HTTPError as errh:
            return "An Http Error occurred:" + repr(errh)
       except requests.exceptions.ConnectionError as errc:
           return "An Error Connecting to the API occurred:" + repr(errc)
       except requests.exceptions.Timeout as errt:
           return "A Timeout Error occurred:" + repr(errt)
       except requests.exceptions.RequestException as err:
           return "An Unknown Error occurred" + repr(err)