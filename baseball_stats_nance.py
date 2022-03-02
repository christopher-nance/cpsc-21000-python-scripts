# Chris Nance
# Prof. Klump
# 3/2/2022
# Baseball Stats Assignment



## MODULES & LIBRARIES
from baseball import * # banner, batting_avg, onBase_pct, hr_ratio, slug_pct, isolated_pwr, onBase_per_slug, earnedRun_avg, walks_hits_innings_pitched
from time import sleep


## VARIABLES
input_validated = False
input_file = ''
output_file = ''

## FILE INPUT VALIDATION
while input_validated == False:
    try:
        input_file = input("Enter the name of stats file: ")
        output_file = open(input_file, 'r')
        input_validated = True
        print("File has been loaded into memory!\n")
    except FileNotFoundError as error:
        print("File Not Found:", error, "\n")
    except Exception as error:
        print("No good:", error, "\n")


## MAIN SCRIPT
while True: # Broken with 'break' instead of a variable two lines down...
    line = output_file.readline()
    if line == '': break

    print(line)
    if line.strip() != "P": # Hitter
        # Do hitter stuff
        print("Hitter Stats:")
    else:
        # Do pitcher stuff
        print("Pitcher Stats:")



