'''Write a python program which will calculate this definition. You have 2 inputs (a , b). Use math.'''
# import math
# a = int(input("Number a - "))
# b = int(input("Number b - "))
# x = math.sqrt((a+b)/2) + (a+b)/math.factorial(a)
# print(x)

'''Write a Python program that accepts an integer ( n ) and computes the value of n+nn+nnn. (example n=5 output should be 5 + 55 + 555=615)'''
# n = int(input("Number: "))
# val1 = str(n) + str(n)
# val2 = str(n) + str(n) + str(n)
# val = n + int(val1) + int(val2)
# print(val)

'''KAM'''
n = input("Number: ")
val = int(n) + int(n+n) + int(n+n+n)
print(val)