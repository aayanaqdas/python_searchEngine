#color code format: "\033[44;33mHello World!\033[m"
# 4 = background color
# 3 text color

# 0 black
# 1 red
# 2 green
# 3 yellow
# 4 blue
# 5 magenta
# 6 cyan
# 7 white
# 9 default

import re
filenames = ["tekstfil1.txt", "tekstfil2.txt", "tekstfil3.txt"]


def main():
    read_file()
    while True: # loop until user exits
        word = str(input('\033[32mEnter a word (4 for exit): \033[m')) # takes the word from userinput as string. (ANSI escape code \033[32m for green)
        if len(word) < 1: #check if word is at least 1 character long
            print("\033[31mWord must be at least 1 characters long\033[m")
        elif word == "4":
            exit_program = input("\033[31mAre you sure you want to exit? J/N \033[m") #(ANSI escape code \033[31m for red)
            if exit_program.lower() == "j":
                break
        else:
            find_line(word)

def read_file():
    # denne funksjonen leser filene og returnerer en kombinert liste av alle tekstene (krav lesInnTekst)
    text_list = []
    for file in filenames: # Loop through each filename in the filenames list.
        with open(file, "r", encoding="utf-8") as f: # Open the current file in read mode with UTF-8 encoding.
            lines = f.readlines() # Read the content of the file and append it to the text list
            text_list.append((file, lines)) # Append a tuple of filename and lines to the text list
    return text_list

def find_line(word):
    # denne funkjsonen kan finne linje (krav finnLinje), ord (krav finnOrd) og returnere true eller false om den fant ordet.
    # viser også hvilken filnavn og linje den ble funnet i
    text_files = read_file() # returns filename and text_list
    found = False
    total_word_count = 0
    lower_word = word.lower()  # Convert the word to lower case
    file_word_counts = {}  # Dictionary to store word counts for each file


    for filename, lines in text_files:
        file_word_count = 0  # Initialize word count for the current file
        for line_number, line in enumerate(lines, start=1):
            lower_line = line.lower()  # Convert the line to lower case
            if lower_word in lower_line:
                # This line uses a regular expression to search for the word (case-insensitive) in the line,
                # and replaces it with the same word highlighted in yellow (ANSI escape code \033[33m for yellow).
                highlighted_line = re.sub(f'(?i)({re.escape(word)})', r'\033[33m\1\033[m', line)  
                print(f"{filename} (line {line_number}): {highlighted_line.strip()}")
                found = True
                file_word_count += 1
                total_word_count += 1
                file_word_counts[filename] = file_word_count  # Store the word count for the current file

    
    if found:
        print(f"Total results for '\033[36m{word}\033[m' found '\033[36m{total_word_count}\033[m' times)") #(ANSI escape code \033[36m for cyan)
        for filename, count in file_word_counts.items():
            print(f"'\033[36m{count}\033[m' times in '\033[34m{filename}\033[m'")
    if not found:
        print(f"\033[31mNo results found for '{word}'\033[m") #(ANSI escape code \033[31m for red)h


main()