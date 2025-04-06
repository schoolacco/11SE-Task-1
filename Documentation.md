# 11 Software Engineering Task 1 Documentation

---

## Functional Requirements

---

### Data Retrieval

---

1. The user must be capable of obtaining the Astronomy Picture Of the Day and any related data including the title, date and explanation of what the picture is. They must be capable of retriving this data for any previous APOD dates.
2. It should be able of accessing NASA's photos of Earth.
(More would be done... but rate limits exist prohibiting use of a majority of the API's uses)

---

### User Interface

---

The user must be capable of interacting with the system via a tkinter GUI, with seperate tabs for each individual function of the program. They must be capable of viewing the generated images or data within the GUI, the GUI must also be capable of presenting Errors caused by user input or general API issues.

---

### Data Display

---

The user must be capable of retrieving the daily APOD of any date and the explanation of what it is from the system, the user must also be capable of opening the link to the APOD in the case they wish to save the image for personal use. The user should also be capable of retriving some of NASA's earth photos (high chance it'll fail due to the API's limitations) and opening a link to the image to save for personal use.

---
---

## Non-Functional Requirements

---

### Performance

---

The program should be able to access and load anything from the priorly mentioned sections of the NASA API in a matter of seconds (unless rate limited). It shouldn't require multiple attempts to access one piece of data (unless ratelimited).

---

### Reliability

---

The system must be consistently functional (unless rate-limited) explaining any possible issues that may have occured and it should always be capable of accessing the most recent daily APOD immediately and access any specific date if desired without issue.

---

### Usability and Accessibility

---

The system must be easily navigatable to the degree such that it is immediately clear what is required for the user to do and the definition of a valid input is immediately clear, it should also be obvious on how to access each tab of the GUI and what each button does.

---
---

## Functional Specifications

---
---

### User Requirements

---

The user must be capable of:

1. Accessing the daily APOD
2. Accesing the explanation of the daily APOD
3. Opening the image URL of the daily APOD from within the program
4. Doing 1-3 with the APOD of any previous dates
5. Access NASA's earth images service
6. Doing 3 but with the NASA earth images service

---

### Inputs and Outputs

---

The program will be capable of recieving the following inputs:

1. The date for the select APOD
2. The date for the NASA earth images service
3. The latitude for the NASA earth images service
4. The longtitude for the NASA earth images service
5. The dimensions (1 number) for the NASA earth images service

and the following outputs:

1. The daily APOD
2. The APOD of any previous date
3. The APOD explanation for any date
4. The NASA earth images
5. The image URLs for 1,2 and 4

---

### Core Features

---

The program must essetinally be capable of accessing the daily APOD (and its explanation) and the APOD and explanation of any previous date and load all of these within the GUI itself whilst also letting the user open the image link with the press of a button. The program must also be capable of accessing the NASA earth images service, load those images within a GUI and finally open the image URL with the press of a button.

---

### User interaction

---

The user will interact with the program via a tkinter GUI, using buttons and tkinter entry boxes and text boxes to allow the user to interact with the program, it must provide information such as the nessecary formatting for inputs to allow the user to enter in their input in a format that can be used.

---

### Error Handling

---

Several errors may occur whilst the program is running, these may be due to invalid user input or issues with accessing the API itself (such as rate limiting), luckily the requests module has several built in exceptions to handle these errors and any further errors can be accounted for (such as recieving nothing due to rate limiting via a KeyError exception).

---
---

## Non-Functional Specifications

---
---

### Performance (Specifications)

---

The program should be capable of running most functions (that don't rely heavily on accessing the web) in under a second (I cannot fix bad internet), this can be done by minimising the steps functions go through to complete a simple task and with some simple optimisations (such as using less global variables).

---

### Usability/Accessibility

---

The program could be made more accessible by using simple colours that contrast each other, ensuring that the user is capable of seeing it even with poor eyesight, the text should not be tiny to allow for ease of reading.

---

### Reliability (Specifications)

---

The program could suffer from an API retrival crash, the best that can be done is to simply warn the user when it has happened, not much else is required as it doesn't save user data.

---
---

## Use Cases

---
---

### Data Retrieval (Use Case)

---

Actor: User
Preconditions: Internet Access, NASA API is available
Main Flow:

1. User opens GUI, and chooses one of the tabs
2. User enters in the nessecary parameters for the image, system retrives image and shows the user it
3. User opens the image in their browser, potentially to save for their own purpose or to interact with it (given it is an interactive image)

Postconditions: User has saved image for their usage or viewed the image for their leisure.

---

### User Interface (Use Case)

---

Actor: System
Preconditions: Dependecies have been downloaded
Main Flow:

1. System sets up GUI using TTK notebook system
2. System adds required buttons and corresponding functions
3. System loads current APOD into HTMLframe
4. User joins

Postconditions: User Interface has been set up

---

### Data Display (Use Case)

---

Actor: User
Preconditions: Connected to internet, NASA API is available
Main Flow:

1. User presses button within GUI
2. System accesses NASA API
3. System takes image URL
4. System inserts image into HTMLframe for user viewing
5. User presses button within GUI to open image link
6. System use image URL to open the link in User's default web browser.

Postconditions: Image is in HTMLframe and open in User's default browser.

---
---

## Design

---
---

## Development

---
---

### Example 1

---

```Python
from api_module import apod
from tkinter import *
root = Tk()
root.title('APOD GUI')
root.configure(bg='black')
root.maxsize(2000,2000)
root.minsize(400,400)
root.geometry("400x400+120+50")
Label(root, text="Welcome to this system", bg="black", fg="white").pack()
Label(root, text="\n", bg="black", fg="white").pack()
Button(root, text="Open Image", bg="black", fg="white", command=lambda: apod.open_image(date_input.get())).pack()
Button(root, text="Open the APOD url", bg="black", fg="white", command=lambda: apod.open_url(date_input.get())).pack()
Label(root, text="\n", bg="black", fg="white").pack()
Label(root, text="Date input (YYYY-MM-DD)", bg="black", fg="white").pack()
date_input = Entry(root, bg="black", fg="white")
date_input.pack()
Label(root, text="\n", bg="black", fg="white").pack()
Button(root, text="Quit :(", fg='white', bg="dark blue", command=lambda: root.destroy()).pack()
Label(root, text="\n", bg="black", fg="white").pack()
bg = PhotoImage(file="stars.png") 
canvas = Canvas(root, width=500, height=500)
canvas.pack()
canvas.create_image( 0, 0, image = bg,  
                     anchor = "nw") 
root.mainloop()

```

---

### Example 2

---

```Python
from api_module import apod, Earth
from tkinter import *
from tkinter import ttk
from tkinterweb import *
def explanation(date):
  global txt
  try:
    txt.insert(1.0, apod.return_explanation(date))
  except TclError:
    pass #For invalid inputs
def display(date):
  global frame, canvas
  try:
    apod.get_apod(date)["image_url"] #A buffer to instantly cause an error in the case of an invalid input, I have tried turning it into a variable but it doesn't function as intended
    frame.destroy()
    frame = HtmlFrame(canvas, horizontal_scrollbar="auto", messages_enabled = False)
    frame.load_website(apod.get_apod(date)["image_url"])
    frame.pack(fill="both", expand=True)
  except TypeError:
    pass #For invalid inputs
root = Tk()
root.title('NASA API')
root.configure(bg='black')
root.maxsize(1000,1000)
root.minsize(1000,1000)
notebook = ttk.Notebook(root)
s = ttk.Style()
s.configure('Apod_frame.TFrame', background="black")
Apod_frame = ttk.Frame(notebook, width=2000, height=2000, style='Apod_frame.TFrame')
Label(Apod_frame, text="Welcome to this system", bg="black", fg="white").pack()
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
Button(Apod_frame, text="Open Image", bg="black", fg="white", command=lambda: display(date_input.get())).pack()
Button(Apod_frame, text="Open the APOD url", bg="black", fg="white", command=lambda: apod.open_url(date_input.get())).pack()
Button(Apod_frame, text="Read APOD explanation", bg="black", fg="white", command=lambda: explanation(date_input.get())).pack()
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
Label(Apod_frame, text="Date input (YYYY-MM-DD)", bg="black", fg="white").pack()
date_input = Entry(Apod_frame, bg="black", fg="white")
date_input.pack()
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
Button(Apod_frame, text="Quit :(", fg='white', bg="dark blue", command=lambda: root.destroy()).pack()
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
txt = Text(Apod_frame, bg = "black", fg= "white", width=101, height=10)
txt.pack()
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
canvas = Canvas(Apod_frame, width=800, height=800)
frame = HtmlFrame(canvas, horizontal_scrollbar="auto", messages_enabled = False)
frame.load_website(apod.get_apod(date_input.get())["image_url"])
frame.pack(fill="both", expand=True)
canvas.pack()
Apod_frame.pack(fill='both', expand=True)
notebook.add(Apod_frame, text="APOD")
# ------------ EARTH IMAGES ----------------
Earth_frame = ttk.Frame(notebook, width=2000, height=2000, style='Apod_frame.TFrame')
Label(Earth_frame, text="WARNING: THERE IS AN INCREDIBLY HIGH CHANCE THIS WILL FAIL AS THE API IS VERY LIMITED IN THIS REGARD", bg="black", fg="crimson").pack()
Label(Earth_frame, text="\n", bg="black", fg="white").pack()
Button(Earth_frame, text="Open Image", bg="black", fg="white", command=lambda: Earth.open_image(lat.get(), lon.get(), dim.get(), date_input2.get())).pack()
Button(Earth_frame, text="Open the Image url", bg="black", fg="white", command=lambda: Earth.open_url(lat.get(), lon.get(), dim.get(), date_input2.get())).pack()
Label(Earth_frame, text="\n", bg="black", fg="white").pack()
Label(Earth_frame, text="Date input (YYYY-MM-DD)", bg="black", fg="white").pack()
date_input2 = Entry(Earth_frame, bg="black", fg="white")
date_input2.pack()
Label(Earth_frame, text="\n", bg="black", fg="white").pack()
Label(Earth_frame, text="Enter in the latitude of the image", bg="black", fg="white").pack()
lat = Entry(Earth_frame, bg="black", fg="white")
lat.pack()
Label(Earth_frame, text="Enter in the longtitude of the image", bg="black", fg="white").pack()
lon = Entry(Earth_frame, bg="black", fg="white")
lon.pack()
Label(Earth_frame, text="Enter in the dimensions of the image (only one number)", bg="black", fg="white").pack()
dim = Entry(Earth_frame, bg="black", fg="white")
dim.pack()
Label(Earth_frame, text="\n", bg="black", fg="white").pack()
Button(Earth_frame, text="Quit :(", fg='white', bg="dark blue", command=lambda: root.destroy()).pack()
Label(Earth_frame, text="\n", bg="black", fg="white").pack()
bg2 = PhotoImage(file="Earth.png") 
canvas2 = Canvas(Earth_frame, width=750, height=750)
canvas2.pack()
canvas2.create_image( 0, 0, image = bg2, anchor="nw") 

Earth_frame.pack(fill='both', expand=True)
notebook.add(Earth_frame, text="Earth Imagery")
notebook.pack(expand=True)
root.mainloop()
```

---

### Final

---

```Python
from api_module import apod, Earth #Importing from my module
from tkinter import * # Import everything
from tkinter import ttk #Specifically import ttk (* doesn't import it)
from tkinterweb import * # Import everything for better tkinterhtml
def explanation(date):
  """Insert the explanation for the APOD into a textbox"""
  global txt #Tkinter textbox is global
  try:
    txt.delete(1.0, END) #Remove text
    txt.insert(1.0, apod.return_explanation(date)) # Fill it with explanation
  except TclError:
    pass #For invalid inputs
def display(date):
  global frame, canvas, txt
  """Insert the the APOD into a html frame"""
  try:
    apod.get_apod(date)["image_url"] #A buffer to instantly cause an error in the case of an invalid input, I have tried turning it into a variable but it doesn't function as intended
    frame.destroy() #Destroy the frame
    frame = HtmlFrame(canvas, horizontal_scrollbar="auto", messages_enabled = False) #Create the html frame, scrollable in the case the image is too large
    frame.load_website(apod.get_apod(date)["image_url"]) # Load the image
    frame.pack(fill="both", expand=True) # Add to frame
  except KeyError:
    frame.load_website("https://www.google.com/APOD_URL_Inaccessible") #This just causes an Error404 message to appear
    frame.pack(fill="both", expand=True)
    txt.delete(1.0,END) # Remove text
    txt.insert(1.0, "There was an error with accessing the APOD, it likely uses a video without a thumbnail.") #Error message
  except TypeError:
    pass # Handle invalid inputs
"""Setting up the GUI"""
root = Tk() # GUI
root.title('NASA API') #Title
root.configure(bg='black') #bg color
root.maxsize(1000,1000) # Maximum size
root.minsize(500,500) # Minimum size
root.geometry('500x500+120+100')
notebook = ttk.Notebook(root) #This allows for creation of tabs
s = ttk.Style() #This has to be a variable for whatever reason
s.configure('Apod_frame.TFrame', background="black") #Change Style() to create bgs for frames
"""Set up the APOD tab"""
Apod_frame = ttk.Frame(notebook, width=2000, height=2000, style='Apod_frame.TFrame') #Create a tab in the notebook
Label(Apod_frame, text="Welcome to this system \n Just know that if anything is ever blank it is due to rate limits from NASA", bg="black", fg="white").pack() #Intro text
Label(Apod_frame, text="\n", bg="black", fg="white").pack() #Add space
Button(Apod_frame, text="Open Image", bg="black", fg="white", command=lambda: display(date_input.get())).pack() #Apod commands
Button(Apod_frame, text="Open the APOD url", bg="black", fg="white", command=lambda: apod.open_url(date_input.get())).pack()
Button(Apod_frame, text="Read APOD explanation", bg="black", fg="white", command=lambda: explanation(date_input.get())).pack() # Refer to the respective functions, lambda is required to allow for the functions to require variables and cause them to not run instantly
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
Label(Apod_frame, text="Date input (YYYY-MM-DD)", bg="black", fg="white").pack() # An explanation of the nessecary format
date_input = Entry(Apod_frame, bg="black", fg="white") # Allows for an input within the GUI
date_input.pack()
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
Button(Apod_frame, text="Quit :(", fg='white', bg="dark blue", command=lambda: root.destroy()).pack() # A button to end the program
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
txt = Text(Apod_frame, bg = "black", fg= "white", width=101, height=10) # This creates a text box which can be edited by the user or have things inserted into it
txt.pack()
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
canvas = Canvas(Apod_frame, width=800, height=800) # This just creates a border for the image
frame = HtmlFrame(canvas, horizontal_scrollbar="auto", messages_enabled = False) # Creates a html frame
try:
  frame.load_website(apod.get_apod(date_input.get())["image_url"]) # It attempts to load the website, if it is a youtube video it will give a link to it instead
except KeyError:
   frame.load_website("https://www.google.com/APOD_URL_Inaccessible")
   txt.delete(1.0,END)
   txt.insert(1.0, "There was an error with accessing the APOD, it likely uses a video without a thumbnail.") # Error messages
   frame.pack(fill="both", expand=True)
except TypeError:
   frame.load_website("https://www.google.com/APOD_URL_Inaccessible")
   txt.delete(1.0,END)
   txt.insert(1.0, "There was an error with accessing the APOD, it is likely due to rate limits") # Error messages
   frame.pack(fill="both", expand=True)
canvas.pack()
Apod_frame.pack(fill='both', expand=True)
notebook.add(Apod_frame, text="APOD") # Adds the frame to the notebook
"""--------EARTH IMAGES--------"""
Earth_frame = ttk.Frame(notebook, width=2000, height=2000, style='Apod_frame.TFrame')
Label(Earth_frame, text="WARNING: THERE IS AN INCREDIBLY HIGH CHANCE THIS WILL FAIL AS THE API IS VERY LIMITED IN THIS REGARD", bg="black", fg="crimson").pack() # A warning
Label(Earth_frame, text="\n", bg="black", fg="white").pack()
Button(Earth_frame, text="Open Image", bg="black", fg="white", command=lambda: Earth.open_image(lat.get(), lon.get(), dim.get(), date_input2.get())).pack() # Refer to the corresponding functions and the buttons in the APOD section for explanation
Button(Earth_frame, text="Open the Image url", bg="black", fg="white", command=lambda: Earth.open_url(lat.get(), lon.get(), dim.get(), date_input2.get())).pack()
Label(Earth_frame, text="\n", bg="black", fg="white").pack()
Label(Earth_frame, text="Date input (YYYY-MM-DD)", bg="black", fg="white").pack() # Format
date_input2 = Entry(Earth_frame, bg="black", fg="white") #Same as APOD section
date_input2.pack()
Label(Earth_frame, text="\n", bg="black", fg="white").pack()
Label(Earth_frame, text="Enter in the latitude of the image", bg="black", fg="white").pack() #Information on what to enter
lat = Entry(Earth_frame, bg="black", fg="white")
lat.pack()
Label(Earth_frame, text="Enter in the longtitude of the image", bg="black", fg="white").pack() # Same as previous
lon = Entry(Earth_frame, bg="black", fg="white")
lon.pack()
Label(Earth_frame, text="Enter in the dimensions of the image (only one number)", bg="black", fg="white").pack() # Same as previous
dim = Entry(Earth_frame, bg="black", fg="white")
dim.pack()
Label(Earth_frame, text="\n", bg="black", fg="white").pack()
Button(Earth_frame, text="Quit :(", fg='white', bg="dark blue", command=lambda: root.destroy()).pack() # End the program again
Label(Earth_frame, text="\n", bg="black", fg="white").pack()
bg2 = PhotoImage(file="Earth.png") # A nice placeholder image
canvas2 = Canvas(Earth_frame, width=750, height=750)
canvas2.pack()
canvas2.create_image( 0, 0, image = bg2, anchor="nw")  # Add image

Earth_frame.pack(fill='both', expand=True)
notebook.add(Earth_frame, text="Earth Imagery") # Add the frame to the notebook
notebook.pack(expand=True)
root.mainloop()
```

### Final (Module)

```Python
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
```

---
---

## Integration

---
---

```Python
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
```

### Main

```Python
from api_module import apod, Earth #Importing from my module
```

---
---

## Testing and Debugging

---
---

---
---

## Installation

---
---

### requirements.txt

```Text
pywebview==5.4
tkinterweb==4.2.0
requests==2.32.3
```

### README.md

```Markdown
# NASA Program

This Python program allows you to retrieve NASA information from an external API. The program uses the `requests` library to fetch data from NASA's API as well as `tkinter` and `tkinterweb` as well as `pywebview` to insert the entire program into a GUI and `webbrowser` to open up your default browser.

## Features

- Fetch the current and previous APOD's data and display it in the GUI.
- Open the APOD's image URL in your default browser.
- Fetch images from NASA's earth images service based on latitude and longtitude (very limited).
- Open the Earth images' image URL in your default browser.

## Requirements

To run this program, you need to install the following dependencies:

- `tkinterweb` to allow for html within the tkinter GUIs
- `requests` to make HTTP requests to the NASA API.
- `pywebview` to view the earth images within a GUI

### Install dependencies

To install the required dependencies, you can run:

```

```bash
pip install -r requirements.txt

```

```Markdown

Or if it fails:

```

```bash
pip install tkinterweb
pip install requests
pip install pywebview

```

---
---

## Maintenance

---
---
