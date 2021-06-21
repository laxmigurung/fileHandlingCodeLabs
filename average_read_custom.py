"""
Program: average_read_custom.py
Programmer: Laxmi Gurung
Purpose: To read the contents of the file and calculate the average
Date: 06/02/2021
"""
# Importing datetime to get the current data time using now()
import datetime
import getpass

#Displays the current date and time
current = datetime.datetime.now()
print("Lab 13.3:", current.strftime("%X on %A, %B %d, %Y \n"))

#Defining the main function
def main():
    # opening the numbers.txt file in write mode
    number_file = open('numbers.txt', 'w')
    # Try, Except and Finally handles exception in a program
    # If there is an IOError, program will execute the EXCEPT block instead of throwing an error
    # "Finally" will be executed no matter try block raises an error or not
    try:
        # Assigning 0 to variable count and total for later to calculate the average
        count = 0
        total = 0
        numberLimit =int(input('Starting from 1, upto which number do you want to calculate the average? '))
        # Creating a for loop to write data in the file for 5 times
        for num in range(1, numberLimit +1):
            # writing the value of num in the file and using str to convert the int data type to string
            number_file.write(str(num) + '\n')
            count += 1  # calculates the number of iteration in the loop
            total += num  # calculates the total value of the num
        average = total / count
        print(f"Average of the integers in the numbers.txt file is: {format(average, '.1f')}")
        number_file.close()

    except IOError:
        print("An error occured while trying to read the file.")
    finally:
        print("File numbers.txt read \n")

    # opening the numbers.txt file in append mode
    #writing "c" in the existing numbers.txt file
    #closing the file
    number_file = open('numbers.txt', 'a')
    number_file.write('C' + '\n')
    number_file.close()

    #Try, Except and Finally handles exception in a program
    #As we added the "C" in the file, it will try to get the average of all line by line
    #When it reaches to "C", line 32 will throw a Value Error
    #instead of showing an error, the program will go to except and print the statement
    #"Finally" will be executed no matter try block raises an error or not

    try:
        count = 0
        total = 0
        number_file = open('numbers.txt','r')
        for line in number_file:
            num = float(line)
            count += 1  # calculates the number of iteration in the loop
            total += num  # calculates the total value of the num
        average = total / count
        print(f"Average of the integers in the numbers.txt file is: {format(average, '.1f')}")
        number_file.close()

    except ValueError:
        print('Non-numeric data found in the file.')
    finally:
        print('File numbers.txt read \n')
#calling the main function
main()
print(getpass.getuser(), ", this is my lab 13.3")