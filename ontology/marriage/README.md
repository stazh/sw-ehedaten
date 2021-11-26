# Ontology marriage
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:Ontology](http://www.w3.org/2002/07/owl#Ontology); |
| [dct:license](http://purl.org/dc/terms/license) | <http://creativecommons.org/licenses/by/3.0/>; |
| [dct:title](http://purl.org/dc/terms/title) | "An ontology about marriage"@en; |
| [dct:description](http://purl.org/dc/terms/description) | """Formal description of a marriage, general subclasses, related classes and properties."""@en; |
| [dct:creator](http://purl.org/dc/terms/creator) | "Rebekka Plüss, research assistant and software developer, States Archive canton of Zürich"@en; |
| [dct:publisher](http://purl.org/dc/terms/publisher) | "States Archive canton of Zürich"@en; |
| [owl:versionInfo](http://www.w3.org/2002/07/owl#versionInfo) | "2021-11-26"^^xsd:date. |
# CLASSES
## Marriage
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage"@en, "Heirat"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Marriage as the event of the union of two people."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [nie-ine-event:Event](http://e-editiones.ch/ontology/event#Event). |
## ParishBook
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "parish book"@en, "Pfarrbuch"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """The book in which a marriage is registered resp. the marriage entry is written."""@en. |
## MarriageEntry
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry"@en, "Eheeintrag"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Marriage entry as a note by the parish priest in a parish book stating that two persons were married on a certain day."""@en. |
## Bride
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "bride"@en, "Braut"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Role of a woman marrying."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [nie-ine-human:PersonRole](http://e-editiones.ch/ontology/human#PersonRole). |
## Bridegroom
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "bridegroom"@en, "Bräutigam"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Role of a man marrying."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [nie-ine-human:PersonRole](http://e-editiones.ch/ontology/human#PersonRole). |
# PROPERTIES
## marriageEntryIsInParishBook
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry is in parish book"@en, "Eheeintrag befindet sich in Pfarrbuch"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to its parish book in which it is written."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [marriage:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [marriage:ParishBook](https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#ParishBook). |
## marriageEntryHasCommentToWoman
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry has comment to woman"@en, "Eheeintrag hat Anmerkung zu Frau"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to the comment written as a note next to the woman registered in the entry."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [marriage:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal). |
## marriageEntryHasGeneralCommentOrCommentToMan
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry has general comment or comment to man"@en, "Eheeintrag hat allgemeine Anmerkung oder Anmerkung zu Mann"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to the comment written as a note next to the man registered in the entry. It mustn't be a comment to the man, it can also be a general comment to the marriage."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [marriage:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/marriage#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal). |
