'''Write a Python program to
 sum all the items in a list'''

# my_list = [1, 2, 3, 4, 5]
# print(sum(my_list))


'''Write a Python program
to multiplies all the items
in a list'''

# my_list = [1,2,3,4,5]
# res = 1
# for x in my_list:
# 	res *= x
# print(res)


'''Write a Python program to
get the largest text from a list'''

my_list = ['Abo','Albert', 'Abul','Albert_python', 'Ab']
# larget = max(my_list, key = len)
# print(larget)
count = 0
for i in my_list:
	if len(i) > count:
		count = len(i)
		res = i
print(res)


'''Write a Python program that have two
lists and returns True if they have at least
one common member.'''

# list1 = ['bmw', 'mers', 'audi', 'buggati']
# list2 = ['mers', 'golf', 'bmw', 'ferrari']
# for x in list1:
# 	if x in list2:
# 		print(x)
# 		print(True)
# 		break
# 	else:
# 		print(False)

