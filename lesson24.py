import random

print('          Hi you play Tic Tac Toe\n')

def print_tablo():

	print('\n\n          ',all_steps[0],'|',all_steps[1],'|',all_steps[2],' ')
	print('          --- --- ---')
	print('          ',all_steps[3],'|',all_steps[4],'|',all_steps[5],' ')
	print('          --- --- ---')
	print('          ',all_steps[6],'|',all_steps[7],'|',all_steps[8],' \n\n')


def start():

	while True:

		global choice
		global steps 
		global all_steps

		steps = []
		all_steps = [1, 2, 3, 
					4, 5, 6, 
					7, 8, 9]

		print('')
		x = input('          You want (X) or (O)   ')
		choice = x.upper()
		if choice == 'X' or choice == 'O':
			break

		else:
			print('           You dont input (X) or (O)')


def player():

	while True:
		print("")
		try:
			players_step = int(input("          Where you want write: "))
			if players_step in range(1,10):
				if players_step not in steps:
					steps.append(players_step)
					result = players_step - 1
					all_steps[result] = choice
					break
				else:
					print('This place is busy')

		except ValueError:
			print("                  Input a correct number")

def comp():

	while True:
		comp_step = random.randint(1,9)
		if comp_step not in steps:
			steps.append(comp_step)
			print("          Comp step", comp_step)
			result_comp = comp_step - 1
			if choice =='X':
				all_steps[result_comp] = 'O'
			else:
				all_steps[result_comp] = 'X'
			break

def game():

	while True:
		if (all_steps[0] == all_steps[1] == all_steps[2] == "X" or
			all_steps[3] == all_steps[4] == all_steps[5] == "X" or
			all_steps[6] == all_steps[7] == all_steps[8] == "X" or
			all_steps[0] == all_steps[4] == all_steps[8] == "X" or
			all_steps[2] == all_steps[4] == all_steps[6] == "X" or
			all_steps[0] == all_steps[3] == all_steps[6] == "X" or
			all_steps[1] == all_steps[4] == all_steps[7] == "X" or
			all_steps[2] == all_steps[5] == all_steps[8] == "X"):
			print('             WIN X -')
			break

		elif len(steps) == 0:
			print('             NOBODY WIN')
			break

		elif (all_steps[0] == all_steps[1] == all_steps[2] == "O" or
			all_steps[3] == all_steps[4] == all_steps[5] == "O" or
			all_steps[6] == all_steps[7] == all_steps[8] == "O" or
			all_steps[0] == all_steps[4] == all_steps[8] == "O" or
			all_steps[2] == all_steps[4] == all_steps[6] == "O" or
			all_steps[0] == all_steps[3] == all_steps[6] == "O" or
			all_steps[1] == all_steps[4] == all_steps[7] == "O" or
			all_steps[2] == all_steps[5] == all_steps[8] == "O"):
			print('             WIN O -')
			break

		elif len(steps) == 0:
			print('             NOBODY WIN')
			break

		else:
			return True

def play():
	start()
	print_tablo()

	while True:
		if choice == "X":
			player()
			print_tablo()
			if not game():
				break
			comp()
			print_tablo()
			if not game():
				break
		else:
			comp()
			print_tablo()
			if not game():
				break
			player()
			print_tablo()
			if not game():
				break
play()


def play_again():

	while True:
		answer = input('          You want play again yes(y) or no? ') == 'y'
		if answer:
			play()
		else:
			break
play_again()

	
