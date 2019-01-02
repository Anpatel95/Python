#Random pi guessing
#random appearing numbers by reading digits of pi (only "appears" random)
if __name__ == '__main__':
    #used https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/digits_of_pi as pi.txt

    pidata  = open("pi.txt","r")
    #user input
    name = input("Enter your name")
    print("Hey, ", name)

    #lenght of name 
    seed = int(len(name))

    #sets the pointer to read using seek()
    pidata.seek(seed)

    #reads only one digit at a time
    digit = pidata.read(1)
    #guess variable
    guess = input("enter a single digit guess or 'q' to quit: -")
    correct = 0
    incorrect = 0

    # while loop that tests that "guess" is a "digit" string
    while guess.isdigit() or guess.isalpha() == False:
        #if digit ( read from pi file) is "." read the next character for digit
        if digit == ".":
            pidata.seek(seed + 1)
            digit = pidata.read(1)
        elif digit == "\n":
            pidata.seek(seed+1)
            digit = pidata.read(1)
        else:
            #if guess equals digit: print "correct" and increment the variable named correct
            if guess == digit:
                print("correct")
                correct += 1
                break
            #if guess not equal digit: print "incorrect" and increment the variable named wrong
            elif guess != digit:
                print("incorrect")
                print(seed)
                print(digit)
                guess = input("enter a single digit guess or 'q' to quit: -")
                incorrect += 1
    #output results
    print("correct guess -", correct)
    print("incorrect guess: -", incorrect)
    pidata.close()
