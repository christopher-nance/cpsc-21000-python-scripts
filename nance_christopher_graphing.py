info = '''
#==============================================================================#
title               :nance_christopher_graphing.py
description         :Creates a UI to plot graphs
author              :Chris Nance
date                :2022-04-04
version             :1.0
usage               :python nance_christopher_graphing.py
notes               :
python_version      :3.10
#==============================================================================#
'''

import math
import PySimpleGUI as sg
from matplotlib import pyplot

xRange = []
yRange = []

newFigNumber = 1


## GUI SETUP
def make_window():

    # Gui Elements
    elements = [
        [sg.Text('This plotting tool shows you the difference between a linear,\nquadratic, cubic, and logarithmic curve.')],
        [sg.Text('What do you want to plot? Check the boxes.')],

        [
            sg.Checkbox('Linear', key='linear'),
            sg.Checkbox('Quadratic', key='quadratic'),
            sg.Checkbox('Cubic', key='cubic'),
            sg.Checkbox('Logarithmic', key='logarithmic'),
            sg.Checkbox('Linearithmic', key='linearithmic')
        ],

        [sg.Text('Enter min x: '), sg.Input(key='min-xValue', size=(5,5)), sg.Text('Enter max x: '), sg.Input(key='max-xValue', size=(5,5))],

        [sg.Submit('Plot'), sg.Exit('Close')]
    ]

    return sg.Window('Function Plotter', elements, finalize=True, use_default_focus=True)


## FUNCTIONS
def validateInput(values): #Pass values from the GUI Window.read(); returns True if validated or returns str='Reason why validation failed'
    # Check: At least one of the check mark boxes is checked.
    if values['linear'] == False and values['quadratic'] == False and values['cubic'] == False and values['logarithmic'] == False and values['linearithmic'] == False: return 'You must check at least one graph to display.'

    # CheckL min-value and max-value are not blank & then attempt to convert them to integers.
    if values['min-xValue'] != '' and values['max-xValue'] != '':
        try:
            int(values['min-xValue'])
            int(values['max-xValue'])
        except:
            return 'Please make sure the min x-value and max x-value are integers.\nEx: 2,5; 5,10; 2,10'
    else:
        return 'A Value MUST be used for the min x-value and max x-value.\nThe min x-value MUST also be lower than the max x-value.'

    # Check: min-value must be smaller than the max-value.
    if int(values['min-xValue']) >= int(values['max-xValue']): return 'Min x-value must be less than the Max x-value'

    # Check: No negatives if Logs are used.
    if (int(values['min-xValue']) < 0 or int(values['max-xValue']) < 0) and (values['logarithmic'] == True or values['linearithmic'] == True): return 'You cannot use negative integers for the x-value(s) if you intend to use Logarithmic or Linearithmic graphs.'

    # Return True if validation was good.
    return True


## MatPlotLib stuff
def button_Plot(values):
    global newFigNumber # Not using this breaks the function...
    pyplot.figure(newFigNumber) # Create a new figure (to keep from replotting on the same figure)
    legend = [] # Define an empty list for the legend.

    newFigNumber += 1 # Prepare the next figure for the next time this function is called.

    # Determine & Plot Linear Function
    if values['linear'] == True: # Evaluate the state of the 'Linear' check-box when 'Plot' was pressed.
        xRange.clear() # Clear old data in list for x-values
        yRange.clear()# Clear old data in list for y-values
        for num in range(int(values['min-xValue']), int(values['max-xValue'])+1): # For each number in the range minimum x-value to maximum x-value ...
            xRange.append(num) # ... add the x value (num) to the x-values list of points called xRange.
            yRange.append(num) # ... add the y value (f(num)=num) to the y-values list of points called yRange.
        pyplot.plot(xRange, yRange, 'b', label='Linear') # Plot the data from xRange and yRange using color magenta and the label 'Linear'.
        legend.append('Linear') # Add 'Linear' to the legend list to add to the legend later.

    if values['quadratic'] == True:
        xRange.clear()
        yRange.clear()
        for num in range(int(values['min-xValue']), int(values['max-xValue'])+1):
            xRange.append(num)
            yRange.append(num**2) # Quadratic: f(num)=num^2
        pyplot.plot(xRange, yRange, 'tab:orange', label='Quadratic')
        legend.append('Quadratic')

    if values['cubic'] == True:
        xRange.clear()
        yRange.clear()
        for num in range(int(values['min-xValue']), int(values['max-xValue'])+1):
            xRange.append(num)
            yRange.append(num**3) # Cubic: f(num)=num^3
        pyplot.plot(xRange, yRange, 'g', label='Cubic')
        legend.append('Cubic')

    if values['logarithmic'] == True:
        xRange.clear()
        yRange.clear()
        for num in range(int(values['min-xValue']), int(values['max-xValue'])+1):
            xRange.append(num)
            if num > 0:
                yRange.append(math.log(num)) # Logarithmic: f(num)=log(num)
            else:
                yRange.append(0)
        pyplot.plot(xRange, yRange, 'r', label='Logarithmic')
        legend.append('Log')

    if values['linearithmic'] == True:
        xRange.clear()
        yRange.clear()
        for num in range(int(values['min-xValue']), int(values['max-xValue'])+1):
            xRange.append(num)
            if num != 0:
                yRange.append(num*math.log(num)) # Linearithmic: f(num)=num*log(num)
            else:
                yRange.append(0)
        pyplot.plot(xRange, yRange, 'indigo', label='Linearithmic')
        legend.append('Linlog')

    pyplot.legend(legend) # Create legend from list
    pyplot.title('Algorithmic Complexity Functions') # Title
    pyplot.xlabel('x') # X-Axis Name
    pyplot.ylabel('y') # Y-Axis Name
    pyplot.show() # Show the plot


## MAIN
window = make_window() # Create the GUI

while True: # Event Loop
    event, values = window.read() # Read the window for events and values
    if event == sg.WINDOW_CLOSED or event == 'Close': # If the window is closed with the X or the Close button is pressed...
        break # break the loop (goto window.close()).
    if event == 'Plot': # If event is called to plot (button Plot pressed) then...
        # Validate Input ...
        if validateInput(values) == True:
            # Plot Graphs.
            button_Plot(values)
        else:
            sg.popup_error('Validation Error', validateInput(values)) # Show popup for any validation errors. 


window.close() # Close the GUI Window