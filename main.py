from api_module import apod, Earth
from tkinter import *
from tkinter import ttk
from tkinterweb import *
def explanation(date):
  global txt
  try:
    txt.delete(1.0, END)
    txt.insert(1.0, apod.return_explanation(date))
  except TclError:
    pass #For invalid inputs
def display(date):
  global frame, canvas, txt
  try:
    apod.get_apod(date)["image_url"] #A buffer to instantly cause an error in the case of an invalid input, I have tried turning it into a variable but it doesn't function as intended
    frame.destroy()
    frame = HtmlFrame(canvas, horizontal_scrollbar="auto", messages_enabled = False)
    frame.load_website(apod.get_apod(date)["image_url"])
    frame.pack(fill="both", expand=True)
  except KeyError:
    frame.load_website("https://www.google.com/APOD_URL_Inaccessible")
    frame.pack(fill="both", expand=True)
    txt.delete(1.0,END)
    txt.insert(1.0, "There was an error with accessing the APOD, it likely uses a video without a thumbnail.")
  except TypeError:
    pass # Handle invalid inputs
root = Tk()
root.title('NASA API')
root.configure(bg='black')
root.maxsize(1000,1000)
root.minsize(1000,1000)
notebook = ttk.Notebook(root)
s = ttk.Style()
s.configure('Apod_frame.TFrame', background="black")
Apod_frame = ttk.Frame(notebook, width=2000, height=2000, style='Apod_frame.TFrame')
Label(Apod_frame, text="Welcome to this system \n Just know that if anything is ever blank it is due to rate limits from NASA", bg="black", fg="white").pack()
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
try:
  frame.load_website(apod.get_apod(date_input.get())["image_url"])
except KeyError:
   frame.load_website("https://www.google.com/APOD_URL_Inaccessible")
   txt.delete(1.0,END)
   txt.insert(1.0, "There was an error with accessing the APOD, it likely uses a video without a thumbnail.")
   frame.pack(fill="both", expand=True)
except TypeError:
   frame.load_website("https://www.google.com/APOD_URL_Inaccessible")
   txt.delete(1.0,END)
   txt.insert(1.0, "There was an error with accessing the APOD, it is likely due to rate limits")
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