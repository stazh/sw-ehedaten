#!/usr/bin/python
#-*- coding:utf-8 -*-
import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD
import sys

inFile = sys.argv[1]
input_file = csv.DictReader(open(inFile), delimiter=';')

inFileBaende = sys.argv[2]
input_file_baende = csv.DictReader(open(inFileBaende), delimiter=';')

ontology_archiving = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#")
ontology_date = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#")
ontology_organisation = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/ontology/organisation#")
ontology_place = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/ontology/place#")
ontology_person = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/ontology/person#")
ontology_marriage = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#")
data = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/data#")

#Erstelle Kirchgemeinden-Dictionary aus kirchgemeinden.csv (erstellt durch create_dictionaries.py-Skript)

kirchgemeinden = csv.DictReader(open('kirchgemeinden.csv'), delimiter=',')
kirchgemeinden_dict = {}
for row in kirchgemeinden:
	kirchgemeinden_dict[row['Kirchgemeinde']] = row['URI']

nachnamen = csv.DictReader(open('Nachnamen.csv'), delimiter=',')
nachnamen_dict = {}
for row in nachnamen:
	nachnamen_dict[row['Nachname']] = row['URI']

frauenvornamen = csv.DictReader(open('Frauenvornamen.csv'), delimiter=',')
frauenvornamen_dict = {}
for row in frauenvornamen:
	frauenvornamen_dict[row['Frauenvorname']] = row['URI']

maennervornamen = csv.DictReader(open('Maennervornamen.csv'), delimiter=',')
maennervornamen_dict = {}
for row in maennervornamen:
	maennervornamen_dict[row['Männervorname']] = row['URI']

eheeintraege_von_bis = csv.DictReader(open('Ehedaten_von_bis.csv'), delimiter=';')
eheeintraege_von_bis_dict = {}
for row in eheeintraege_von_bis:
	eheeintraege_von_bis_dict[row['ID']] = {'Entstehungszeitraum_von':row['Entstehungszeitraum_von'],'Entstehungszeitraum_bis':row['Entstehungszeitraum_bis']}

herkunftsorte = csv.DictReader(open('herkunftsorte.csv'), delimiter=',')
orte_dict = {}
for row in herkunftsorte:
	orte_dict[row['Herkunftsort']] = row['URI']
for entry in kirchgemeinden_dict:
	if not entry in orte_dict:
		if entry == "Fraumünster" or entry == "Grossmünster" or entry == "St. Peter" or entry == "Predigern" or entry == "Spitalpfarramt":
			pass
		else:
			orte_dict[entry] = 'https://github.com/stazh/sw-ehedaten/tree/main/data#PlaceName_' + entry.replace('ü','ue')
			print(orte_dict[entry])


band_signaturen = csv.DictReader(open('Bandsignaturen.csv'), delimiter=',')
band_dict = {}
counter = 0
for row in band_signaturen:
	input_file_baende = csv.DictReader(open(inFileBaende), delimiter=';')
	for rowb in input_file_baende:
		if row['Bandsignatur'] == rowb['Signatur']:
			band_dict[row['Bandsignatur']] = {
			'URI':row['URI'],
			'Entstehungszeitraum':rowb['Entstehungszeitraum'],
			'Entstehungszeitraum_Von':rowb['Entstehungszeitraum_Von'],
			'Entstehungszeitraum_Bis':rowb['Entstehungszeitraum_Bis'],
			'Titel':rowb['Titel'],
			'Inhalt_und_Form':rowb['Inhalt_und_Form'],
			'Provenienz':rowb['Provenienz'],
			'Weblink_Digitalisat':rowb['Weblink_Digitalisat'],
			'ID':rowb['ID'],
			'Weblink_AIS':rowb['Weblink_AIS']
			}

output_graph = Graph()
output_graph.bind('archiving', ontology_archiving)
output_graph.bind('date', ontology_date)
output_graph.bind('organisation', ontology_organisation)
output_graph.bind('person', ontology_person)
output_graph.bind('place', ontology_place)
output_graph.bind('marriage', ontology_marriage)
output_graph.bind('data', data)
counter = 0
record_dict = {}
for entry in orte_dict:
	output_graph.add((URIRef(orte_dict[entry]), RDF.type, ontology_place.Place))	
	output_graph.add((URIRef(orte_dict[entry]), RDFS.label, Literal(entry, lang='de')))
	output_graph.add((URIRef(orte_dict[entry]), ontology_place.placeHasNameLiteral, Literal(entry, lang='de')))

for entry in band_dict:
	counter+=1
	counter_str = str(counter)
	while len(counter_str) < 5:
		counter_str  = '0' + counter_str 
	recordURI = "https://github.com/stazh/sw-ehedaten/tree/main/data#Record_" + counter_str
	record_dict[entry] = recordURI
	volumeURI = band_dict[entry]['URI']
	output_graph.add((URIRef(recordURI.replace('Record','ParishBook')), RDF.type, ontology_marriage.ParishBook))
	output_graph.add((URIRef(recordURI), ontology_archiving.recordRepresents, URIRef(recordURI.replace('Record','ParishBook'))))
	output_graph.add((URIRef(recordURI.replace('Record','ParishBook')), ontology_marriage.parishBookIsKeptByParish, URIRef(kirchgemeinden_dict[band_dict[entry]['Provenienz'].replace('Kirchgemeinde ','')])))
	
for entry in kirchgemeinden_dict:
	output_graph.add((URIRef(kirchgemeinden_dict[entry]),RDF.type,ontology_organisation.Parish))
	output_graph.add((URIRef(kirchgemeinden_dict[entry]),ontology_organisation.parishHasNameLiteral, Literal("Kirchgemeinde " + entry)))
	if entry == "Grossmünster" or entry == "St. Peter" or entry == "Fraumünster" or entry == "Predigern" or entry == "Spitalpfarramt":		
		output_graph.add((URIRef(kirchgemeinden_dict[entry]),ontology_organisation.parishHasSeatAtPlace, URIRef(orte_dict['Zürich'])))
	else:
		output_graph.add((URIRef(kirchgemeinden_dict[entry]),ontology_organisation.parishHasSeatAtPlace, URIRef(orte_dict[entry])))


fileName = 'data_triples_basic_parish' + '.ttl'
output_graph.serialize(destination=fileName, format='turtle')
print(fileName)

output_graph = Graph()
output_graph.bind('archiving', ontology_archiving)
output_graph.bind('date', ontology_date)
output_graph.bind('organisation', ontology_organisation)
output_graph.bind('person', ontology_person)
output_graph.bind('place', ontology_place)
output_graph.bind('marriage', ontology_marriage)
output_graph.bind('data', data)

rowCounter = 0
fileCounter = 0
for row in input_file:

	row = dict(row)
	rowCounter += 1

	if row['Signatur'] != "":
		
		rowCountString = str(rowCounter)
		while len(rowCountString) < 6:
			rowCountString = '0' + rowCountString

		k = row['Signatur'].rfind(",")
		band_signatur_string = row['Signatur'][:k]
		volumeURI = band_dict[band_signatur_string]['URI']
		recordURI = record_dict[band_signatur_string]
		RecordPartURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#RecordPart_' + rowCountString
		MarriageEntryURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#MarriageEntry_' + rowCountString
		ManURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#Man_' + rowCountString
		WomanURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#Woman_' + rowCountString
		DatingURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#Dating_' + rowCountString
		ManifestationOfRecordPartURI = "https://github.com/stazh/sw-ehedaten/tree/main/data#ManifestationOfRecordPart_"+ rowCountString

		output_graph.add((URIRef(MarriageEntryURI), RDF.type, ontology_marriage.MarriageEntry))
		output_graph.add((URIRef(RecordPartURI), ontology_archiving.recordPartRepresents, URIRef(MarriageEntryURI)))
		output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryIsInParishBook, URIRef(recordURI.replace('Record','ParishBook'))))

		output_graph.add((URIRef(ManURI), RDF.type, ontology_person.Man))
		output_graph.add((URIRef(WomanURI), RDF.type, ontology_person.Woman))
		output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryRegistersWoman, URIRef(WomanURI)))
		output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryRegistersMan, URIRef(ManURI)))
		output_graph.add((URIRef(ManURI), ontology_person.personHasFirstNameLiteral, Literal(row['Vorname_Mann'])))
		output_graph.add((URIRef(WomanURI), ontology_person.personHasFirstNameLiteral, Literal(row['Vorname_Frau'])))
		output_graph.add((URIRef(ManURI), ontology_person.personHasLastNameLiteral, Literal(row['Nachname_Mann'])))
		output_graph.add((URIRef(WomanURI), ontology_person.personHasLastNameLiteral, Literal(row['Nachname_Frau'])))
		if row['Herkunft_Mann'] != "":
			item = row['Herkunft_Mann']
			item = item.replace(' ?','')
			item = item.replace(' (?)','')
			item = item.replace('?','')
			output_graph.add((URIRef(ManURI), ontology_person.personHasPlaceOfOrigin, URIRef(orte_dict[item])))
		if row['Herkunft_Frau'] != "":
			item = row['Herkunft_Frau']
			item = item.replace(' ?','')
			item = item.replace(' (?)','')
			item = item.replace('?','')
			output_graph.add((URIRef(WomanURI), ontology_person.personHasPlaceOfOrigin, URIRef(orte_dict[item])))
		
		#HIER WEITER UND ÜBERPRÜFEN OB NICHTS VERGESSEN AUS ARCHIVING
		if eheeintraege_von_bis_dict[row['ID']]['Entstehungszeitraum_von'] == eheeintraege_von_bis_dict[row['ID']]['Entstehungszeitraum_bis']:
			output_graph.add((URIRef(DatingURI), RDF.type, ontology_date.Date))
			output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryHasDatingOnDate, URIRef(DatingURI)))			
			date_list = eheeintraege_von_bis_dict[row['ID']]['Entstehungszeitraum_von'].split(".")
			if int(date_list[2]) < 1700:
				output_graph.add((URIRef(DatingURI), ontology_date.julianDating, Literal(date_list[2] + "-"+ date_list[1] + "-"+ date_list[0],datatype=XSD.date)))
			else:
				output_graph.add((URIRef(DatingURI), ontology_date.gregorianDating, Literal(date_list[2] + "-"+ date_list[1] + "-"+ date_list[0],datatype=XSD.date)))
		else:	
			output_graph.add((URIRef(DatingURI), RDF.type, ontology_date.DatePeriod))
			output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryHasDatingWithinDatePeriod, URIRef(DatingURI)))
			date_start_list = eheeintraege_von_bis_dict[row['ID']]['Entstehungszeitraum_von'].split(".")
			date_end_list = eheeintraege_von_bis_dict[row['ID']]['Entstehungszeitraum_bis'].split(".")
			if int(date_start_list[2]) < 1700:
				output_graph.add((URIRef(DatingURI), ontology_date.julianStartDating, Literal(date_start_list[2] + "-"+ date_start_list[1] + "-"+ date_start_list[0],datatype=XSD.date)))
			else:
				output_graph.add((URIRef(DatingURI), ontology_date.gregorianStartDating, Literal(date_start_list[2] + "-"+ date_start_list[1] + "-"+ date_start_list[0],datatype=XSD.date)))
			if int(date_end_list[2]) < 1700:
				output_graph.add((URIRef(DatingURI), ontology_date.julianEndDating, Literal(date_end_list[2] + "-"+ date_end_list[1] + "-"+ date_end_list[0],datatype=XSD.date)))
			else:
				output_graph.add((URIRef(DatingURI), ontology_date.gregorianEndDating, Literal(date_end_list[2] + "-"+ date_end_list[1] + "-"+ date_end_list[0],datatype=XSD.date)))

	if rowCounter % 7000 == 0:
		fileCounter += 1
		fileName = 'data_triples_' + str(fileCounter) + '.ttl'
		output_graph.serialize(destination=fileName, format='turtle')
		output_graph = Graph()
		output_graph.bind('archiving', ontology_archiving)
		output_graph.bind('date', ontology_date)
		output_graph.bind('organisation', ontology_organisation)
		output_graph.bind('person', ontology_person)
		output_graph.bind('place', ontology_place)
		output_graph.bind('marriage', ontology_marriage)
		output_graph.bind('data', data)
		print(fileName)

fileCounter += 1
fileName = 'data_triples_' + str(fileCounter) + '.ttl'
output_graph.serialize(destination=fileName, format='turtle')
print(fileName)
