#Program: poem mixer
#program flow gathers the word list, modifies the case and order, and prints

#word_mixer Function has 1 argument: an original list of string words,- 
#containing greater than 5 words and the function returns a new list.
def word_mixer(word_lista):
    word_lista.sort()
    new_words = []
    while len(word_lista) > 5:
        #pop the word 5th from the end of the list and append to the new list
        new_words.append(word_lista.pop(-5))
        #pop the first word in the list and append to the new list
        new_words.append(word_lista.pop(0))
        #pop the last word in the list and append to the new list
        new_words.append(word_lista.pop(-1))
        
    return new_words

#program flow gathers the word list, modifies the case and order, and prints

if __name__ == '__main__':

    user = input("Enter any string: -")
    word_list = user.split()
    #print(word_list)
    size = len(word_list)

    for item in range(0, size):
        if len(word_list[item]) < 6:
            word_list.insert(item ,word_list[item].lower())
            word_list.pop(item + 1)
        else:
            word_list.insert(item ,word_list[item].upper())
            word_list.pop(item + 1)
        
    #new list returned from the funtion
    new_list = word_mixer(word_list)
    #join list to string
    newpoem = " ".join(new_list)

    print(newpoem)   
