#Program: Element_Quiz
#In this program the user enters the name of any 5 of the first 20 Atomic Elements and is given a grade and test report for items correct and incorrect.

#used !curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/elements1_20.txt -o elements1_20.txt

#function get names
#creating list of five elements to return
def get_names():
    #empty element list
    five_ele = []
    while len(five_ele) != 5 :
        elems = input("Enter the name of an element: ")
        #if the copy of the element enter then display msg    
        if elems.capitalize() in five_ele or elems == "":
            print(elems," was already entered          <--no duplicates allowed")
            
        else:
            five_ele.append(elems.capitalize())
    
    return five_ele

#main
if __name__ == '__main__':  
    #open the file with the first 20 elements
    elements = open("elements1_20.txt", "r")
    #reads elements from the file
    elemdata = elements.readlines()
    count = 0
    #remove whitespace or new line
    for item in elemdata:
        elemdata[count] = item[:-1].lower()
        count += 1
    
    print(elemdata)
    correct = 0
    incorrect = 0
    elem5 = []


    #calling funtion for getting the 5 elem
    elem5 = get_names()
    found = ""
    notfound = ""
    #find  how many elem are in 1st 20elem from 5 elem in funtion
    for item in elem5:
        #compare each response to the list of 20 elements
        if item.lower() in elemdata:
            #addes the space in the big string
            found += item + " "
            correct += 1
        
        else:
            notfound += item + " "
            incorrect +=1
        
    print("")
    #calculate the % correct
    percent  = (correct /5) * 100

    #output results
    print(int(percent), "% correct")
    print("Found: -", found)
    print("Not Found: -", notfound)

    #close the file
    elements.close()

'''Sample input and output:
list any 5 of the first 20 elements in the Period table
Enter the name of an element: argon
Enter the name of an element: chlorine
Enter the name of an element: sodium
Enter the name of an element: argon
argon was already entered          <--no duplicates allowed
Enter the name of an element: helium
Enter the name of an element: gold

80 % correct
Found: Argon Chlorine Sodium Helium 
Not Found: Gold '''