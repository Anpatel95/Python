 #Given a text file with the story, the program will ask the user to fill in the blanks. The program will then show the user the final story
 #description
 
"""
Mad Libs are a type of word template game.
#A story is written with multiple blank spaces. The game has two players. 
One player asks the other for words to fill in the blanks. 
The player suggesting words does not know what the story is or what the words are for. 
Once all the blanks have been filled in, the story is read. 
Since the person suggesting the words does not know the context, this will lead to a funny but nonsensical story.
"""


print("Welcome to a fun word replacement game.")


try:
    #use example1.txt, example2.txt, mad_lib.txt to test
    file = input("Enter the name of the file to use:\n")
    fileopn = open(file, 'r')
    #reads the file and put it into the list
    data = fileopn.readline().split()
    count = 0
    middle = ""
    start = True

    for word in data:
        #reads the list and find blanks to fill out
        if '[' in word:
            
            if word[0] == '[':
                if word[1] == 'a':
                    print("Please give an ", end ='')
                else:
                    print("Please give a ", end ='')
                    
            
            
            for chara in word:
                
                if chara == '[':
                    pass
                elif chara == ']':
                    pass
                elif chara == '-':
                    middle += ' '
                else:
                    middle += chara
            #finds the text in the []      
            for st in middle:
                if st == '.':
                    pass
                elif st == ',':
                    pass
                else:
                    print(st, end = '')
                
            print()
            #input for the blank
            verb = input()
            
            #if else to delete the blank and insert user input
            if '.' in middle:
                verb += '.'
                data[count] = verb
            elif ',' in middle:
                verb += ','
                data[count] = verb
            else:
                data[count] = verb

        #reset variables to use for another blanks
        middle = ""         
        innercount = 0
        count += 1
    #used .join to convert list to strings     
    story = ' '.join(data)    
    print("Here is your story:")
    print("--------------------")
    print(story)
except IOError:
    print("Error Bad File Name")


        
                

    
