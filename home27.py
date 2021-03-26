'''1 - You have two list convert it in dictionary and add
in (mydict.txt) and show result:'''

# first = ['Ani', 'Jessy', 'Ben']
# second = [1,2,3]
# my_dict = {}
# for i, j in zip(first, second):
# 	my_dict[i] = j
# c = []
# c.append(my_dict)
# print(c)
# with open('home27.txt', 'w') as f:
# 	f.write(f'{c}')


'''2 - Create json file and save them lyrics (song)
and print in cmd word this song'''

# import json

# file_name = 'home27.json'
# try:
# 	with open(file_name) as file:
# 		user = json.load(file)
# 		print(user)

# except FileNotFoundError:
	
# 	with open(file_name, 'w') as file:
# 		song = input('what is your favorite song? ')
# 		user = json.dump(song, file)
# 		print(song) 
# count_upper = 0
# count_lower = 0
# for i in user:
# 	if i.isupper():	
# 		count_upper += 1
# 	print('count upper', count_upper)

# 	if i.islower():
# 		count_lower +=1
# 	print('count lower',count_lower)


'''3 - Write a python program which have one input an
integer, representing the sum of all the multiples of
3 and 5 below the given input. and save this result
in json file'''

# import json
# number = int(input('Number: '))
# count = 0
# for i in range(1,number+1):
# 	if i % 3 == 0 or i % 5 == 0:
# 		count += 1
# print(count)
# with open('about_users.json', 'w') as f:
# 	file = json.dump(count,f)


'''4 - Write a program that takes in a string as input,
counts and outputs the number of vowels.
And add result in json file.'''

# bar = input('Bar ')
# dzaynavorner = ['a', 'e', 'u', 'o', 'i']
# count = 0
# for i in dzaynavorner:
# 	if i in bar:
# 		count += 1
# 		print('Bar ', bar, 'count ', count)
# 	else:
# 		print('Dzer bari mej chkan dzaynavorner')

# with open ('dzaynavorner.json', 'w') as f:
# 	f.write(f'{bar}')


'''5 - You have text.txt file and contains such text:
Another pause and more eying and siding around
each other
You can create one dict where you have.'''

# text = ['Another pause and more eying and siding around each other']
# count = 0
# for i in text:
# 	for j in i:
# 		count += 1
# 		print(j, count, end='')


'''6 - Write a python function which get a new list
from a given list, consisting of the first
repeating elements.'''

# my_list = ['a', 'b', 'a', 'c', 'b']
# print(set(my_list))


'''7 - You have word.txt file and in them you have
one story.
Write a Python function that accepts this
story and calculate the number of uppercase
letters and lowercase letters. '''

# my_story = 'Albert'
# with open('story.txt', 'w') as f:
# 	f.write(f'{my_story}')
# count_upper = 0
# count_lower = 0
# for i in my_story:
# 	if i.isupper():
# 		count_upper += 1
# 		print('count upper ', count_upper)
# 	if i.islower():
# 		count_lower += 1
# 		print('count lower ', count_lower)
