info = '''
#==============================================================================#
title               :riskCalculator_Nance.py
description         :
author              :Chris Nance
date                :2022-04-24
version             :1.0
usage               :python riskCalculator_Nance.py
notes               :
python_version      :3.10
#==============================================================================#
'''

import PySimpleGUI as sg


## Variables Needed
# Age
# Geight
# Weight
# Systolic Blood Pressure
# Diastolic Blood Pressure
# Diabetes?
# Cancer?
# Alzheimers?

points = 0

def validate_input(height_inches, weight, age, sysbp, diabp):
    try:
        int(height_inches)
    except:
        return 'Verify your height was typed in correctly with only non-negative integers.'

    try:
        float(weight)
    except:
        return 'Verify your weight was typed in correctly with only non-negative floats.'
        
    try:
        int(age)
    except:
        return 'Verify your age was typed in correctly with only non-negative integers.'
        
    try:
        int(sysbp)
    except:
        return 'Verify your sysbp was typed in correctly with only non-negative integers.'
        
    try:
        int(diabp)
    except:
        return 'Verify your diabp was typed in correctly with only non-negative integers.'
    
    if int(age) < 0: return 'Your age cannot be less than 0.'
    if int(height_inches) < 36 or int(height_inches) > 120: return 'You cant possibly be this tall...'
    if int(age) > 120: return 'You cant possibly be this old...'
    if int(sysbp) > 200 or int(sysbp) < 20: return 'You cant possibly have this type of systolic blood pressure'
    if int(diabp) > 200 or int(diabp) < 20: return 'Your diabp is a bit too high. Are you sure you typed it in right?'

    return True
    

def createWindow():

    elements = [
        [sg.Text("Please enter the information asked below to the best of your knowledge then hit Submit:", justification='center')],
        [sg.Text("Enter your Height in WHOLE Inches: "), sg.Input(key='height', size=(3,0))],
        [sg.Text("Enter your Weight in Pounds: "), sg.Input(key='weight', size=(3,0))],
        [sg.Text("Enter your Current Age: "), sg.Input(key='age', size=(3,0))],
        [sg.Text("Enter your Systolic Blood Pressure: "), sg.Input(key='sysbp', size = (3,0))],
        [sg.Text("Enter your Diastolic Blood Pressure: "), sg.Input(key='diabp', size = (3,0))],

        [sg.Text("Please check any boxes below if you have history of the following in your family:", justification='center')],
        [sg.Checkbox('Diabetes?', key='diabetes_bool')],
        [sg.Checkbox('Cancer?', key='cancer_bool')],
        [sg.Checkbox('Alzheimers?', key='alzheimers_bool')],

        [sg.Submit()],
    ]

    return sg.Window('Calculator', elements, finalize=True)

window = createWindow()
while True: # Event Loop
    event, values = window.read() # Read the window for events and values
    if event == sg.WINDOW_CLOSED or event == 'Close': # If the window is closed with the X or the Close button is pressed...
        break # break the loop (goto window.close()).
    if event == 'Submit': # If event is called to plot (button Plot pressed) then...
        height_inches = values['height']
        weight = values['weight']
        age = values['age']
        sysbp = values['sysbp']
        diabp = values['diabp']
        diabetes = values['diabetes_bool']
        cancer = values['cancer_bool']
        alzheimers = values['alzheimers_bool']
        print("Height:", height_inches, "\nAge:", age, "\nSystolic Blood Pressure:", sysbp, "\nDiaBP:", diabp, "\nDiabetes:", diabetes, "\nCancer:", cancer, "\nAlzeimhers:", alzheimers)
        if validate_input(height_inches, weight, age, sysbp, diabp) == True:
            # Do maths here
            height_inches = float(height_inches)
            weight = float(weight)
            age = int(age)
            sysbp = int(sysbp)
            diabp = int(diabp)
            print("Go")
            bmi = int(weight)/int(height_inches)**2*703

            if int(age) < 30: points += 0
            elif int(age) < 45: points += 0
            elif int(age) < 60: points += 20
            else: points += 30

            if bmi>18.5 and bmi < 24.9: points += 0
            elif bmi>24.9 and bmi<29.9: points += 30
            elif bmi>29.9 and bmi<30.0: points += 75
            else: print("IDK! BMI")

            if (sysbp < 120) and (diabp < 80): points+= 0
            elif (sysbp >= 120 and sysbp <= 129) and (diabp < 80): points += 15
            elif (sysbp >= 130 and sysbp <= 139) and (diabp >= 80 and diabp <= 89): points += 30
            elif (sysbp >= 140) and (diabp >= 90): points += 75
            elif (sysbp > 180) and (diabp < 120): points += 100

            if diabetes == True: points += 10
            if alzheimers == True: points += 10
            if cancer == True: points += 10
            
            if points <= 20: sg.PopupOK("Low Risk", "You are at a low risk for health problems and are insurable.")
            elif points <= 50: sg.PopupOK("Moderate Risk", "You are at a moderate risk for health problems and are insurable.")
            elif points <= 75: sg.PopupOK("High Risk", "You are at a high risk for health problems and are insurable.")
            else: sg.PopupOK("Uninsurable", "Sorry, but you are not insurable because you are really unhealthy.")

            points = 0

        else:
            sg.popup_error("Input Validation Error", validate_input(height_inches, weight, age, sysbp, diabp))


window.close() # Close the GUI Window