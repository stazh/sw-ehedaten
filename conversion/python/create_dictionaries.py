import csv
from datetime import datetime
from datetime import date
import sys

inFile = sys.argv[1]
input_file = csv.DictReader(open(inFile), delimiter=';')
data_prefix = "https://github.com/stazh/sw-ehedaten/tree/main/data#"

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

def insert_item_in_dict_by_counter(item, dictionary,item_counter,placeHolder):
	item = item.replace(' ?','')
	item = item.replace(' (?)','')
	item = item.replace('?','')
	if not item == "" and not item in dictionary:
		item_counter += 1
		item_counter_str = str(item_counter)
		while len(item_counter_str) < 5:
  			item_counter_str = '0' + item_counter_str
		dictionary[item] = data_prefix + placeHolder + item_counter_str
	return dictionary, item_counter

def insert_item_in_dict_by_name(item, dictionary,placeHolder):
	item = item.replace(' ?','')
	item = item.replace(' (?)','')
	item = item.replace('?','')
	item_name = item.replace(' ','_')
	item_name = item_name.replace('(','')
	item_name = item_name.replace(')','')
	item_name = item_name.replace('.','')
	item_name = item_name.replace('"','')
	item_name = item_name.replace('ä','ae')
	item_name = item_name.replace('ö','oe')
	item_name = item_name.replace('ü','ue')
	item_name = item_name.replace('Ä','Ae')
	item_name = item_name.replace('Ö','Oe')
	item_name = item_name.replace('Ü','Ue')
	item_name = item_name.replace('é','e')
	if not item == "" and not item in dictionary:
		dictionary[item] = data_prefix + placeHolder + item_name
	return dictionary

for row in input_file_list:
	row = dict(row)
	Herkunftsorte = insert_item_in_dict_by_name(row['Herkunft_Mann'], Herkunftsorte, 'PlaceName_')
	Herkunftsorte = insert_item_in_dict_by_name(row['Herkunft_Frau'], Herkunftsorte, 'PlaceName_')
	Nachnamen = insert_item_in_dict_by_name(row['Nachname_Mann'], Nachnamen, 'FamilyName_')
	Nachnamen = insert_item_in_dict_by_name(row['Nachname_Frau'], Nachnamen,  'FamilyName_')
	Frauenvornamen = insert_item_in_dict_by_name(row['Vorname_Frau'], Frauenvornamen, 'FirstNameWoman_')
	Maennervornamen = insert_item_in_dict_by_name(row['Vorname_Mann'], Maennervornamen, 'FirstNameMan_')	
	Kirchgemeinden = insert_item_in_dict_by_name(row['Kirchgemeinde'], Kirchgemeinden, 'Parish_')	
	
	k = row['Signatur'].rfind(",")
	bandSignaturString = row['Signatur'][:k]
	Band_Signaturen, band_sigantur_counter = insert_item_in_dict_by_counter(bandSignaturString, Band_Signaturen, band_sigantur_counter, 'Volume_')	
	
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

