from tkinter import *

###################################################################
################# Calculator Window ###############################
###################################################################
def open_calculator():
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