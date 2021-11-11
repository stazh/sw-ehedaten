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
for entry in band_signaturen_dict:
	counter+=1
	counter_str = str(counter)
	while len(counter_str) < 5:
  		counter_str  = '0' + counter_str 
	recordURI = "https://github.com/stazh/sw-ehedaten/data/archiving#Record_" + counter_str
	volumeURI = "https://github.com/stazh/sw-ehedaten/data/archiving#Volume_" + counter_str
	output_graph.add((URIRef(recordURI), RDF.type, ontology_archiving.Record))	
	output_graph.add((URIRef(volumeURI), RDF.type, ontology_archiving.Volume))
	output_graph.add((URIRef(recordURI), ontology_archiving.recordHasManifestation, URIRef(volumeURI)))
	output_graph.add((URIRef(band_signaturen_dict[entry]), RDF.type, ontology_archiving.Identifier))
	output_graph.add((URIRef(volumeURI), ontology_archiving.manifestationIsIdentifiedByIdentifier, URIRef(band_signaturen_dict[entry])))				
	output_graph.add((URIRef(band_signaturen_dict[entry]), ontology_archiving.identifierHasLiteral, Literal(entry)))
output_graph.add((data_archiving.stazh, ontology_archiving.archiveHasNameLiteral, Literal("Staatsarchiv des Kantons Zürich")))

output_graph_kirchgemeinden = Graph()
output_graph_baende = Graph()

rowCounter = 0
fileCounter = 0
for row in input_file:
	# convert it from an OrderedDict to a regular dict
	row = dict(row)
	#print(row)
	rowCounter += 1
	#output_graph.bind('archiving', ontology_archiving)
	#output_graph.bind('archiving-data', data_archiving)

	output_graph_kirchgemeinden.bind('archiving', ontology_archiving)
	output_graph_kirchgemeinden.bind('archiving-data', data_archiving)
	output_graph_baende.bind('archiving-data', data_archiving)
	output_graph_baende.bind('archiving', ontology_archiving)
	

	if row['Signatur'] != "":
		
		rowCountString = str(rowCounter)
		while len(rowCountString) < 6:
  			rowCountString = '0' + rowCountString

		RecordPartURI = 'https://github.com/stazh/sw-ehedaten/data/archiving#RecordPart_' + rowCountString
		ManifestationURI = 'https://github.com/stazh/sw-ehedaten/data/archiving#Manifestation_' + rowCountString
		ManifestationOfRecordPartURI = "https://github.com/stazh/sw-ehedaten/data/archiving#ManifestationOfRecordPart_"+ rowCountString
		SignaturURI = "https://github.com/stazh/sw-ehedaten/data/archiving#Signatur_" + rowCountString
		TitleURI = "https://github.com/stazh/sw-ehedaten/data/archiving#Title_"+ rowCountString
		AdditionalContentURI = "https://github.com/stazh/sw-ehedaten/data/archiving#AdditionalContent_"+ rowCountString
		DateOfOriginURI = "https://github.com/stazh/sw-ehedaten/data/archiving#DateOfOrigin_"+ rowCountString

		output_graph.add((URIRef(RecordPartURI), RDF.type, ontology_archiving.RecordPart))
		output_graph.add((URIRef(ManifestationURI), RDF.type, ontology_archiving.Manifestation))
		output_graph.add((URIRef(RecordPartURI),ontology_archiving.recordPartHasManifestation, URIRef(ManifestationOfRecordPartURI)))
		output_graph.add((URIRef(SignaturURI), RDF.type, ontology_archiving.Identifier))
		output_graph.add((URIRef(ManifestationOfRecordPartURI), ontology_archiving.manifestationIsIdentifiedByIdentifier, URIRef(SignaturURI)) ) 

		#Literal(row['Signatur'])
		output_graph.add((URIRef(TitleURI), RDF.type, ontology_archiving.Title))
		output_graph.add((URIRef(AdditionalContentURI), RDF.type, ontology_archiving.AdditionalContent)) 
		output_graph.add((URIRef(DateOfOriginURI), RDF.type, ontology_archiving.DateOfOrigin))	
		output_graph.add((URIRef(row['Webseite']), RDF.type, ontology_archiving.Webpage))
		output_graph.add((URIRef(row['Webseite']), ontology_archiving.webpageHasURL, Literal(row['Webseite'], datatype=XSD.anyURI)) )	
	#output_graph_kirchgemeinden.add((URIRef(row['Index Kirchgemeinde']), RDF.type, edbzh_po.Kirchgemeinde))#Ontologie
	#output_graph_kg.add((URIRef(row['Index Kirchgemeinde']), edbzh_po.kirchgemeindeLiteral, Literal(row['Kirchgemeinde'])) )#Ontologie
	#output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatKirchgemeinde, (URIRef(row['Index Kirchgemeinde']))) )#Ontologie

	
	#if rowCounter % 3000 == 0:
		#fileCounter += 1
		#fileName = 'edb_' + str(fileCounter) + '.ttl'
		#output_graph.serialize(destination=fileName, format='turtle')
		#output_graph = Graph()
		#output_graph.bind('archiving', ontology_archiving)
		#output_graph.bind('archiving-data', data_archiving)

fileCounter += 1
fileName = 'edb_' + str(fileCounter) + '.ttl'
output_graph.serialize(destination=fileName, format='turtle')
print(fileName)

