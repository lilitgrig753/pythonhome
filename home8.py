'''Write a Python program to check
whether an alphabet is a vowel or
consonant.'''
# letter = input("Letter: ").lower()
# alphabet = "a, e, i, o, u"
# if letter in alphabet:
# 	print('consonant')
# else:
# 	print('no consonant')

'''Write a Python program to check this
year is leap year or no.'''
# year = int(input("Year: "))
# if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
# 	print("leap year")
# else:
#     print("No leap year")

'''Write a Python program to check if
your number is odd or even'''
# number = int(input("Number: "))
# if number % 2 == 0:
# 	print("Number is even")
# else:
# 	print("Number is odd")

'''Write a python program which will say who
win in game.
The winner is the one which have 2 point.You
should try to find pc number(0-5):
if find (your point +=1) otherwise (pc point +=1):'''
# import random
# point_user = 0
# point_pc = 0
# user1 = int(input("Number: "))
# user2 = int(input("Number: "))
# pc1 = random.randint(0,5)
# pc2 = random.randint(0,5)
# if user1 == pc1 and user2 == pc2:
# 	point_user += 2

# if user1 == pc1 or user2 == pc2:
# 	point_user += 1

# if user1 != pc1 and user2 != pc2:
# 	point_pc += 2
# else:
# 	point_pc += 1

# print("Number pc1 = ", pc1)
# print("Number pc2 = ", pc2)
# print("Number user1 = ", user1)
# print("Number user2 = ",user2)
# print(point_user)
# print(point_pc)

import random
point_user = 0
point_pc = 0
user1 = int(input("Number: "))
user2 = int(input("Number: "))
pc1 = random.randint(0,5)
pc2 = random.randint(0,5)
if user1 == pc1 and user2 == pc2:
	point_user += 2

if user1 == pc1 or user2 == pc2:
	point_user += 1
	user = int(input("New number: "))
	pc = random.randint(0,5)
	if user == pc:
		point_user += 1
	if user != pc:
		point_pc += 1

if user1 != pc1 and user2 != pc2:
	point_pc += 2
else:
	point_pc += 1

print("Number pc1 = ", pc1)
print("Number pc2 = ", pc2)
print("Number user1 = ", user1)
print("Number user2 = ",user2)
print(point_user)
print(point_pc)