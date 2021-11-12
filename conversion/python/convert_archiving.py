#!/usr/bin/python
#-*- coding:utf-8 -*-
import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD
import sys

inFile = sys.argv[1]
input_file = csv.DictReader(open(inFile), delimiter=';')

ontology_archiving = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#")
data_archiving = Namespace("https://github.com/stazh/sw-ehedaten/data/archiving#")

kirchgemeinden = csv.DictReader(open('kirchgemeinden.csv'), delimiter=',')
kirchgemeinden_dict = {}
for row in kirchgemeinden:
    kirchgemeinden_dict[row['Kirchgemeinde']] = row['URI']

band_signaturen = csv.DictReader(open('Bandsignaturen.csv'), delimiter=',')
band_signaturen_dict = {}
for row in band_signaturen:
    band_signaturen_dict[row['Bandsignatur']] = row['URI']

output_graph = Graph()
output_graph.bind('archiving', ontology_archiving)
output_graph.bind('archiving-data', data_archiving)
counter = 0
record_dict = {}
for entry in band_signaturen_dict:
	counter+=1
	counter_str = str(counter)
	while len(counter_str) < 5:
  		counter_str  = '0' + counter_str 
	recordURI = "https://github.com/stazh/sw-ehedaten/data/archiving#Record_" + counter_str
	record_dict[entry] = recordURI
	volumeURI = band_signaturen_dict[entry]
	output_graph.add((URIRef(recordURI), RDF.type, ontology_archiving.Record))	
	output_graph.add((URIRef(volumeURI), RDF.type, ontology_archiving.Volume))
	output_graph.add((URIRef(volumeURI), ontology_archiving.manifestationIsIdentifiedByIdentifierLiteral, Literal(entry)))
	output_graph.add((URIRef(recordURI), ontology_archiving.recordHasManifestation, URIRef(volumeURI)))
	#über Regel dynamisch?
	#output_graph.add((URIRef(band_signaturen_dict[entry]), RDF.type, ontology_archiving.Identifier))
	#output_graph.add((URIRef(volumeURI), ontology_archiving.manifestationIsIdentifiedByIdentifier, URIRef(band_signaturen_dict[entry])))				
	#output_graph.add((URIRef(band_signaturen_dict[entry]), ontology_archiving.identifierHasLiteral, Literal(entry)))
for entry in kirchgemeinden_dict:
	output_graph.add((URIRef(kirchgemeinden_dict[entry]),RDF.type,ontology_archiving.Agent))
	output_graph.add((URIRef(kirchgemeinden_dict[entry]),ontology_archiving.agentHasNameLiteral, Literal("Kirchgemeinde " + entry)))


output_graph.add((data_archiving.stazh, RDF.type, ontology_archiving.Archive))
output_graph.add((data_archiving.stazh, ontology_archiving.archiveHasNameLiteral, Literal("Staatsarchiv des Kantons Zürich")))

fileName = 'triples_archiving_records_and_agents' + '.ttl'
output_graph.serialize(destination=fileName, format='turtle')

output_graph = Graph()
output_graph.bind('archiving', ontology_archiving)
output_graph.bind('archiving-data', data_archiving)

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
		volumeURI = band_signaturen_dict[band_signatur_string]
		recordURI = record_dict[band_signatur_string]
		RecordPartURI = 'https://github.com/stazh/sw-ehedaten/data/archiving#RecordPart_' + rowCountString
		ManifestationOfRecordPartURI = "https://github.com/stazh/sw-ehedaten/data/archiving#ManifestationOfRecordPart_"+ rowCountString

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
		if row['Zusatzinfo_Mann'] != "":
			additional_content_string = "Zusatzinformationen zu Mann:\n"+row['Zusatzinfo_Mann']
		if row['Zusatzinfo_Frau'] != "":
			if row['Zusatzinfo_Mann'] != "":
				additional_content_string = additional_content_string + "\nZusatzinformationen zu Frau:\n"+row['Zusatzinfo_Frau']
			else:
				additional_content_string = "Zusatzinformationen zu Frau:\n"+row['Zusatzinfo_Frau']

		output_graph.add((URIRef(RecordPartURI), ontology_archiving.recordPartHasTitleLiteral, Literal(title_string)))
		if additional_content_string != "":
			output_graph.add((URIRef(RecordPartURI), ontology_archiving.recordPartHasAdditionalContentLiteral, Literal(additional_content_string))) 
		output_graph.add((URIRef(RecordPartURI), ontology_archiving.recordPartHasdateOfOriginLiteral, Literal(row['Datum'])))	
		output_graph.add((URIRef(RecordPartURI), ontology_archiving.recordPartHasWebpageURI, Literal(row['Webseite'], datatype=XSD.anyURI)))
	
	if rowCounter % 3000 == 0:
		fileCounter += 1
		fileName = 'triples_archiving_' + str(fileCounter) + '.ttl'
		output_graph.serialize(destination=fileName, format='turtle')
		output_graph = Graph()
		output_graph.bind('archiving', ontology_archiving)
		output_graph.bind('archiving-data', data_archiving)
		print(fileName)

fileCounter += 1
fileName = 'triples_archiving_' + str(fileCounter) + '.ttl'
output_graph.serialize(destination=fileName, format='turtle')
print(fileName)

