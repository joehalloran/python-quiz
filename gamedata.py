# TODO: Add description of gamedata.py

import filehandler

def saveScore(user, score):
	filehandler.saveScore(user, score)	

def reportScore(user, score):
	print()
	print("Well done " + user + " your final score was...")
	print(score)
	showFinalMenu(user)

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

def getHighScores(user):
	return filehandler.loadHighScores(user)
	