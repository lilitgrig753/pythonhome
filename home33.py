''' 1 - Write a python class to find max, min num and
and sum in your list:
don’t use max sum and min function'''

# class Mylist:

# 	def __init__(self,c):
# 		self.c = c

# 	def minmax(self):
# 		minimum = self.c[0]
# 		maximum = self.c[0]
# 		for number in self.c:
# 			if number < minimum:
# 				minimum = number
# 			if number > maximum:
# 				maximum = number
# 		print('Minimum =',minimum, 'Maximum =',maximum)
		
# a = Mylist('12345')
# a.minmax()


'''2 - Write a python class to find two highest values in
your dict:'''

# class Mydict:

# 	def __init__(self,my_dict):
# 		self.my_dict = my_dict

# 	def highest(self):

		
# 		valu = self.my_dict.values()
# 		c = []
# 		c.append(valu)
# 		maximum = c[0]
# 		for number in c:
# 			print(self.my_dict[number])
			# if self.my_dict[number] > maximum:
			# 	maximum = self.my_dict[number]
			# print(maximum)

# x = Mydict({'Abo':21, 'Meri':20})
# x.highest()



'''3 - Write a python class where your child class takes
all methods in parent class and print them'''


# class Xumb1:

# 	def __init__(self,fname,lname):
# 		self.firstname = fname
# 		self.lastname = lname

# 	def res1(self):
# 		print(self.firstname, self.lastname)

# class Xumb2(Xumb1):
# 	def __init__(self,fname,lname, age):
# 		super().__init__(fname, lname)
# 		self.age = age

# 	def res2(self):
# 		print(self.firstname, self.lastname, self.age)

# x = Xumb1('Albert', 'Zakaryan')
# x = Xumb2('Meri', 'Karapetyan', 20)
# x.res1()
# x.res2()


'''4 - Write a Python class named Rectangle
constructed by a length and width and a method
which will compute the area of a rectangle'''


# class Rectangle:

# 	def __init__(self,lenght, width):
# 		self.lenght = lenght
# 		self.width = width

# 	def area(self):
# 		s = self.lenght * self.width
# 		print(s)

# x = Rectangle(5, 10)
# x.area()


'''5 - Write a python class where we use polymorphism'''

# class Armenia:

# 	def country(self):
# 		print('Erevan')


# class France:

# 	def country(self):
# 		print('Paris')

# A = Armenia()
# F = France()
# A.country()
# F.country()




class Student(Person):
	def __init__(self, fname, lname, age):
		super().__init__(fname, lname)
		self.age = age
	def welcome(self):
		print(self.firstname, self.lastname, self.age) 