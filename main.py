from api_module import apod, Earth #Importing from my module
from tkinter import * # Import everything
from tkinter import ttk #Specifically import ttk (* doesn't import it)
from tkinterweb import * # Import everything for better tkinterhtml
def explanation(date):
  global txt #Tkinter textbox is global
  try:
    txt.delete(1.0, END) #Remove text
    txt.insert(1.0, apod.return_explanation(date)) # Fill it with explanation
  except TclError:
    pass #For invalid inputs
def display(date):
  global frame, canvas, txt
  try:
    apod.get_apod(date)["image_url"] #A buffer to instantly cause an error in the case of an invalid input, I have tried turning it into a variable but it doesn't function as intended
    frame.destroy() #Destroy the frame
    frame = HtmlFrame(canvas, horizontal_scrollbar="auto", messages_enabled = False) #Create the html frame, scrollable in the case the image is too large
    frame.load_website(apod.get_apod(date)["image_url"]) # Load the image
    frame.pack(fill="both", expand=True)
  except KeyError:
    frame.load_website("https://www.google.com/APOD_URL_Inaccessible") #This just causes an Error404 message to appear
    frame.pack(fill="both", expand=True)
    txt.delete(1.0,END) # Remove text
    txt.insert(1.0, "There was an error with accessing the APOD, it likely uses a video without a thumbnail.") #Error message
  except TypeError:
    pass # Handle invalid inputs
root = Tk() # GUI
root.title('NASA API') #Title
root.configure(bg='black') #bg color
root.maxsize(1000,1000) # Maximum size
root.minsize(1000,1000) # Minimum size
notebook = ttk.Notebook(root) #This allows for creation of tabs
s = ttk.Style() #This has to be a variable for whatever reason
s.configure('Apod_frame.TFrame', background="black") #Change Style() to create bgs for frames
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
# ------------ EARTH IMAGES ----------------
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