import csv
import ast

from collections import defaultdict

with open('newmatched2.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter='#')

	masterdict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))
	with open('timetomatch2.csv') as csvfile:
		spamreader = csv.reader(csvfile, delimiter='#', quotechar='|')
		for row in spamreader:
			print(row[6])
			masterdict[row[1]][row[2]][row[3]][int(row[4])] += float(row[6])

		# print(masterdict)

	with open('timetomatch2.csv') as csvfile:
		spamreader = csv.reader(csvfile, delimiter='#', quotechar='|')
		for row in spamreader:
			if int(row[4]) == 2008:
				continue
			else:
				prev = int(row[4]) - 2
				try:
					thingtoadd = masterdict[row[1]][row[2]][row[3]][prev]
					row.append(thingtoadd)
				except:
					row.append("+++++++++++++++")
				print(row)
				row.pop(-2)
				row.pop(-2)
				spamwriter.writerow(row)




	# print(masterdict['FL']['14']['NON'][2008])




