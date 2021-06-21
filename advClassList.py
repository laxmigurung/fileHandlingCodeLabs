"""
Programmer: Laxmi Gurung
Project: Creating a file classList.txt file and prompts the user to enter three names.
Date: 06/01/2021
"""
import getpass
import datetime

current = datetime.datetime.now()
print("Lab 13.1:", current.strftime("%X on %A, %B %d, %Y \n"))

def main():
    # File input and output has three steps: Open the file | Process the file | Close the file
    # make sure all these three steps are fulfilled when opening a file
   #opening the file named classList.txt
    nameFile = open('classList.txt', 'w')

    #writing the three names in the classList file
    #Prompts the user to enter names.
    #In the line 14, 15 and 16 the user inputs the name and at the sametime
    #the data is also written in the file.
    print("Enter three names for Class 30")
    nameFile.write(input("Enter 1st Name: ") + '\n')
    nameFile.write(input("Enter 2nd Name: ") + '\n')
    nameFile.write(input("Enter 3rd Name: ") + '\n')

    # closing the file
    nameFile.close()

    # opening the file to read the names
    nameFile = open('classList.txt', 'r')

    print("These are the current names in the classList file. \n")
    #(file_name.read()) reads the file name line by line. It also saves the lines in the code than reading the names
    #using .readline() funciton.
    print(nameFile.read())

    nameFile.close()

    print("Add Ling Dong and Peter Mei to the class list.")
    #append mode let's the user add data into an existing file, while write mode deletes all
    #previous data. So using append to write on existing data is very useful.
    nameFile = open('classList.txt', 'a')
    nameFile.write('Ling Dong' + '\n')
    nameFile.write('Peter Mei' + '\n')
    nameFile.close()

    again = input("Enter 'Y' to continue: ")
    while again == 'y' or again == 'Y':
        print("These are the new names in the classList file. \n")
        # opening the file to read the names
        nameFile = open('classList.txt', 'r')
        # reading the file line by line
        print(nameFile.read())
        break


#calling the main function
main()

