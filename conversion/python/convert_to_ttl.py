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
data = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/data/")

#Erstelle Kirchgemeinden-Dictionary aus kirchgemeinden.csv (erstellt durch create_dictionaries.py-Skript)

kirchgemeinden = csv.DictReader(open('kirchgemeinden.csv'), delimiter=',')
kirchgemeinden_dict = {}
for row in kirchgemeinden:
	kirchgemeinden_dict[row['Kirchgemeinde']] = row['URI']

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
for entry in band_dict:
	counter+=1
	counter_str = str(counter)
	while len(counter_str) < 5:
		counter_str  = '0' + counter_str 
	recordURI = "https://github.com/stazh/sw-ehedaten/tree/main/data/Record_" + counter_str
	record_dict[entry] = recordURI
	volumeURI = band_dict[entry]['URI']
	output_graph.add((URIRef(recordURI), RDF.type, ontology_archiving.Record))	
	output_graph.add((URIRef(volumeURI), RDF.type, ontology_archiving.Volume))

	output_graph.add((URIRef(volumeURI), ontology_archiving.manifestationIsIdentifiedByIdentifierLiteral, Literal(entry)))
	if band_dict[entry]['Weblink_Digitalisat'] != "":
		output_graph.add((URIRef(volumeURI.replace('Volume','DigitalCopy')), RDF.type, ontology_archiving.DigitalCopy))
		output_graph.add((URIRef(volumeURI.replace('Volume','DigitalCopy')), ontology_archiving.digitalCopyHasWebpageURI, Literal(band_dict[entry]['Weblink_Digitalisat'], datatype=XSD.anyURI)))
		output_graph.add((URIRef(recordURI), ontology_archiving.recordHasManifestation, URIRef(volumeURI.replace('Volume','DigitalCopy'))))
	output_graph.add((URIRef(recordURI), ontology_archiving.recordHasManifestation, URIRef(volumeURI)))
	output_graph.add((URIRef(recordURI), ontology_archiving.recordIsIdentifiedByIdentifierLiteral, Literal(band_dict[entry]['ID'])))
	output_graph.add((URIRef(recordURI), ontology_archiving.recordHasProvenance, URIRef(kirchgemeinden_dict[band_dict[entry]['Provenienz'].replace('Kirchgemeinde ','')])))
	if band_dict[entry]['Inhalt_und_Form'] != "":
		output_graph.add((URIRef(recordURI), ontology_archiving.recordHasAdditionalContentLiteral, Literal(band_dict[entry]['Inhalt_und_Form'].replace('\\n','\n'))))
	output_graph.add((URIRef(recordURI), ontology_archiving.recordHasTitleLiteral, Literal(band_dict[entry]['Titel'])))
	output_graph.add((URIRef(recordURI), ontology_archiving.recordHasdateOfOriginLiteral, Literal(band_dict[entry]['Entstehungszeitraum'])))	
	output_graph.add((URIRef(recordURI), ontology_archiving.recordHasWebpageURI, Literal(band_dict[entry]['Weblink_AIS'], datatype=XSD.anyURI)))
	output_graph.add((URIRef(recordURI.replace('Record','ParishBook')), RDF.type, ontology_marriage.ParishBook))
	output_graph.add((URIRef(recordURI), ontology_archiving.recordRepresents, URIRef(recordURI.replace('Record','ParishBook'))))
	
	#über Regel dynamisch?
	#output_graph.add((URIRef(band_dict[entry]), RDF.type, ontology_archiving.Identifier))
	#output_graph.add((URIRef(volumeURI), ontology_archiving.manifestationIsIdentifiedByIdentifier, URIRef(band_dict[entry])))				
	#output_graph.add((URIRef(band_dict[entry]), ontology_archiving.identifierHasLiteral, Literal(entry)))
for entry in kirchgemeinden_dict:
	output_graph.add((URIRef(kirchgemeinden_dict[entry]),RDF.type,ontology_organisation.Parish))
	output_graph.add((URIRef(kirchgemeinden_dict[entry]),ontology_organisation.parishHasNameLiteral, Literal("Kirchgemeinde " + entry)))


output_graph.add((data.stazh, RDF.type, ontology_archiving.Archive))
output_graph.add((data.stazh, ontology_archiving.archiveHasNameLiteral, Literal("Staatsarchiv des Kantons Zürich")))

fileName = 'data_triples_record_volume_parish' + '.ttl'
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
		RecordPartURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data/archiving#RecordPart_' + rowCountString
		ManifestationOfRecordPartURI = "https://github.com/stazh/sw-ehedaten/tree/main/data/archiving#ManifestationOfRecordPart_"+ rowCountString

		output_graph.add((URIRef(RecordPartURI), RDF.type, ontology_archiving.RecordPart))
		output_graph.add((URIRef(recordURI), ontology_archiving.recordHasRecordPart, URIRef(RecordPartURI)))
		output_graph.add((URIRef(ManifestationOfRecordPartURI), RDF.type, ontology_archiving.Manifestation))
		output_graph.add((URIRef(RecordPartURI),ontology_archiving.recordPartHasManifestation, URIRef(ManifestationOfRecordPartURI)))
		output_graph.add((URIRef(ManifestationOfRecordPartURI),ontology_archiving.manifestationIsIdentifiedByIdentifierLiteral, Literal(row['Signatur'])))
		if row['Band'] != "":
			output_graph.add((URIRef(RecordPartURI),ontology_archiving.recordPartHasReferenceLiteral, Literal(row['Band'])))
		output_graph.add((URIRef(RecordPartURI),ontology_archiving.recordPartIsIdentifiedByIdentifierLiteral, Literal(row['ID'])))
		output_graph.add((URIRef(RecordPartURI),ontology_archiving.recordPartHasProvenance, URIRef(kirchgemeinden_dict[row['Kirchgemeinde']])))

		title_string = row['Nachname_Mann'] + ", " + row['Vorname_Mann']
		if row['Herkunft_Mann'] != "":
			title_string = title_string + ", " + row['Herkunft_Mann']
		title_string = title_string + ", getraut mit " + row['Nachname_Frau'] + ", " + row['Vorname_Frau']
		if row['Herkunft_Frau'] != "":
			title_string = title_string + ", " + row['Herkunft_Frau']
		additional_content_string = ""
		if row['Zusatzinfo_Mann'] != "" and row['Zusatzinfo_Mann'] != "-":
			additional_content_string = "Zusatzinformation Mann: "+row['Zusatzinfo_Mann']
			output_graph.add((URIRef(RecordPartURI), ontology_archiving.recordPartHasAdditionalContentLiteral, Literal(additional_content_string))) 
		if row['Zusatzinfo_Frau'] != "" and row['Zusatzinfo_Frau'] != "-":
			additional_content_string = "Zusatzinformation Frau: "+row['Zusatzinfo_Frau']
			output_graph.add((URIRef(RecordPartURI), ontology_archiving.recordPartHasAdditionalContentLiteral, Literal(additional_content_string))) 

		output_graph.add((URIRef(RecordPartURI), ontology_archiving.recordPartHasTitleLiteral, Literal(title_string)))
		output_graph.add((URIRef(RecordPartURI), ontology_archiving.recordPartHasdateOfOriginLiteral, Literal(row['Datum'])))	
		output_graph.add((URIRef(RecordPartURI), ontology_archiving.recordPartHasWebpageURI, Literal(row['Webseite'], datatype=XSD.anyURI)))
	
	if rowCounter % 10000 == 0:
		fileCounter += 1
		fileName = 'triples_archiving_' + str(fileCounter) + '.ttl'
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

