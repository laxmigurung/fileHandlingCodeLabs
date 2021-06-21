#this program reads rthe contents of the philosophers.txt file one at a time

def main():
    #open a file named philosphers.txt
    infile = open('philosophers.txt','r')

    #read three lines from the file
    #line1 = infile.readline()
    #line2 = infile.readline()
    line3 = infile.readline()

    #Close the file
    infile.close()

    #print the data that was read into memory
    #print(line1)
    #print(line2)
    print(line3)

#call the main function
main()

