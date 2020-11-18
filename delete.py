#Function to delete the content of the file
def delete(filename):
    f = open(filename, "r+")
    f.truncate(0)

# another way to delete the content, is implemented below
# open("file.txt", "w").close()