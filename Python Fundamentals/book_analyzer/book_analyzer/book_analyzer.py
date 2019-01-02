
import sys
#the program counts how many words have the given character in the correct position
#use modest.txt and poe.txt to test

def main(msg):  
    try:
        #gets name of file from user
        print(msg)
        filename = input("Enter File Name to Read:\n")
        fileopen = open(filename, 'r')
        
        letter = input("Letter to search for:\n")
        if " " in letter or letter.isalpha() == False or len(letter) >=2:
            print("Error: A single letter is required.")
            
            sys.exit(0)
    
        #gets position the user wants to search
        position = input("Enter Position (0 for first letter):\n")
        
        if position.isdigit() == False:
            print("Error: A number is required.")
            sys.exit(0)
        else:
            position = int(position)
        #read the file
        filedata = fileopen.read().split()
        count = 0
        #loop to count letter on specific place
        for item in filedata:
            if len(item) >= (position +1):
                if item[position] == letter.lower() or item[position] == letter.upper():
                    count += 1
                    
        print("There are", count ,"words with", letter ,"in position", position)
        
    except OSError:
        print("Error: Could Not Open File.")
        
main("Welcome to Book Analyzer v0.1")
