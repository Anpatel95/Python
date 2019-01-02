#funtion that finds key of the letter on number pad
def let_to_num(letter):
    key = 0
    while key < 10:
        if letter in phone_letters[key]: #"key" = phone dial pad key
            if letter == "":# Create Code: determine if letter is **`in`** any of the phone_letters[key] where key is the index 0 -9:
                key = 1
                return key
            return key
        else:
            key = key + 1
    return "not found"
        
#program to find number on phone key pad.  
if __name__ == '__main__':
    phone_letters = [' ', '', 'ABC', 'DEF', 'GHI', 'JKL','MNO','PQRS','TUV','WXYZ']
    print(phone_letters)
    findletter = input("find letter in key pads: - ")
    let = findletter.upper()
    print(let_to_num(let))
    
    
