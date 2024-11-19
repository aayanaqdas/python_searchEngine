filenames = ["tekstfil1.txt", "tekstfil2.txt", "tekstfil3.txt"]

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
    word_lower = word.lower()
    for line in text:
        if word_lower in line.lower():
            print(line.replace(word_lower, f'\033[33m{word_lower}\033[m')) # Highlight the word in the line with 33m color code (yellow)
            found = True
            word_count += 1
    print(f"The word '{word}' was found {word_count} times)")
    if not found:
        print("Word not found")




def main():
    while True: # loop until user exits
        word = str(input("Enter a word (4 for exit): ")) # takes the word from userinput
        if len(word) < 1:
            print("Word must be at least 1 characters long")
        elif word == "4":
            break
        else:
            findLine(word)

main()