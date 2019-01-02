
#This function will print out a certain number of stars * and spaces.
def fractal(length, spaces):
    if length == 1:
        print(spaces * " ", end = '')
        print('*')
        
    else:
    
        fractal(int(length / 2), spaces)
        print(spaces * " ", end='')
        print(length * "*")
        fractal(int(length / 2),spaces + int (length / 2))
    
    
def main():
    print("Fractal Generator")
    
    check = False
    
    while not check:
        
        user_int = input("Enter an integer > 0:\n")
        try:
            user_int = int(user_int)
            print("",end='')
            fractal(user_int, 0)
            check = True
        except ValueError:
            pass    
    
main()
'''output should be like 
*
**
 *
****
  *
  **
   *
********
    *
    **
     *
    ****
      *
      **
       *
       '''
