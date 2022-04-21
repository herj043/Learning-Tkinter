from Windows import test_windows as test_win, calc
import replit
import time

# Selecting windows from user input
def select_windows():
  # Default selection (Used for testing code more effiecient)
  selection = True
  skip_selection = False
  if selection == True:
    selection = input("Open a window (window, calculator): ")
  else:
    selection = "cal"
    skip_selection = True

  # Selects Windows
  if selection == "window" or selection == "1" or selection == "win":
    print("windows running")
    test_win.open_windows()
    print("windows end")
    
  elif selection == "calculator" or selection == "2" or selection == "cal":
    print("calculator running")
    calc.open_calculator()
    print("calculator end")
    
  else:
    if selection !="exit":
      print("Invalid Input")
      
  if (selection != "exit") and (skip_selection != True):
    time.sleep(0.5)
    replit.clear()
    select_windows()



################## Running program ###################
select_windows()
print("exited program")