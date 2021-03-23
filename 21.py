import random


ch = random.choice('pu')

point = 0
if ch == 'u':
	print('User Start')
	while True:

		while True:
			user = input('(1-3): ')
			end = 4

			if point > 18:
				end = 22-point
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					
					print("User-",point,'+',user,'=',point+user)
					point += user
					break
				else:
					print('\n\tplease input betwen :1','-',end-1)
			else:			
				print('\n\tplease input only Number:')		

		if point == 21:
			print('\n\tWin PC')
			break

		pc = 4 - point % 4
		print("Pc-",point,'+',pc,'=',point+pc)
		point += pc

		if point == 21:
			print('\n\tWin USER')
			break	

else:
	print('Start pc')
	while True:
		if point % 4 == 0:
			pc = random.randint(1,3)
		else:	

			pc = 4 - point % 4
		print("Pc-",point,'+',pc,'=',point+pc)
		point += pc

		if point == 21:
			print('\n\tWin USER')
			break	



		while True:
			user = input('(1-3): ')
			end = 4

			if point > 18:
				end = 22-point
			if user.isdigit():
				user = int(user)
				if 0 < user < end:
					
					print("User-",point,'+',user,'=',point+user)
					point += user
					break
				else:
					print('\n\tplease input betwen :1','-',end-1)
			else:			
				print('\n\tplease input only Number:')		

		if point == 21:
			print('\n\tWin PC')
			break