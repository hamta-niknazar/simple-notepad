#Function to get input from the user and write them in the file, each time it starts a new line
def write(filename):
    f = open(filename, "a")
    myContent = input ("Type something :") 
    f.write(myContent + '\n')
    f.close()
