# Ontology date
## Modell
<div align="center"><img src="date_model.jpg" width="500"></div>

[//]: <> (## Beispiel)
[//]: <> (<div align="center"><img src="xxx.png" width="800"></div>)

## Definition der Klassen und Beziehungen
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:Ontology](http://www.w3.org/2002/07/owl#Ontology); |
| [dct:license](http://purl.org/dc/terms/license) | <http://creativecommons.org/licenses/by/3.0/>; |
| [dct:title](http://purl.org/dc/terms/title) | "An ontology about date and time"@en; |
| [dct:description](http://purl.org/dc/terms/description) | """Formal description of a gregorian and julian dates, general subclasses, related classes and properties."""@en; |
| [dct:creator](http://purl.org/dc/terms/creator) | "Rebekka Plüss, research assistant and software developer, States Archive canton of Zürich"@en; |
| [dct:publisher](http://purl.org/dc/terms/publisher) | "States Archive canton of Zürich"@en; |
| [owl:versionInfo](http://www.w3.org/2002/07/owl#versionInfo) | "2021-11-26"^^xsd:date. |
# CLASSES
## Date
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#Date>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Date"@en, "Datum"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """date of a day."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [archiving:TimePeriod](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#TimePeriod). |
## DatePeriod
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#DatePeriod>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Date period"@en, "Datumsperiode"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """date period with start date and end date."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [archiving:TimePeriod](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#TimePeriod). |
# PROPERTIES
## julianDating
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#julianDating>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "julian dating"@en, "julianische Datierung"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a date object to its julian date."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [date:Date](https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#Date); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:date](http://www.w3.org/2001/XMLSchema#date). |
## gregorianDating
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#gregorianDating>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "gregorian dating"@en, "gregorianische Datierung"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a date object to its gregorian date."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [date:Date](https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#Date); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:date](http://www.w3.org/2001/XMLSchema#date). |
## julianStartDating
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#julianStartDating>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "julian start dating"@en, "julianische Startdatierung"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a date period object to its julian start date."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [date:DatePeriod](https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#DatePeriod); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:date](http://www.w3.org/2001/XMLSchema#date). |
## gregorianStartDating
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#gregorianStartDating>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "gregorian start dating"@en, "gregorianische Startdatierung"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a date period object to its gregorian start date."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [date:DatePeriod](https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#DatePeriod); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:date](http://www.w3.org/2001/XMLSchema#date). |
## julianEndDating
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#julianEndDating>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "julian end dating"@en, "julianische Enddatierung"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a date period object to its julian end date."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [date:DatePeriod](https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#DatePeriod); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:date](http://www.w3.org/2001/XMLSchema#date). |
## gregorianEndDating
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#gregorianEndDating>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "gregorian end dating"@en, "gregorianische Enddatierung"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a date period object to its gregorian end date."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [date:DatePeriod](https://github.com/stazh/sw-ehedaten/tree/main/ontology/date#DatePeriod); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:date](http://www.w3.org/2001/XMLSchema#date). |
