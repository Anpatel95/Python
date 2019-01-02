#program flow which can be modified to ask for a specific type of item. This is the programmers choice. Add a list of fish, trees, books, movies, songs.... your choice.

#list-o-matic: -Function which takes arguments of a string and a list. The function modifies the list and returns a message as seen below.

def lst_o_matic(userin):
    if userin == "":#if the string is empty then the last item is popped from the list
        listanimals.pop()
        return "something have removed from the end of the list"
    elif userin in listanimals:#if string is in the list it removes the first instance from list
        listanimals.remove(userin)
        return "that animals was already existed, so it's been remove"
    else:#if string is not in the list the input gets appended to the list
        listanimals.append(userin)
        return "new animal name have been added"


if __name__ == '__main__':

    
    listanimals = ["cat"]#initialize list with one animal name

    while(listanimals):
        if listanimals:
            print(listanimals) 
            userinput = input("Enter name of the animals: -")
            if userinput == "quit":
                print("end")
                break
            else:
                dis = lst_o_matic(userinput)
                print(dis)
        else:
            print("list is empty","good bye!")#if the list becomes empty the program ends
   

