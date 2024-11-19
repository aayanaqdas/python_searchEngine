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
            print(line)
            found = True
            word_count += 1
    print(f"The word '{word}' was found {word_count} times)")
    if not found:
        print("Word not found")




def main():
    while True: # loop until user exits
        word = input("Enter a word (4 for exit): ") # takes the word from userinput
        if word == "4":
            break
        findLine(word)

main()