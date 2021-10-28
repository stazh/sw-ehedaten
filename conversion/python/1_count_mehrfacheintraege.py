import csv
from datetime import datetime
from datetime import date
input_file = csv.DictReader(open("Ehedaten_erweitert_3.csv"), delimiter=';')
output_file = open('Ehedaten_konvertiert.csv', 'w', newline='')
dict_writer = csv.DictWriter(output_file,fieldnames=input_file.fieldnames)
dict_writer.writeheader()
input_file_list = list(input_file)
rowCounter = 0
for row in input_file_list:
	row = dict(row)
	dateISO = ""
	if row['Datum Range zwischen'] != "ja":
		dateISO = row['DatumJahr'] + "-" + row['DatumMonat'] + "-" + row['DatumTag']
	else:
		dateISO = row['StartdatumJahr'] + "-" + row['StartdatumMonat'] + "-" + row['StartdatumTag']
		print("ja")
	if len(dateISO) == 10:
		datum = date.fromisoformat(dateISO)
		rowCounterTemp = rowCounter + 1
		dateISODif = 0
		marCounter = 0
		while dateISODif <= 10:
			dateISOComp = input_file_list[rowCounterTemp]['Datum'].replace(".","-")
			if len(dateISOComp) == 10:
				datumComp = date.fromisoformat(dateISOComp)
				dateISODif = datum - datumComp
				dateISODif = dateISODif.days
				if (input_file_list[rowCounterTemp]['Nachname Mann'] == row['Nachname Mann']) and (input_file_list[rowCounterTemp]['Nachname Frau'] == row['Nachname Frau']):
					marCounter += 1
			rowCounterTemp += 1
		row['Marriage-ID'] = marCounter
		dict_writer.writerow(row)
	else:
		row['Marriage-ID'] = 0
		dict_writer.writerow(row)
	rowCounter += 1