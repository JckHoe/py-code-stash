# LOGIN PAGE: 
# enter in username and password: pair must match in terms of index as in 1:1, 2:2 from the list of passwords and usernames

import re


def registration():
	print('Welcome Adventurer! \n' + 'New Account Registration \n'+ 'Enter Username:')
	
	userList = open('C:\\Users\\sarizal\\myPythonScripts\\loginPage\\unpw.txt')	
	existingUsers = userList.readlines()
	#print(existingUsers)

	unpw = open('C:\\Users\\sarizal\\myPythonScripts\\loginPage\\unpw.txt', 'a')

	x = 0

	while x != 1: # DONE: need to create a loop here 
		newUser = input()	

		if newUser + ' ' in existingUsers:		
			print('The username has already been taken. Try another username!')	### CURRENT ISSUE: DOES NOT WORK
		

		elif newUser == '000':
			print('That is an invalid username. Try another username.')

		elif ' ' in newUser:
			print('The username cannot contain spaces.')

		else: 
			unpw.write(newUser + ';') 
			x = 1

	# DONE: must check if user matches with any existing users. Prompt to choose another username if username already taken.

	#user.close()
	#userList.close()
	
	print('Enter Password:')
	#userPassword = open('C:\\Users\\sarizal\\myPythonScripts\\loginPage\\unpw.txt', 'a')
	
	newPassword = input()

	while len(newPassword) < 6:
		print('Password must be at least 6 characters long.')
		print('Please re-enter password')
		newPassword = input()

	# DONE: password must be more than 6 characters
	unpw.write(newPassword + ';' + '\n')
	unpw.close()



	# TODO: password must be linked with  username: instead of using two files, use one file with user and p/w seperated by a symbol
	# 		then i can use regex to match
	# userPassword x existingUser

	#userPassword.close()

	print('Thank you!')

	while True:												# Note: while True loops are forever! Unless it returns a False value or there is a break :)
		print('Press Enter to return to login page.')
		x = input()
		if x == '':
			break


	# return to login page:
	#loginpage()		# TODO: i dont think this should be here. the initial call for loginpage() will keep on looping infinitely. [add else statement]

# DONE: once i have created an account, press something to be able to return to login page.
# DONE: need to save newUser and userPassword in external file





def loginpage():

	#userList = open('C:\\Users\\sarizal\\myPythonScripts\\loginPage\\unpw.txt')
	#existingUsers = userList.readlines()

	# need to create a unpw file if its not already there

	print('Welcome to Runescape! Please enter username and password.')
	print('to create a new account, enter 000 as the username')

	# TODO: while login is unsuccessful:
	print('Username: ')
	userName = input()
	# TODO: checkusername()
	# TODO: must check if user matches with any existing users. if not, request to re-enter username



	acceptedUser = ''

	while acceptedUser != 'accepted':
		userList = open('C:\\Users\\sarizal\\myPythonScripts\\loginPage\\unpw.txt')
		existingUsers = userList.readlines()
		print(existingUsers)

		if userName + ';' in existingUsers:				# CURRENT ISSUE: DOES NOT WORK. if 'skeels ' only then can match?
			# TODO: keep the value to match with linked password
			#acceptedUser = 'accepted'
			acceptedUser = 'accepted'
			print('Password:')
			password = input()

			print('Login was succesful! \n End of program.' )

		#DONE: make sure not possible to register with 000 / integer values --> use regex?
				
		
			# DONE: the two ELIFs can be true at the same time!

		#elif userName + '\n' not in existingUsers:
		elif userName == '000':
			registration()
			print('Enter your username.')
			userName = input()
			#break			# << breaks the entire loop? not this elif loop...
		else:
			print('Username not found. Try again with a different username.')
			userName = input()

			# TODO: must recheck usernames, makes this a def()?

		















# Actual program starts here:
loginpage()					# DONE: Resolve loop issue




# openFile(variable)
# .readlines()



	





		# try and except for username/password not in lists

# need to match password with a username in the system
	# keep in mind those with the same password!

# REGISTRATION:
# pair of input (user and pw) transferred out into a file containing a list
# both must be more than 5 characters long
	# cannot have empty
	# how to openfile and store strings (MUST MATCH)




# use variable.append()
# 2 lists, must equal spam[1][1],[2][2]
# can also variable.index('string')



'skeels wheels'