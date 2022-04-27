info = '''
#========================================================================================#
title               :collection_nance.py
description         :Creates a UI to make a list of CPUs and save it
author              :Chris Nance
date                :2022-04-27
version             :1.0
usage               :python collection_nance.py
notes               :Uses object oriented programming to create array of CPU objects
python_version      :3.10
#========================================================================================#
'''


import datetime
import PySimpleGUI as sg

AMD_Series = ['Ryzen', 'Threadripper', 'Other'] #   AMD CPU Series
Intel_Series = ['Core', 'Xeon', 'Other'] #          Intel CPU Series
CPUs = [] # Class Objects of CPUs. 

multilineString = '' # Placeholder for creating the string that gets 'updated' on the GUI (see lines 116-124)

def createWindow(): # Create the window for the main Gui Frame


    elements = [
        [sg.Text('CPU Collection Tool')],

        [sg.Text('CPU Manufacturer:'), sg.DropDown(['AMD', 'Intel'], size=(5,0), key='manufacturer', enable_events=True)],
        [sg.Text('CPU Series:'), sg.DropDown([], size=(13,0), key='series', enable_events=True)],
        [sg.Text('CPU Name:'), sg.Input(size=(7,0), key='name')],
        [sg.Text('CPU Base Clock Speed  (GHz):'), sg.Input(size=(5,0), key='base_speed')],
        [sg.Text('CPU Boost Clock Speed (GHz):'), sg.Input(size=(5,0), key='boost_speed')],
        [sg.Text('Year Introduced:'), sg.Input(size=(4,0), key='year')],
        [sg.OK(), sg.CloseButton('Close'), sg.Save('Save to File', key='save')],
        [sg.Multiline('', key='cpu_list', size=(325,300))]
    ]

    return sg.Window('CPU Collection', elements, size=(350,550), use_default_focus=True)

def createSaveWindow(): # Create the save window

    elements = [
        [sg.Text('Enter a file name or browse for a location:')],
        [sg.Input(key='fileToSaveTo'), sg.FileSaveAs('Browse')],
        [sg.OK(), sg.Cancel()],
    ]

    return sg.Window('Save CPU Collection', elements, use_default_focus=True)

def validate(manufacturer, name, series, base_speed, boost_speed, year): # Validate the input. Returns True if it's good, or a string if it is an error.

    if manufacturer == '' or name == '' or series == '' or base_speed == '' or boost_speed == '' or year == '': return 'Please make sure all fields are filled out.' # Test for all field filled out

    try:
        bases = float(base_speed) # Test if integer
        if bases < 0 or bases > 7: return 'Your base speed is out of bounds.' # Test for out-of-bounds ranges
    except:
        return 'Ensure that your Base Speed is a numeric decmial with no letters.'
    
    try:
        boosts = float(boost_speed)
        if boosts < 3 or boosts > 10: return 'Your boost speed is out of bounds.'
        if boosts < float(base_speed): return 'Your boost clock cannot be less than your base clock.'
    except:
        return 'Ensure that your Boost Speed is a numeric decmial with no letters.'
    
    try:
        if len(year) != 4: # Test if year is 4 long.
            return 'Ensure that your Year Introduced is a four-digit integer. [1]'
        if int(year) > datetime.datetime.now().year: # Test to make sure yea rinputted is not in the future
            return 'Impossible! The year you inputted has not happened yet...'
    except:
        return 'Ensure that your Year Introduced is a four-digit integer. [2]'
    
    return True # Validated

class CPU: # Create a class called CPU for creating CPU Objects
    
    def __init__(self, manufacturer, name, series, base_speed, boost_speed, year):
        self.manufacturer = str(manufacturer)
        self.series = str(series)
        self.name = str(name)
        self.base_speed = float(base_speed)
        self.boost_speed = float(boost_speed)
        self.year = int(year)
    
    def __str__(self):
        return ('CPU:' + self.manufacturer + ' ' + self.series + ' ' + self.name + '\t' + 'Base/Boost Speeds (GHz):' + str(self.base_speed) + '/' + str(self.boost_speed) + 'GHz\n')
    
    def __gt__(self, other): # Allow ython's sort command to sort the CPUs based on CPU base speed.
        return self.base_speed > other.base_speed
    
    def age(self): # Determine how long ago the CPU was released according to the current year for the computer this program runs on.
        self.cpuAge = int(datetime.datetime.now().year) - self.year
    
    def speed_delta(self): # Determine the speed difference between the boost clock and the base clock
        self.cpu_speed_delta = self.boost_speed - self.base_speed



window = createWindow()
while True:
    event, values = window.read()
    if event == 'manufacturer': # Help maintain valid input by limiting what series are available when selecting the intel or cpu brand./
        if values['manufacturer'] == 'AMD':
            window['series'].update('', AMD_Series)
        else:
            window['series'].update('', Intel_Series)

    if event == sg.WIN_CLOSED or event=="Exit":
        exit()
    elif event == 'OK':
        if validate(values['manufacturer'], values['name'], values['series'], values['base_speed'], values['boost_speed'], values['year']) == True: # If validation was good...
            CPUs.append(CPU(values['manufacturer'], values['name'], values['series'], values['base_speed'], values['boost_speed'], values['year'])) # Create a new object CPU and append to list of CPUs.
            CPUs.sort(reverse=True) # Reverse sort (SO higher clock speed is better)
            for cpu in CPUs: # Compile a string for the multiline.
                if multilineString == '':
                    multilineString = 'Manufacturer:\t\t'+ cpu.manufacturer+ '\nSeries:\t\t'+ cpu.series + '\nName:\t\t' + cpu.name + '\nBase Speed:\t\t' + str(cpu.base_speed) + ' GHz\nBoost Speed:\t\t' + str(cpu.boost_speed) + 'GHz\nYear Introduced:\t\t' + str(cpu.year)
                else:
                    multilineString = multilineString + '\n\nManufacturer:\t\t'+ cpu.manufacturer+ '\nSeries:\t\t'+ cpu.series + '\nName:\t\t' + cpu.name + '\nBase Speed:\t\t' + str(cpu.base_speed) + ' GHz\nBoost Speed:\t\t' + str(cpu.boost_speed) + 'GHz\nYear Introduced:\t\t' + str(cpu.year)
            window['cpu_list'].update(multilineString) # Update the multiline.
            multilineString = '' # Reset multiline string placeholder.
        else:
            sg.popup_error('Validation Error', validate(values['manufacturer'], values['name'], values['series'], values['base_speed'], values['boost_speed'], values['year'])) # Validation error popup
    if event == 'save':
        window2 = createSaveWindow() # Handle saving below...
        while True:
            event2, values2 = window2.read()
            if event2 == 'OK':
                try:
                    file = open(values2['fileToSaveTo'], 'w') # Create or write to an existing file.
                    for cpu in CPUs:
                        file.write(cpu.__str__()) # Write all CPU object data to the file using the __str__() function. 
                    file.close() # Close the file.
                    window2.close() # Close save window
                    sg.PopupOK("Save Success", "The file has been saved to the following location:\n", values2['fileToSaveTo']) # Popup saying save was good
                except Exception as error:
                    window2.close()
                    sg.PopupError("Save Error", "Unable to write data to file:\n", error) # Popup saying save failed
            elif event2 == sg.WIN_CLOSED or event2=="Exit" or event2 == 'Cancel':
                window2.close() # SSave window closed or cancel clicked.
                break # Break the save window loop and go back to the main window.

    

