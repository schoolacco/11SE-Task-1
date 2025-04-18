from api_module import apod, Earth #Importing from my module
from tkinter import * # Import everything
from tkinter import ttk #Specifically import ttk (* doesn't import it)
from tkinterweb import * # Import everything for better tkinterhtml
import os #Import the system itself
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
Label(Apod_frame, text="Welcome to this system \n Just know that if anything is ever blank it is due to rate limits from NASA \n These rate limits may have been caused by the school Wifi somehow...", bg="black", fg="white").pack() #Intro text
Label(Apod_frame, text="\n", bg="black", fg="white").pack() #Add space
Button(Apod_frame, text="Open Image", bg="black", fg="white", command=lambda: display(date_input.get())).pack() #Apod commands
Button(Apod_frame, text="Open the APOD url", bg="black", fg="white", command=lambda: apod.open_url(date_input.get())).pack()
Button(Apod_frame, text="Read APOD explanation", bg="black", fg="white", command=lambda: explanation(date_input.get())).pack() # Refer to the respective functions, lambda is required to allow for the functions to require variables and cause them to not run instantly
Button(Apod_frame, text="Save APOD", bg="black", fg="white", command=lambda: apod.save_APOD(date_input.get())).pack()
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
Label(Earth_frame, text="Do: lon: -95.33, lat: 29.78, date: 2018-01-01, dim: 0.15 if you want evidence of this functioning", bg = "black", fg="white").pack()
Label(Earth_frame, text="\n", bg="black", fg="white").pack()
Button(Earth_frame, text="Open Image", bg="black", fg="white", command=lambda: Earth.open_image(lat.get(), lon.get(), dim.get(), date_input2.get())).pack() # Refer to the corresponding functions and the buttons in the APOD section for explanation
Button(Earth_frame, text="Open the Image url", bg="black", fg="white", command=lambda: Earth.open_url(lat.get(), lon.get(), dim.get(), date_input2.get())).pack()
Button(Earth_frame, text="Save Image", bg="black", fg="white", command=lambda: Earth.save_Image(lat.get(), lon.get(), dim.get(), date_input2.get())).pack()
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
Management = ttk.Frame(notebook, width=2000, height=2000, style='Apod_frame.TFrame') # File management frame
Values = Variable(value= os.listdir("Images")) # Creates a list of files
List = Listbox(master=Management, listvariable=Values, selectmode=MULTIPLE) # Creates a selectable list within the GUI
def Delete():
  '''Delete the selected items from the list'''
  global Values
  global List
  for item in [List.get(i) for i in List.curselection()]: #For every selected item
    os.remove(f"Images/{item}") #Delete the file
  List.destroy() #Destroy the list to update it
  Values = Variable(value= os.listdir("Images"))
  List = Listbox(master=Management, listvariable=Values, selectmode=MULTIPLE) # Remake the list
  List.pack()
def Refresh():
  '''Refresh the list incase you have new files'''
  global Values, List
  List.destroy()
  Values = Variable(value= os.listdir("Images"))
  List = Listbox(master=Management, listvariable=Values, selectmode=MULTIPLE) #Destroy the list to update it
  List.pack()
Button(Management, text="Delete selected files", bg="black", fg="white", command=lambda: Delete()).pack() #Button to delete files nad refresh respectively.
Button(Management, text="Refresh List", bg="black", fg="white", command=lambda: Refresh()).pack()
List.pack()
notebook.add(Management, text="Storage Management")
'''-----Help-----'''
Help = ttk.Frame(notebook, width=2000, height=2000, style='Apod_frame.TFrame')
Message(Help, text="Are you confused by all of this? It honestly isn't too hard to understand. Enter in the date input within the APOD frame in the given format to recieve the APOD of that given date, do not that you may run into some issues, these likely relate to the APOD being a video instead of an image or you simply being rate limited. If you want today's APOD just leave it blank. The Open Image buttons in either frame will simply open up the image within the GUI,  the open the image URL buttons will open the image within your default browser. The APOD explanation button with the APOD frame will simply insert the explanation (given by NASA) of the APOD of the date you chose. In the Earth frame the latitude and longtitude entry points are as you'd expect them to be, latitude and longtitude of the Earth image, the dimensions parameter is rather unclear but doesn't matter too much. If you run into any issues first ensure that you have gone through the README and make sure you aren't just rate limited, otherwise, report the issue.", bg="black", fg="white").pack() # A warning
notebook.add(Help, text="Help") # Add the frame to the notebook
notebook.pack(expand=True)
root.mainloop()