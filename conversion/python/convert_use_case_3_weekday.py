#!/usr/bin/python
#-*- coding:utf-8 -*-
import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD
import sys
from datetime import date, timedelta
import calendar
#Parameter: 1: OGD-Datensatz zu Ehedaten des Staatsarchivs Zürich
inFile = sys.argv[1]
input_file = csv.DictReader(open(inFile), delimiter=';')

inFileBaende = sys.argv[2]
input_file_baende = csv.DictReader(open(inFileBaende), delimiter=';')

inFileDoppeleintraege = sys.argv[3]
input_file_doppeleintraege = csv.DictReader(open(inFileDoppeleintraege), delimiter=';')

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

rowCounter = 0
idMarriageEntryDict = {}
for row in input_file:
    row = dict(row)
    rowCounter += 1  
    if row['Signatur'] != "":       
        rowCountString = str(rowCounter)
        while len(rowCountString) < 6:
            rowCountString = '0' + rowCountString
        MarriageEntryURI = 'https://github.com/stazh/sw-ehedaten/tree/main/data#MarriageEntry_' + rowCountString
        idMarriageEntryDict[row['ID']] = MarriageEntryURI

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
input_file = csv.DictReader(open(inFile), delimiter=';')
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

        if row['Datum_Von'] == row['Datum_Bis']:
            gregDate = ''  
            weekday = ''     
            if int(row['Datum_Von'][:4]) < 1701:
                julianDateList = row['Datum_Von'].split('-')
                julianDate = date(int(julianDateList[0]),int(julianDateList[1]),int(julianDateList[2]))
                dateOrig = julianDate
                gregDate = julianDate + timedelta(days=10)
                weekday = calendar.day_name[gregDate.weekday()]
                weekdayURI = 'https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#' + weekday
                output_graph.add((URIRef(DatingURI), ontology_date.gregorianDating, Literal(gregDate,datatype=XSD.date)))
                output_graph.add((URIRef(DatingURI), ontology_date.dateHasWeekday, URIRef(weekdayURI)))
                output_graph.add((URIRef(DatingURI),ontology_date.dateIsInGregorianYear,Literal(gregDate.year,datatype=XSD.gYear)))
            else:
                gregDateList = row['Datum_Von'].split('-')
                gregDate = date(int(gregDateList[0]),int(gregDateList[1]),int(gregDateList[2]))
                dateOrig = gregDate
                weekday = calendar.day_name[gregDate.weekday()]
                weekdayURI = 'https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#' + weekday
                output_graph.add((URIRef(DatingURI), ontology_date.dateHasWeekday, URIRef(weekdayURI)))
                output_graph.add((URIRef(DatingURI),ontology_date.dateIsInGregorianYear,Literal(gregDate.year,datatype=XSD.gYear)))
            if weekday == 'Sunday' and gregDate > date(1620,6,26) or row['Zusatzinfo_Mann'].find('Verkünddatum') >= 0 or row['Zusatzinfo_Mann'].lower().find('getraut zu ') >= 0 or row['Zusatzinfo_Mann'].lower().find('getraut im ') >= 0 or row['Zusatzinfo_Mann'].lower().find('getraut in ') >= 0:
                output_graph.add((URIRef(MarriageEntryURI),ontology_marriage.marriageEntryDocumentsMarriageProclamationWithCertaintyValue,ontology_certainty_value.VeryLikely))
            else:
                output_graph.add((URIRef(MarriageEntryURI),ontology_marriage.marriageEntryDocumentsWeddingWithCertaintyValue,ontology_certainty_value.Likely))
        else:   
            DatingSURI = DatingURI + '_s'
            DatingEURI = DatingURI + '_e'
            if int(row['Datum_Von'][:4]) < 1701:
                julianDateList = row['Datum_Von'].split('-')
                julianDate = date(int(julianDateList[0]),int(julianDateList[1]),int(julianDateList[2]))
                gregDate = julianDate + timedelta(days=10)
                weekday = calendar.day_name[gregDate.weekday()]
                weekdayURI = 'https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#' + weekday
                output_graph.add((URIRef(DatingSURI), ontology_date.gregorianDating, Literal(gregDate,datatype=XSD.date)))
                output_graph.add((URIRef(DatingSURI), ontology_date.dateHasWeekday, URIRef(weekdayURI)))
                output_graph.add((URIRef(DatingSURI),ontology_date.dateIsInGregorianYear,Literal(gregDate.year,datatype=XSD.gYear)))
            else:
                gregDateList = row['Datum_Von'].split('-')
                gregDate = date(int(gregDateList[0]),int(gregDateList[1]),int(gregDateList[2]))
                weekday = calendar.day_name[gregDate.weekday()]
                weekdayURI = 'https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#' + weekday
                output_graph.add((URIRef(DatingSURI), ontology_date.dateHasWeekday, URIRef(weekdayURI)))
                output_graph.add((URIRef(DatingSURI),ontology_date.dateIsInGregorianYear,Literal(gregDate.year,datatype=XSD.gYear)))
            if int(row['Datum_Bis'][:4]) < 1701:
                julianDateList = row['Datum_Bis'].split('-')
                julianDate = date(int(julianDateList[0]),int(julianDateList[1]),int(julianDateList[2]))
                gregDate = julianDate + timedelta(days=10)
                weekday = calendar.day_name[gregDate.weekday()]
                weekdayURI = 'https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#' + weekday
                output_graph.add((URIRef(DatingEURI), ontology_date.gregorianDating, Literal(gregDate,datatype=XSD.date)))
                output_graph.add((URIRef(DatingEURI), ontology_date.dateHasWeekday, URIRef(weekdayURI)))
                output_graph.add((URIRef(DatingEURI),ontology_date.dateIsInGregorianYear,Literal(gregDate.year,datatype=XSD.gYear)))
            else:
                gregDateList = row['Datum_Bis'].split('-')
                gregDate = date(int(gregDateList[0]),int(gregDateList[1]),int(gregDateList[2]))
                weekday = calendar.day_name[gregDate.weekday()]
                weekdayURI = 'https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#' + weekday
                output_graph.add((URIRef(DatingEURI), ontology_date.dateHasWeekday, URIRef(weekdayURI)))
                output_graph.add((URIRef(DatingEURI),ontology_date.dateIsInGregorianYear,Literal(gregDate.year,datatype=XSD.gYear)))
            if row['Zusatzinfo_Mann'].find('Verkünddatum') >= 0 or row['Zusatzinfo_Mann'].lower().find('getraut zu ') >= 0 or row['Zusatzinfo_Mann'].lower().find('getraut im ') >= 0 or row['Zusatzinfo_Mann'].lower().find('getraut in ') >= 0:
                output_graph.add((URIRef(MarriageEntryURI),ontology_marriage.marriageEntryDocumentsMarriageProclamationWithCertaintyValue,ontology_certainty_value.VeryLikely))
            else:
                output_graph.add((URIRef(MarriageEntryURI),ontology_marriage.marriageEntryDocumentsWeddingWithCertaintyValue,ontology_certainty_value.Likely))

    if rowCounter % 50000 == 0:
        fileCounter += 1
        fileName = 'data_triples_use_case_3_' + str(fileCounter) + '.ttl'
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
fileName = 'data_triples_use_case_3_' + str(fileCounter) + '.ttl'
output_graph.serialize(destination=fileName, format='turtle')
print(fileName)

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
input_file_doppeleintraege = csv.DictReader(open(inFileDoppeleintraege), delimiter=';')
for row in input_file_doppeleintraege:
    row = dict(row)
    input_file_doppeleintraege = csv.DictReader(open(inFileDoppeleintraege), delimiter=';')
    for row2 in input_file_doppeleintraege:
        row2 = dict(row2)
        if row['Marriage_ID'] == row2['Marriage_ID'] and not(row['Scope-ID'] == row2['Scope-ID']):
            marrieageEntryURI_1 = idMarriageEntryDict[row['Scope-ID']]
            marrieageEntryURI_2 = idMarriageEntryDict[row2['Scope-ID']]
            #output_graph.add(URIRef(marrieageEntryURI_1), ontology_marriage.marriageEntryDocumentsProbablySameCoupleThanMarriageEntry, URIRef(marrieageEntryURI_2))


fileName = 'data_triples_double_marriageEntry' + '.ttl'
output_graph.serialize(destination=fileName, format='turtle')
print(fileName)

