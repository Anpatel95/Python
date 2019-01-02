#Challenge: reverse a string
# [ ] Challenge: write the code for "reverse a string" reversing some_numbers
some_numbers =[1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77]
revnum = []
count = 0
print(some_numbers)

while some_numbers:
    takeitem =some_numbers.pop()
    revnum.insert(count, takeitem)
    count += 1
    
print(revnum)

