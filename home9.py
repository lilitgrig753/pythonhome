'''Take two int values from user and print greatest among them'''
# value1 = int(input("Number 1: "))
# value2 = int(input("Number 2: "))
# if value1 > value2:
# 	print(value1)
# else:
# 	print(value2)

'''Take input of age of 3 people by user and determine oldest
and youngest among them.'''
# Albert = int(input("Age Albert: "))
# Mary = int(input("Age Mary: "))
# Arno = int(input("Age Arno: "))
# if Albert <= Mary < Arno:
# 	print("Arno is older, Albert is younger")
# if Arno <= Mary < Albert:
# 	print("Albert is older, Arno is younger")
# if Mary <= Albert < Arno:
# 	print("Arno is older, Mary is younger")
# if Arno <= Albert < Mary:
# 	print("Mary is older, Arno is younger")
# if Albert <= Arno < Mary:
# 	print("Mary is older, Albert is younger")
# if Mary <= Arno < Albert:
# 	print("Albert is older, Mary is younger")
# if Mary == Arno == Albert:
# 	print("equal")

'''Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using
following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in
anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban
areas only.
And any other input of age should print "ERROR"'''

# Age = int(input("Age "))
# Sex = input("M or F ").upper()
# Status = input("Y or N ").upper()
# if Sex == "F":
# 	print("work only in urban areas")
# if Sex == "M" and 20 <= Age <= 40:
# 	print("work in anywhere")
# if Sex == "M" and 40 <= Age <= 60:
# 	print("work only in urban areas")
# if Sex != "M" and Sex != "F":
# 	print(input("M or F ").upper())
# if Status != "Y" and Status != "N":
# 	print(input("Y or N ").upper())
# if Age < 20 and Age > 60: 
# 	print("ERROR")

'''Rock, Paper, Scissors'''
# import random
# User = input("Rock, Paper, Scissors ")
# Pc = random.choice("RPS")
# print("User ", User)
# print("Pc ", Pc)
# if User == "Rock" and Pc == "P":
# 	print("Win Pc !!!")

# elif User == "Rock" and Pc == "R":
# 	print("even !!!")

# elif User == "Rock" and Pc == "S":
# 	print("Win User !!!")

# elif User == "Paper" and Pc == "P":
# 	print("even !!!")

# elif User == "Paper" and Pc == "R":
# 	print("Win User !!!")

# elif User == "Paper" and Pc == "S":
# 	print("Win Pc !!!")

# elif User == "Scissors" and Pc == "P":
# 	print("Win User !!!")

# elif User == "Scissors" and Pc == "R":
# 	print("Win Pc !!!")

# else:
# 	print("even !!!")

'''Rock, Paper, Scissors'''

# import random
# User = int(input("Rock - 1, Paper - 2, Scissors - 3 "))
# Pc = random.randint(1,3)
# print("User ", User)
# print("Pc ", Pc)
# if User == Pc:
# 	print("Even")
# elif User == 1 and Pc == 3 or User == 2 and Pc == 1 or User == 3 and Pc == 2 :
# 	print("Win User!!!")
# else:
# 	print("Win Pc!!!")

