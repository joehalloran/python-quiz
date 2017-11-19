def saveScore(user, score):
	#TODO
	return

def reportScore(user, score):
	print("Well done " + user + " your final score was...")
	print(score)
	showFinalMenu(user)

def showFinalMenu(user):
	print("Press 1 to show your high scores")
	print("Press 2 to quit")
	userSelection = input("> ")
	if userSelection == '1':
		highScores = getHighScores(user)
		for score in highScores:
			print(score)
		showFinalMenu(user)
	else: 
		print("Thanks for playing. Goodbye")
		exit()

def getHighScores(user):
	#TODO
	return ["1st Jan 2017: 2", "2nd Feb 2017: 3", "4th June 2017: 5"]
