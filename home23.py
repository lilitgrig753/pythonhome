'''Password generator'''
chars = ('!', '@', '#', '$', '%','&', '*')
while True:
	password = input("Passowrd: ")
	chars_count = 0
	number_count = 0
	if len(password) < 8:
		print("Your password is not strong: ")
		continue
	for i in password:
		if i.isdigit():
			number_count += 1

		elif i in chars:
			chars_count += 1

	if number_count < 2:
		print("input 2 numbers: ")
		continue

	if chars_count < 2:
		print("input 2 chars: ")
		continue

	else:
		print("Your password is strong: ")
		break