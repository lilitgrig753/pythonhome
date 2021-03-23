'''Create new list which have 6 different data types.
For example: str, int'''

# my_list = ['Ab', 'Meri', 12, 5.2, True, ('tuple','aaa'), ['list', 'bbb']  ]
# print(my_list)


'''Create new list which have data notebooks and you want check if
the data have Mac?
For example: my_list = [“Hp”, “Asus”, “Dell”, “Mac”, ”Lenovo”]'''

# my_list = ['Hp', 'Asus', 'Dell', 'Mac', 'Lenovo', 'Hp']
# user = input('Pc: ').title()
# if user in my_list:
# 	print("Yes", my_list.count(user))
# else:
# 	print("No", my_list.count(user))


'''Create python program which will check if your password is strong
or no. if Len your password is great than 8 and if your password have
2 numbers and 2 of the following special characters ('!', '@', '#', '$', '%',
'&', '*') Sample Input: Python@$World11'''

# chars = ('!', '@', '#', '$', '%','&', '*')
# while True:
# 	password = input("Passowrd: ")
# 	chars_count = 0
# 	number_count = 0
# 	if len(password) < 8:
# 		print("Your password is not strong: ")
# 		continue
# 	for i in password:
# 		if i.isdigit():
# 			number_count += 1

# 		elif i in chars:
# 			chars_count += 1

# 	if number_count < 2:
# 		print("input 2 numbers: ")
# 		continue

# 	if chars_count < 2:
# 		print("input 2 chars: ")
# 		continue

# 	else:
# 		print("Your password is strong: ")
# 		break


'''Create python program where you want to find id in link if link have
id print id.
Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU'''

# link = 'https://www.youtube.com/watch?v=RRW2aUSw5vU'
# print(link[link.index('=')+1:])


'''Create python program where you want to check if input word is
palindrome or no .if yes print Open otherwise Trash'''

# user = input("word: ")
# if user == user [::-1]:
# 	print("Yes")
# else:
# 	print("No")


'''Create python program to convert string to a list'''

# string = 'Albert', 'Abul'
# my_list = []
# my_list.append(string)
# print(my_list)


'''Create python program which will show all even numbers in your               ???
string. Note: you have input where have 5 numbers'''

# my_str = input("Numbers:")
# my_list = []
# for i in my_str:
# 	if i % 2 != 0:
# 		my_list.apped(i)
# print(my_list)


'''Write a Python program to select the odd items of a list. And delete
even items.'''

# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = []
# for i in list1:
# 	if i % 2 == 0:
# 		list2.append(i)
# print(list2)


'''Your group have 5 people and each of them can              ???
take one name and when take this name is delete
from this list.And he can not take his name:'''

# import random
# my_list = ['Albert', 'Meri', 'Razo', 'Arshak', 'Sargis']
# for i in range(len(my_list)):
#     print(my_list[i],"buys for",my_list[(i + 1) % (len(my_list))])

# import random
# people = ['Albert', 'Meri', 'Razo', 'Arshak', 'Sargis']
# i = 0
# temp_list = []
# while i != len(people):
# 	x = random.choice(people)
# 	if x not in temp_list:
# 		temp_list.append(x)
# 	if len(temp_list)==2:
# 		print(temp_list)
# 		temp_list = []
# 		i += 1


# import random
# people = ['Albert', 'Meri', 'Razo', 'Arshak', 'Sargis']
# my_list = []
# count = 0
# while True:
# 	while True:
# 		x = random.choice(people)
# 		y = random.choice(people)
# 		if x != y:
# 			my_list.append([x, y])
# 			print(my_list)
# 		else:
# 			continue
# 	if 


# import random
# people = ["Abul", "Mary", "Razo", "Arshak", "Sargis"]
# choice_list = []
# for name in people:
#     index = people.index(name)
#     for i in range(len(people)):
#         if i != index:
#             choice_list.append(people[i])
#     choice = random.choice(choice_list)
#     print("{0}--{1}".format(name,choice))
#     if i == index:
#     	continue


# import random
# people = ["Abul", "Mary", "Razo", "Arshak", "Sargis"]
# choice_list = []
# for name in people:
#     choice_list = people.copy()
#     choice_list.remove(name)
#     choice = random.choice(choice_list)

#     print("{0}--{1}".format(name,choice))


	# count +=1
	# print(my_list)
	# if count == 3:
	# 	break


# for i in range(len(my_list)):
# 	numbers1 = random.randint(0,4)
# 	numbers2 = random.randint(0,4)

# 	print(my_list[numbers1], my_list[numbers2])

# numbers = random.randont(1,5)
# while True:
# 	if group == numbers:

# group_new = []
# numbers = random.randint(1,5)
# # group2.extend.(group1)
# # print(group2)
# for i in group1:
# 	if i == numbers:
# 		continue
# 		if i not in group_new:
# 			group_new.append(i)
# print(group_new)



'''Create a python program which delete all
duplicate items in list.'''

# list1 = ['Albert', 'Meri', 'Arno', 'Meri']
# list2 = []
# for i in list1:
# 	if i not in list2:
# 		list2.append(i)
# print(list2)






import random
import copy
peoples=['Albert', 'Mery', 'Razo', 'Arshak', 'Sargis']

temp_peoples = copy.deepcopy(peoples)
result_list = []
i = 0
j = 0
while i != len(peoples):
	j += 1
	if j > len(peoples):
		i, j = 0, 0
		result_list = []
		temp_peoples = copy.deepcopy(peoples)
	people = peoples[i]
	temp_people = random.choice(temp_peoples)
	if people == temp_people:
		continue
	temp_peoples.remove(temp_people)
	result_list.append([people,temp_people])
	i += 1
	
for i in result_list:
	print(i)