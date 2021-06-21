"""
Program: average_read.py
Programmer: Laxmi Gurung
Purpose: To read the contents of the file and calculate the average
Date: 06/02/2021
"""
# Importing datetime to get the current data time using now()
import datetime
import getpass

#Displays the current date and time
current = datetime.datetime.now()
print("Lab 13.2:", current.strftime("%X on %A, %B %d, %Y \n"))

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

        # Creating a for loop to write data in the file for 5 times
        for num in range(1, 6):
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
        print("File numbers.txt read")

#calling the main function
main()
print(getpass.getuser(), ", this is my lab 13.3")