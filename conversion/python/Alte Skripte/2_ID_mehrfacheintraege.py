import csv
from datetime import datetime
from datetime import date
input_file = csv.DictReader(open("Ehedaten_erweitert_4.csv"), delimiter=';')
output_file = open('Ehedaten_konvertiert_2.csv', 'w', newline='')
dict_writer = csv.DictWriter(output_file,fieldnames=input_file.fieldnames)
dict_writer.writeheader()
input_file_list = list(input_file)
rowCounter = 0
for row in input_file_list:
	# convert it from an OrderedDict to a regular dict
	row = dict(row)
	dateISO = ""
	if row['Datum Range zwischen'] != "ja":
		dateISO = row['DatumJahr'] + "-" + row['DatumMonat'] + "-" + row['DatumTag']
	else:
		dateISO = row['StartdatumJahr'] + "-" + row['StartdatumMonat'] + "-" + row['StartdatumTag']
		print("ja")
	if len(dateISO) == 10:
		datum = date.fromisoformat(dateISO)
		rowCounterTemp = rowCounter - 1
		dateISODif = 0
		marID = ''
		while dateISODif <= 10 and rowCounterTemp >= 0:
			dateISOComp = input_file_list[rowCounterTemp]['Datum'].replace(".","-")
			if len(dateISOComp) == 10:
				datumComp = date.fromisoformat(dateISOComp)
				dateISODif = datum - datumComp
				dateISODif = dateISODif.days
				if (input_file_list[rowCounterTemp]['Nachname Mann'] == row['Nachname Mann']) and (input_file_list[rowCounterTemp]['Nachname Frau'] == row['Nachname Frau']):
					marID = input_file_list[rowCounterTemp]['Marriage ID']
					print(marID)
			rowCounterTemp -= 1
		row['Anzahl-Ehen'] = marID
		dict_writer.writerow(row)
	else:
		row['Anzahl-Ehen'] = ''
		dict_writer.writerow(row)
	rowCounter += 1