import re
filenames = ["tekstfil1.txt", "tekstfil2.txt", "tekstfil3.txt"]


def main():
    while True: # loop until user exits
        word = str(input('\033[32mEnter a word (4 for exit): \033[m')) # takes the word from userinput as string. (ANSI escape code \033[32m for green)
        if len(word) < 1: #check if word is at least 1 character long
            print("\033[31mWord must be at least 1 characters long\033[m")
        elif word == "4":
            exit_program = input("\033[31mAre you sure you want to exit? J/N \033[m") #(ANSI escape code \033[31m for red)
            if exit_program.lower() == "j":
                break
        else:
            findLine(word)

def read_file():
    text = ""
    for file in filenames: # Loop through each filename in the filenames list.
        with open(file, "r", encoding="utf-8") as f: # Open the current file in read mode with UTF-8 encoding.
            text += f.read() # Read the content of the file and append it to the text string
            text_list = text.splitlines() # Split the text string into a list of lines
    return text_list

def findLine(word):
    text = read_file() # reads the text from the files
    found = False
    word_count = 0
    lower_word = word.lower()  # Convert the word to lower case
    for line in text:
        lower_line = line.lower()  # Convert the line to lower case
        if lower_word in lower_line:
            # This line uses a regular expression to search for the word (case-insensitive) in the line,
            # and replaces it with the same word highlighted in yellow (ANSI escape code \033[33m for yellow).
            highlighted_line = re.sub(f'(?i)({re.escape(word)})', r'\033[33m\1\033[m', line)  
            print(highlighted_line)
            found = True
            word_count += 1
        
    if found:
        print(f"Results for '\033[36m{word}\033[m' found '\033[36m{word_count}\033[m' times)") #(ANSI escape code \033[36m for cyan)
    if not found:
        print(f"\033[31mNo results found for '{word}'\033[m") #(ANSI escape code \033[31m for red)


main()