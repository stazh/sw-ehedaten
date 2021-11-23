import csv
from datetime import datetime
from datetime import date
import sys
inFile = sys.argv[1]
input_file = csv.DictReader(open(inFile), delimiter=';')

input_file_list = list(input_file)
bandSignaturen = {}
bandSignaturString = ""
for row in input_file_list:
	# convert it from an OrderedDict to a regular dict
	row = dict(row)
	k = row['Signatur'].rfind(",")
	bandSignaturString = row['Kirchgemeinde'] + "#" + row['Signatur'][:k]
	if  bandSignaturString in bandSignaturen:
		bandSignaturen[bandSignaturString] +=1
	else:
		bandSignaturen[bandSignaturString] = 1

with open('band_signaturen.csv', 'w') as bs:
    writerbs = csv.writer(bs)
    writerbs.writerow(["Band-Signatur", "Anzahl"])
    for be in bandSignaturen:
    	i = be.find("#")
    	writerbs.writerow([be[:i],be[i+1:],bandSignaturen[be]])