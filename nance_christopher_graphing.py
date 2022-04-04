info = '''
#==============================================================================#
title               :nance_christopher_graphing.py
description         :turtle draw assignment
author              :Chris Nance
date                :2022-03-30
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

    # Theme
    #sg.theme('Python')

    # Gui Elements
    elements = [
        [sg.Text('This plotting tool shows you the difference between\na linear, quadratic, cubic, and logarithmic curve.', font='Default 15')],
        [sg.Text('What do you want to plot? Check the boxes.')],

        [
            sg.Checkbox('Linear', key='linear'),
            sg.Checkbox('Quadratic', key='quadratic'),
            sg.Checkbox('Cubic', key='cubic'),
            sg.Checkbox('Logarithmic', key='logarithmic'),
            sg.Checkbox('Linearithmic', key='linearithmic')
        ],

        [sg.Text('Enter min x: '), sg.Input(key='min-xValue'), sg.Text('Enter max x: '), sg.Input(key='max-xValue')],

        [sg.Submit('Plot'), sg.Exit('Close')]
    ]

    return sg.Window('Function Plotter', elements, finalize=True, use_default_focus=True)


## FUNCTIONS
def validateInput(values): #Pass values from the GUI Window.read(); returns True if validated or returns str='Reason why validation failed'
    if values['linear'] == False and values['quadratic'] == False and values['cubic'] == False and values['logarithmic'] == False and values['linearithmic'] == False: return 'Make sure you check a graph to display!'
    if values['min-xValue'] != '' and values['max-xValue'] != '':
        try:
            int(values['min-xValue'])
            int(values['max-xValue'])
        except:
            return 'Validation error. Please ensure the x-value and the y-value are typed in correctly.'
    else:
        return 'You need to fill something in for the X and Y Values & Select one of the check boxes to display a graph.'
    if int(values['min-xValue']) >= int(values['max-xValue']): return 'Min-xValue must be less than the Max-xValue'
    return True




## MatPlotLib stuff
def button_Plot(values):
    print("Button Done Pressed ::: plotting")
    xRange.clear()
    yRange.clear()
    if values['linear'] == True:
        for num in range(int(values['min-xValue']), int(values['max-xValue'])+1):
            xRange.append(num)
            yRange.append(num)
        pyplot.plot(xRange, yRange)
    if values['quadratic'] == True:
        for num in range(int(values['min-xValue']), int(values['max-xValue'])+1):
            xRange.append(num)
            yRange.append(num**2)
        pyplot.plot(xRange, yRange)
    if values['cubic'] == True:
        for num in range(int(values['min-xValue']), int(values['max-xValue'])+1):
            xRange.append(num)
            yRange.append(num**3)
        pyplot.plot(xRange, yRange)
    if values['logarithmic'] == True:
        for num in range(int(values['min-xValue']), int(values['max-xValue'])+1):
            xRange.append(num)
            yRange.append(math.log(num))
        pyplot.plot(xRange, yRange)
    if values['linearithmic'] == True:
        for num in range(int(values['min-xValue']), int(values['max-xValue'])+1):
            xRange.append(num)
            yRange.append(num*math.log(num))
        pyplot.plot(xRange, yRange)
    
    newFigure = pyplot.figure(newFigNumber) # Create a new figure with a random 3-digit integer ID.
    newFigNumber += 1

    pyplot.show()





## MAIN
window = make_window()

while True:  # Event Loop
    event, values = window.read()
    print(values)
    if event == sg.WINDOW_CLOSED or event == 'Close':
        break
    if event == 'Plot':
        # Validate Input
        print('Validating input')
        if validateInput(values) == True:
            # Plot Graphs
            print('Plotting graphs')
            button_Plot(values)
        else:
            sg.popup_error('Validation Error', validateInput(values))


window.close()