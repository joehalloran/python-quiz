# TODO: Add description of user.py
import filehandler

def registerUserIfRequired():
	registrationRequired = isRegistrationRequired()
	if (registrationRequired):
		registerUser()

def isRegistrationRequired():
	print()
	print("Do you need to register?")
	print("Press 1 to login")
	print("Press 2 to register")
	userSelection = input("> ")
	print(userSelection)
	if (userSelection == "1"):
		return False
	elif (userSelection == "2"):
		return True
	else:
		print("Invalid selection. Try again.")
		return isRegistrationRequired()

def registerUser():
	print()
	print("REGISTER:")
	name = input("What is your name > ")
	if filehandler.nameAlreadyRegistered(name):
		print("This name has already been registered. Try again.")
		registerUser()
		return
	age = input("How old are you > ")
	yearGroup = input("What year group are you in?")
	password = choosePassword()
	saveRegistrationDetails(name, age, yearGroup, password)

def choosePassword():
	print("Choose a password")
	print("It must be longer than 6 letters")
	passwordOne = input("Enter password > ")
	passwordTwo = input("Re-enter password > ")
	if (len(passwordOne) < 7):
		print("Password must be longer than 6 letters")
		return choosePassword()
	elif (passwordOne != passwordTwo):
		print("Passwords must match")
		return choosePassword()
	else:
		return passwordOne

def saveRegistrationDetails(name, age, yearGroup, password):
	filehandler.saveRegistrationDetailsToFiles(name, age, yearGroup, password)

def login(attemps):
	print()
	print("LOGIN:")
	userName = input("Username > ")
	password = input("Password > ")
	if loginValid(userName, password):
		return userName
	else:
		attemps = attemps -1
		print("Username and password incorrect")
		if attemps > 0:
			print("You have " + str(attemps) + " left. Please try again.")
			login(attemps)
		else:
			print("You have no more attempts left. Exiting quiz.")
			exit()

			
def loginValid(userName, password):
	return filehandler.loginValid(userName, password)



