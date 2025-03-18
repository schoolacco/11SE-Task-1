from api_module import apod
from tkinter import *
from tkinter import ttk
from api_module import Earth
def explanation(date):
    root = Tk()
    root.title(apod.get_apod(date)["title"])
    root.configure(bg="black")
    root.minsize(200,200)
    Message(root, text=apod.return_explanation(date), bg="black", fg="white").pack()
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
Button(Apod_frame, text="Open Image", bg="black", fg="white", command=lambda: apod.open_image(date_input.get())).pack()
Button(Apod_frame, text="Open the APOD url", bg="black", fg="white", command=lambda: apod.open_url(date_input.get())).pack()
Button(Apod_frame, text="Read APOD explanation", bg="black", fg="white", command=lambda: explanation(date_input.get())).pack()
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
Label(Apod_frame, text="Date input (YYYY-MM-DD)", bg="black", fg="white").pack()
date_input = Entry(Apod_frame, bg="black", fg="white")
date_input.pack()
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
Button(Apod_frame, text="Quit :(", fg='white', bg="dark blue", command=lambda: root.destroy()).pack()
Label(Apod_frame, text="\n", bg="black", fg="white").pack()
bg = PhotoImage(file="stars.png") 
canvas = Canvas(Apod_frame, width=800, height=800)
canvas.pack()
canvas.create_image( 0, 0, image = bg,  
                     anchor = "nw") 
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