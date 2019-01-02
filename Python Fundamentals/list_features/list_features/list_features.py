#Task 9
#list(string) & print("hello",end=' ')
#Cast a string to a list
#print to the same line
# [ ] cast the long_word into individual letters list 
# [ ] print each letter on a line
long_word = 'decelerating'
lis = list(long_word)
for item in range(0, len(lis)):
    print(lis[item])

# [ ] use use end= in print to output each string in questions with a "?" and on new lines
questions = ["What's the closest planet to the Sun", "How deep do Dolphins swim", "What time is it"]

for item in range(0,len(questions)):
    print(questions[item], end = "? ")
    print("")
# [ ] print each item in foot bones 
#    - capitalized, both words if two word name
#    - separated by a comma and space
#    - and keeping on a single print line
foot_bones = ["calcaneus", "talus", "cuboid", "navicular", "lateral cuneiform", 
            "intermediate cuneiform", "medial cuneiform"]
count = 0
for item in foot_bones:
    
    if " " in item:
        ind = item.index(" ")
        item[ind + 1].capitalize()
        print(item.capitalize(), end = ", ")
    else:
        print(item.capitalize(), end = ", ")
        
        