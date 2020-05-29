existingUsername = ['albert ', 'skeels ']
existingPassword = ['einstein\n', 'wheels\n']

# need to assign pairs, whenever i call for skeels, password MUST == wheels

x = 0

while x != 1 :
    print('Enter username.')
    username = input()

    if username + ' ' in existingUsername:
        x = 1
    else:
        print('Invalid username.')

y = 0

while y != 1:
    print('Enter Password: ')
    password = input()

    if password + '\n' in existingPassword:
        print('Login was successful')
        y = 1
        
    else:
        print('Incorrect password')




