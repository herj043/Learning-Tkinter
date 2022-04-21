from tkinter import *

###################################################################
################# Calculator Window ###############################
###################################################################
def open_calculator():
  calculator_win = Tk(className="Calculator")

  # Calculator Box
  calc_box = Entry(calculator_win, width=30, bg="white", fg="black")
  calc_box.grid (row=0, column=0, columnspan=3)
  calc_box.insert(0, "")

  def button_click(number):
    current = calc_box.get()
    calc_box.delete(0, END)
    calc_box.insert(0,str(current) + str(number))

  def clear_box():
    calc_box.delete(0,END)

  def add_number():
    pass

  def subtract_number():
    pass
    
  # Draws Buttons
  button_1 = Button(calculator_win, text="1", padx=40, pady=20,
                    command=lambda: button_click(1))
  button_2 = Button(calculator_win, text="2", padx=40, pady=20,
                    command=lambda: button_click(2))
  button_3 = Button(calculator_win, text="3", padx=40, pady=20,
                    command=lambda: button_click(3))
  button_4 = Button(calculator_win, text="4", padx=40, pady=20,
                    command=lambda: button_click(4))
  button_5 = Button(calculator_win, text="5", padx=40, pady=20,
                    command=lambda: button_click(5))
  button_6 = Button(calculator_win, text="6", padx=40, pady=20,
                    command=lambda: button_click(6))
  button_7 = Button(calculator_win, text="7", padx=40, pady=20,
                    command=lambda: button_click(7))
  button_8 = Button(calculator_win, text="8", padx=40, pady=20,
                    command=lambda: button_click(8))
  button_9 = Button(calculator_win, text="9", padx=40, pady=20,
                    command=lambda: button_click(9))
  button_0 = Button(calculator_win, text="0", padx=40, pady=20,
                    command=lambda: button_click(0))
  
  button_add = Button(calculator_win, text="+", padx=40, pady=20,
                      command= add_number())
  button_subtract = Button(calculator_win, text="-", padx=40, pady=20,
                           command= subtract_number())
  
  button_clear = Button(calculator_win, text="Clear", padx=75, pady=20,
                        command=lambda: clear_box())


  
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
  button_clear.grid(row=4, column=1, columnspan=2)

  button_add.grid(row=5, column=0)
  button_subtract.grid(row=5, column=1)
  
  calculator_win.mainloop()