import csv

from collections import defaultdict

with open('mostyearstemp.csv') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='#', quotechar='|')
	# print(spamreader)

	mydict = defaultdict(lambda: "OTHER")
	mydict['Republican'] = 'REP'
	mydict['Libertarian'] = 'LIB'
	mydict['Independent'] = 'IND'
	mydict['Democratic'] = 'DEM'
	mydict['Green'] = 'GRE'
	mydict['Write-In'] = 'WRI'
	mydict['No Party Affiliation'] = 'NON'

	nada = mydict['N']
	print(nada)
	# for row in spamreader:
	# 		# try:
	# 	try:
	# 		print(row[3])
	# 	except:
	# 		print(row)
	# 		print("##############")

	print(mydict)

	with open('mostfinal.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')

		for row in spamreader:
			# try:
			print(row[3])
			row[3] = mydict[row[3]]
			
			spamwriter.writerow(row)