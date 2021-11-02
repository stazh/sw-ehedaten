import csv
from datetime import datetime
from datetime import date
import sys
inFile = sys.argv[1]
input_file = csv.DictReader(open(inFile), delimiter=';')

input_file_list = list(input_file)
Zusatzinfos_Frau = {}
Zusatzinfos_Mann = {}
bandSignaturString = ""
for row in input_file_list:
	# convert it from an OrderedDict to a regular dict
	row = dict(row)
	if row['Zusatzinfo_Mann'] != "" or row['Zusatzinfo_Mann'] != "-":
		zusatzinfos_mann_in_row = row['Zusatzinfo_Mann'].split(";")
		for zm in zusatzinfos_mann_in_row:
			zm = zm.lstrip()
			if zm in Zusatzinfos_Mann:
				Zusatzinfos_Mann[zm] +=1
			else:
				Zusatzinfos_Mann[zm] = 1

	if row['Zusatzinfo_Frau'] != "" or row['Zusatzinfo_Frau'] != "-":		
		zusatzinfos_frau_in_row = row['Zusatzinfo_Frau'].split(";")
		for zf in zusatzinfos_frau_in_row:
			zf = zf.lstrip()
			if zf in Zusatzinfos_Frau:
				Zusatzinfos_Frau[zf] +=1
			else:
				Zusatzinfos_Frau[zf] = 1


with open('zusatzinfos_mann.csv', 'w') as zm:
    writerZm = csv.writer(zm)
    writerZm.writerow(["Info", "Anzahl"])
    for zim in Zusatzinfos_Mann:
    	writerZm.writerow([zim,Zusatzinfos_Mann[zim]])

with open('zusatzinfos_frau.csv', 'w') as zf:
    writerZf = csv.writer(zf)
    writerZf.writerow(["Info", "Anzahl"])
    for zif in Zusatzinfos_Frau:
    	writerZf.writerow([zif,Zusatzinfos_Frau[zif]])