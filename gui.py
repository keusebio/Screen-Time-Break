import PySimpleGUI as sg
from main import *

# Define the window's contents
layout = [  [sg.Text("Welcome to Screen Time!") ],
            [sg.Text("In minutes, how often would you like to be reminded to take a break?")],
            [sg.Input(key='-INPUT-')],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Save'),sg.Button('Start'),sg.Button('Demo'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
        
    # Save and overwrites previous data to data.txt
    if event =='Save':
        file = open('data.txt','w+')
        file.truncate(0)
        file.write(values['-INPUT-'])
        file.close()
        window['-OUTPUT-'].update('You will now be reminded every '
                + values['-INPUT-'] + " minutes! ")

    # starts the notification event with current data
    if event == 'Start':
        print('start')
        ST_start()

    #for demo purposes. Displays notification with current data.
    if event == 'Demo':
        print('Demo')
        notify()

# Finish up by removing from the screen
window.close()
