filenames = ["tekstfil1.txt", "tekstfil2.txt", "tekstfil3.txt"]

def read_file():
    text = ""
    for file in filenames: # Loop through each filename in the filenames list.
        with open(file, "r", encoding="utf-8") as f: # Open the current file in read mode with UTF-8 encoding.
            text += f.read() # Read the content of the file and append it to the text string
            text_list = [line for line in text.splitlines()] # Split the text string into a list of lines
    return text_list

def findLine():
    text = read_file() # reads the text from the files
    while True: #infinite loop
        word = input("Enter a word: ") # takes the word from userinput
        found = False
        for line in text:
            if word in line.split(): #if word is in the text line
                print(line)
                found = True

        if not found:
            print("Word not found")

findLine()
