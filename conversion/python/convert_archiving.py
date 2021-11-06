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


agent_counter = 0
agent_dict = {}
band_dict = {}

all_Data = csv.DictReader(open('/Users/rebekkapluss/Documents/Studium/Masterarbeit/OGD_Datensatz/01-EDB_16_18_Jh_Stand_2021_07_14 (csv).csv'), delimiter=';')

input_file_list = list(all_Data)
bandSignaturen = {}
bandSignaturString = ""
for row in input_file_list:
	# convert it from an OrderedDict to a regular dict
	row = dict(row)
	k = row['Signatur'].rfind(",")
	bandSignaturString = row['Signatur'][:k]
	if  bandSignaturString in bandSignaturen:
		bandSignaturen[bandSignaturString] +=1
	else:
		bandSignaturen[bandSignaturString] = 1

output_graph = Graph()
output_graph.bind('archiving', ontology_archiving)
output_graph.bind('archiving-data', data_archiving)
output_graph.add((data_archiving.stazh, RDF.type, ontology_archiving.Archive))
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
	output_graph.bind('archiving', ontology_archiving)
	output_graph.bind('archiving-data', data_archiving)

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
		output_graph.add((URIRef(SignaturURI), ontology_archiving.manifestationIsIdentifiedByIdentifier, Literal(row['Signatur'])) ) 
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

