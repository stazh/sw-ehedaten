import csv
from datetime import datetime
from datetime import date
import math

class EdbEnrichment():

	def __init__(self):
		self.main()
		return

	def main(self):
		input_file = csv.DictReader(open("EDB_16_18_Jh_Stand_2021_04_13_2.csv"), delimiter=';')
		output_file = open('Ehedaten_erweitert.csv', 'w', newline='')
		fieldnames = ['Startdatum Jahr','Startdatum Monat', 'Startdatum Tag','Signatur','Nachname Mann','Vorname Mann','Herkunft Mann','Nachname Frau','Vorname Frau','Herkunft Frau','Zusatzinformation Mann','Zusatzinformation Frau','Datum AIS','Datumrange','Startdatum','Startdatum unsicher','Enddatum','Enddatum unsicher','Startdatum Wochentag','Enddatum Jahr','Enddatum Monat', 'Enddatum Tag','Enddatum Wochentag','Kalender','Kirchgemeinde','Seite im Band','Webseite']
		dict_writer = csv.DictWriter(output_file,fieldnames=fieldnames)
		dict_writer.writeheader()
		input_file_list = list(input_file)

		for row in input_file_list:

			row = dict(row)

			if '-' in row['Datum']:
				datumRange = 'y'
				datumArr = row['Datum'].split('-')
				startdatum = datumArr[0]
				enddatum = datumArr[1]
			else:
				datumRange = 'n'
				startdatum = row['Datum']
				enddatum = row['Datum']
			
			startdatumUnsicher = self.istDatumUnsicher(startdatum)
			startdatum = startdatum.replace(' (ca.)', '')

			enddatumUnsicher = self.istDatumUnsicher(enddatum)
			enddatum = enddatum.replace(' (ca.)', '')

			startDatumJahr = ''
			startDatumMonat = ''
			startDatumTag = ''

			tempStartDatumArr = startdatum.split('.')

			if len(tempStartDatumArr) == 1:
				startDatumJahr = tempStartDatumArr[0]
			elif len(tempStartDatumArr) == 2:
				startDatumJahr = tempStartDatumArr[0]
				startDatumMonat = tempStartDatumArr[1]
			else:
				startDatumJahr = tempStartDatumArr[0]
				startDatumMonat = tempStartDatumArr[1]
				startDatumTag = tempStartDatumArr[2]

			endDatumJahr = ''
			endDatumMonat = ''
			endDatumTag = ''

			tempEndDatumArr = enddatum.split('.')

			if len(tempEndDatumArr) == 1:
				endDatumJahr = tempEndDatumArr[0]
			elif len(tempEndDatumArr) == 2:
				endDatumJahr = tempEndDatumArr[0]
				endDatumMonat = tempEndDatumArr[1]
			else:
				endDatumJahr = tempEndDatumArr[0]
				endDatumMonat = tempEndDatumArr[1]
				endDatumTag = tempEndDatumArr[2]

			if int(endDatumJahr) <= 1700:
				kalender = 'julianisch'
			else:
				kalender = 'gregorianisch'

			startWochentag = ''
			
			if len(startDatumTag) != 0:
				startWochenTag = self.getWochentag(int(startDatumJahr), int(startDatumMonat), int(startDatumTag))
			else:
				startWochenTag = ''

			endWochenTag = ''
			if len(endDatumTag) != 0:
				endWochenTag = self.getWochentag(int(endDatumJahr), int(endDatumMonat), int(endDatumTag))
			else:
				endWochenTag = ''

			#ein paar Bereinigungen...
			if 'TAI 1.708; ERKGA St. Peter IV B 39, EDB 4176' in row['\ufeffSignatur']:
				row['Herkunft Frau'] = row['Herkunft Frau'].replace('\nOberglatt SG','')
			zusatzinfoMann = row['Zusatzinformation Mann'].replace('\n','')
			zusatzinfoFrau = row['Zusatzinformation Frau'].replace('\n','')

			dict_writer.writerow({'Signatur': row['\ufeffSignatur'], 'Vorname Mann': row['Vorname Mann'], 'Nachname Mann': row['Nachname Mann'], 'Herkunft Mann': row['Herkunft Mann'],'Nachname Frau': row['Nachname Frau'],'Vorname Frau': row['Vorname Frau'],'Herkunft Frau': row['Herkunft Frau'],'Zusatzinformation Mann': zusatzinfoMann,'Zusatzinformation Frau': zusatzinfoFrau ,'Datum AIS': row['Datum'],'Datumrange': datumRange,'Startdatum': startdatum,'Startdatum unsicher': startdatumUnsicher,'Enddatum': enddatum,'Enddatum unsicher': enddatumUnsicher,'Startdatum Jahr': startDatumJahr,'Startdatum Monat': startDatumMonat, 'Startdatum Tag': startDatumTag,'Startdatum Wochentag': startWochenTag,'Enddatum Jahr': endDatumJahr,'Enddatum Monat': endDatumMonat, 'Enddatum Tag': endDatumTag,'Enddatum Wochentag': endWochenTag,'Kalender': kalender,'Kirchgemeinde': row['Kirchgemeinde'],'Seite im Band': row['Seite im Band'],'Webseite': row['Webseite']})
		output_file.close()
		
		
	def getWochentag(self,jahr,monat,tag):
		if monat > 2:
			Y = jahr
			M = monat
		else:
			Y = jahr - 1
			M = monat + 12
		D = tag
		
		if jahr <= 1700:
			B = 0
		else:
			B = 2 - math.floor(Y/100) + math.floor(Y/400)
		
		JD = math.floor(365.25*(Y+4716)) + math.floor(30.6001*(M+1)) + D + B - 1524.5

		wochentagnr = math.floor(JD + 0.5) % 7

		if wochentagnr == 0:
			wochentag = 'Montag'
		elif wochentagnr == 1:
			wochentag = 'Dienstag'
		elif wochentagnr == 2:
			wochentag = 'Mittwoch'
		elif wochentagnr == 3:
			wochentag = 'Donnerstag'
		elif wochentagnr == 4:
			wochentag = 'Freitag'
		elif wochentagnr == 5:
			wochentag = 'Samstag'
		else:
			wochentag = 'Sonntag'
		
		return wochentag
	
	def istDatumUnsicher(self, datum):
		if ' (ca.)' in datum:
			return 'y'
		else:
			return 'n'

if __name__ == '__main__':

	EE = EdbEnrichment()	



