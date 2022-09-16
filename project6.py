#SarahHadi
#CMSC210
#Project 6

#import relevant modules
import random
import string


#1st Function: Normalize emails 
def normalizeEmail(emailIn):
    # strip whitespace and put in lowercase
    sema = emailIn.strip()
    lema = sema.lower()

    #split email into user and domain
    at = lema.find('@')
    dom = lema[at:]
    user = lema[:at]

    #remove '.' and '+' from user
    if '.' in user:
        user = user.replace('.', "")
    if '+' in user:
        plus = user.find('+')
        extra = user[plus:]
        user= user.replace(extra, '')

    #combine user and domain to deliver normalized email
    email = user + dom
    return email


#2nd Function: Create dictionary of emails with counts to prevent double entries
def createDictionary(fileName):
    emailDict = dict()
    
    # attempt to open file and execute function
    try:
        file = open(fileName, "r")

        #read files and split lines
        content=file.read()
        emails = content.split()
        
        #for-loop to normalize emails and increment key-values
        for email in emails:
            email = normalizeEmail(email)
            if email not in emailDict.keys():
                emailDict[email] = 1
            else:
                emailDict[email] += 1
        return emailDict
    
   # print error if file doesn't exist 
    except:
        return 'File cannot be opened'
        
        


#3rd Function: Create list of eligible emails that have only entered once
def getEligibleEmails(emailDictionary):
    emailList = []
    
    #for loop iterates through dictionary and creates a list of non-repeating emails
    for email in emailDictionary:
        if emailDictionary[email] == 1:
            emailList.append(email)
            
    #deliver list with a value
    return emailList


#4th Function: Select winner from list of eligible emails at random
def selectWinner(emailList):
    winner = random.choice(emailList)

    #deliver result
    return winner




if __name__ == "__main__":
    # Displays 'debraduke@gmail.com'
    print(normalizeEmail('debraduke+cmsc210@gmail.com'))
    # Displays 'debraduke@gmail.com'
    print(normalizeEmail('dEbRa.DuKe@gmail.com'))

    # Displays the number of unique emails --> 40 with sample file
    allEntries = createDictionary("allEmails.txt")
    print(len(allEntries))
    # Displays an error message if eml.txt doesn't exist
    fileError = createDictionary("eml.txt") # no file
    print(fileError)

    # Displays the number of email address with a value of 1 -->34 with sample file
    singleEmails = getEligibleEmails(allEntries)
    print(len(singleEmails))

    # Displays one email address randomly selected
    print(selectWinner(singleEmails))

