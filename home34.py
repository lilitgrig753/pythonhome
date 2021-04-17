'''Create a class: Some people are standing in a row in a park. There are trees
between them which cannot be moved. Your task is to rearrange the people by
their heights in a non-descending order without moving the trees. People can be
very tall!'''


# class Park:


# 	def __init__(self,a):
# 		self.a = a


# 	def sort(self):
# 	    res = sorted([i for i in self.a if i != -1])
# 	    count  = 0
# 	    for i in range(len(self.a)):
# 	        if self.a[i] == -1:
# 	            continue
# 	        else:
# 	            self.a[i] = res[count ]
# 	            count += 1
# 	    return self.a

# x = Park([-1, 150, 190, 170, -1, -1, 160, 180])
# print(x.sort())



'''Several people are standing in a row and need to be divided into two teams. The
first person goes into team 1, the second goes into team 2, the third goes into
team 1 again, the fourth into team 2, and so on.You are given an array of positive
integers - the weights of the people. Return an array of two integers, where the
first element is the total weight of team 1, and the second element is the total
weight of team 2 after the division is complete.'''



# a = [50, 60, 60, 45, 70]

# class Myclass:

# 	def __init__(self,a):
# 		self.a = a


# 	def team(self):
# 		res1 = []
# 		res2 = []
# 		res = []
		
# 		for i in range(len(self.a)):
# 			if i % 2 == 0:
# 				res1.append(self.a[i])
# 			if i % 2 == 1:
# 				res2.append(self.a[i])
			
# 		res.append(sum(res1))
# 		res.append(sum(res2))
# 		return res

	
# x = Myclass([50, 60, 60, 45, 70])
# print(x.team())




