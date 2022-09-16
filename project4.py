#Sarah Hadi
#CMSC 210
#Project 4 Triangle Pattern

#step 0 import systems
import math
import sys

#Step 1: read input from command line
numRows = int(sys.argv[1])


#Step 2: define function to be called later
def printing():
    #Step 2.1: assigning & initializing 
    #assign string to variable
    #initialize row for printing and counter for counting 
    #row doesn't start at 0 because parameter is 1 < numRows < 20
    star = "* "
    row = 1
    counter = 0
    #Step 2.2: while loop condition
    #while conditional statement based on input, not parameters
    while row <= numRows:
        #Step 2.2-a: creating shape, new string, and delivering result 
        indent = (numRows - row) * " "
        line = row * star
        line = indent + line
        print(line)
        #Step 2.2-b: star count is updated using invokation using count() method on line variable
        counter = counter + line.count("*")
        #Step 2.2-c: incrementing row after delivering result so code can iterate through all values within numRows
        row = int(row) + 1
    #Step 2.3: printing final count at the end after while loop is done and all the pyramid 
    print(counter)


#Step 3: selection or rejection based on parameters
if numRows < 1:
    print("Invalid input value. The number of rows cannot be less than 1.")
elif numRows > 20:
    print("Invalid input value. The number of rows cannot be more than 20.")
else:
    printing()

        
