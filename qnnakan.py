'''                                   ----- 1 -----
	The doctors and the scientists are found out that you can learn about your illness 
coronavirus  from home by the following formula. If you duplicate your  body temperature
 by Celsus with the number of pi(math) and round up to the nearest whole number and if 
 it is between the intervals of 120 to 128  so you have coronavirus otherwise no. '''

'''Create a class that accepts a number of  your  body temperature by Celsius and duplicate 
with the number of pi and rounded up to the nearest whole number '''

# import math

# class Temperature:
# 	def __init__(self, temp):
# 		self.temp = temp

# 	def corona(self):
# 		result = self.temp * math.pi
# 		res = math.ceil(result)

# 		if 120 <= res <= 128:
# 			return (res, 'You Have coronavirus ((( ')
# 		else:
# 			return (res, 'Everything is ok’ )))')

# x = Temperature(40.75)
# print(x.corona())


'''                                   ----- 2 -----
The english scientists found out that each english letter has its corresponding numbers. And they create a chart where: 1 = a, j, s  2 = b, k, t  3 = c, l, u  4 = d, m, v   5 = e, n, w   6 = f, o, x 
7 = g, p, y   8 = h, q, z   9 = i, r   and you will know if your name is widespread or no when you
square root your name number and  arranging number in ascending order is less than 5:
'''
'''Create a class that accepts a string of your name and it will tell the number of your name 
will tell if it is widespread or not .
'''


# import math


# class Myname:
#     my_dict = {1: "a,j,s", 2: "b,k,t", 3: "c,i,u", 4: "d,m,v", 5: "e,n,w",
#                6: "f,o,x", 7: "g,p,y", 8: "h,q,z", 9: "i,r"}

#     def __init__(self):
#         self.name = input("Name: ")
#         self.count = 0

#     def res(self):
#         for i in range(len(self.name)):
#             if self.name[i] in self.my_dict[i + 1]:
#                 self.count = i + 1
#         if math.sqrt(self.count) < 5:
#             print("yes", self.count)
#         else:
#             print("No", self.count)


# x = Myname()
# x.res()




'''3 - You are Harry Potter and you fight with Lord Voldemort in order to protect your friends.
You should use magic words for winning him. You both use the following magic words
during fighting:  Avada Kedavra,  Crucio, Imperio  . You get 1 point when your word corresponds to his, otherwise you lose 1 point. You have three attempts and you will
become a winner if  you have 2 corresponding words.'''

'''Create a class that accepts three string through which you will try to guess the random 
magic word of the Lord Voldemort.'''

''''Avada Kedavra = 1, Crucio = 2, Imperio = 3'''

# import random

# class HarryPoter:

# 	def __init__(self):
# 		self.count_Harry = 0
# 		self.count_Vold = 0

# 	def game(self):
# 		while True:
# 			Harry = int(input('Number: '))
# 			Vold = random.randint(1,3)
			
# 			if Harry == Vold:
# 				self.count_Harry += 1
# 				print('Number Harry =',Harry, 'Number Vold =',Vold)
# 				print('Win Harry', self.count_Harry)
# 			else:
# 				self.count_Vold += 1
# 				print('Number Harry =',Harry, 'Number Vold =',Vold)
# 				print('Win Vold', self.count_Vold)

# 			if self.count_Harry == 2:
# 				print('Win Harry!!!!!')
# 				break
# 			if self.count_Vold == 2:
# 				print('Win Vold!!!!!')
# 				break

# x = HarryPoter()
# x.game()



