

file = False

def openFile(folderAndFile, mode) {
	file = open(folderAndFile, mode)
}

def getQuestionsFromFile(difficulty) {
	openFile()
}

#>>> for line in f: print line,

# f.write('This is a test\n')