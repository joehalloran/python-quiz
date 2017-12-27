# Quiz module is responible for displaying questions & answers, and handling all user 
# input in the quiz.
# SIMPLE BRANCH

import filehandler

def runQuiz(user):
	difficulty = selectDifficulty()
	questions = loadQuestions(difficulty)
	answers = loadAnswers(difficulty)
	correctAnswers = loadCorrectAnswers(difficulty)
	score = askQuestions(questions, answers, correctAnswers)
	return score

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

def loadQuestions(difficulty):
	return filehandler.getQuestionsFromFile(difficulty)

def loadAnswers(difficulty):
	return filehandler.getAnswersFromFile(difficulty)

def loadCorrectAnswers(difficulty):
	return filehandler.getCorrectAnswersFromFile(difficulty)

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

