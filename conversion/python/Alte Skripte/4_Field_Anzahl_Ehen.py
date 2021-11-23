import csv
from datetime import datetime
from datetime import date
input_file = csv.DictReader(open("Ehedaten_konvertiert_3.csv"), delimiter=',')
output_file = open('Ehedaten_konvertiert_4.csv', 'w', newline='')
dict_writer = csv.DictWriter(output_file,fieldnames=input_file.fieldnames)
dict_writer.writeheader()
input_file_list = list(input_file)
eheIDDict = {}
for row in input_file_list:
	# convert it from an OrderedDict to a regular dict
	row = dict(row)
	
	if row['Marriage ID'] in eheIDDict:
		eheIDDict[row['Marriage ID']] +=1
	else:
		eheIDDict[row['Marriage ID']] = 1
		
for row in input_file_list:
	# convert it from an OrderedDict to a regular dict
	row = dict(row)
	row['Anzahl Ehen'] = eheIDDict[row['Marriage ID']]
	dict_writer.writerow(row)


