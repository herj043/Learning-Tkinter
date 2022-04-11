from tkinter import *
from functions import *

win = Tk()

# Counts the number of clicks
pre = 0

def click():
  global pre
  pre += 1

  
  my_label = Label(win, text=str(got) + str(pre), bg="#ffffff")
  my_label.pack()

  if pre % 7 == 1:
    win.config(bg="#0000ff")
  elif pre % 7 == 2:
    win.config(bg="#00ff00")
  elif pre % 7 == 3:
    win.config(bg="#ff0000")
  elif pre % 7 == 4:
    win.config(bg="#00ffff")
  elif pre % 7 == 5:
    win.config(bg="#ffff00")
  elif pre % 7 == 6:
    win.config(bg="#ffff00")
  else:
    win.config(bg="#ffffff")


txt_box = Entry(win, width=30, bg="white")
txt_box.pack()
txt_box.insert(0, text="Enter Text")
got = txt_box.get() + " "

# Creates button
my_button = Button(win, text="Print!",padx=20, pady= 20, command=click)
my_button.pack()

win.mainloop()