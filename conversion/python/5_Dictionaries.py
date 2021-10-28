import csv
from datetime import datetime
from datetime import date
input_file = csv.DictReader(open("Ehedaten_V4.csv"), delimiter=',')
#output_file = open('Ehedaten_konvertiert_4.csv', 'w', newline='')
#dict_writer = csv.DictWriter(output_file,fieldnames=input_file.fieldnames)
#dict_writer.writeheader()
input_file_list = list(input_file)
Herkunftsorte = {}
Nachnamen = {}
Frauenvornamen = {}
Maennervornamen = {}
Kirchgemeinden = {}
for row in input_file_list:
	# convert it from an OrderedDict to a regular dict
	row = dict(row)
	
	if row['Herkunft Mann'] in Herkunftsorte:
		Herkunftsorte[row['Herkunft Mann']] +=1
	else:
		Herkunftsorte[row['Herkunft Mann']] = 1
	
	if row['Herkunft Frau'] in Herkunftsorte:
		Herkunftsorte[row['Herkunft Frau']] +=1
	else:
		Herkunftsorte[row['Herkunft Frau']] = 1

	if row['Nachname Mann'] in Nachnamen:
		Nachnamen[row['Nachname Mann']] +=1
	else:
		Nachnamen[row['Nachname Mann']] = 1
	
	if row['Nachname Frau'] in Nachnamen:
		Nachnamen[row['Nachname Frau']] +=1
	else:
		Nachnamen[row['Nachname Frau']] = 1
		
	if row['Vorname Frau'] in Frauenvornamen:
		Frauenvornamen[row['Vorname Frau']] +=1
	else:
		Frauenvornamen[row['Vorname Frau']] = 1
	
	if row['Vorname Mann'] in Maennervornamen:
		Maennervornamen[row['Vorname Mann']] +=1
	else:
		Maennervornamen[row['Vorname Mann']] = 1
	
	if row['Kirchgemeinde'] in Kirchgemeinden:
		Kirchgemeinden[row['Kirchgemeinde']] +=1
	else:
		Kirchgemeinden[row['Kirchgemeinde']] = 1

print(Kirchgemeinden)
print(Herkunftsorte)

	
with open('kirchgemeinden.csv', 'w', newline='') as fk:
    writerk = csv.writer(fk)
    writerk.writerow(["Kirchgemeinde", "Anzahl"])
    for kk in Kirchgemeinden:
   	 	writerk.writerow([kk, Kirchgemeinden[kk]])
   	 	
with open('herkunftsorte.csv', 'w', newline='') as fh:
    writerh = csv.writer(fh)
    writerh.writerow(["Herkunftsort", "Anzahl"])
    for kh in Herkunftsorte:
   	 	writerh.writerow([kh, Herkunftsorte[kh]])

with open('Nachnamen.csv', 'w', newline='') as fn:
    writern = csv.writer(fn)
    writern.writerow(["Nachname", "Anzahl"])
    for kn in Nachnamen:
   	 	writern.writerow([kn, Nachnamen[kn]])
   	 	
with open('Frauenvornamen.csv', 'w', newline='') as ff:
    writerf = csv.writer(ff)
    writerf.writerow(["Frauenvorname", "Anzahl"])
    for kf in Frauenvornamen:
   	 	writerf.writerow([kf, Frauenvornamen[kf]])

with open('Maennervornamen.csv', 'w', newline='') as fm:
    writerm = csv.writer(fm)
    writerm.writerow(["Männervorname", "Anzahl"])
    for km in Maennervornamen:
   	 	writerm.writerow([km, Maennervornamen[km]])

