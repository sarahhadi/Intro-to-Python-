#CMSC 210
#Sarah Hadi
#Final Project

#necessary modules imported for encode_message function
import random

def calculate_tip(charge, tip_percent):
    #Returns Invalid messages based on parameter specifications
    if tip_percent <= 0:
        total = "Invalid tip percent"
    elif charge  <= 0:
        total = "Invalid charge amount"

    #Calculates the tip amount
    else:
        tip = float(tip_percent/100)
        total = float(tip*charge)

    #returns result
    return total


def classify_student(credits):
    #Returns Invalid message
    if credits <= 0:
        student = "Insufficient credits for classification"

    #Classifies students through if-elif condition chain
    if credits >= 85:
        student = "Senior"
    elif credits >= 54:
        student = "Junior"
    elif credits >= 24:
        student = "Sophomore"
    elif credits >= 1:
        student= "Freshman"

    #returns result
    return student
        

def encode_message(inString):
    #initializes output string
    outString = ''

    #define vowels and randomized letter variable
    vow = ['a', 'e', 'i', 'o', 'u']
    let = random.choice(['r', 's', 't'])

    #for-loop iterates through characters and adds them to the empty string
    for char in inString:
        
        #if-then condition checks characters for vowels to encode 
        if char in vow:
            #outstring will add the vowel, a random r-t, and the same vowel
            outString += char + let + char
        else:
            outString += char
            
    #returns result
    return outString

def decode_message(message):
    #initializes empty output string
    outString = ''

    #defines vowels 
    vow = ['a', 'e', 'i', 'o', 'u']
    
    #initialize counter as an index position tracker for the message
    count = 0
    
    #while-loop iterates through each index position in the message ....
    #(cont.) as long as the index position is less than the length of the message
    while count < len(message):

        #character is defined as the message[index position]
        char = message[count]
        outString += char
        
        #if-then condition checks if char is a vowel and will skip ... 
        # (cont.) over the next two index positions that has the "extra letters"
        if char in vow:
            count += 2
        
        #index position is incremented to move to the next character    
        count += 1

    return outString


if __name__ == "__main__":
    print('Tests for calculate_tip function: ')
    # Displays the 20% tip on a bill of 27.5 --> 5.5
    print(calculate_tip(27.5, 20))

    # Displays Invalid charge amount for a bill of negative dollars
    print(calculate_tip(-1.0, 20))

    # Displays Invalid tip percent for a -1% tip
    print(calculate_tip(27.5, -1))
    print()

    print('Tests for classify_student function: ')
    # Displays Freshman
    print(classify_student(20))

    # Displays Senior
    print(classify_student(120))

    # Displays Insufficient credits for classification
    print(classify_student(0))
    print()

    print('Tests for encode_message function: ')
    # Displays something like Heselloro Wosorld
    print(encode_message("Hello World"))

    # Displays something like Ditinneser totoniright asat Tararasa Thasaiti.
    print(encode_message("Dinner tonight at Tara Thai."))

    # Displays something like Mereeret atat setevesen oroclotock.
    print(encode_message("Meet at seven oclock."))
    print()

    print('Tests for decode_message function: ')
    # Displays Hello World
    print(decode_message("Heselloro Wosorld"))

    # DisplaysDinner tonight at Tara Thai.
    print(decode_message("Ditinneser totoniright asat Tararasa Thasaiti."))

    # Displays Meet at seven oclock.
    print(decode_message("Mereeret atat setevesen oroclotock."))
    print()
