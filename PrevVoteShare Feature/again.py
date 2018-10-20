import csv
import ast

from collections import defaultdict

with open('bro.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter='#')
	with open('another.csv') as csvfile:
		tempor = []
		for row in reversed(list(csv.reader(csvfile, delimiter='#', quotechar='|'))):
			
			if len(list(row[-1])) > 1:
				tempor = []
				x = row.pop()
				x = ast.literal_eval(x)
				print(x)
				tempor = x
			row.append(tempor.pop())
			if row[-2] == '':
				row.pop(-2)	
			spamwriter.writerow(row)

	# with open('bro.csv', 'wb') as csvfile:
	# 	spamwriter = csv.writer(csvfile, delimiter='#')


	# 	initstate = 'AL'
	# 	initdistrict = '1'
	# 	inityear = 2006
	# 	totevote = 0

	# 	votingvals = []

	# 	# for row in spamreader:
	# 	# 	if row[-1] == 'Unopposed':
	# 	# 		row[-1] = 1
	# 	# 	print(row)
	# 	# 	spamwriter.writerow(row)

	# 	for row in spamreader:
	# 		curstate, curdistrict, curyear = row[1], row[2], row[4]
	# 		curvote = int(row[5])

	# 		if (curstate, curdistrict, curyear) == (initstate, initdistrict, inityear):
	# 			votingvals.append(curvote)
	# 			initstate, initdistrict, inityear = curstate, curdistrict, curyear

	# 		else:
	# 			temp = []
	# 			print(votingvals)
	# 			totevote = sum(votingvals)
	# 			for x in votingvals:
	# 				try:
	# 					temp.append(float(x)/totevote)
	# 				except ZeroDivisionError:
	# 					temp.append(float(x))

	# 			row.append(temp)
	# 			temp = []
	# 			votingvals = []
	# 			totevote = 0
	# 			initstate, initdistrict, inityear = curstate, curdistrict, curyear
	# 			votingvals.append(curvote)

	# 		# print(row[3])
	# 		# row[3] = mydict[row[3]]
	# 		print(row)
	# 		spamwriter.writerow(row)