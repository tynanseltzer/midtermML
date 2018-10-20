import csv
with open('collatedelection.csv') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='#', quotechar='|')
	# print(spamreader)
	for row in spamreader:
		try:

			# name and party
			row.pop()
			nameparty = row[2].split()
			temp = nameparty[-1]
			row.append(temp)
			nameparty.pop()
			row[2] = ' '.join(nameparty)
			row[2] = row[2].upper()
			row[-1] = row[-1].upper()

			districtstate = row[1].split()
			state = districtstate.pop()
			district = int(districtstate[0])
			row.append(state)
			row[1] = district

			print(row)
		except IndexError:
			print("index error BEGIN")
			print(row)
			print("index error END")
		# print('###'.join(row))

