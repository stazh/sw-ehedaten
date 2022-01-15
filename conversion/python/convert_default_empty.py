#!/usr/bin/python
#-*- coding:utf-8 -*-
import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD
import sys
#Parameter: 1: OGD-Datensatz zu Ehedaten des Staatsarchivs Zürich
inFile = sys.argv[1]
input_file = csv.DictReader(open(inFile), delimiter=';')

inFileBaende = sys.argv[2]
input_file_baende = csv.DictReader(open(inFileBaende), delimiter=';')


ontology_archiving = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#")
ontology_certainty_value = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#")
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


counter = 0
record_dict = {}

for entry in band_dict:
    counter+=1
    counter_str = str(counter)
    while len(counter_str) < 5:
        counter_str  = '0' + counter_str 
    recordURI = "https://github.com/stazh/sw-ehedaten/tree/main/data#Record_" + counter_str
    record_dict[entry] = recordURI
    volumeURI = band_dict[entry]['URI']


output_graph = Graph()
output_graph.bind('archiving', ontology_archiving)
output_graph.bind('certainty-value', ontology_certainty_value)
output_graph.bind('date', ontology_date)
output_graph.bind('organisation', ontology_organisation)
output_graph.bind('person', ontology_person)
output_graph.bind('place', ontology_place)
output_graph.bind('marriage', ontology_marriage)
output_graph.bind('data', data)

rowCounter = 0
fileCounter = 0
pageURIList = []
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
        parishBookURI = recordURI.replace('Record','ParishBook')
        RecordPartURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#RecordPart_' + rowCountString
        MarriageEntryURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#MarriageEntry_' + rowCountString
        ManURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#Man_' + rowCountString
        WomanURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#Woman_' + rowCountString
        DatingURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#Dating_' + rowCountString
        FirstNameManSpezificationURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#FirstNameManSpezification_' + rowCountString
        LastNameManSpezificationURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#LastNameManSpezification_' + rowCountString
        FirstNameWomanSpezificationURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#FirstNameWomanSpezification_' + rowCountString
        LastNameWomanSpezificationURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#LastNameWomanSpezification_' + rowCountString
        PlaceOfOriginManSpezificationURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#PlaceOfOriginManSpezification_' + rowCountString
        PlaceOfOriginWomanSpezificationURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#PlaceOfOriginWomanSpezification_' + rowCountString

        #HIER TRIPPEL GENERIEREN
        
    if rowCounter % 50000 == 0: #ANPASSEN JE NACH ANZAHL TRIPPLE
        fileCounter += 1
        fileName = 'data_triples_basic_marriage_entry_' + str(fileCounter) + '.ttl'
        output_graph.serialize(destination=fileName, format='turtle')
        output_graph = Graph()
        output_graph.bind('archiving', ontology_archiving)
        output_graph.bind('certainty-value', ontology_certainty_value)
        output_graph.bind('date', ontology_date)
        output_graph.bind('organisation', ontology_organisation)
        output_graph.bind('person', ontology_person)
        output_graph.bind('place', ontology_place)
        output_graph.bind('marriage', ontology_marriage)
        output_graph.bind('data', data)
        print(fileName)

fileCounter += 1
fileName = 'data_triples_basic_marriage_entry_' + str(fileCounter) + '.ttl'
output_graph.serialize(destination=fileName, format='turtle')
print(fileName)

