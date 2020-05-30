import ast

def loginPage():
    print(unpw)

    userKey = input('Enter existing username: ')
    userValue = unpw.get(userKey)

    while userValue is None:
        print('Username not found')
        userKey = input('Enter existing username again: ')
        userValue = unpw.get(userKey)

    password = input('Enter password: ')

    if password == userValue:
        print('Login successful')
        
    
def registration():
    newUser = input('Enter new username: ')
    existingUsers = list(unpw.keys())
    print(existingUsers)
    print(newUser)

    while newUser in existingUsers:
        print('Username already exists.')
        newUser = input()

    
        
    
    newPassword = input('Enter password: ')
    
    unpw.setdefault(str(newUser),str(newPassword))

    f = open('simpleunpw.txt','a+')
    f.write(str(unpw))
    #f.write(unpw) must be written as string
    f.close()


fileContents = open('simpleunpw.txt','r')
contents = fileContents.readlines()

print(contents)
print(type(contents))
#unpw = {'skeels':'wheels'}



#unpw = ast.literal_eval(str(contents)) <--- tried to convert the file (which is a list) into a dictionary

#fileContents.close()
#print(unpw)

#print(unpw.get('skeels'))


#registration()

#loginPage()

# DONE: if username/key not found --> return None value (use if statement)
# table resets everytime program is run, need to transfer to external file
