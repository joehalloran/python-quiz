import user, quiz, gamedata

def main(user, quiz, gamedata):
	user.registerUserIfRequired()
	user = user.login(3)
	score = quiz.runQuiz(user)
	gamedata.saveScore(user, score)
	gamedata.reportScore(user, score)

if __name__ == '__main__':
   main(user, quiz, gamedata)