# [ ] Complete the following program to display the probability of a certain die roll
#predict the probability (or chance) of getting a certain die roll
from random import randint

def die_roller():
    return(randint(1, 6))

#TODO
count1  = 0
count2  = 0
count3  = 0
count4  = 0
count5  = 0
count6  = 0

for item in range(0, 1001):
    die = die_roller()
    
    if die == 1:
        count1 += 1
    elif die == 2:
        count2 += 1
    elif die == 3:
        count3 += 1
    elif die == 4:
        count4 += 1
    elif die == 5:
        count5 += 1
    elif die == 6:
        count6 += 1
        
print("%.2f" %((count1 / 1000) *100)+"%")
print("%.2f" %((count2 / 1000) *100)+"%")
print("%.2f" %((count3 / 1000) *100)+"%")
print("%.2f" %((count4 / 1000) *100)+"%")
print("%.2f" %((count5 / 1000) *100)+"%")
print("%.2f" %((count6 / 1000) *100)+"%")

print("In theory, each dice should roll 16.6 out of 1000.00 times")
