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

def insert_item_in_dict(item, dictionary,item_counter,placeHolder):
	item = item.replace(' ?','')
	item = item.replace(' (?)','')
	item = item.replace('?','')
	if not item == "" and not item in dictionary:
		item_counter += 1
		item_counter_str = str(item_counter)
		while len(item_counter_str) < 5:
  			item_counter_str = '0' + item_counter_str
		dictionary[item] = data_archiving + placeHolder + item_counter_str
	return dictionary, item_counter

for row in input_file_list:
	row = dict(row)
	Herkunftsorte, herkunfts_ort_counter = insert_item_in_dict(row['Herkunft_Mann'], Herkunftsorte, herkunfst_ort_counter, 'PlaceName_')
	Herkunftsorte, herkunfts_ort_counter = insert_item_in_dict(row['Herkunft_Frau'], Herkunftsorte, herkunfst_ort_counter, 'PlaceName_')
	Nachnamen, nachnamen_counter = insert_item_in_dict(row['Nachname_Mann'], Nachnamen, nachnamen_counter, 'FamilyName_')
	Nachnamen, nachnamen_counter = insert_item_in_dict(row['Nachname_Frau'], Nachnamen, nachnamen_counter, 'FamilyName_')
	Frauenvornamen, frauenvornamen_counter = insert_item_in_dict(row['Vorname_Frau'], Frauenvornamen, frauenvornamen_counter, 'FirstNameWoman_')
	Maennervornamen, maennervornamen_counter = insert_item_in_dict(row['Vorname_Mann'], Maennervornamen, maennervornamen_counter, 'FirstNameMan_')	
	Kirchgemeinden, kirchgemeinden_counter = insert_item_in_dict(row['Kirchgemeinde'], Kirchgemeinden, kirchgemeinden_counter, 'Parish_')	
	k = row['Signatur'].rfind(",")
	bandSignaturString = row['Signatur'][:k]
	Band_Signaturen, band_sigantur_counter = insert_item_in_dict(bandSignaturString, Band_Signaturen, band_sigantur_counter, 'Volume_')	
	
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

