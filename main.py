from Windows import test_windows as test_win, calc
import replit
import time

# Selecting windows
def select_windows():
  selection = input("Open a window (window, calculator): ")
  if selection == "window" or selection == "1":
    print("windows running")
    test_win.open_windows()
    print("windows end")
    
  elif selection == "calculator" or selection == "2":
    print("calculator running")
    calc.open_calculator()
    print("calculator end")
    
  else:
    if selection !="exit":
      print("Invalid Input")
    
  if selection != "exit":
    time.sleep(0.5)
    replit.clear()
    select_windows()



################## Running program ###################
select_windows()
print("exited program")