def getQuestionsFromFile(difficulty):
	questions = []
	file = open("data/questions/questions_" + difficulty + ".txt", 'r')
	for line in file:
		line = line.splitlines()
		questions.append(line)
	file.close()
	return questions


def getAnswersFromFile(difficulty):
	answers = []
	file = open("data/questions/answers_" + difficulty + ".txt", 'r')
	allLines = file.read().splitlines()
	for line in allLines:
		answers.append(line.split(','))
	file.close()
	print(answers)
	return answers


def getCorrectAnswersFromFile(difficulty):
	correctAnswers = []
	file = open("data/questions/correct_answers_" + difficulty + ".txt", 'r')
	allLines = file.read().splitlines()
	for line in allLines:
		correctAnswers.append(line)
	file.close()
	print(correctAnswers)
	return correctAnswers


def saveRegistrationDetailsToFiles(name, age, yearGroup, password):
	file = open('data/users/registered_users.txt', 'a+')
	file.write(name + ',' + age + ',' + yearGroup  + ',' + password + '\n')
	file.close

def nameAlreadyRegistered(name):
	userNameFound = False
	file = open('data/users/registered_users.txt', 'r')
	for line in file:
		userdata = line.split(',')
		if userdata[0] == name:
			print("This name has already been registered. Try again.")
			userNameFound = True
			break
	file.close()
	return userNameFound
