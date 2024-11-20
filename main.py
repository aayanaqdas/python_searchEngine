filenames = ["tekstfil1.txt", "tekstfil2.txt", "tekstfil3.txt"]


def main():
    while True: # loop until user exits
        word = str(input('\033[32mEnter a word (4 for exit): \033[m')) # takes the word from userinput as string
        if len(word) < 1: #check if word is at least 1 character long
            print("Word must be at least 1 characters long")
        elif word == "4": 
            break #Exit program
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
    for line in text:
        if word.lower() in line.lower():
            print(line.replace(word, f'\033[33m{word}\033[m')) # Highlight the word in the line with 33m color code (yellow)
            found = True
            word_count += 1
        
    if found:
        print(f"The word '\033[36m{word}\033[m' was found '\033[36m{word_count}\033[m' times)") #cyan color
    if not found:
        print(f"\033[31mNo results found for '{word}'\033[m") #red color


main()