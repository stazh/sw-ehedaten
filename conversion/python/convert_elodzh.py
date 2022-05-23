#!/usr/bin/python
#-*- coding:utf-8 -*-
import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD
import sys
from datetime import date, timedelta
import calendar

#Parameter: 1: OGD-Datensatz zu Ehedaten des Staatsarchivs Zürich, 2: Metadaten zu Kirchbänden (Export aus Archivinformationssystem des Staatsarchivs Zürich)
inFile = sys.argv[1]
input_file = csv.DictReader(open(inFile), delimiter=';')

inFileBaende = sys.argv[2]
input_file_baende = csv.DictReader(open(inFileBaende), delimiter=';')

ontology_elodzh = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#")
data = Namespace("https://github.com/stazh/sw-ehedaten/tree/main/data#")

#Erstelle Kirchgemeinden-Dictionary aus kirchgemeinden.csv (erstellt durch create_dictionaries.py-Skript)
kirchgemeinden = csv.DictReader(open('kirchgemeinden.csv'), delimiter=',')
kirchgemeinden_dict = {}
for row in kirchgemeinden:
    kirchgemeinden_dict[row['Kirchgemeinde']] = row['URI']


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

#Erstelle Dictionary um Metadaten zu Kirchband eines bestimmten Eheeintrags nachschlagen zu können (über Signatur)
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

#Erstelle Graph
output_graph = Graph()
output_graph.bind('elodzh', ontology_elodzh)
output_graph.bind('data', data)
counter = 0
record_dict = {}

#Erstelle Tripple auf Stufe Ort
for entry in orte_dict:
    output_graph.add((URIRef(orte_dict[entry]), RDF.type, ontology_elodzh.Place))    
    output_graph.add((URIRef(orte_dict[entry]), RDFS.label, Literal(entry, lang='de')))
    output_graph.add((URIRef(orte_dict[entry]), ontology_elodzh.placeHasNameLiteral, Literal(entry, lang='de')))

#Erstelle Tripple auf Stufe Record (Kirchbuch)
for entry in band_dict:
    counter+=1
    counter_str = str(counter)
    while len(counter_str) < 5:
        counter_str  = '0' + counter_str 
    parishBookURI = "https://github.com/stazh/sw-ehedaten/tree/main/data#ParishBook_" + counter_str
    record_dict[entry] = parishBookURI
    output_graph.add((URIRef(parishBookURI),RDF.type, ontology_elodzh.ParishBook))
    output_graph.add((URIRef(parishBookURI), ontology_elodzh.parishBodkHasRecordWebpageURI, Literal(band_dict[entry]['Weblink_AIS'], datatype=XSD.anyURI)))
    output_graph.add((URIRef(parishBookURI), ontology_elodzh.parishBookIsKeptByParish, URIRef(kirchgemeinden_dict[band_dict[entry]['Provenienz'].replace('Kirchgemeinde ','')])))

#Erstelle Tripple auf Stufe Kirchgemeinde
for entry in kirchgemeinden_dict:
    output_graph.add((URIRef(kirchgemeinden_dict[entry]),RDF.type, ontology_elodzh.Parish))
    output_graph.add((URIRef(kirchgemeinden_dict[entry]),ontology_elodzh.parishHasNameLiteral, Literal("Kirchgemeinde " + entry)))
    if entry == "Grossmünster" or entry == "St. Peter" or entry == "Fraumünster" or entry == "Predigern" or entry == "Spitalpfarramt":      
        output_graph.add((URIRef(kirchgemeinden_dict[entry]),ontology_elodzh.parishHasSeatAtPlace, URIRef(orte_dict['Zürich'])))
    else:
        output_graph.add((URIRef(kirchgemeinden_dict[entry]),ontology_elodzh.parishHasSeatAtPlace, URIRef(orte_dict[entry])))


fileName = 'data_triples_parish_parish_book' + '.ttl'
output_graph.serialize(destination=fileName, format='turtle')
print(fileName)

output_graph = Graph()
output_graph.bind('elodzh', ontology_elodzh)
output_graph.bind('data', data)

#Erstelle Tripple auf Stufe Record Part (Eheeintrag)
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
        parishBookURI = record_dict[band_signatur_string]
        MarriageEntryURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#MarriageEntry_' + rowCountString
        ManURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#Man_' + rowCountString
        WomanURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#Woman_' + rowCountString
        
        output_graph.add((URIRef(MarriageEntryURI), RDF.type, ontology_elodzh.MarriageEntry))
        output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryHasRecordWebpageURI, Literal(row['Webseite'], datatype=XSD.anyURI)))

        output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryIsInParishBook, URIRef(parishBookURI)))
        output_graph.add((URIRef(ManURI), RDF.type, ontology_elodzh.Man))
        output_graph.add((URIRef(WomanURI), RDF.type, ontology_elodzh.Woman))
        output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryRegistersWoman, URIRef(WomanURI)))
        output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryRegistersMan, URIRef(ManURI)))
        if row['Zusatzinfo_Frau'] != '' and row['Zusatzinfo_Frau'] != '-':
            output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryHasCommentToWoman, Literal(row['Zusatzinfo_Frau'])))
        if row['Zusatzinfo_Mann'] != '' and row['Zusatzinfo_Mann'] != '-':
            output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryHasGeneralCommentOrCommentToMan, Literal(row['Zusatzinfo_Mann'])))
        output_graph.add((URIRef(ManURI), ontology_elodzh.personHasFirstNameLiteral, Literal(row['Vorname_Mann'])))
        output_graph.add((URIRef(WomanURI), ontology_elodzh.personHasFirstNameLiteral, Literal(row['Vorname_Frau'])))
        output_graph.add((URIRef(ManURI), ontology_elodzh.personHasLastNameLiteral, Literal(row['Nachname_Mann'])))
        output_graph.add((URIRef(WomanURI), ontology_elodzh.personHasLastNameLiteral, Literal(row['Nachname_Frau'])))

        #Trippel Herkunft
        if row['Herkunft_Mann'] != "":
            herkunft_mann = row['Herkunft_Mann']
            herkunft_mann = herkunft_mann.replace(' ?','')
            herkunft_mann = herkunft_mann.replace(' (?)','')
            herkunft_mann = herkunft_mann.replace('?','')
            output_graph.add((URIRef(ManURI), ontology_elodzh.personHasPlaceOfOrigin, URIRef(orte_dict[herkunft_mann])))
        
        if row['Herkunft_Frau'] != "":
            herkunft_frau = row['Herkunft_Frau']         
            herkunft_frau = herkunft_frau.replace(' ?','')
            herkunft_frau = herkunft_frau.replace(' (?)','')
            herkunft_frau = herkunft_frau.replace('?','')
            output_graph.add((URIRef(WomanURI), ontology_elodzh.personHasPlaceOfOrigin, URIRef(orte_dict[herkunft_frau])))

        
        #Trippel Date
        if row['Datum_Von'] == row['Datum_Bis']:      
            if int(row['Datum_Von'][:4]) < 1701:
                julianDateList = row['Datum_Von'].split('-')
                julianDate = date(int(julianDateList[0]),int(julianDateList[1]),int(julianDateList[2]))
                gregDate = julianDate + timedelta(days=10)
                weekday = calendar.day_name[gregDate.weekday()]
                output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryHasDatingOnDate, Literal(gregDate,datatype=XSD.date)))
            else:
                gregDateList = row['Datum_Von'].split('-')
                gregDate = date(int(gregDateList[0]),int(gregDateList[1]),int(gregDateList[2]))
                weekday = calendar.day_name[gregDate.weekday()]
                output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryHasDatingOnDate, Literal(gregDate,datatype=XSD.date)))

            if weekday == 'Sunday' and gregDate > date(1620,6,26) or row['Zusatzinfo_Mann'].find('Verkünddatum') >= 0 or row['Zusatzinfo_Mann'].lower().find('getraut zu ') >= 0 or row['Zusatzinfo_Mann'].lower().find('getraut im ') >= 0 or (row['Zusatzinfo_Mann'].lower().find('prom') >= 0 and not(row['Zusatzinfo_Mann'].lower().find('nicht prom'))) or row['Zusatzinfo_Mann'].lower().find('prokl') >= 0:
                output_graph.add((URIRef(MarriageEntryURI),ontology_elodzh.marriageEntryDocumentsMarriageProclamationWithCertaintyValue,ontology_elodzh.VeryLikely))
            else:
                output_graph.add((URIRef(MarriageEntryURI),ontology_elodzh.marriageEntryDocumentsWeddingWithCertaintyValue,ontology_elodzh.Likely))
        else:   
            if int(row['Datum_Von'][:4]) < 1701:
                julianDateList = row['Datum_Von'].split('-')
                julianDate = date(int(julianDateList[0]),int(julianDateList[1]),int(julianDateList[2]))
                gregDate = julianDate + timedelta(days=10)
                output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryHasDatePeriodStartDate, Literal(gregDate,datatype=XSD.date)))
            else:
                output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryHasDatePeriodStartDate, Literal(row['Datum_Von'],datatype=XSD.date)))
            if int(row['Datum_Bis'][:4]) < 1701:
                julianDateList = row['Datum_Bis'].split('-')
                julianDate = date(int(julianDateList[0]),int(julianDateList[1]),int(julianDateList[2]))
                gregDate = julianDate + timedelta(days=10)
                output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryHasDatePeriodEndDate, Literal(gregDate,datatype=XSD.date)))
            else:
                output_graph.add((URIRef(MarriageEntryURI), ontology_elodzh.marriageEntryHasDatePeriodEndDate, Literal(row['Datum_Bis'],datatype=XSD.date)))
            
            if row['Zusatzinfo_Mann'].find('Verkünddatum') >= 0 or row['Zusatzinfo_Mann'].lower().find('getraut zu ') >= 0 or row['Zusatzinfo_Mann'].lower().find('getraut im ') >= 0 or (row['Zusatzinfo_Mann'].lower().find('prom') >= 0 and not(row['Zusatzinfo_Mann'].lower().find('nicht prom'))) or row['Zusatzinfo_Mann'].lower().find('prokl') >= 0:
                output_graph.add((URIRef(MarriageEntryURI),ontology_elodzh.marriageEntryDocumentsMarriageProclamationWithCertaintyValue,ontology_elodzh.VeryLikely))
            else:
                output_graph.add((URIRef(MarriageEntryURI),ontology_elodzh.marriageEntryDocumentsWeddingWithCertaintyValue,ontology_elodzh.Likely))


    if rowCounter % 20000 == 0:
        fileCounter += 1
        fileName = 'data_triples_archiving_recordpart_' + str(fileCounter) + '.ttl'
        output_graph.serialize(destination=fileName, format='turtle')
        output_graph = Graph()
        output_graph.bind('elodzh', ontology_elodzh)
        output_graph.bind('data', data)
        print(fileName)

fileCounter += 1
fileName = 'data_triples_archiving_recordpart_' + str(fileCounter) + '.ttl'
output_graph.serialize(destination=fileName, format='turtle')
print(fileName)

