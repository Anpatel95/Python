#Task 1
#Order the Rainbow


if __name__ == '__main__':

    #get textfile from github
    #!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/rainbow -o rainbow.txt
    


    #read data from rainbow.txt
    rainbow = open("rainbow.txt","r")
    raindata = rainbow.readlines()
    count = 0

    #insert data into list
    for item in raindata:
        raindata[count] =  item[:-1]
        count += 1
    

    #sort data in rainbow file
    raindata.sort()
    #print out loop
    for item in raindata:
        print(item)
    
    rainbow.close()

