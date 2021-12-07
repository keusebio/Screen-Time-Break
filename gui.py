import PySimpleGUI as sg

# Define the window's contents
layout = [  [sg.Text("Welcome to Screen Time!") ],
            [sg.Text("In minutes, how often would you like to be reminded to take a break?")],
            [sg.Input(key='-INPUT-')],
            [sg.Text(size=(40,1), key='-OUTPUT-')],
            [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('You will now be reminded every '
            + values['-INPUT-'] + " minutes! ")

# Finish up by removing from the screen
window.close()
