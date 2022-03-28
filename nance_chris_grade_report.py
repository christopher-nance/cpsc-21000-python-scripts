info = '''
#==============================================================================#
title               :transcript_nance.py
description         :numbers assignment...
author              :Chris Nance
date                :2022-03-28
version             :1.0
usage               :python transcript_nance.py
notes               :
python_version      :3.10
#==============================================================================#
'''

print(info+'''
**********************************************************************
                        Grade Report Tool
**********************************************************************
''')
qualityPointsDict = {
##########>> Outstanding
'A' : 4.0,
'A-': 3.7,
##########>> Good
'B+': 3.3,
'B' : 3.0,
'B-': 2.7,
##########>> Satisfactory
'C+': 2.3,
'C' : 2.0,
##########>> Passing
'C-': 1.7,
'D+': 1.3,
'D' : 1.0,
'D-': 0.7,
##########>> Failing
'F' : 0.0,
}

input_validated = False
input_file = r""
output_file = ''

def generateGPA(qualityPoints, creditHours):
    try:
        float(qualityPoints)
        float(creditHours)
    except:
        print("You need to pass a floatable argument to generateGPA.")


## INPUT VALIDATION
while input_validated == False:
    try:
        input_file = input("Enter name of grade report file: ")
        output_file = open(input_file, 'r')
        input_validated = True
        print("File has been loaded into memory!\n")
    except FileNotFoundError as error:
        print("File Not Found:", error, "\n")
    except Exception as error:
        print("No good:", error, "\n")


line = output_file.readline()

totalCreditHours = 0
totalQualityPoints = 0
gpa = 0

runningAverageGPA = 0
runningTotalPoints = 0
runningTotalHours = 0

outputList = [['Semester', 'Hours', 'Points', 'GPA', 'Standing'], ['----------------------------------------------------------------------', '', '', '', '']]
while line:
    line = line.strip()
    lineParts = line.split('\t')

    if lineParts[0] == '':
        gpa = 0
        totalQualityPoints = 0
        totalCreditHours = 0
    elif lineParts[0] == 'Semester':
        print("Semester:", lineParts[1])

    else:
        print("Class:", lineParts[0], "Name of Class:", lineParts[1], "Credit Hours:", lineParts[2], "Grade:", lineParts[3])
        totalCreditHours += int(lineParts[2])
        totalQualityPoints += qualityPointsDict[lineParts[3]]
    
    
    line = output_file.readline()
