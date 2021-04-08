'''Write a recursive function to determine whether all
digits of the number are odd or not. '''

# def number(x):
# 	for i in str(x):
# 		if int(i) % 2 == 0 and int((i + 1)) % 2 == 0:
# 			print(False)
# 		else:
# 			print(True) 
# number(79)


'''Write a python function all even number in
10.000 use threading and print time.'''

# import time
# start_time = time.time()
# def num(x):
# 	for i in range(1, x + 1):
# 		if i % 2 == 0:
# 			print(i)

# num(10000)
# print(time.time() - start_time)



'''Given N number. Write a recursive function that
should print from 1 to N numbers.'''

def number(n):
	print(n)
	if n > 0:
	
		number(n-1)
number(5)
	


