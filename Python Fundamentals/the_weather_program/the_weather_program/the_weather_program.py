

#the program prints cities and highest temperature of it

if __name__ == '__main__':
    #used !curl to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv as mean_temp.txt

    #opened in append plus mode 
    temp = open("mean_temp.txt","a+")
    #a new line for Rio de Janeiro "Rio de Janeiro,Brazil,30.0,18.0\n"
    temp.write("Rio de Janeiro,Brazil,30.0,18.0\n")

    #move pointer to the starting
    temp.seek(0)
    heading = temp.readline().split(",")


    # [ ] The Weather: use while loop to print city and highest monthly average temp in celsius
    city_temp = temp.readline()
    while (city_temp) :
            #made this extra list so it won't go out of range
            liscity = city_temp.split(",")
            print(heading[0], " of ", liscity[0], heading[2], "is", liscity[2], "Celsius")
            #to make the loop going
            city_temp = temp.readline()
      
    temp.close()

'''Output: The output should resemble the following

City of Beijing month ave: highest high is 30.9 Celsius
City of Cairo month ave: highest high is 34.7 Celsius
City of London month ave: highest high is 23.5 Celsius
City of Nairobi month ave: highest high is 26.3 Celsius
City of New York City month ave: highest high is 28.9 Celsius
City of Sydney month ave: highest high is 26.5 Celsius
City of Tokyo month ave: highest high is 30.8 Celsius
City of Rio De Janeiro month ave: highest high is 30.0 Celsius'''
