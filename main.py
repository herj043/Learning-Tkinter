from tkinter import *
from functions import *

win = Tk()


# Counts the number of clicks
pre = 0

def click():
  global pre
  pre += 1
  
  my_label = Label(win,text= txt_box.get() + " " + str(pre),
                   bg="#ffffff")
  my_label.pack()

  # Select Color according to the number 
  if pre % 7 == 1:
    win_two.config(bg="#0000ff")
  elif pre % 7 == 2:
    win_two.config(bg="#00ff00")
  elif pre % 7 == 3:
    win_two.config(bg="#ff0000")
  elif pre % 7 == 4:
    win_two.config(bg="#00ffff")
  elif pre % 7 == 5:
    win_two.config(bg="#ffff00")
  elif pre % 7 == 6:
    win_two.config(bg="#ff00ff")
  else:
    win_two.config(bg="#ffffff")

# Creates Textbox 
txt_box = Entry(win, width=30, bg="black", fg="white")
txt_box.pack()
txt_box.insert(0, "Enter Text")


# Creates button
my_button = Button(win, text="Print!",padx=20, pady= 20, command=click)
my_button.pack()


###################################################################
################# Second Window ###################################
###################################################################
win_two = Tk(className="the color box")

my_label_two = Label(win_two, text="I'm Colorful")
my_label_two.pack()

win_two.geometry("200x200")



###################################################################
################# Calculator Window ###############################
###################################################################
calculator_win = Tk(className="Calculator")

def button_add():
  return


# Draws Buttons

button_1 = Button(calculator_win, text="1", padx=40, pady=20, command=button_add)
button_2 = Button(calculator_win, text="2", padx=40, pady=20, command=button_add)
button_3 = Button(calculator_win, text="3", padx=40, pady=20, command=button_add)
button_4 = Button(calculator_win, text="4", padx=40, pady=20, command=button_add)
button_5 = Button(calculator_win, text="5", padx=40, pady=20, command=button_add)
button_6 = Button(calculator_win, text="6", padx=40, pady=20, command=button_add)
button_7 = Button(calculator_win, text="7", padx=40, pady=20, command=button_add)
button_8 = Button(calculator_win, text="8", padx=40, pady=20, command=button_add)
button_9 = Button(calculator_win, text="9", padx=40, pady=20, command=button_add)
button_0 = Button(calculator_win, text="0", padx=40, pady=20, command=button_add)


# Sets the Drawn Buttons into Rows and Columns

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)


calculator_win.mainloop()


# Creates GUI
win_two.mainloop()
win.mainloop()