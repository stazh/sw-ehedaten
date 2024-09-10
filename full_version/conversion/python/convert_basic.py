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


output_graph = Graph()
output_graph.bind('archiving', ontology_archiving)
output_graph.bind('certainty-value', ontology_certainty_value)
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

#Erstelle Tripple auf Stufe Kirchgemeinde
fileName = 'data_triples_basic_parish' + '.ttl'
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
        
        #Trippel Marriage und Person
        output_graph.add((URIRef(MarriageEntryURI), RDF.type, ontology_marriage.MarriageEntry))
        output_graph.add((URIRef(RecordPartURI), ontology_archiving.recordPartRepresents, URIRef(MarriageEntryURI)))
        output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryIsInParishBook, URIRef(parishBookURI)))
        output_graph.add((URIRef(ManURI), RDF.type, ontology_person.Man))
        output_graph.add((URIRef(WomanURI), RDF.type, ontology_person.Woman))
        output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryRegistersWoman, URIRef(WomanURI)))
        output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryRegistersMan, URIRef(ManURI)))
        if row['Zusatzinfo_Frau'] != '' and row['Zusatzinfo_Frau'] != '-':
            output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryHasCommentToWoman, Literal(row['Zusatzinfo_Frau'])))
        if row['Zusatzinfo_Mann'] != '' and row['Zusatzinfo_Mann'] != '-':
            output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryHasGeneralCommentOrCommentToMan, Literal(row['Zusatzinfo_Mann'])))
        output_graph.add((URIRef(ManURI), ontology_person.personHasFirstNameLiteral, Literal(row['Vorname_Mann'])))
        output_graph.add((URIRef(WomanURI), ontology_person.personHasFirstNameLiteral, Literal(row['Vorname_Frau'])))
        output_graph.add((URIRef(ManURI), ontology_person.personHasLastNameLiteral, Literal(row['Nachname_Mann'])))
        output_graph.add((URIRef(WomanURI), ontology_person.personHasLastNameLiteral, Literal(row['Nachname_Frau'])))
        
        #Trippel Vorname Mann. Wenn ? in Namen : unsichere Lesung
        output_graph.add((URIRef(FirstNameManSpezificationURI), RDF.type, ontology_person.FirstNameSpezification))
        output_graph.add((URIRef(ManURI), ontology_person.personHasFirstNameSpezification, URIRef(FirstNameManSpezificationURI)))
        name = row['Vorname_Mann']
        if name.find('?') > -1:
            name = name.replace(' ?','')
            name = name.replace(' (?)','')
            name = name.replace('?','')
            output_graph.add((URIRef(FirstNameManSpezificationURI),ontology_person.firstNameSpezificationHasCertaintyValue,ontology_certainty_value.Uncertain))
        else:
            output_graph.add((URIRef(FirstNameManSpezificationURI),ontology_person.firstNameSpezificationHasCertaintyValue,ontology_certainty_value.Certain))
        output_graph.add((URIRef(FirstNameManSpezificationURI),ontology_person.firstNameSpezificationHasLiteral,Literal(name)))
        
        #Trippel Vorname Frau. Wenn ? in Namen : unsichere Lesung
        output_graph.add((URIRef(FirstNameWomanSpezificationURI), RDF.type, ontology_person.FirstNameSpezification))
        output_graph.add((URIRef(WomanURI), ontology_person.personHasFirstNameSpezification, URIRef(FirstNameWomanSpezificationURI)))
        name = row['Vorname_Frau']  
        if name.find('?') > -1:
            name = name.replace(' ?','')
            name = name.replace(' (?)','')
            lname = name.replace('?','')
            output_graph.add((URIRef(FirstNameWomanSpezificationURI),ontology_person.firstNameSpezificationHasCertaintyValue,ontology_certainty_value.Uncertain))
        else:
            output_graph.add((URIRef(FirstNameWomanSpezificationURI),ontology_person.firstNameSpezificationHasCertaintyValue,ontology_certainty_value.Certain))
        output_graph.add((URIRef(FirstNameWomanSpezificationURI),ontology_person.firstNameSpezificationHasLiteral,Literal(name)))
        
        #Trippel Nachname Mann. Wenn ? in Namen : unsichere Lesung
        output_graph.add((URIRef(LastNameManSpezificationURI), RDF.type, ontology_person.LastNameSpezification))
        output_graph.add((URIRef(ManURI), ontology_person.personHasLastNameSpezification, URIRef(LastNameManSpezificationURI)))         
        name = row['Nachname_Mann']
        if name.find('?') > -1:
            name = name.replace(' ?','')
            name = name.replace(' (?)','')
            name = name.replace('?','')
            output_graph.add((URIRef(LastNameManSpezificationURI),ontology_person.lastNameSpezificationHasCertaintyValue,ontology_certainty_value.Uncertain))
        else:
            output_graph.add((URIRef(LastNameManSpezificationURI),ontology_person.lastNameSpezificationHasCertaintyValue,ontology_certainty_value.Certain))
        output_graph.add((URIRef(LastNameManSpezificationURI),ontology_person.lastNameSpezificationHasLiteral,Literal(name)))
        
        #Trippel Nachname Frau. Wenn ? in Namen : unsichere Lesung
        output_graph.add((URIRef(LastNameWomanSpezificationURI), RDF.type, ontology_person.LastNameSpezification))
        output_graph.add((URIRef(WomanURI), ontology_person.personHasLastNameSpezification, URIRef(LastNameWomanSpezificationURI))) 
        name = row['Nachname_Frau'] 
        if name.find('?') > -1:
            name = name.replace(' ?','')
            name = name.replace(' (?)','')
            lname = name.replace('?','')
            output_graph.add((URIRef(LastNameWomanSpezificationURI),ontology_person.lastNameSpezificationHasCertaintyValue,ontology_certainty_value.Uncertain))
        else:
            output_graph.add((URIRef(LastNameWomanSpezificationURI),ontology_person.lastNameSpezificationHasCertaintyValue,ontology_certainty_value.Certain))
        output_graph.add((URIRef(LastNameWomanSpezificationURI),ontology_person.lastNameSpezificationHasLiteral,Literal(name)))

        #Trippel Herkunft
        if row['Herkunft_Mann'] != "":
            output_graph.add((URIRef(PlaceOfOriginManSpezificationURI), RDF.type, ontology_person.PlaceOfOriginSpezification))
            output_graph.add((URIRef(ManURI),ontology_person.personHasPlaceOfOriginSpezification,URIRef(PlaceOfOriginManSpezificationURI)))
            herkunft_mann = row['Herkunft_Mann']
            if herkunft_mann.find('?') > -1:
                herkunft_mann = herkunft_mann.replace(' ?','')
                herkunft_mann = herkunft_mann.replace(' (?)','')
                herkunft_mann = herkunft_mann.replace('?','')
                output_graph.add((URIRef(PlaceOfOriginManSpezificationURI),ontology_person.placeOfOriginSpezificationHasCertaintyValue,ontology_certainty_value.Uncertain))
            else:
                output_graph.add((URIRef(PlaceOfOriginManSpezificationURI),ontology_person.placeOfOriginSpezificationHasCertaintyValue,ontology_certainty_value.Certain))
                output_graph.add((URIRef(ManURI), ontology_person.personHasPlaceOfOrigin, URIRef(orte_dict[herkunft_mann])))
            output_graph.add((URIRef(PlaceOfOriginManSpezificationURI),ontology_person.placeOfOriginSpezificationHasPlace,URIRef(orte_dict[herkunft_mann])))
        
        if row['Herkunft_Frau'] != "":
            output_graph.add((URIRef(PlaceOfOriginWomanSpezificationURI), RDF.type, ontology_person.PlaceOfOriginSpezification))
            output_graph.add((URIRef(WomanURI),ontology_person.personHasPlaceOfOriginSpezification,URIRef(PlaceOfOriginWomanSpezificationURI)))
            herkunft_frau = row['Herkunft_Frau']
            if herkunft_frau.find('?') > -1:
                herkunft_frau = herkunft_frau.replace(' ?','')
                herkunft_frau = herkunft_frau.replace(' (?)','')
                herkunft_frau = herkunft_frau.replace('?','')
                output_graph.add((URIRef(PlaceOfOriginWomanSpezificationURI),ontology_person.placeOfOriginSpezificationHasCertaintyValue,ontology_certainty_value.Uncertain))
            else:
                output_graph.add((URIRef(PlaceOfOriginWomanSpezificationURI),ontology_person.placeOfOriginSpezificationHasCertaintyValue,ontology_certainty_value.Certain))
                output_graph.add((URIRef(WomanURI), ontology_person.personHasPlaceOfOrigin, URIRef(orte_dict[herkunft_frau])))
            output_graph.add((URIRef(PlaceOfOriginWomanSpezificationURI),ontology_person.placeOfOriginSpezificationHasPlace,URIRef(orte_dict[herkunft_frau])))
        
        #Trippel Date
        if row['Datum_Von'] == row['Datum_Bis']:
            output_graph.add((URIRef(DatingURI), RDF.type, ontology_date.Date))
            output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryHasDatingOnDate, URIRef(DatingURI)))         
            if int(row['Datum_Von'][:4]) < 1701:
                output_graph.add((URIRef(DatingURI), ontology_date.julianDating, Literal(row['Datum_Von'],datatype=XSD.date)))
            else:
                output_graph.add((URIRef(DatingURI), ontology_date.gregorianDating, Literal(row['Datum_Von'],datatype=XSD.date)))
        else:   
            output_graph.add((URIRef(DatingURI), RDF.type, ontology_date.DatePeriod))
            output_graph.add((URIRef(MarriageEntryURI), ontology_marriage.marriageEntryHasDatingWithinDatePeriod, URIRef(DatingURI)))
            DatingSURI = DatingURI + '_s'
            DatingEURI = DatingURI + '_e'
            output_graph.add((URIRef(DatingSURI), RDF.type, ontology_date.Date))
            output_graph.add((URIRef(DatingEURI), RDF.type, ontology_date.Date ))
            output_graph.add((URIRef(DatingURI), ontology_date.datePeriodHasStartDate, (URIRef(DatingSURI))))
            output_graph.add((URIRef(DatingURI), ontology_date.datePeriodHasEndDate, (URIRef(DatingEURI))))

            if int(row['Datum_Von'][:4]) < 1701:
                output_graph.add((URIRef(DatingSURI), ontology_date.julianDating, Literal(row['Datum_Von'],datatype=XSD.date)))
            else:
                output_graph.add((URIRef(DatingSURI), ontology_date.gregorianDating, Literal(row['Datum_Von'],datatype=XSD.date)))
            if int(row['Datum_Bis'][:4]) < 1701:
                output_graph.add((URIRef(DatingEURI), ontology_date.julianDating, Literal(row['Datum_Bis'],datatype=XSD.date)))
            else:
                output_graph.add((URIRef(DatingEURI), ontology_date.gregorianDating, Literal(row['Datum_Bis'],datatype=XSD.date)))

    if rowCounter % 10000 == 0:
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

