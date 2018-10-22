import random

# Game globals
rooms	= {}
nexters	= ['Where next?', 'Where to go?', 'Enter a room name:']

# Append room to `rooms` dictionary
#
# @param	string	name			Name of room. Must be unique
# @param	string	instructions	Instuctions printed to user when entering
# @param	list	access			List of rooms the user can enter from here
# @return	void
def create_room(name, instructions, access = None):
	rooms[name]					= {}
	rooms[name]['instructions']	= instructions
	rooms[name]['access']		= access if access is not None else []

# Create entrance
create_room('entrance',
	'You are in the entrance of my house. Not much to see here.', \
	['kitchen', 'toilet', 'lounge', 'upstairs landing'])

# Create kitchen
create_room('kitchen',
	'This is where I cook up some deliciously shit meals for me and the missus.', \
	['entrance'])

# Create toilet
create_room('toilet',
	'You can still smell the remains of my last visit. Noice.', \
	['entrance'])

# Create the lounge
create_room('lounge',
	'Here you will find me lounging around in my underwear playing games.', \
	['entrance', 'garden'])

# Create garden
create_room('garden',
	'It is raining out here. Let\'s go back in.', \
	['lounge'])

# Create upstairs landing
create_room('upstairs landing',
	'Nothing exciting here, just the crossroad to our upstairs.', \
	['bathroom', 'gym', 'bedroom'])

# Create bathroom
create_room('bathroom',
	'If you don\'t want to see my junk then I suggest leaving.', \
	['upstairs landing'])

# Create gym
create_room('gym',
	'Yes I have a home "gym" and pumping iron is what I do best (lol jks I\'m shit).', \
	['upstairs landing'])

# Create bedroom
create_room('bedroom',
	'"Marvin Gaye - Let\'s get it on" starts playing ;)',
	['upstairs landing'])


# Setup games initial state
last	= None # Store the last room so we can go back
current	= 'entrance' # Set the starting room

# Welcome message to user
print('Welcome to a virtual "tour" of my house. Type "exit" end the tour.')

# Continous loop
while True:

	# Catch if a wrong room name was passed
	try:

		room	= rooms[current] # Get the current room attributes
		access	= ', '.join( room['access'] ) # List room access

		print( '--------------------------------' )
		print( room['instructions'] )
		print( 'You can enter: %s' % access )
		print( '--------------------------------' )

		# As the user where they want to go
		response = input( '%s ' % random.choice(nexters) ).lower()

		# Move into room if exists
		if response in room['access']:
			last	= current # Save last visit room
			current	= response # Set room to enter

		# Allow user to go to the last room by typing "back"
		elif response == 'back' and last in rooms:
			current = last

		# End the tour If the user types "exit"
		elif response == 'exit':
			print('Hope you enjoyed your tour. Adiós amigos!')
			break

		# Else throw generic error
		else:
			print( 'That room doesn\'t exist. Retry.' )

	except TypeError:
		print('Room not found [%s]' % current)
		current = input( 'Try another room name: ' ).lower()







