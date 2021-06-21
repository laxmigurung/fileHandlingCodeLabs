#This program displays the records in the coffee.txt file
def main():
    #Open the coffee.txt file
    coffee_file = open('coffee.txt','r')
    #Read the first record's description field
    descr = coffee_file.readline()

    while descr != '':
        #read the quantity field
        qty = float(coffee_file.readline())

        #strip the \n from the description.
        descr = descr.rstrip('\n')

        #Display the record
        print('Description: ', descr)
        print('Quantity: ', qty)

        #Read the next description
        descr = coffee_file.readline()

    #close the file
    coffee_file.close()

#call the main function
main()