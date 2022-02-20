# Chris Nance
# Prof. Klmup
# Programming Fundamentals
# 2/6/2022


## MODULES/LIBRARIES
from random import randint


print(r'''
*******************************************************
                  Rock Paper Scissors                
*******************************************************

In this classic game, you will play a number of
seven-game series of rock-paper-scissors against
the computer. I will show you who won each series,
and I will show you how many series you won and
lost at the end.
''')


## VARIABLES
series_to_play = int(input("Enter the amount of series you want to play: "))
user_score = 0
cpu_score = 0
series_ties = 0
round_ties = 0
user_series_won = 0
cpu_series_won = 0
user_action = ''
cpu_action = ''


## FUNCTION: Rock, Paper, Scissors LOGIC
def rpsLogic(user_input, cpu_input): # Function handles logic for the game. returns 0 if the pc wins, 1 if the human wins, and 2 if it's a tie.
    if user_input == 'r' and cpu_input == 'paper': return 0 # User: Rock   VS   PC: Paper
    if user_input == 'p' and cpu_input == 'scissors': return 0 # User: Paper  VS   PC: Scissors
    if user_input == 's' and cpu_input == 'rock': return 0 # User: Scissors VS PC: Rock
    if user_input == cpu_input[0]: return 2 #                User == PC (Need to parse string for the first letter for cpu_input for comparrison)
    return 1 # PC Didn't win, and there wasn't a tie so the human must have won


for series in range(1, series_to_play+1): # Iterate through all the rounds the user wanted to play, series denotes the series number; loop starts at 1 not 0 for output printing purposes.
    print("\nSeries:", series)

    ## COUNTER RESET
    user_score = 0
    cpu_score = 0
    round_ties = 0
    round_num = 0 # Round number counter.

    while round_num < 7: # Iterate through all 7 rounds of Rock, Paper, Scissors.
        round_num += 1

        ## INPUT & VALIDATION
        user_action = input("Enter r for rock, p for paper or s for scissors: ")
        while user_action.lower() != "r" and user_action.lower() != "p" and user_action.lower() != "s":  # Check input against lower()
            print("Oops! You need to choose either 'r' for rock, 'p' for paper or 's' for scissors.")
            user_action = input("Enter r for rock, p for paper or s for scissors: ")

        ## CPU_INPUT GENERATION
        # Randomy generate an integer from 1 up to and including 3 and convert it to a string for comparrison to user input. 
        cpu_action = randint(1,3)
        if cpu_action == 3:
            cpu_action = 'rock'
        elif cpu_action == 2:
            cpu_action = 'paper'
        elif cpu_action == 1:
            cpu_action = 'scissors'
        
        ## SERIES OUTPUT (Using Function: rpsLogic())
        if rpsLogic(user_action.lower(), cpu_action) == 0: # Call function fpsLogic() with arguments user_action as lower() and cpu_action
            print("The CPU won the round. They threw %s." % cpu_action)
            cpu_score += 1
            if cpu_score == 4: break # If the cpu_score is 4 then end the series early
        elif rpsLogic(user_action.lower(), cpu_action) == 1:
            print("You won the round! The CPU threw %s." % cpu_action)
            user_score += 1
            if user_score == 4: break # If the user_score is 4 then end the series early
        else: #  rpsLogic() returned 2 == Tie
            print("You TIED! You both threw", cpu_action)
            round_ties += 1

    ## SERIES COMPLETION OUTPUT
    print("Series #" + str(series), "is Over!")
    if user_score > cpu_score:
        print("You won the series!\nYou won", user_score, "rounds versus the CPU winning", cpu_score, "rounds and there were", round_ties, "tie(s).")
        user_series_won += 1
    elif cpu_score > user_score:
        print("You lost the series!\nYou won", user_score, "rounds versus the CPU winning", cpu_score, "rounds and there were", round_ties, "tie(s).")
        cpu_series_won += 1
    else:
        print("It was a tie!\nYou won", user_score, "the CPU won", cpu_score, "and there were", round_ties, "tie(s).")
        series_ties += 1


## GAME COMPLETION OUTPUT
print("\nGame Over!")
if user_series_won > cpu_series_won:
    print("You WON the game! You won", user_series_won, "series versus the CPU winning", cpu_series_won, "series. There were", str(series_ties), "tie(s).")
elif cpu_series_won > user_series_won:
    print("You LOST the game! You won", user_series_won, "series versus the CPU winning", cpu_series_won, "series. There were", str(series_ties), "tie(s).")
else:
    print("The game ended in a TIE! You won", user_series_won, "series versus the CPU winning", cpu_series_won, "series. There were", str(series_ties), "tie(s).")

print('''
*******************************************************
                THANK YOU FOR PLAYING!                
*******************************************************
''')
