import csv
from datetime import datetime
from datetime import date
input_file = csv.DictReader(open("Ehedaten_konvertiert_2.csv"), delimiter=',')
output_file = open('Ehedaten_konvertiert_3.csv', 'w', newline='')
dict_writer = csv.DictWriter(output_file,fieldnames=input_file.fieldnames)
dict_writer.writeheader()
input_file_list = list(input_file)
for row in input_file_list:
	# convert it from an OrderedDict to a regular dict
	row = dict(row)
	if row['Anzahl-Ehen'] == '':
		dict_writer.writerow(row)
	else:
		row['Marriage ID'] = row['Anzahl-Ehen']
		dict_writer.writerow(row)
