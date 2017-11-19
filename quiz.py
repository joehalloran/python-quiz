def runQuiz(user):
	difficulty = selectDifficulty()
	questions = loadQuestions(difficulty)
	answers = loadAnswers(difficulty)
	correctAnswers = loadCorrectAnswers(difficulty)
	score = askQuestions(questions, answers, correctAnswers)
	return score

def selectDifficulty():
	print("Select difficulty")
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

def loadQuestions(difficulty):
	#TODO
	return ["Capital of France?", "Capital of UK?", "Capital of Russia?"]

def loadAnswers(difficulty):
	#TODO
	return [["Paris", "Berlin", "Rome"], ["London", "Cardiff", "Edinborough"], ["Moscow", "Warsaw", "Kiev"]]

def loadCorrectAnswers(difficulty):
	#TODO
	return ["Paris", "London", "Moscow"]

def askQuestions(questions, answers, correctAnswers):
	score = 0
	counter = 0
	while counter < len(questions):
		print(questions[counter])
		answerCounter = 0
		for answer in answers[counter]:
			print(str(answerCounter) + ": " + answer)
			answerCounter = answerCounter + 1
		userSelection = int(input("> "))
		if (answers[counter][userSelection] == correctAnswers[counter]):
			score = score + 1
		counter = counter + 1
	return score

