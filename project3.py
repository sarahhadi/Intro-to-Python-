#Sarah Hadi
#CMSC 210
#Project 3: How Far Away? (continued)

#sys module import
import sys

#read input from command line
timesFar = int(sys.argv[1])

#condition block: input must be between 1 and 5
if timesFar < 1:
    print("The Universe is vast your view is too small.")

elif timesFar > 5:
    print("Enough already; you're going too far.")

else:
    print("\nA long time ago in a galaxy" + (timesFar * " far") + " away...")
      

