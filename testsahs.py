def tari(add_month):
	month = 1
	year = 2000
	count = 1
	if add_month >= 13:
		year += 1
		count == add_month % 12
		month += count
		print(year, month)
	
tari(13)