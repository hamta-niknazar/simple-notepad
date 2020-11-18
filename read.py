#Function to display everything in the file in terminal
def read(filename):
  f = open(filename, "r")
  for x in f:
    print(x)
  f.close()
