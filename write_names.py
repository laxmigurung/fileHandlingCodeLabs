#this program gets three names from the user
#and writes them to a file

def main():
    #get three names
    print('Enter the names of three friends.')
    name1 = input('Friend #1: ')
    name2 = input('Friend #2: ')
    name3 = input('Friend #3: ')

    #open a file named friends.txt
    myfile = open('friends.txt', 'w')

    #write the names to the file
    myfile.write(name1 + '\n')
    myfile.write(name2 + '\n')
    myfile.write(name3 + '\n')


    print('The names were written to friends.txt.')

    # close the file
    myfile.close()



#calling the main function
main()