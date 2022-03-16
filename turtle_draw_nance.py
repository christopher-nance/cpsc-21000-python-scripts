info = '''
#==============================================================================#
title               :turtle_draw_nance.py
description         :turtle draw assignment
author              :Chris Nance
date                :2022-03-14
version             :1.0
usage               :python turtle_draw_nance.py
notes               :
python_version      :3.10
#==============================================================================#
'''

## MODULES
import turtle


## VARIABLES
input_validated = False
input_file = ''
pen = turtle.Turtle()
boxSize = 450



## INPUT VALIDATION
while input_validated == False:
    try:
        input_file = input("Enter the name of the file you want to open: ")
        output_file = open(input_file, 'r')
        input_validated = True
        print("File has been loaded into memory!\n")
    except FileNotFoundError as error:
        print("File Not Found:", error, "\n")
    except Exception as error:
        print("No good:", error, "\n")



## FUNCTIONS
