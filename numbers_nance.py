info = '''
#==============================================================================#
title               :numbers_nance.py
description         :numbers assignment...
author              :Chris Nance
date                :2022-03-13
version             :1.0
usage               :python numbers_nance.py <int>
notes               :
python_version      :3.10
#==============================================================================#
'''

## MODULES
import sys

## VARIABLES
numberOfArgs = len(sys.argv)

## MAIN SCRIPT

print("\nNumbering Systems with Python\n", info)
print("Total arguments passed: " + str(numberOfArgs))

for arg in range(numberOfArgs): # List all arguments passed.
    print("Argument", str(arg+1)+':', sys.argv[arg]) # Arguement #: <Argument>

def convertNumbers():
    numberAsAString = ''
    numberAsAnInt = 0
    numberAsHex = hex(0)
    print()
    try:
        numberAsAString = sys.argv[1]
        numberAsAnInt = int(numberAsAString, base=10)
        numberAsHex = hex(numberAsAnInt)
        print("Input:  " + numberAsAString)
        print("Hex:    " + numberAsHex)
        print("Number: " + str(numberAsAnInt))
    except ValueError as error:
        print('[ERROR]: The 2nd argument MUST be an integer.')

if numberOfArgs == 2:
    convertNumbers()
elif numberOfArgs == 1:
    print("You must pass an additional INTEGER argument...")
else:
    print("Too many arguments passed, only using the 2nd one...")
    convertNumbers()
