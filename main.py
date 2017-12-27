import os

# Main function to run all parts of the quiz.
def main():
	registerUserIfRequired()
	user = login(3)
	score = runQuiz(user)
	saveScore(user, score)
	reportScore(user, score)

# Asks user to register or login
def registerUserIfRequired():
	print()
	print("Do you need to register?")
	print("Press 1 to login")
	print("Press 2 to register")
	userSelection = input("> ")
	print(userSelection)
	if (userSelection == "1"):
		# Do nothing and return to main()
		return
	elif (userSelection == "2"):
		registerUser()
	else:
		print("Invalid selection. Try again.")
		return isRegistrationRequired()	

# Register user, asking for required details
def registerUser():
	print()
	print("REGISTER:")
	name = input("What is your name > ")
	if nameAlreadyRegistered(name):
		print("This name has already been registered. Try again.")
		registerUser()
		return
	age = input("How old are you > ")
	yearGroup = input("What year group are you in?")
	password = choosePassword()
	saveRegistrationDetails(name, age, yearGroup, password)

# Checks if a user with this name is already registered
def nameAlreadyRegistered(name):
	userNameFound = False
	makeRegisteredUsersFileIfRequired()
	file = open('data/users/registered_users.txt', 'r')
	for line in file:
		userdata = line.split(',')
		if userdata[0] == name:
			userNameFound = True
			break
	file.close()
	return userNameFound

# Creates the file to save user details if it does not exist.
def makeRegisteredUsersFileIfRequired():
	folderPath = 'data/users/'
	makeFolderIfRequired(folderPath)
	file = open(folderPath + 'registered_users.txt', 'a+')
	file.close()

# Makes a folder if it does not exist.
def makeFolderIfRequired(path):
	if not os.path.exists(path):
	    os.makedirs(path)

# Ask user to choose a password and performs validation
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

# Saves registration details to file
def saveRegistrationDetails(name, age, yearGroup, password):
	file = open('data/users/registered_users.txt', 'a+')
	file.write(name + ',' + age + ',' + yearGroup  + ',' + password + '\n')
	file.close()

# User can login with given number of attempts.
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

# Checks the login details supplied by the uers are valid			
def loginValid(userName, password):
	loginValid = False
	file = open('data/users/registered_users.txt', 'r')
	allLines = file.read().splitlines()
	for line in allLines:
		userdata = line.split(',')
		if userdata[0] == userName and userdata[3] == password:
			loginValid = True
			break
	file.close()
	return loginValid

# Controls the all the parts of the quiz. Returns final score the main()
def runQuiz(user):
	difficulty = selectDifficulty()
	questions = getQuestions(difficulty)
	answers = getAnswers(difficulty)
	correctAnswers = getCorrectAnswers(difficulty)
	score = askQuestions(questions, answers, correctAnswers)
	return score

# User can choose appropriate difficulty
def selectDifficulty():
	print()
	print("SELECT DIFFICULTY")
	print("Press 1 for Easy")
	print("Press 2 for Medium")
	print("Press 3 for Hard")
	difficulty = input('> ')
	if difficulty == '1':
		return "easy"
	elif difficulty == '2':
		return "medium"
	elif difficulty == '3':
		return "hard"
	else:
		print("Invalid selection. Try again.")
		return selectDifficulty()

# Get questions from file with appropriate difficulty
def getQuestions(difficulty):
	questions = []
	file = open("data/questions/questions_" + difficulty + ".txt", 'r')
	for line in file:
		line = line.splitlines()
		questions.append(line)
	file.close()
	return questions

# Get answers from file with appropriate difficulty
def getAnswers(difficulty):
	answers = []
	file = open("data/questions/answers_" + difficulty + ".txt", 'r')
	allLines = file.read().splitlines()
	for line in allLines:
		answers.append(line.split(','))
	file.close()
	return answers

# Get correect answers from file with appropriate difficulty
def getCorrectAnswers(difficulty):
	correctAnswers = []
	file = open("data/questions/correct_answers_" + difficulty + ".txt", 'r')
	allLines = file.read().splitlines()
	for line in allLines:
		correctAnswers.append(line)
	file.close()
	return correctAnswers

# Ask questions in order, check answers, and award points
def askQuestions(questions, answers, correctAnswers):
	score = 0
	counter = 0
	while counter < len(questions):
		print()
		print("QUESTION " + str(counter + 1) + ":")
		print(questions[counter])
		answerCounter = 0
		for answer in answers[counter]:
			print(str(answerCounter) + ": " + answer)
			answerCounter = answerCounter + 1
		userSelection = int(input("> "))
		if (answers[counter][userSelection] == correctAnswers[counter]):
			print("correct")
			score = score + 1
		else:
			print("unlucky")
		counter = counter + 1
	return score

# Save final score at end of quiz.
def saveScore(user, score):
	folderPath = 'data/scores/'
	makeFolderIfRequired(folderPath) 
	file = open(folderPath + 'saved_scores.txt', 'a+')
	file.write(user + ',' + str(score) + '\n')
	file.close

# Show the user final score at the end of quiz.
def reportScore(user, score):
	print()
	print("Well done " + user + " your final score was...")
	print(score)
	showFinalMenu(user)

# Show the user the final menu
def showFinalMenu(user):
	print()
	print("Press 1 to show your high scores")
	print("Press 2 to quit")
	userSelection = input("> ")
	if userSelection == '1':
		highScores = getHighScores(user)
		print()
		print("Your highscores:")
		for score in highScores:
			print(score)
		showFinalMenu(user)
	else: 
		print("Thanks for playing. Goodbye")
		exit()

# Load historical highscores
def getHighScores(user):
	scores = []
	file = open('data/scores/saved_scores.txt', 'r')
	allLines = file.read().splitlines()
	for line in allLines:
		data = line.split(',')
		if data[0] == user:
			scores.append(data[1])
	scores = sorted(scores)
	return scores

# Runs the main method at the top of this file. This is where the program begins
main()