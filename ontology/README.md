# Ontologien

Bei den Zürcher Ehedaten handelt es sich um Einträge in reformatorischen Kirch- und Pfarrbüchern. Das Wissen, welches diese Einträge beinhalten, wurde in modularen Ontologien erfasst:

## Ontologie Archiving

<div align="center"><img src="/images/ais.jpg" width="700"></div>

Sowohl die Kirch- und Pfarrbücher, als auch die Einträge sind im Archivinformationssystem des Staatsarchiv des Kantons Zürich verzeichnet und über eine [thematische Suche](https://archives-quickaccess.ch/search/stazh/edb) gezielt abfragbar. Die erste Ontologie [Archiving](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving) betrachtet die Daten aus dieser Perspektive. Dabei bedient sich das Konzept unter anderem bei [Records in Contexts](https://www.ica.org/en/records-in-contexts-conceptual-model) - einem Standard für Archivdaten in Grafdatenbanken.

## Ontologien Marriage, Date, Place, Organisation und Person

Um die Ehedaten als historische Quelle(n) zu erfassen wurden fünf weitere Ontologien, die an die Ontologie Archiving anknüpfen, erstellt. Diese erfassen die Daten in ihrer Grundstruktur und lassen sich anhand definierter Anwendungsfällen stetig erweiteren. Es sind dies [Marriage](https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage), [Date](https://github.com/stazh/sw-ehedaten/tree/main/ontology/date), [Place](https://github.com/stazh/sw-ehedaten/tree/main/ontology/place), [Organisation](https://github.com/stazh/sw-ehedaten/tree/main/ontology/organisation) und [Person](https://github.com/stazh/sw-ehedaten/tree/main/ontology/person).

<div align="center"><img src="/images/Ontologybasic.jpg" width="1000"></div>


## Ontologie Certainty-Value

Bei der Ontologie [certainty-value](https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value) handelt es sich um eine Art Hilfsontologie, welche von allen anderen Ontologien verwendet wird. Darin werden Sicherheitswerte wie "sicher", "unsicher", "möglich", "unmöglich" etc. definiert, um anzugeben wie gesichert, bzw. wie wahrscheinlich eine bestimmte Information in den Daten ist. 

