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
banner('intro')
while input_validated == False:
    try:
        input_file = input("Enter the name of stats file: ")
        output_file = open(input_file, 'r')
        input_validated = True
        print("File has been loaded into memory!\n")
    except FileNotFoundError as error:
        print("[ERROR] File Not Found:", error, "\n")
    except Exception as error:
        print("[ERROR] No good:", error, "\n")


## TABLES/LISTS
Hitters, HitterStatsTitles = [], [['First Name', 'Last Name', 'Avg', 'OBP', 'HRR', 'SP', 'ISO', 'OPS']]
Pitchers, PitcherStatsTitles = [], [['First Name', 'Last Name', 'ERA', 'WHIP']]


## MAIN SCRIPT
while True: # Broken with 'break' instead of a variable two lines down...
    line = output_file.readline().strip()
    if line == '': break
    if line.upper() != "P": # Hitter
        # Do hitter stuff
        hitterStats_ = [] # First0, Last1, At-Bats2, Runs3, Hits4, Doubles5, Triples6, Home aRuns7, Runs Batted In8, Walks9, Strikeouts10, Stolen Bases11
        hitterStats_.append(output_file.readline().strip()) # First Name
        hitterStats_.append(output_file.readline().strip()) # Last Name
        for stat in range(1, 11): hitterStats_.append(float(output_file.readline().strip())) # For each stat, add it to the hitterStats_ as a float value.
        calculatedStats_Hitter = [ # Create a list for each player with their name and calculated stats using functions in module baseball.
            hitterStats_[0], hitterStats_[1],
            batting_avg(hitterStats_[4], hitterStats_[2]), # AVG
            onBase_pct(hitterStats_[4], hitterStats_[9], 0, hitterStats_[2], 0), # OBP
            hr_ratio(hitterStats_[2], hitterStats_[7]), # HRR
            slug_pct(hitterStats_[4], hitterStats_[5], hitterStats_[6], hitterStats_[7], hitterStats_[2]), # SP
            isolated_pwr(slug_pct(hitterStats_[4], hitterStats_[5], hitterStats_[6], hitterStats_[7], hitterStats_[2]), batting_avg(hitterStats_[4], hitterStats_[2])), # ISO
            onBase_per_slug(onBase_pct(hitterStats_[4], hitterStats_[9], 0, hitterStats_[2], 0), slug_pct(hitterStats_[4], hitterStats_[5], hitterStats_[6], hitterStats_[7], hitterStats_[2])), # OPS
        ]
        Hitters.append(calculatedStats_Hitter) # Append our completed hitter stats list to the compiled Hitters List for final output. [[Nested], [Lists]]
    else:
        # Do pitcher stuff (same as hitter but less to work with)
        pitcherStats_ = [] # First0, Last1, Wins2, Losses3, Innings Pitched4, Hits Allowed5, Earned Runs6, Homeruns7, Walks8, Strikeouts9
        pitcherStats_.append(output_file.readline().strip())
        pitcherStats_.append(output_file.readline().strip())
        for stat in range(1, 9): pitcherStats_.append(float(output_file.readline().strip()))
        calculatedStats_Pitcher = [
            pitcherStats_[0], pitcherStats_[1],
            earnedRun_avg(pitcherStats_[6], pitcherStats_[4]), # ERA
            walks_hits_innings_pitched(pitcherStats_[8], pitcherStats_[5], pitcherStats_[4]) # WHIP
        ]
        Pitchers.append(calculatedStats_Pitcher) # Append to compiled Pitchers List for final output.


## OUTPUT
print('                                   *** Batting Statistics ***\n')
for item in HitterStatsTitles: print("{: <15} {: <15} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10}".format(*item))
print('-------------------------------------------------------------------------------------------------')            
for item in Hitters: print("{: <15} {: <15} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10}".format(*item))
print('\n\n')
print('                  *** Pitching Statistics ***\n')
for item in PitcherStatsTitles: print("{: <15} {: <15} {: >10} {: >10}".format(*item))
print('-----------------------------------------------------')              
for item in Pitchers: print("{: <15} {: <15} {: >10} {: >10}".format(*item)) 


## CLOSING BANNER
print('\n')
banner('closing')
input('\nPress ENTER to exit...')