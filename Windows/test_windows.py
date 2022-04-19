from tkinter import *

################################################
### ! "pre" variable doesn't work function ! ###
################################################
pre = 0
def open_windows():
  win = Tk()

  # Counts the number of clicks
  global pre
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

  win_two.mainloop()
  win.mainloop()
