
import requests
import os
import time
from tkinter import *
root = Tk()
root.title("IsEven v9.9.9")
root.configure(background="black")
root.maxsize(10000,10000)
root.minsize(500,500)
root.geometry("500x500+20+100")
Label(root, text="Insert a number between 0 and 999999 (inclusive) to begin!", bg = "dark grey").pack()
inputtxt = Text(root, height = 10, width = 25, bg = "white")
inputtxt.pack()
num = 0
def Take_input():
   global inputtxt
   INPUT =  inputtxt.get("1.0", "end-1c")
   return INPUT
# API Base URL
API_URL = "https://api.isevenapi.xyz/api/iseven/"
def is_even(num):
    if num != int:
       raise ValueError
    if int(num) > 999999 or int(num) < 0:
       raise KeyError
    response = requests.get(API_URL + num)
    if response.status_code == 200:
        result = response.json()
    return result
def Main():
  try:
    num = Take_input()
    even = is_even(num)
    if even["iseven"]:
       print("The number is even.")
    else:
       print("Your number is odd.")
    print(even["ad"]+"\nDeveloper's note: Sorry we can't remove the ads :(")
  except KeyError:
     print("Enter a number within the range.")
  except ValueError:
     print("Number. I said a number.")
  time.sleep(3)
  os.system('cls')
Button(root, text="Check even-ness!", command= Main()).pack()
root.mainloop()
