'''Write a Python program to check if pc
number is great than 10. random(1,20)
when True break.'''
# import random 
# while True:
# 	pc = random.randint(1,20)
# 	print(pc)
# 	if pc > 10:
# 		break
# 	else:
# 		continue

'''Chinga Chung'''
import random
Point_User = 0
Point_Pc = 0
while True:
	User = int(input("Rock - 1, Paper - 2, Scissors - 3 "))
	Pc = random.randint(1,3)
	if User == Pc:
		print("Even")
		continue
	elif User == 1 and Pc == 3 or User == 2 and Pc == 1 or User == 3 and Pc == 2 :
		Point_User += 1
		print("Win User!!!", Point_User)
	elif Pc == 1 and User == 3 or Pc == 2 and User == 1 or Pc == 3 and User == 2:
		Point_Pc += 1
		print("Win Pc!!!", Point_Pc)
	if Point_Pc == 3 or Point_User == 3:
		break