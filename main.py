# Branch Dev

##### Import #####

# This import bring GUI
import PySimpleGUI as sg

sg.theme("BlueMono")

##### Variables #####



##### Functions #####



##### main.py Run ######


layout = [[sg.Text('Input text test.')],
                  [sg.InputText()],
                  [sg.Submit(), sg.Cancel()]]      

window = sg.Window('PySimpleGUI Window', layout)    

event, values = window.read()    
window.close()

text_input = values[0]    
sg.popup('You entered', text_input)

