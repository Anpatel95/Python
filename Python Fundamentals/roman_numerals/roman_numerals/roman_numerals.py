def roman(num, one, five, ten): 
    return "XL"



def roman_num(number):
    #list of comman roman numbers
   ints = (10000,5000,1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
   nums = ('x','v','M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')


   result = ""
   #loop to go through the list to find roman numbers  
   for i in range(len(ints)):
      count = int(number / ints[i])
      result += nums[i] * count
      number -= ints[i] * count
    
   return result



if __name__=="__main__":
    print("Roman Number Generator. Enter 0 to quit.")
    while(True):
        #get int from the user between 1 to 9999
        num = int(input("Enter a number between 1 and 9,999:\n"))
        if(num == 0):
            print("Roman Numerals: ")
            print("Bye.")
            break
        else:
            print("Roman Numerals:",roman_num(num))
