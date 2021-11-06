import csv
from datetime import datetime
from datetime import date
import sys
inFile = sys.argv[1]
input_file = csv.DictReader(open(inFile), delimiter=';')
data_archiving = "https://github.com/stazh/sw-ehedaten/data/archiving#"

input_file_list = list(input_file)
herkunfst_ort_counter = 0
Herkunftsorte = {}
nachnamen_counter = 0
Nachnamen = {}
frauenvornamen_counter = 0
Frauenvornamen = {}
maennervornamen_counter = 0
Maennervornamen = {}
kirchgemeinden_counter = 0
Kirchgemeinden = {}
band_sigantur_counter = 0
Band_Signaturen = {}
for row in input_file_list:
	# convert it from an OrderedDict to a regular dict
	row = dict(row)

	if not row['Herkunft_Mann'] == "" and not row['Herkunft_Mann'] in Herkunftsorte:
		herkunfst_ort_counter += 1
		herkunfst_ort_counter_str = str(herkunfst_ort_counter)
		while len(herkunfst_ort_counter_str) < 5:
  			herkunfst_ort_counter_str = '0' + herkunfst_ort_counter_str
		Herkunftsorte[row['Herkunft_Mann']] = data_archiving + 'PlaceName_' + herkunfst_ort_counter_str
	
	if not row['Herkunft_Frau'] == "" and not row['Herkunft_Frau'] in Herkunftsorte:
		herkunfst_ort_counter += 1
		herkunfst_ort_counter_str = str(herkunfst_ort_counter)
		while len(herkunfst_ort_counter_str) < 5:
  			herkunfst_ort_counter_str = '0' + herkunfst_ort_counter_str
		Herkunftsorte[row['Herkunft_Frau']] = data_archiving + 'PlaceName_' + herkunfst_ort_counter_str

	if not row['Nachname_Mann'] == "" and not row['Nachname_Mann'] in Nachnamen:
		nachnamen_counter += 1
		nachnamen_counter_str = str(nachnamen_counter)
		while len(nachnamen_counter_str) < 5:
  			nachnamen_counter_str = '0' + nachnamen_counter_str
		Nachnamen[row['Nachname_Mann']] = data_archiving + 'FamilyName_' + nachnamen_counter_str

	if not row['Nachname_Frau'] == "" and not row['Nachname_Frau'] in Nachnamen:
		nachnamen_counter += 1
		nachnamen_counter_str = str(nachnamen_counter)
		while len(nachnamen_counter_str) < 5:
  			nachnamen_counter_str = '0' + nachnamen_counter_str
		Nachnamen[row['Nachname_Frau']] = data_archiving + 'FamilyName_' + nachnamen_counter_str
		
	if not row['Vorname_Frau'] == "" and not row['Vorname_Frau'] in Frauenvornamen:
		frauenvornamen_counter += 1
		frauenvornamen_counter_str = str(frauenvornamen_counter)
		while len(frauenvornamen_counter_str) < 5:
  			frauenvornamen_counter_str= '0' + frauenvornamen_counter_str
		Frauenvornamen[row['Vorname_Frau']] = data_archiving + 'FirstNameWoman_' + frauenvornamen_counter_str
	
	if not row['Vorname_Mann'] == "" and not row['Vorname_Mann'] in Maennervornamen:
		maennervornamen_counter += 1
		maennervornamen_counter_str = str(maennervornamen_counter)
		while len(maennervornamen_counter_str) < 5:
  			maennervornamen_counter_str = '0' + maennervornamen_counter_str
		Maennervornamen[row['Vorname_Mann']] = data_archiving + 'FirstNameMan_' + maennervornamen_counter_str
	
	if not row['Kirchgemeinde'] == "" and not row['Kirchgemeinde'] in Kirchgemeinden:
		kirchgemeinden_counter += 1
		kirchgemeinden_counter_str = str(kirchgemeinden_counter)
		while len(kirchgemeinden_counter_str) < 5:
  			kirchgemeinden_counter_str = '0' + kirchgemeinden_counter_str
		Kirchgemeinden[row['Kirchgemeinde']] = data_archiving + 'Parish_' + kirchgemeinden_counter_str

	k = row['Signatur'].rfind(",")
	bandSignaturString = row['Signatur'][:k]
	if  not bandSignaturString in Band_Signaturen:
		band_sigantur_counter += 1
		band_sigantur_counter_str = str(band_sigantur_counter)
		while len(band_sigantur_counter_str) < 5:
  			band_sigantur_counter_str = '0' + band_sigantur_counter_str
		Band_Signaturen[bandSignaturString] = data_archiving + 'VolumeIdentifier_' + band_sigantur_counter_str

	
with open('kirchgemeinden.csv', 'w', newline='') as fk:
    writerk = csv.writer(fk)
    writerk.writerow(["Kirchgemeinde", "URI"])
    for kk in Kirchgemeinden:
   	 	writerk.writerow([kk, Kirchgemeinden[kk]])
   	 	
with open('herkunftsorte.csv', 'w', newline='') as fh:
    writerh = csv.writer(fh)
    writerh.writerow(["Herkunftsort", "URI"])
    for kh in Herkunftsorte:
   	 	writerh.writerow([kh, Herkunftsorte[kh]])

with open('Nachnamen.csv', 'w', newline='') as fn:
    writern = csv.writer(fn)
    writern.writerow(["Nachname", "URI"])
    for kn in Nachnamen:
   	 	writern.writerow([kn, Nachnamen[kn]])
   	 	
with open('Frauenvornamen.csv', 'w', newline='') as ff:
    writerf = csv.writer(ff)
    writerf.writerow(["Frauenvorname", "URI"])
    for kf in Frauenvornamen:
   	 	writerf.writerow([kf, Frauenvornamen[kf]])

with open('Maennervornamen.csv', 'w', newline='') as fm:
    writerm = csv.writer(fm)
    writerm.writerow(["Männervorname", "URI"])
    for km in Maennervornamen:
   	 	writerm.writerow([km, Maennervornamen[km]])

with open('Bandsignaturen.csv', 'w', newline='') as bs:
    writerb = csv.writer(bs)
    writerb.writerow(["Bandsignatur", "URI"])
    for kbs in Band_Signaturen:
   	 	writerb.writerow([kbs, Band_Signaturen[kbs]])

