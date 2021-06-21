"""
Programmer: Laxmi Gurung
Project: Creating a file classList.txt file and prompts the user to enter three names.
Date: 06/01/2021
"""
import datetime
import getpass

current = datetime.datetime.now()
print("Lab 13.1:", current.strftime("%X on %A, %B %d, %Y \n"))

def main():
    #Prompts the user to enter three name
    print("Enter three names for Class 30")
    firstName = input("Enter 1st Name: ")
    secondName = input("Enter 2nd Name: ")
    thirdName = input("Enter 3rd Name: ")

    # File input and output has three steps: Open the file | Process the file | Close the file
    # make sure all these three steps are fulfilled when opening a file
    #opening the file name to write the user inputted name in the file
    nameFile = open('classList.txt', 'w')

    #writing the three names in the classList file
    nameFile.write(firstName  + '\n')
    nameFile.write(secondName  + '\n')
    nameFile.write(thirdName  + '\n')

    # closing the file
    nameFile.close()

    # opening the file to read the names
    nameFile = open('classList.txt', 'r')

    # reading the file line by line
    line1 = nameFile.readline()
    line2 = nameFile.readline()
    line3 = nameFile.readline()

    # strip the \n from eah string.
    line1 = line1.rstrip('\n')
    line2 = line2.rstrip('\n')
    line3 = line3.rstrip('\n')

    # closing the file
    nameFile.close()
   #print the lines
    print(line1)
    print(line2)
    print(line3)

    print("Add Ling Dong and Peter Mei to the class list.")
    # append mode let's the user add data into an existing file, while write mode deletes all
    # previous data. So using append to write on existing data is very useful.
    nameFile = open('classList.txt', 'a')
    nameFile.write('Ling Dong' + '\n')
    nameFile.write('Peter Mei' + '\n')
    nameFile.close()

    again = input("Enter 'Y' to continue: ")
    while again == 'y' or again == 'Y':
        #print("These are the new names in the classList file.")
        # opening the file to read the names
        nameFile = open('classList.txt', 'r')
        # reading the file line by line
        line1 = nameFile.readline()
        line2 = nameFile.readline()
        line3 = nameFile.readline()
        line4 = nameFile.readline()
        line5 = nameFile.readline()

        #strip the \n from eah string.
        line1 = line1.rstrip('\n')
        line2 = line2.rstrip('\n')
        line3 = line3.rstrip('\n')
        line4 = line4.rstrip('\n')
        line5 = line5.rstrip('\n')

        #closing the file
        nameFile.close()
        #printing all the names
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        print(line5)
        break

#calling the main function
main()

