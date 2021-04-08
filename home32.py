'''Calculator'''

class Calculator():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def gumar(self):
		return self.x + self.y

	def hanum(self):
		return self.x - self.y

	def bajanum(self):
		return self.x / self.y

	def bazmapatkum(self):
		return self.x * self.y



while True:
	cragir = input('On/Off ===> ').title()
	if cragir == 'On':
		while True:
			try:
				x = float(input('Number 1: '))
				y = float(input('Number 2: '))
				nshan = input('Inch gorcoxutyun eq cankanum katarel    +, -, /, * ===> ')
				res = Calculator(x, y)
				if nshan == '+':
					print(res.gumar())
					continue
				elif nshan == '-':
					print(res.hanum())
					continue
				elif nshan == '/':
					print(res.bajanum())
					continue
				elif nshan == '*':
					print(res.bazmapatkum())
					continue
			
			except ValueError:
				print('Greq miayin tiv: ')
			continue
	else:
		print('Cragiry anjatvac e: ')
		break









