info = '''
#==============================================================================#
title               :TurtleDraw_cn.py
description         :turtle draw assignment
author              :Chris Nance
date                :2022-03-26
version             :1.0
usage               :python TurtleDraw_cn.py
notes               :
python_version      :3.10
#==============================================================================#
'''

## MODULES
import turtle


## VARIABLES
#> Edit these:
boxSize = 450 # Window size 
penSpeed = 0 # Max Speed is in-fact 0, not 10.

#> Leave these alone...
input_validated = False
input_file = r""
output_file = ''
pen = turtle.Turtle()
counter = 0
prev_xPoint = 0
prev_yPoint = 0
totalDistance = 0
countDistance = False


## INPUT VALIDATION

print(info+'\n')
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


## INITIAL TURTLE SETUP
pen.speed(penSpeed)
pen.penup()
turtle.setup(boxSize, boxSize)


## MAIN SCRIPT
line = output_file.readline()
while line:
    counter += 1
    args = line.split(' ') # Split text args into an array of args
    line = output_file.readline() # Advance line +1
    if len(args) == 3:
        lineColor, xPoint, yPoint = args[0], int(args[1]), int(args[2]) # Define Arguments

        pen.color(lineColor) # Set line color
        pen.goto(xPoint, yPoint) # Move turtle
        pen.pendown() # Place pen down to mark turtle line
        
        if countDistance == True: # Count the distance if the pen was already down.
            distanceMoved = pen.distance(prev_xPoint, prev_yPoint)
            totalDistance += distanceMoved
        
        prev_xPoint = xPoint
        prev_yPoint = yPoint
        countDistance = True # Pen is forsure down now, so let's start counting distance.

    elif len(args) == 1:
        pen.penup() # Stop marking turtle lines.
        countDistance = False # Pen is up, stop counting distance.
    else:
        print("Uh oh, there was a problem with the arguments passed from line ", str(counter), '.\nOnly allowed to pass either single argument "stop" or 3 arguments <color>, <xPoint>, <yPoint>.')


## ENDING OUTPUT AND FILE CLOSE
pen.goto(50,-200) # Move to bottom right area of screen
totalDistance = round(totalDistance, 2) # Roujnd off the total distance float.
pen.write("Total Distance Moved: "+str(totalDistance), font=("Arial", 10, "bold")) # Output total distance to turtle window.
input('Press any key to close the window.') # Wait for key press to close window. 
output_file.close() # Close the input file after the user is done with it.
