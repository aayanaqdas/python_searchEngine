filenames = ["tekstfil1.txt", "tekstfil2.txt", "tekstfil3.txt"]

def read_file():
    text = ""
    for file in filenames: # Loop through each filename in the filenames list.
        with open(file, "r", encoding="utf-8") as f: # Open the current file in read mode with UTF-8 encoding.
            text += f.read() # Read the content of the file and append it to the text string
            text_list = [line for line in text.splitlines()]
            
    return text_list 

