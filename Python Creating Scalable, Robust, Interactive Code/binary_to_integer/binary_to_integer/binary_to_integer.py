
import sys
#the program will convert binary values to decimals

#getStr will ask user for binary values until user wants to exit
def getStr(question):
    check = False
    print(question)
    
    
    while not check:
        user_input = input("Enter a Binary Value:\n")
        if user_input == str or user_input.lower() == 'exit':
            check = True
            sys.exit(0)
        else:
            #checks binary is int or not
            try:
                user_input = int(user_input)
                strBinary(user_input)
            except ValueError:
                print("Not a Number.")
                
#funtion converts binary to decimals
def strBinary(binarydig): 

    decimals = 0    
    count = 0

    while binarydig != 0: 
        dec = binarydig % 10
        decimals = decimals + dec * pow(2, count) 
        binarydig = binarydig//10
        count += 1
    print("As Integer:",decimals)
 


getStr("Welcome to Binary Converter\nEnter exit to quit at any time.")
               
                
                
        
   
