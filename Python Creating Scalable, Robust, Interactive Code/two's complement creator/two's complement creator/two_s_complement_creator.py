

#popular method to store negative numbers in Binary is Two's Complement
#for instance 
'''
Welcome to Two's Complement Creator
Enter a Binary Value:
11111111
In Two's Complement:
00000001
'''

# The function twoscomp will return a string with the Two's Complement version of the binary number
def twoscomp(num):
    comp = "" 
    for i in range(len(num)):
        if num[i] == '0':
            comp = comp + '1'
        else:
            comp = comp + '0'


    num = comp 
    carry = 1
    comp = ""
    
    for i in range(len(num)-1,-1,-1):
        if carry == 1:
            if num[i] == '1': 
                comp = '0' + comp 
                carry = 1 
            else: 
                comp = '1' + comp 
                carry = 0 
        else: 
            comp = num[i] + comp
    return comp


if __name__ == "__main__":

    print("Welcome to Two's Complement Creator")
    num = input("Enter a Binary Value:\n")
    print("In Two's Complement:")
    print(twoscomp(num)) 


