#the program will give back
#      - The number of quarters due
#      - The number of dimes due
#      - The number of nickels due
#      - The number of cents due

#the funtion returns number of quarters to be returned 
def quarters_count(input_cents):
    #TODO
    qut  = input_cents // 25
    remainingcents = input_cents % 25
    print("Quarters :", qut)
    return remainingcents
    
    


#the funtion returns number of dimes to be returned
def dimes_count(input_cents):
    #TODO
    dm  = input_cents // 10
    remainingcents = input_cents % 10
    print("Dimes :", dm)
    return remainingcents
    

#the funtion returns number of nickels to be returned
def nickels_count(input_cents):
    #TODO
    nkl = input_cents // 5
    remainingcents = input_cents % 5
    print("Nickels :", nkl)
    return remainingcents


# The coins_due function should print:
#      - The number of quarters due
#      - The number of dimes due
#      - The number of nickels due
#      - The number of cents due


def coins_due(amount_paid, item_price):
    print("Change due:")
    #TODO
    change = amount_paid - item_price 
    print(change)
    remaningafquter  = quarters_count(change)
   
    if remaningafquter != 0:
        remaningafdimes = dimes_count(remaningafquter)#sending remaining change after quarters
        
    if remaningafdimes != 0:
        remaningafnick = nickels_count(remaningafdimes)
        
    if remaningafnick != 0:
        print("Cents :", remaningafnick)
    
amount_paid = 10 * 100 # in cents $10 gave
item_price = 5.37 * 100 # in cents $5.37 price
coins_due(amount_paid, item_price)
