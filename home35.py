# class Dog:
# 	def __init__(self,name,age):
# 		self.name = name
# 		self.age = age
# 	def __str__(self):
# 		return f"{self.name} is {self.age} years old"
# c = Dog('Sevuk',7)
# print(c) 


'''Create a python class which given an list of integers, find
the maximal absolute difference between any two of its
adjacent elements.'''


# class elements:

# 	def __init__(self, c):
# 		self.c = c

# 	def res(self):
# 		for i in self.c:





res = 0
c = [2, 4, 1, 0]
for i in c:
	res = i - (i + 1)
	print(res)