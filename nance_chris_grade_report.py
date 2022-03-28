info = '''
#=====================================================================#
title               :nance_chris_grade_report.py
description         :Programming Fund. Assignment
author              :Chris Nance
date                :2022-03-28
version             :1.0
usage               :python nance_chris_grade_report.py
notes               :
python_version      :3.10
#=====================================================================#
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

totalCreditHours = 0
totalQualityPoints = 0


runningTotalPoints = 0
runningTotalHours = 0
semesterName = ['', '']
semesterGPA = [0, 100]
gpas = []

outputList = [['Semester', 'Hours', 'Points', 'GPA', 'Standing'], ['-----------------------------------------------------------------', '', '', '', '']]
outputParts = []
grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F']
gradesBreakdown = [[],[],[],[],[],[],[],[],[],[],[],[]] #A, A-, B+, B, B-, C+, C, C-, D+, D, D-, F


def appendToOutputList():
    outputParts.append(str(totalCreditHours))
    outputParts.append(str(totalQualityPoints))
    outputParts.append(round(totalQualityPoints/totalCreditHours, 2))
    if round(totalQualityPoints/totalCreditHours, 2) > 3.5:
        outputParts.append("DEAN'S LIST")
    else: outputParts.append('') # Placeholder string for the output.
    outputList.append(outputParts)
    if totalQualityPoints/totalCreditHours > semesterGPA[0]: # Best GPA: 0
        semesterName[0] = outputParts[0]
        semesterGPA[0] = totalQualityPoints/totalCreditHours
    elif totalQualityPoints/totalCreditHours < semesterGPA[1]: # Worst GPA: 1
        semesterName[1] = outputParts[0]
        semesterGPA[1] = totalQualityPoints/totalCreditHours

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


## MAIN
line = output_file.readline() # Begin reading the file.
while line: # While there are still lines to be read...
    line = line.strip() # Remove ending \n
    lineParts = line.split('\t') #Compile a list of line elements seperated by tab.

    if lineParts[0] == '': #New semester coming up...
        # Calculations and Appendages (Must be done in order: Hours, Points, GPA, Standing)
        gpas.append(totalQualityPoints/totalCreditHours)
        appendToOutputList()
        # Reset Counters & Output List 
        totalQualityPoints = 0
        totalCreditHours = 0
        outputParts = []
    elif lineParts[0][0:8] == 'Semester': # Semester line. (Parse the first element of lineParts from position 0 to 8.)
        # Append Semester to New Line
        outputParts.append(lineParts[1])
    else: # Must be a class with grades...
        totalCreditHours += int(lineParts[2]) # Track total credit hours for THIS semester.*
        runningTotalHours += int(lineParts[2]) # Track total credit hours for ALL TIME.**
        totalQualityPoints += qualityPointsDict[lineParts[3]] * int(lineParts[2]) # * but for points.
        runningTotalPoints += qualityPointsDict[lineParts[3]] * int(lineParts[2]) # ** but for points.

        for grade in grades: # Starts to compile lists within lists of classes organized by grade.
            if lineParts[3] == grade: # Basically I use the index of the grade in the \\ list for the correct list in the gradesBreakdown list of lists. Each sub-list in the gradesBreakdown list is a house for a list of classes belonging to the particular letter grade. That's a lot of lists!
                if len(gradesBreakdown[grades.index(lineParts[3])]) == 0: # Determine if leading element in sub-list ands then attach the letter grade if it is.
                    gradesBreakdown[grades.index(lineParts[3])].append(grade+'\t'+lineParts[0]) # Append to look like: "A-  CPSC10000"
                else:
                    gradesBreakdown[grades.index(lineParts[3])].append('\t'+lineParts[0])       # Append to look like: "    CPSC10000"
    
    line = output_file.readline() # Advance to the new line.


## OUTPUT
appendToOutputList() # Appends the last 'semester' of data to my output list.
outputList.append(['-----------------------------------------------------------------', '', '', '', '']) # Spacer for semesters and the Cumulative tail.
if round(runningTotalPoints/runningTotalHours , 2) > 3.5: # Determine HONORS note.
    outputList.append(['Cumulative', runningTotalHours, runningTotalPoints, round(runningTotalPoints/runningTotalHours , 2), 'HONORS'])
else:
    outputList.append(['Cumulative', runningTotalHours, runningTotalPoints, round(runningTotalPoints/runningTotalHours, 2), ''])
print('\n')
for item in outputList: print("{: <15} {: >7} {: >13} {: >13} {: >13}".format(*item)) # print my output list like a table.
print('\n')
print('Your best semester was', semesterName[0].upper(), '\nYour worst semester was', semesterName[1].upper(), '\n') #Print the best semesters.
print('Here is a breakdown of your classes by grades...')
for listByGrade in gradesBreakdown: # Loop through my list of lists and print them in order from A to F, letter grades not obtained are omitted already. (See line 110 - 115)
    for classStr in listByGrade:
        print(classStr)

input("Press any key to close the file and exit...")
output_file.close()
exit()