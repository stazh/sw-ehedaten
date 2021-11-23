import csv
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, RDFS, SKOS, XSD

edbzh_po = Namespace("http://e-editiones.ch/project/ontology/edbzh#")
edbzh_pd = Namespace("http://e-editiones.ch/project/data/edbzh#")
input_file = csv.DictReader(open("csv/Ehedaten_V5.csv"), delimiter=';')

output_graph = Graph()
output_graph_kg = Graph()
output_graph_vm = Graph()
output_graph_vf = Graph()
output_graph_nn = Graph()
output_graph_h = Graph()
output_graph_m = Graph()
rowCounter = 0
fileCounter = 0
for row in input_file:
	# convert it from an OrderedDict to a regular dict
	row = dict(row)
	#print(row)
	rowCounter += 1
	output_graph.bind('edbzh_po', edbzh_po)
	output_graph.bind('edbzh_pd', edbzh_pd)
	output_graph_kg.bind('edbzh_po', edbzh_po)
	output_graph_kg.bind('edbzh_pd', edbzh_pd)
	output_graph_vm.bind('edbzh_po', edbzh_po)
	output_graph_vm.bind('edbzh_pd', edbzh_pd)
	output_graph_nn.bind('edbzh_po', edbzh_po)
	output_graph_nn.bind('edbzh_pd', edbzh_pd)
	output_graph_vf.bind('edbzh_po', edbzh_po)
	output_graph_vf.bind('edbzh_pd', edbzh_pd)
	output_graph_h.bind('edbzh_po', edbzh_po)
	output_graph_h.bind('edbzh_pd', edbzh_pd)
	output_graph_m.bind('edbzh_po', edbzh_po)
	output_graph_m.bind('edbzh_pd', edbzh_pd)
	output_graph.add((URIRef(row['\ufeffEintrag ID']), RDF.type, edbzh_po.Eheeintrag))
	output_graph_m.add((URIRef(row['Marriage ID']), RDF.type, edbzh_po.Ehe))
	output_graph.add((URIRef(row['Archive-Record ID']), RDF.type, edbzh_po.Archiveintrag))


	if row['Nachname Mann'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatNachnameMann, (URIRef(row['Index Nachname Mann']))) )#Ontologie
		output_graph_nn.add((URIRef(row['Index Nachname Mann']), RDF.type, edbzh_po.Nachname))
		output_graph_nn.add((URIRef(row['Index Nachname Mann']), edbzh_po.nachnameLiteral, Literal(row['Nachname Mann'])) )#Ontologie
		if row['UL Nachname Mann'] != "":
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungNachnameMann, Literal('true', datatype=XSD.boolean)) )#Ontologie
		else:
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungNachnameMann, Literal('false', datatype=XSD.boolean)) )	
	if row['Vorname Mann'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatVornameMann, (URIRef(row['Index Vorname Mann']))) )#Ontologie
		output_graph_vm.add((URIRef(row['Index Vorname Mann']), RDF.type, edbzh_po.VornameMann)) 
		output_graph_vm.add((URIRef(row['Index Vorname Mann']), edbzh_po.vornameMannLiteral, Literal(row['Vorname Mann'])) )#Ontologie
		if row['UL Vorname Mann'] != "":
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungVornameMann, Literal('true', datatype=XSD.boolean)) )
		else:
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungVornameMann, Literal('false', datatype=XSD.boolean)) )
	if row['Herkunft Mann'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatHerkunftMann, (URIRef(row['Index Herkunft Mann'])) ))#Ontologie
		output_graph_h.add((URIRef(row['Index Herkunft Mann']), RDF.type, edbzh_po.Herkunft))
		output_graph_h.add((URIRef(row['Index Herkunft Mann']), edbzh_po.herkunftLiteral, Literal(row['Herkunft Mann'])) )#Ontologie
		if row['UL Herkunft Mann'] != "":
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungHerkunftMann, Literal('true', datatype=XSD.boolean)) )
		else:
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungHerkunftMann, Literal('false', datatype=XSD.boolean)) )
	if row['Nachname Frau'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatNachnameFrau, (URIRef(row['Index Nachname Frau'])) ))#Ontologie
		output_graph_nn.add((URIRef(row['Index Nachname Frau']), RDF.type, edbzh_po.Nachname)) 
		output_graph_nn.add((URIRef(row['Index Nachname Frau']), edbzh_po.nachnameLiteral, Literal(row['Nachname Frau'])) )#Ontologie
		if row['UL Nachname Frau'] != "":
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungNachnameFrau, Literal('true', datatype=XSD.boolean)) )
		else:
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungNachnameFrau, Literal('false', datatype=XSD.boolean)) )
	if row['Vorname Frau'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatVornameFrau, (URIRef(row['Index Vorname Frau'])) ))
		output_graph_vf.add((URIRef(row['Index Vorname Frau']), RDF.type, edbzh_po.VornameFrau)) 
		output_graph_vf.add((URIRef(row['Index Vorname Frau']), edbzh_po.vornameFrauLiteral, Literal(row['Vorname Frau'])) )
		if row['UL Vorname Frau'] != "":
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungVornameFrau, Literal('true', datatype=XSD.boolean)) )
		else:
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungVornameFrau, Literal('false', datatype=XSD.boolean)) )
	if row['Herkunft Frau'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatHerkunftFrau, (URIRef(row['Index Herkunft Frau'])) ))
		output_graph_h.add((URIRef(row['Index Herkunft Frau']), RDF.type, edbzh_po.Herkunft)) 
		output_graph_h.add((URIRef(row['Index Herkunft Frau']), edbzh_po.herkunftLiteral, Literal(row['Herkunft Frau'])) )
		if row['UL Herkunft Frau'] != "":
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungHerkunftFrau, Literal('true', datatype=XSD.boolean)) )
		else:
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.unsichereLesungHerkunftFrau, Literal('false', datatype=XSD.boolean)) )	
	if row['Datum'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.datum, Literal(row['Datum'])) )
	if row['DatumJahr'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.datumJahr, Literal(row['DatumJahr'], datatype=XSD.int)) )
		if int(row['DatumJahr']) > 1700:
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatGregorianischenKalender, Literal('true', datatype=XSD.boolean)) )
		else:
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatJulianischenKalender, Literal('true', datatype=XSD.boolean)) )
	if row['DatumMonat'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.datumMonat, Literal(row['DatumMonat'], datatype=XSD.int)) )
	if row['DatumTag'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.datumTag, Literal(row['DatumTag'], datatype=XSD.int)) )
	if row['Startdatum'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.startdatum, Literal(row['Startdatum'])) )
	if row['StartdatumJahr'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.startdatumJahr, Literal(row['StartdatumJahr'], datatype=XSD.int)) )
		if int(row['StartdatumJahr']) > 1700:
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatGregorianischenKalender, Literal('true', datatype=XSD.boolean)) )
		else:
			output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatJulianischenKalender, Literal('true', datatype=XSD.boolean)) )
	if row['StartdatumMonat'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.startdatumMonat, Literal(row['StartdatumMonat'], datatype=XSD.int)) )
	if row['StartdatumTag'] != "":	
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.startdatumTag, Literal(row['StartdatumTag'], datatype=XSD.int)) )
	if row['Enddatum'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.enddatum, Literal(row['Enddatum'])) )
	if row['EnddatumJahr'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.enddatumJahr, Literal(row['EnddatumJahr'], datatype=XSD.int)) )
	if row['EnddatumMonat'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.enddatumMonat, Literal(row['EnddatumMonat'], datatype=XSD.int)) )
	if row['EnddatumTag'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.enddatumTag, Literal(row['EnddatumTag'], datatype=XSD.int)) )
	if row['Datum Range zwischen'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.datumIstPeriode, Literal('true', datatype=XSD.boolean)) )
	else:
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.datumIstPeriode, Literal('false', datatype=XSD.boolean)) )
	if row['Datum unsicher'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.datumIstUnsicher, Literal('true', datatype=XSD.boolean)) )
	else:
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.datumIstUnsicher, Literal('false', datatype=XSD.boolean)) )		
	output_graph_kg.add((URIRef(row['Index Kirchgemeinde']), RDF.type, edbzh_po.Kirchgemeinde))#Ontologie
	output_graph_kg.add((URIRef(row['Index Kirchgemeinde']), edbzh_po.kirchgemeindeLiteral, Literal(row['Kirchgemeinde'])) )#Ontologie
	output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.eintragHatKirchgemeinde, (URIRef(row['Index Kirchgemeinde']))) )#Ontologie
	output_graph.add((URIRef(row['Archive-Record ID']), edbzh_po.signatur, Literal(row['Signatur'])) )
	if row['Seite im Band'] != "":
		output_graph.add((URIRef(row['Archive-Record ID']), edbzh_po.seiteImBand, Literal(row['Seite im Band'])) )
	output_graph.add((URIRef(row['Archive-Record ID']), edbzh_po.weblink, Literal(row['Weblink'], datatype=XSD.anyURI)) )
	output_graph.add((URIRef(row['Archive-Record ID']), edbzh_po.archiveintragGehoertZuEheeintrag, (URIRef(row['\ufeffEintrag ID'])) ))#Ontologie
	output_graph_m.add((URIRef(row['Marriage ID']), edbzh_po.eheHatEheeintrag, (URIRef(row['\ufeffEintrag ID'])) ))#Ontologie
	output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.anzahlEhen, (URIRef(row['Anzahl Ehen'])) ))#Ontologie
	
	if row['Zusatzinformationen Mann oder Allgemein'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.zusatzinformationMannAllgemein, Literal(row['Zusatzinformationen Mann oder Allgemein'])) )
	if row['Zusatzinformationen Frau oder Allgemein'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.zusatzinformationFrauAllgemein, Literal(row['Zusatzinformationen Frau oder Allgemein'])) )
	if row['Zusatzinformationen Mann Frau oder Allgemein'] != "":
		output_graph.add((URIRef(row['\ufeffEintrag ID']), edbzh_po.zusatzinformationAllgemeinMannFrau, Literal(row['Zusatzinformationen Mann Frau oder Allgemein'])) )
	
	if rowCounter % 3000 == 0:
		fileCounter += 1
		fileName = 'edb_' + str(fileCounter) + '.ttl'
		output_graph.serialize(destination=fileName, format='turtle')
		output_graph = Graph()
		output_graph.bind('edbzh_po', edbzh_po)
		output_graph.bind('edbzh_pd', edbzh_pd)
		print(fileName)

fileCounter += 1
fileName = 'edb_' + str(fileCounter) + '.ttl'
output_graph.serialize(destination=fileName, format='turtle')
print(fileName)
output_graph_kg.serialize(destination='ttl/pd_kirchgemeinden.ttl', format='turtle')
output_graph_vm.serialize(destination='ttl/pd_VornamenMaenner.ttl', format='turtle')
output_graph_vf.serialize(destination='ttl/pd_VornamenFrauen.ttl', format='turtle')
output_graph_nn.serialize(destination='ttl/pd_Nachnamen.ttl', format='turtle')
output_graph_h.serialize(destination='ttl/pd_Herkunftsorte.ttl', format='turtle')
output_graph_m.serialize(destination='pd_Marriages.ttl', format='turtle')

