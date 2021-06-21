"""
Program: studentContract.py
Programmer: Laxmi Gurung
Purpose: To input the name and contract points of students of the prompted week.
Date: 06/03/2021
"""
# Importing datetime to get the current data time using now()
import datetime

#Displays the current date and time
current = datetime.datetime.now()
print("Lab 13.4:", current.strftime("%X on %A, %B %d, %Y \n"))

#Calling main function
def main():
    #Prompting user to input week number and storing it in a variable week
    #Prompting user to input how many students user want to write for.
    week = int(input("Enter Week Number: "))
    student = int(input("Enter the number of students: "))

    #Opening the file studentContract.txt in write mode and creating a variable student_file
    #for the instance to open the file
    student_file = open('studentContract.txt','w')

    #Using for to let the user input the informations for the number od students stored in variable 'student'
    #Prompt the user to input name and point
    for num in range(1, student +1):
        name = input("Enter the name of the student: ")
        point = int(input("Enter the contract point: "))

        #this writes the name and point to the file.
        #using str(point) because it was int when prompting user to input
        # as we need to concatenate '\n', we have to convert int to str.
        student_file.write(name + '\n')
        student_file.write(str(point) + '\n')

    #closing the file
    student_file.close()

    #Opening the file to read the data.
    student_file = open('studentContract.txt', 'r')
    print(f"\nThese are Contract Points for Week : {week}")
    print("------------------------------------------------")

    # reading the first line of the file.
    name = student_file.readline()

    #Using while condtion in order to read the all line until while condition is false.
    while name != '':
        point = student_file.readline()

        #We need to remove the new line '\n', in order to place the data in the required position.
        #Using rstrip we can remove the \n. Also try commenting out the line 55 and 56, then you will see that
        #we should remove the \n.
        name = name.rstrip('\n')
        point = point.rstrip('\n')
        print(f'Name: {name}  Contract Point: {point}')
        #After it readline the second line, it needs to read the third line which is another name
        #so we need to write the following statement again for the loop to continue.
        name = student_file.readline()

    #Closing the file
    student_file.close()

#calling the main function
main()

