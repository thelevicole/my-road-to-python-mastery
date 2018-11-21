import random

alphabet	= 'abcdefghijklmnopqrstuvwxyz'

tries		= 10	# User is allowed this many WRONG guesses

rand_word	= None	# Randomly selected word
guessed		= ''	# Current successfully guessed characters
wrong		= ''	# Current unsuccessful guessed characters

# Select random word from dictionary file.
#
# @see http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain
#
# @return	void
def choose_word():
	global rand_word
	words = open('dictionary.txt').read().splitlines()
	rand_word = random.choice(words)
	print('Your word has been choosen. It is has a total of %d characters' % len(rand_word))


# Check if a user has won the game
#
# @return	boolean
def has_won():
	won = True

	for c in rand_word:
		if c not in guessed:
			won = False
	return won

# Print available characters
#
# @return void
def print_available_chars():
	# Check a random word has been guessed
	if rand_word is not None:

		# Print characters
		for char in alphabet:
			if char not in (wrong + guessed):
				print('[%s]' % char.upper(), end = '')

		# Print closing newline
		print( '\n' )

# Print the users current progress and guessed characters
#
# @return void
def print_progress():
	# Check a random word has been guessed
	if rand_word is not None:
		# Create a repeated character for length of word plus surrounding []
		spliter = '-' * len(rand_word)

		# Print opening splitter
		print(spliter)

		# Print characters
		for char in rand_word:
			print_char = '_'
			if char in guessed:
				print_char = char
			print('%s' % print_char, end = '')

		# Print closing splitter
		print( '\n' + spliter )
	else:
		print('No game has been initialised.')

# Ask the user to guess a character and validate input
#
# @param	string	question
# @return	void
def ask_user(question = 'Guess a character'):
	global wrong, guessed

	if len(wrong) <= tries:
		print_available_chars()
		response = input(question + ': ').lower()
		if len(response) > 1 or len(response) < 1:
			print('Please choose a single character.')
			ask_user('Try again')
		elif response in guessed or response in wrong:
			print('You have already used that character.')
			ask_user('Try again')
		elif response not in rand_word:
			print('That character is not in this word. You have %d guesses remaining.' % (tries - len(wrong)))
			wrong += response
			ask_user('Try again')
		else:
			guessed += response

			if has_won():
				won()
			else:
				print('Correct, that letter is in the word!')
				print_progress()
				ask_user()
	else:
		lost()

# Start a game. Choose a word, print progress, and ask for user input
#
# @return void
def start():
	global wrong, guessed

	wrong	= ''	# Reset wrong guessed characters
	guessed	= ''	# Reset guessed characters

	choose_word()
	print_progress()
	ask_user()

# Ask user if they would like to play again
#
# @return void
def replay(question = 'Play again?'):
	response = input(question + ' [Y/n] ')
	if response.lower() in ['y', 'yes', '1', 'true']:
		start()

# Fired when the user has won the game
#
# @return void
def won():
	print('Congratulations! You have successfully won the game!')
	print('The word was "%s"' % rand_word)
	replay()

# Fired when the user has lost the game
#
# @return void
def lost():
	print('You ran out of guesses. The word you were looking for was [%s]' % rand_word)
	replay('Retry?')



# --------------------------------------------------------
#  Here we will start the game
# --------------------------------------------------------
start()





