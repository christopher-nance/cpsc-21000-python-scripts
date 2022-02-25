# Match-Maker.py

# Christopher Nance
# Prof. Pogue
# 2/25/2022
# Version 1.0


## MODULES/LIBRARIES
from random import randint
from time import sleep


## VARIABLES
user_score = 0
user_answer = 0


## DICTIONARIES & TABLES
questionAndAnswerDict = (
#   ['QUESTION', SCORE, WEIGHT] 
    ['question 1 s=1', 1, 1],
    ['question 2 s=2', 2, 3],
    ['question 3 s=3', 3, 2],
    ['question 4 s=4', 4, 1],
    ['question 5 s=5', 5, 2],
)


## MAIN PROGRAM
for question_num in range(0,5):
    print("Asking question", str(question_num+1), ".")
    question, answer, weight, user_answer = questionAndAnswerDict[question_num][0], questionAndAnswerDict[question_num][1], questionAndAnswerDict[question_num][2], 0
    print('\n')
    print("Question:", question)
    while user_answer not in [1,2,3,4,5]:
        try:
            user_answer = int(input('Your Answer (From 1 to 5): '))
        except ValueError as error:
            print("[ERROR]: Sorry, you MUST enter an INTEGER from 1 to 5:", error)
        except Exception as error: 
            print("[ERROR]: There was an unknown error. Please try entering in an integer from 1 to 5:", error)
    
    user_score += user_answer * weight


## SCORE OUTPUT/REMARKS
print("You scored", str(user_score), "points out of the possible 100 available.")
if user_score < 50:
    print("Probably not the best match...")
elif user_score < 70:
    print("This seems like we would be better off without eachother...")
elif user_score < 90:
    print("This could really work out!")
elif user_score > 90:
    print("Perfect")
print('\n'*2)
input('Press Enter to close this window...')