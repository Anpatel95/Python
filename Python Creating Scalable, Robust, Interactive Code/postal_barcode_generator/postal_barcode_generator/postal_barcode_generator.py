#this program will take the zip code and prints out the barcode
#HW description
'''The bar code also always starts and ends with a large bar. This is used by the scanner to align the letter.

Drexel's Zip Code is 19104

The check digit is 5. The sum of the digits is 1+9+1+0+4 = 15. To make 15 a multiple of 10, we need to add 5.

The bar code will be |:::|||:|:::::||||::::|::|:|:|:|
'''
'''the checksum funtion
Adds all the digits together
Determine what needs to be added to make the total a multiple of 10'''

def checksum(zipc):
    check = 0
    count = 0

    #convert zipcode to integer
    if zipc.isdigit():
        for x in zipc:
            check += int(x)

    #check the total is multiple of 10
    if check % 10 == 0:
        
        return 0
    else:
        #loop to get the diff
        for x in range(1, 11):
            #check the total is multiple of 10
            if ((check % 10) == 0):
                
                return str(count)
            check += 1
            count += 1 
    
def barcode(zipc):

    code = ["||:::", ":::||", "::|:|", "::||:", ":|::|", ":|:|:", ":||::", "|:::|", "|::|:", "|:|::"]
    barcd = ""
    
    dif = checksum(zipc)
    #add the difference into barcode as a string
    barcod = zipc + str(dif)
    
    barcd += "|"
    #loop will go through the list to generate barcode
    for i in barcod:
        barcd +=  code[int(i)]
       
    barcd += "|"
    return barcd
   
    
    
if __name__=="__main__":
    print("Welcome to Bar Code Generator")
    while(True):
        #user input of the zipcode
        zip_code = input('Enter Zip Code (exit to quit):\n')
        
        if zip_code == "exit":
            print("Thanks for using me.")
            break
        else:
            
            print("Bar Code:")
            print(barcode(zip_code))
            
