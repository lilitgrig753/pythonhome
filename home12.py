# import random

# ch = random.choice('pu')
# point_pc = 0
# point_user = 0
# point = 0
# if ch == 'u':
# 	print('User Start')
# 	while True:

# 		while True:
# 			user = input('(1-3): ')
# 			end = 4

# 			if point > 18:
# 				end = 22-point
# 			if user.isdigit():
# 				user = int(user)
# 				if 0 < user < end:
			
# 					print("User-",point,'+',user,'=',point + user)
# 					point += user
# 					break
# 				else:
# 					print('\n\tplease input betwen :1','-',end - 1)
# 			else:			
# 				print('\n\tplease input only Number:')		

# 		if point == 21:
# 			point_pc += 1
# 			print('\n\tWin PC',"Pc points =", point_pc)
# 			break

# 		pc = 4 - point % 4
# 		print("Pc-",point,'+',pc,'=',point + pc)
# 		point += pc

# 		if point == 21:
# 			point_user += 1
# 			print('\n\tWin USER', "User points =", point_user)
# 			break




# else:
# 	print('Start pc')
# 	while True:
# 		if point % 4 == 0:
# 			pc = random.randint(1,3)
# 		else:	

# 			pc = 4 - point % 4
# 		print("Pc-",point,'+',pc,'=',point + pc)
# 		point += pc

# 		if point == 21:
# 			point_user += 1
# 			print('\n\tWin USER',"User points =", point_user)
# 			break	


# 		while True:
# 			user = input('(1-3): ')
# 			end = 4

# 			if point > 18:
# 				end = 22-point
# 			if user.isdigit():
# 				user = int(user)
# 				if 0 < user < end:
					
# 					print("User-",point,'+',user,'=',point + user)
# 					point += user
# 					break
# 				else:
# 					print('\n\tplease input betwen :1','-',end - 1)
# 			else:			
# 				print('\n\tplease input only Number:')		

# 		if point == 21:
# 			point_pc += 1
# 			print('\n\tWin PC',"Pc points =", point_pc)
# 			break



import random

point = 0
user_point = 0
pc_point = 0


while True:
	user = int(input("Number(1-3): "))
	pc = random.randint(1,3)
	x = 1 <= user <= 3
	point += x
	point += pc
	print("User points =", x, "Pc points =", pc, "Sum =", point)
	if point == 21:

		break
		# print("User points =", user, "Pc points =", pc, "Sum =", point)



