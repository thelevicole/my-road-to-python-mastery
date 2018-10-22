import random

words = open('dictionary.txt').read().splitlines()

# List each character in the string, shuffle them and the join
# 
# @param	string	String to shuffle
# @return	string
def shuffle_str( wrd ):
	chars = list( wrd )
	random.shuffle( chars )
	return ''.join( chars )

# Config
goes		= 10 # Total number of goes a user can have
word		= random.choice( words ) # Select a random word from the dictionary file
scrambled	= shuffle_str( word ).lower() # Shuffle letters

# Keep trying until the user runs out of goes
while goes > 0:

	# Print the scrambled word
	print('-- %s --' % scrambled)

	# Get the user input
	guess = input('Take a guess: ').lower()

	# If guessed correctly
	if guess is word:
		print('Hooray! You guessed %s correctly' % word)
	else:
		# Guessed wrong, decrease goes count
		goes -= 1

		# If user has ran out of goes, print the expected word
		if goes <= 0:
			print('You lost. The word you were looking for was: %s' % word)
		else:
			print('Sorry please try again. You have %d number of guesses left.' % goes)