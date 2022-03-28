input_validated = False
input_file = r""
output_file = ''


## INPUT VALIDATION
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


wordListForGame = []

line = output_file.readline()
while line:
    line.strip()
    characters = line.split()
    if len(line) ==5:
        wordListForGame.append(line)
    line = output_file.readline()

print(wordListForGame)
print(len(wordListForGame[0]))
print(wordListForGame[0])