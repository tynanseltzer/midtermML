import csv
import ast

from collections import defaultdict

with open('finale.csv', 'wb') as writer:
	spamwriter = csv.writer(writer, delimiter='#', quotechar='|')

	masterdict = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: defaultdict(int))))

	with open('newmatched2.csv') as csvfile:
		spamreader = csv.reader(csvfile, delimiter='#', quotechar='|')
		for row in spamreader:
			masterdict[row[1]][row[2]][row[3]][int(row[4])] = row[5]

	# print(masterdict)

	with open('formatcandids.csv') as csvfile:
		spamreader = csv.reader(csvfile, delimiter='#', quotechar='|')
		for row in spamreader:
			first = row.pop(1)
			last = row[0]
			row[0] = last + ", " + first
			row.append(masterdict[row[1]][row[2]][row[3]][int(row[4])])
			print(row)
			spamwriter.writerow(row)


## 4477 
# with open('formatcandids.csv') as 2ndcsv:
			
			# spamreader = csv.reader(csvfile, delimiter='#', quotechar='|')
			# for row in spamreader:
			# 	if int(row[4]) == 2008:
			# 		continue
			# 	else:
			# 		prev = int(row[4]) - 2
			# 		try:
			# 			thingtoadd = masterdict[row[1]][row[2]][row[3]][prev]
			# 			row.append(thingtoadd)
			# 		except:
			# 			row.append("+++++++++++++++")
			# 		print(row)
			# 		row.pop(-2)
			# 		row.pop(-2)
			# 		spamwriter.writerow(row)




	# print(masterdict['FL']['14']['NON'][2008])




