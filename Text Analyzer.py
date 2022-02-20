# Chris Nance
# Prof. Klump
# Feb. 20th, 2022
# Text Analyzer

print('''
**********************************************************************
                          TEXT ANALYZER V1.0
**********************************************************************
This program first asks you to enter the name of a text file. It will
load the file into memory. It will then give you a set of options
to
choose from that will enable you to learn more about the contents of
the file.
''')

## VARIABLES
input_validated = False
input_file = ''
user_option = 0


## TABLES
menu_options_table = [1, 2, 3, 4, 5, 6]
vowels = ['a', 'e', 'i', 'o', 'u']


## FUNCTIONS
def menu_options(): # Ask, Validate and Return the user option. Shows mneu too.
    print('''Here are your choices:
    1. Count the number of characters.
    2. Count the number of vowels.
    3. Count the number of words.
    4. Extract a portion of the file.
    5. Print the characters of the file backwards
    6. Quit
    ''')
    user_option = 0
    while user_option not in menu_options_table:
        try:
            user_option = int(input("Select a Menu Option: "))
            if user_option in menu_options_table: break
            print("That is NOT a valid menu option.\n")
        except ValueError as error:
            print("ERROR: You need to select an integer:", error, "\n")
    return user_option # Return the user_option AFTER validation.


## FILE INPUT VALIDATION
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
    

## MAIN PROGRAM
while user_option != 6:
    output_file = open(input_file, 'r')
    
    if user_option == 5:
        print("Printing characters of the file in reverse!")
        output_file_string = output_file.read() # Convert contents of file to string
        rev_string = output_file_string[::-1] # Splice from end --> start
        rev_string_limited = ''
        count = 0
        for num, char in enumerate(rev_string):
            rev_string_limited += char # Build the new string with 70 character per line limit.
            if num % 70 == 0: # Check if the line is ending on a multiple of 70 (means 70 characters on the line) Remainder is 0 if True
                rev_string_limited += '\n'
        print(rev_string_limited)
    elif user_option == 4:
        print("I need a bit more information before I can extract some text...")
        output_file_string = output_file.read() # Convert contents of file to string
        valid_indexes = False
        while valid_indexes != True:
            try:
                index_1 = int(input("Please enter the index of the first character to include: "))
                index_2 = int(input("Please enter the index of the last character to include: "))
                valid_indexes = True
            except ValueError as error:
                print("ERROR: The index MUST be an integer, not a letter.", error, "\n")
        # Validation complete, use index_1 and index_2 to splice string.
        print(output_file_string[index_1:index_2+1])
    elif user_option == 3:
        print("Counting the number of words in the file...")
        number_of_words = 0
        for line in output_file: # Iterate lines
            words = line.split(' ') # Create a list of the words without spaces.
            number_of_words += len(words) # Add each line of words to the total number of words
        print("There are", str(number_of_words), "words in the file.")
        output_file.close()
    elif user_option == 2:
        print("Counting the number of vowels in the file...")
        number_of_vowels = 0
        for line in output_file: # Iterate per line
            for char in line: # Iterate per character
                if char.lower() in vowels: # Check char.lower() if it is in vowels. 
                    number_of_vowels += 1
        print("Thre are", str(number_of_vowels), "vowels in the file.")
        output_file.close()
    elif user_option == 1:
        print("Counting the number of characters in the file...")
        number_of_characters = 0
        for line in output_file:
            for char in line:
                if char != '' and char != ' ':
                    number_of_characters += 1
        print("Thre are", str(number_of_characters), "charcaters in the file.")
        output_file.close()
    
    output_file.close()
    user_option = menu_options()

print('''
**********************************************************************
                  Thank you for using this program.
**********************************************************************
''')