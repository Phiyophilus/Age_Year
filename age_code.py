print ('Welcome to the age calculator ')

#This will prompt the user to enter their birth year
birth_year = input('Enter your birth year( in numeric format ) : ')

if (birth_year.isnumeric()):
  #loop to allow user to be prompt for th birthyear
    while birth_year != 'quit':
      

        Current_year = 2021
        birth_year.lower()

        if int(birth_year) > Current_year:
            print("birth year can not be greater than " + str(Current_year))
            birth_year = input('Enter your birth year or (Enter quit to exit program): ')
            birth_year.lower()
        else:
        
            age = Current_year - int(birth_year)
            print ("Your current age is : " + str(age) )
            #To be improved to give out interesting facts about your age 
            #print ("Interesting things about your age")
            birth_year = input('Enter your birth year or (Enter quit to exit program): ')
            birth_year.lower()

    print("Thank you for using this service")
else:
    print("Your birth year is not a number")
    print("You want to crush my program, lol read the instructions")



