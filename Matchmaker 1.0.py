#title           :matchmaker_nance.py
#description     :This will ask a series of questionsd and determine match %.
#author          :Chris Nance
#date            :20220313
#version         :1.0
#usage           :python matchmaker_nance.py
#notes           :Edit the questionAndAnswerDict Dictionary below.
#python_version  :3.10
#==============================================================================#==============================================================================#==============================================================================

# Please add, remove or modify any questions in the dictionary. The first number in each array is the correct score for the question while the second number is the weight (or how important) the question is to you.
# The script will automatically adjust the total points available and output based on your modifications to this dictionary. 
questionAndAnswerDict = (
#   ['QUESTION', SCORE, WEIGHT] 
    ['iPhone is better than Android', 4, 1],
    ['I prefer the outdoors rather than being inside', 4, 3],
    ['Computer Science is one of the coolest fields of study', 5, 3],
    ['Data science is really fun', 1, 2],
    ['I like all four seasons rather than it just being hot all year', 2, 2],
)

#==============================================================================#==============================================================================#==============================================================================



## VARIABLES
user_score = 0
user_score_nw = 0
user_answer = 0
total_available = 0
total_available_nw = 0


## HEADER
print('''
--------------------------------------
--          MATCHMAKER 1.0          --
--------------------------------------

This program will ask '''+str(len(questionAndAnswerDict))+''' questions.\nYou will respond to each question with a\nnumber 1 through 5. The number 1 means you\ndisagree while the number 5 means you highly\nagree.At the end you wil be given your final\nscore and match maker percentage.
''')


## MAIN PROGRAM
for question_num in range(0,len(questionAndAnswerDict)): # Ask all questions in the dictionary; in order.
    question, answer, weight, user_answer = questionAndAnswerDict[question_num][0], questionAndAnswerDict[question_num][1], questionAndAnswerDict[question_num][2], 0 # Multi-Assignment of question, answer, weight and placeholder for user_score.
    print('\n')
    print("Question:", question)
    while user_answer not in [1,2,3,4,5]:
        try:
            user_answer = int(input('Your Answer (From 1 to 5): '))
            if user_answer in [1,2,3,4,5]: break # Break on condition being met so error print does not happen.
        except ValueError as error:
            print("[ERROR]: Sorry, you MUST enter an INTEGER from 1 to 5:", error)
        except Exception as error: 
            print("[ERROR]: There was an unknown error. Please try entering in an integer from 1 to 5:", error)
        print("[ERROR]: You need to enter an INTEGER from 1 to 5...") 
    
    user_score += abs(answer - user_answer) * weight # Calculate the running total of points the user has accumulated. Abs prevents negatives.
    user_score_nw += abs(answer - user_answer)
    total_available += answer*weight # Calculate the total points available based on the dictionary of questions. Adding/Removing/Editing questions require no code change.
    total_available_nw += answer

user_score = total_available - user_score # Obtain true user score by subtracting their score from the total score available.


## SCORE OUTPUT/REMARKS
print(f"\n\nMatch Percent: {user_score/total_available*100:.2f}%.\nYou scored", str(user_score), "weighted points out of the possible", str(total_available), "available.\nYou scored", str(user_score_nw), "non-weighted points out of the possible", str(total_available_nw), "available.")
if user_score < total_available*0.5: # <50% match
    print("Maybe we would be better off never talking again...")
elif user_score < total_available*0.7: # <70% match
    print("I'm thinking we're just friends...")
elif user_score < total_available*0.9: # <90% match
    print("This could really work out...")
elif user_score > total_available*0.9: # >90% match
    print("Perfect!")
print('''
--------------------------------------
--          MATCHMAKER 1.0          --
--------------------------------------
''')
input('Thank you for using Match Maker 1.0\nPress Enter to close this window...')