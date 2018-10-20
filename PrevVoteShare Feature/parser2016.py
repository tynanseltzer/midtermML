import csv

from collections import defaultdict

with open('2016new.csv') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='#', quotechar='|')
	# print(spamreader)

	mydict = defaultdict(lambda: "OTHER")
	mydict['R'] = 'REP'
	mydict['L'] = 'LIB'
	mydict['I'] = 'IND'
	mydict['D'] = 'DEM'
	mydict['G'] = 'GRE'

	nada = mydict['N']
	print(nada)

	print(mydict)

	stateabbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
	with open('2016final.csv', 'wb') as csvfile:
		spamwriter = csv.writer(csvfile, delimiter=',')

		for row in spamreader:
			try:
				# print(row)

				nameparty = row[0].split()
				if nameparty[-1] == '(i)':
					nameparty.pop()
				# print(nameparty)
				Party = nameparty.pop(0)
				# row.append(mydict[Party])
				if nameparty[0] == 'Winner':
					nameparty.pop(0)
				f = nameparty[0]
				nameparty.append(",")
				nameparty.append(f)
				nameparty.pop(0)
				row[0] = ' '.join(nameparty)
				row[3] = mydict[Party]
				row.pop()
				row.pop()
				row.pop()
				try:
					intlast = row[-1].replace(',', '')
					row[-1] = int(intlast)
				except ValueError:
					row[-1] = 1
				# try:
				row[2] = int(row[2])
				row[-2] = int(row[-2])

				row[1] = row[1].replace('-', ' ')
				Tempor = row[1].split()
				for x in range(len(Tempor)):
					Tempor[x] = Tempor[x].capitalize()

				row[1] = ' '.join(Tempor)

				# if row[-1] == 'NA':
				# 	row[-1] = 1 

				row[1] = stateabbrev[row[1]]


				print(row)

				
				spamwriter.writerow(row)

			except IndexError:
				print("index error BEGIN")
				print(row)
				print("index error END")
			# print('###'.join(row))

