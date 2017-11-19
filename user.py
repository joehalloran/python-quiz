def registerUserIfRequired():
	registrationRequired = isRegistrationRequired()
	if (registrationRequired):
		registerUser()

def isRegistrationRequired():
	print("Do you need to register?")
	print("Press y to register")
	print("Press n to login")
	userSelection = input("> ")
	print(userSelection)
	if (userSelection == "y"):
		return True
	elif (userSelection == "n"):
		return False
	else:
		print("Invalid selection. Try again.")
		return isRegistrationRequired()

def registerUser():
	name = input("What is your name > ")
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
	#TODO
	return

def login(attemps):
	userName = input("Username > ")
	password = input("Password > ")
	if loginValid(userName, password):
		return "user"
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
	#TODO
	return True



