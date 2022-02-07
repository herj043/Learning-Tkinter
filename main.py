import PySimpleGUI as sg

# layout the insides of the window
layout = [[sg.Text('Input text test.')],
  [sg.Text("BMI Calculator")],
  [
    sg.Text(
      'Enter your age, height, and weight to get your Body Mass Index value and description',
      size=(40, 3)
    )

  ],
  [
    sg.Text("Age"),
    sg.Input(size=(3, 1), key='-AGE-')
  ],
  [sg.InputText()],
  [sg.Submit(), sg.Cancel()]]      

# Inputs everything noted from "layout"
window = sg.Window('PySimpleGUI Window', layout)    

# event command inserts whatever the user inputs
event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('You entered', text_input)
