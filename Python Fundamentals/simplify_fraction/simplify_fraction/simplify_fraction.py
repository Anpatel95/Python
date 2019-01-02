import os, math
#the program will have numerator and denominator values of a fraction and compute its simplified form.
print('Welcome to Fraction Simplifier\nType "exit" to quit.')

check = False
#loop to run continuously until user wants to exit
while check == False:
   
    fraction = input("Enter Fraction (Int/Int):\n")

    if fraction == "exit" or fraction == "Exit":
        check = True
        print("Bye.")
    else:
        numi = ''
        denom = ''
        lst_fraction = []

        #input the user given values to the list
        for x in range(len(fraction)):
            lst_fraction += fraction[x]

        ind = lst_fraction.index("/")

        #seperate numi from the input(int/int)
        for x in range(0, ind):
            numi += lst_fraction[x]


        #seperate denom from the input(int/int)
        for x in range(ind+1, len(lst_fraction)):
            denom += lst_fraction[x]

        numi = int(numi)
        denom = int(denom)
        ans = numi / denom


        #checks gcd from fraction       
        get_gcd = math.gcd(numi, denom)

        #if the denominator is not 0 or 1 then it will print out simplified form of fraction
        if (denom//get_gcd) != 1 or 0:


            print("Simplified Fraction")
            print((numi//get_gcd),end='/')
            print((denom//get_gcd))
        else:
            print("Simplified Fraction")
            print(int(ans))
        
          



        
        
