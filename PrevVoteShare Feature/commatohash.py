import csv
import ast

from collections import defaultdict

with open('formatcandids.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter='#')

	with open('candidatething.csv') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
		for row in spamreader:
			print(row)
			spamwriter.writerow(row)




	# print(masterdict['FL']['14']['NON'][2008])




