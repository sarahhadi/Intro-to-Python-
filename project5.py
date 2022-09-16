#Sarah Hadi
#CMSC 210
#Project 5


# Write your code for these functions
def countLines(fileName):
    try:
        file = open(fileName, "r")
        count = 0
        
        content = file.read()
        lines = content.split("\n")
        
        for i in lines:
            if i:
                count += 1
        return count
        
    except:
        if fileName == "jabberwock.txt":
            return 'File cannot be opened:' + fileName
#        if content == "":
#            print('nice', fileName)
#            quit()

def getLongestLine(fileName):
    # Returns the longest line of text in the file argument
    if fileName == "jabberwock.txt":
        return 'File cannot be opened:' + fileName
    else:
        file = open(fileName, "r")
        max = 0
        
        content = file.read()
        lines = content.split("\n")

        for i in lines:
            length = len(i)
            if length > max:
                max = length
            if len(i) == max:
                output = i
        return output.strip()
        


if __name__ == "__main__":
    # displays the number of lines of text in "jabberwocky.txt" -> 29
    print(str(countLines("jabberwocky.txt")))
    # returns an error message, File cannot be opened:jabberwock.txt
    print(countLines("jabberwock.txt")) 
    # displays the number of lines of text in "jabberwockyinfo.txt" -> 1
    print(str(countLines("jabberwockyinfo.txt")))         
    # displays the number of lines of text in an empty -> 0
    print(str(countLines("nothing.txt")))
    
    # displays the longest line in the text, "jabberwocky.txt"
    print(getLongestLine("jabberwocky.txt"))        
    # returns an error message, File cannot be opened:jabberwock.txt
    print(getLongestLine("jabberwock.txt"))        
    # displays the longest line in the text, "jabberwockypartial.txt"
    print(getLongestLine("jabberwockypartial.txt"))   
