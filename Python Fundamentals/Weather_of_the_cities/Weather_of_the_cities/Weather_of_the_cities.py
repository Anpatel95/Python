

if __name__ == '__main__':
    #task 2
    #program that reads from a file to display city name and average temperature in Celsius.
    # [ ] The Weather: open file, read/print first line, convert line to list (splitting on comma)
    #use !curl to download https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv as mean_temp.txt
    # [ ] The Weather: import world_mean_team.csv as mean_temp.txt
    temp = open("mean_temp.txt","r")
    #reads heading from the txt file
    heading = temp.readline()
    lisheading = heading.split(",")
    print(lisheading)


    citydata = temp.readline()
    #while loop to read the remaining lines from the file
    while citydata:
        #Convert the city_temp to a list using .split(',') for each .readline() in the loop
        liscity = citydata.split(",")
        #Print each city & the highest monthly average temperature
        print(liscity)
        citydata = temp.readline()
   
    temp.close()
