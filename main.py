import user
import quiz

def main(user, quiz):
	user.registerUserIfRequired()
	user = user.login()
	difficulty = selectDifficulty()
	score = runQuiz(user, difficulty)
	saveScore(score)
	reportScore(score)

if __name__ == '__main__':
   main(user, quiz)