# TODO: Add description

import os

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
	return answers


def getCorrectAnswersFromFile(difficulty):
	correctAnswers = []
	file = open("data/questions/correct_answers_" + difficulty + ".txt", 'r')
	allLines = file.read().splitlines()
	for line in allLines:
		correctAnswers.append(line)
	file.close()
	return correctAnswers

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


def saveRegistrationDetailsToFiles(name, age, yearGroup, password):
	file = open('data/users/registered_users.txt', 'a+')
	file.write(name + ',' + age + ',' + yearGroup  + ',' + password + '\n')
	file.close()


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

def saveScore(user, score):
	folderPath = 'data/scores/'
	makeFolderIfRequired(folderPath) 
	file = open(folderPath + 'saved_scores.txt', 'a+')
	file.write(user + ',' + str(score) + '\n')
	file.close

def loadHighScores(user):
	scores = []
	file = open('data/scores/saved_scores.txt', 'r')
	allLines = file.read().splitlines()
	for line in allLines:
		data = line.split(',')
		if data[0] == user:
			print(data[0] + data[1])
			scores.append(data[1])
	scores = sorted(scores)
	return scores

def makeRegisteredUsersFileIfRequired():
	folderPath = 'data/users/'
	makeFolderIfRequired(folderPath)
	file = open(folderPath + 'registered_users.txt', 'a+')
	file.close()

def makeFolderIfRequired(path):
	if not os.path.exists(path):
	    os.makedirs(path)