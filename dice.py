import random

# Roll dice nth number of times
# 
# @param	integer		total	Total number of times to roll the dice
# @param	boolean		debug	Print additional information to the user
# @return	integer		top		The top rolled face for this bulk run
def roll(total = 100, debug = False):

	# Setup counters for each dice face
	faces = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0,'6': 0}

	# Loop nth number of times and choose random number between 1 and 6 (inclusive)
	for i in range(total):
		result = str( random.randint(1, 6) )
		faces[result] += 1

	# Tell the user how many iterations were made
	if debug:
		print('Dice rolling probability out of %s roles' % (total))

	# Calculate the percentages and print the on screen
	for side, count in faces.items():
		percent = count / total * 100

		if debug:
			print('Dice side [%s] totaled at "%s" rolls. Which is %d%%' % (side, count, percent))

	# Get the top rolled dice face
	top = max(faces, key = faces.get)

	# Tell the user which face was rolled most
	if debug:
		print('The most rolled face was [%s]' % top)

	# Return top so we can reuse
	return top

# --------------------------------------------------------
#  Here we will run the `roll` function
# --------------------------------------------------------

go = True
while go:
	run = 10000 # Roll the dice this number of times
	top = roll(run)

	# Format run total into comma seperated and print top rolled face
	print('Out of {:,} rolls the face that was rolled most was [{}]'.format(run, top))

	# Allowed responses from user
	allowed = ['y', 'yes', '1', 'true']

	# Ask user if they want to run again
	response = input('Run again? [Y/n] ').lower()

	# Set while operator
	go = response in allowed






