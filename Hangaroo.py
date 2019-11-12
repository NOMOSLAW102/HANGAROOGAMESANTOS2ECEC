import string
alph = string.ascii_lowercase
print ("Give me a word in lower case to start the game. Give it by calling the function: hangaroo('*yourword*')")
def isWordGuessed(secretWord, lettersGuessed):
    count = 0
    for i, c in enumerate(secretWord):
    	if c in lettersGuessed:
    		count += 1
    if count == len(secretWord):
    	return True
    else:
    	return False
def getGuessedWord(secretWord, lettersGuessed):
    result = []
    for i in secretWord:
        if i in lettersGuessed:
            result.append(i)
        else:
            result.append('_')
    return ' '.join(result)
def getAvailableLetters(lettersGuessed):
    remain = []
    for i in alph:
        if i not in lettersGuessed:
            remain.append(i)
    return ''.join(remain)
def hangaroo(secretWord):
    print('Welcome to Hangaroo!')
    print('I have a word! It is', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []

    while 5 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('------------')
            print('You won!!!!')
            break
        else:
        	print('------------')
        	print('You have', 5 - mistakesMade, 'guesses left.')
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Give me a letter!: ')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('Nice!: ', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("You already gave that letter, pick another one!", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("That letter is not in my word, pick another one!", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 5 - mistakesMade == 0:
        	print('------------')
        	print('Sorry, you lost! The word was', secretWord)
        	break
        else:
        	continue

    