# def factorial(n):
# 	if n < 0:
# 		raise ValueError('N y chi karox linel 0')
# 	elif n == 1:
# 		return 1
# 	else:
# 		count = 1
# 		for i in range(2,n + 1):
# 			count *= i
# 		return count


# def cilinder(r,h):
# 	v = r ** 2 * h * 3.14
# 	a = (2 * r * h * 3.14) + (2 * r ** 2 * h * 3.14)
# 	return a,v


# def sphere(r):
# 	v = 4/3 * 3.14 * r ** 3
# 	a = 4 * 3.14 * r ** 2
# 	return a,v


# def radian(r):
# 	d = 90 * r / 1.57
# 	return d


# def specified(n):
# 	for i in range(1, n):
# 		if i > 1:
# 			for j in range(2, i):
# 				if(i % j == 0):
# 					break
# 			else:
# 				print(i)