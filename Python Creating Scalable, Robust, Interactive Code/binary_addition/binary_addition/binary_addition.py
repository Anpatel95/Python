import sys

#this program will implement two binary addition


#getInt will ask user for two binary numbers, and it will stop when user whats to exit
def getInt(question):
    check = False
    print(question)
    
    while not check:
        #asks for first binary number
        user_input = input("Enter first Binary Value:\n")
        if user_input == str or user_input.lower() == 'exit':
            check = True
            sys.exit(0)
        else:
            try:
                user_input = str(user_input)
                while not check:
                    #asks for second binary number
                    user_bits = input("Enter Second Binary Value:\n")
                    if user_bits == str or user_bits.lower() == 'exit':
                        check = True
                        sys.exit(0)
                    else:
                        try:
                            user_bits = str(user_bits)
                            #sending both binary number for addition to funtion binary_nums
                            output = binary_nums(user_input, user_bits)
                            print("Sum: ", end='')
                            #reverse the binary values to print the right ans
                            print(revs(output))
                            break
                        except ValueError:
                            print("Not a Number.")
                
                
            except ValueError:
                print("Not a Number.")
#this funtion will reverse the the binary value to get the right ans                 
def revs(binary_rev):
    
    summ = ''

    for x in range(len(binary_rev)-1,-1,-1):
        summ += binary_rev[x]
        
    return summ
    


'''
There are a total of 8 possible cases for each column.
c + a + b = or

0 + 0 + 0 = 00
0 + 0 + 1 = 01
0 + 1 + 0 = 01
0 + 1 + 1 = 10
1 + 0 + 0 = 01
1 + 0 + 1 = 10
1 + 1 + 0 = 10
1 + 1 + 1 = 11 '''
def binary_nums(fir, sec):
    c = '0'
    o = ''#carry for next column
    r = ''#bit results
    total = ""

    #this will check the length of the both binary is same or not 
    if len(fir) == len(sec):
        
        for x in range(len(fir)-1,-1,-1):
            a = fir[x]
            b = sec[x]
            
            
            r = c + a + b
            o = r[0]
            if c == '0' and a =='0' and b == '0':
                r = '00'
                c = r[0]
                total += r[1]
            elif c == '0' and a =='0' and b == '1':
                r = '01'
                c = r[0]
                total += r[1]
            elif c == '0' and a =='1' and b == '0':
                r = '01'
                c = r[0]
                total += r[1]
            elif c == '0' and a =='1' and b == '1':
                r = '10'
                c = r[0]
                total += r[1]
            elif c == '1' and a =='0' and b == '0':
                r = '01'
                c = r[0]
                total += r[1]
            elif c == '1' and a =='0' and b == '1':
                r= '10'
                c = r[0]
                total += r[1]
            elif c == '1' and a =='1' and b == '0':
                r= '10'
                c = r[0]
                total += r[1]
            elif c == '1' and a =='1' and b == '1':
                r = '11'
                c = r[0]
                total += r[1]
    #if the length of the both binary is not same than additon can't be made
    elif len(fir) != len(sec):
        
        return "!ddA tonnaC"
                                 
    return total
getInt("Welcome to Binary Adder\nEnter exit to quit at any time.")


