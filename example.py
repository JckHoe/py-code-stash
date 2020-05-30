
# contents[0] = sarizal;password\n
# contents[1] = sarizal1;password1\n

# Enter username
isValidUsername = false
isAuth = false

def readFile(fileName)
    fileContents = open(fileName,'r')
    contents = fileContents.readlines()
    return contents


def validateUsername(username):
    #Read input here

    isValidUsername = false
    contents = readFile("Filename")
    
    for line in contents
        temp = line.strip() #sarizal;password
        arrayTmp = temp.split(";") # Split into 2 string 
        if arrayTmp[0] == username
            print("Username is valid");
            return True

    return False

def validatePassword(username, password):
    #Read input here
    fileContents = open('simpleunpw.txt','r')
    contents = fileContents.readlines()

    isValidUsername = false
    for line in contents
        temp = line.strip() #sarizal;password
        arrayTmp = temp.split(";") # Split into 2 string 
        # Structure 
        # arrayTmp[0] == username
        # arrayTmp[1] == password
        if arrayTmp[0] == username
            if arrayTmp[1] == password
                isAuth = true



def login():

    # Enter some username and password then we validate here
    if validateUsername(username) == true && validatePassword(username, password) == true
        initMainThing();
    else 
        print("Fail Login")
    


def other():
    if isValidUsername == true
        #check password lo
        isAuth = true

def initMainThing():
    if isAuth == true
        

