import sys
#this program will convert integer to binary along with as many as bits user wants to convert

#input funtion to get integer from the user 
def getInt(question):
    check = False
    print(question)
    
    #loop to continuesly convert integer to binary as long as the user wants. 
    while not check:
        user_input = input("Enter a Positive Int:\n")

        if user_input == str or user_input.lower() == 'exit':
            check = True
            sys.exit(0)
        else:
            #test input is int or not
            try:
                user_input = int(user_input)
                while not check:
                    
                    user_bits = input("Number of Bits:\n")
                    if user_bits == str or user_bits.lower() == 'exit':
                        check = True
                        sys.exit(0)
                    else:
                        #test bits user have input
                        try:
                            user_bits = int(user_bits)
                            print("As Binary: ", end ='')
                            binaryStr(user_input, user_bits)
                            print("\n", end ='')
                            break
                        except ValueError:
                            print("Not a Number.")
                
                
            except ValueError:
                print("Not a Number.")
                
        

#binaryStr funtion takes the int and bits to convert decimals to binary 
def binaryStr(num, bits):
   
    total = ''

    if bits > 0 and num == 0:
        total += '0'
        binaryStr(0, bits -1)

    elif bits > 0 and num > 0:
        rem = num % 2
        
        total += str(rem)
        
        binr = binaryStr(num //2, bits - 1)
    
    print(total, end = '')
    
getInt("Welcome to Binary Printer\nEnter exit to quit at any time.")


    
    
