# Ontology elodzh
## Modell
<div align="center"><img src="marriage_model.jpg" width="800"></div>

## Beispiel
<div align="center"><img src="marriage_example.png" width="800"></div>

## Definition der Klassen und Beziehungen
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:Ontology](http://www.w3.org/2002/07/owl#Ontology); |
| [dct:license](http://purl.org/dc/terms/license) | <http://creativecommons.org/licenses/by/3.0/>; |
| [dct:title](http://purl.org/dc/terms/title) | "An ontology about marriage entries from the 16th to 18th century in Zürich"@en; |
| [dct:description](http://purl.org/dc/terms/description) | """Formal description marriage entries, general subclasses, related classes and properties."""@en; |
| [dct:creator](http://purl.org/dc/terms/creator) | "Rebekka Plüss, research assistant and software developer, States Archive canton of Zürich"@en; |
| [dct:publisher](http://purl.org/dc/terms/publisher) | "States Archive canton of Zürich"@en; |
| [owl:versionInfo](http://www.w3.org/2002/07/owl#versionInfo) | "2022-05-23"^^xsd:date. |

# CLASSES
## Wedding
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Wedding"@en, "Heirat"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Wedding as the event of the union of two people."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [nie-ine-event:Event](http://e-editiones.ch/ontology/event#Event). |
## MarriageProclamation
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Marriage proclamation"@en, "Heiratsverkündung"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Marriage proclamation as the event of the proclamation of the union of two people in future."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [nie-ine-event:Event](http://e-editiones.ch/ontology/event#Event). |
## ParishBook
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Parish book"@en, "Pfarrbuch"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """The book in which a wedding or marriage proclamation is registered resp. the marriage entry is written."""@en. |
## MarriageEntry
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Marriage entry"@en, "Eheeintrag"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Marriage entry as a note by the parish priest in a parish book stating that two persons were married on a certain day or that the marriage of two persons is proclaimed on a certain day."""@en. |
## :Parish
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Parish"@en, "Kirchgemeinde"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Parish as a religious organization that conducts preaching and usually has an associated church."""@en. |
## Person
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Person"@en, "Person"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """A real born human"""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [nie-ine-human:Person](http://e-editiones.ch/ontology/human#Person). |
## Woman
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Woman"@en, "Frau"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """A real born human with female sex"""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [elodzh:Person](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Person). |
## Man
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Man"@en, "Mann"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """A real born human with male sex"""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [elodzh:Person](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Person). |
## Place
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Place"@en, "Ort"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """A place with political boundaries. It's f.e. a village, town or city."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [rico:Place](https://www.ica.org/standards/RiC/ontology#Place). |
## CertaintyValue
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Certainty value"@en, "Sicherheitswert"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Value of a certainty in a proposition by a certain agent in a certain time."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [cidoc-inf:I2_Belief](http://www.ics.forth.gr/isl/CRMinf/I2_Belief); |
| [owl:oneOf](http://www.w3.org/2002/07/owl#oneOf) | [elodzh:Certain elodzh:Uncertain elodzh:VeryLikely elodzh:Likely elodzh:LessLikely elodzh:Neutral elodzh:LessUnlikely elodzh:Unlikely elodzh:VeryUnlikely elodzh:Impossible](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Certain elodz). |
# INSTANCES
## Certain
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "certain"@en, "sicher"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing being 'true'."""@en. |
## Uncertain
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "uncertain"@en, "unsicher"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing that being 'true' can not be assured."""@en. |
## VeryLikely
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "very likely"@en, "sehr warscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a high probability of being true."""@en. |
## Likely
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "likely"@en, "warscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a moderate probability of being true."""@en. |
## LessLikely
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "less likely"@en, "wenig warscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a low probability of being true."""@en. |
## Neutral
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "neutral"@en, "neutral"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing being neither true nor false."""@en. |
## LessUnlikely
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "less unlikely"@en, "wenig unwarscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a low probability of being false."""@en. |
## Unlikely
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "unlikely"@en, "unwarscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a moderate probability of being false."""@en. |
## VeryUnlikely
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "very unlikely"@en, "sehr unwarscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a high probability of being false."""@en. |
## Impossible
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "impossible"@en, "unmöglich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing being 'false'."""@en. |
# PROPERTIES
## marriageEntryIsInParishBook
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry is in parish book"@en, "Eheeintrag befindet sich in Pfarrbuch"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to its parish book in which it is written."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [elodzh:ParishBook](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#ParishBook). |
## marriageEntryHasCommentToWoman
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry has comment to woman"@en, "Eheeintrag hat Anmerkung zu Frau"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to the comment written as a note next to the woman registered in the entry."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal). |
## marriageEntryHasGeneralCommentOrCommentToMan
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry has general comment or comment to man"@en, "Eheeintrag hat allgemeine Anmerkung oder Anmerkung zu Mann"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to the comment written as a note next to the man registered in the entry. It mustn't be a comment to the man, it can also be a general comment to the marriage."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal). |
## parishBookIsKeptByParish
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "parish book is kept by parish"@en, "Pfarrbuch wird geführt von Kirchgemeinde"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a parish book to the parish in which it is kept."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:ParishBook](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#ParishBook); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [elodzh:Parish](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Parish). |
## marriageEntryRegistersWoman
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry registers woman"@en, "Eheeintrag registriert Frau"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to the woman it registers."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [elodzh:Woman](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Woman). |
## marriageEntryRegistersMan
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry registers man"@en, "Eheeintrag registriert Mann"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to the man it registers."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [elodzh:Man](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Man). |
## marriageEntryHasDatingOnDate
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry has dating on date"@en, "Eheeintrag hat Datierung auf Datum"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to its registered gregorian date (julian datings were converted into gregorian dating)."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:date](http://www.w3.org/2001/XMLSchema#date). |
## marriageEntryHasDatePeriodStartDate
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry has date period start date"@en, "Eheeintrag hat Datumsperiode-Startdatum"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to the date period startdate (startdate of the period within its dating is possible)."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:date](http://www.w3.org/2001/XMLSchema#date). |
## marriageEntryHasDatePeriodEndDate
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry has date period end date"@en, "Eheeintrag hat Datumsperiode-Enddatum"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to the date period enddate (enddate of the period within its dating is possible)."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:date](http://www.w3.org/2001/XMLSchema#date). |
## marriageEntryDocumentsMarriageProclamationWithCertaintyValue
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry documents marriage proclamation with certainty value"@en, "Eheeintrag dokumentiert Eheverkündung mit Sicherheitswert"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to the certainty value with which it is possible, that the marriage entry documents a marriage proclamation."""@en, """Ein Eheeintrag betrifft entweder eine Verkündung (Proclamation) oder eine Trauung (Wedding): a) Fällt die Datierung eines Eheeintrags auf den Sonntag, so betrifft dieser ab 1620 (Verbot von Sonntagsheiraten) sehr wahrscheinlich eine Verkündung. b) Vermerkte der Editor '[Verkünddatum]' in den Zusatzinformationen eines Eheeintrags oder steht 'promulgiert' oder 'proklamiert' so betrifft dieser sehr wahrscheinlich eine Verkündung. c) Steht in den Zusatzinformationen eines Eheeintrags 'getraut zu ', so betrifft dieser sehr wahrscheinlich eine Verkündung. Trifft a, b und c nicht zu, so betrifft der Eheeintrag wahrscheinlich die Trauung (Wedding)."""@de; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue). |
## marriageEntryDocumentsWeddingWithCertaintyValue
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry documents wedding with certainty value"@en, "Eheeintrag dokumentiert Heirat mit Sicherheitswert"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to the certainty value with which it is possible, that the marriage entry documents a wedding."""@en, """Ein Eheeintrag betrifft entweder eine Verkündung (Proclamation) oder eine Trauung (Wedding): a) Fällt die Datierung eines Eheeintrags auf den Sonntag, so betrifft dieser ab 1620 (Verbot von Sonntagsheiraten) sehr wahrscheinlich eine Verkündung. b) Vermerkte der Editor '[Verkünddatum]' in den Zusatzinformationen eines Eheeintrags oder steht 'promulgiert' oder 'proklamiert' so betrifft dieser sehr wahrscheinlich eine Verkündung. c) Steht in den Zusatzinformationen eines Eheeintrags 'getraut zu ', so betrifft dieser sehr wahrscheinlich eine Verkündung. Trifft a, b und c nicht zu, so betrifft der Eheeintrag wahrscheinlich die Trauung (Wedding)."""@de; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [elodzh:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#CertaintyValue). |
## parishHasNameLiteral 
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "parish has name literal"@en, "Kirchgemeinde hat Namenliteral"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a parish to the literal of its name."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:Parish](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Parish); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal). |
## parishHasSeatAtPlace 
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "parish has seat at place"@en, "Kirchgemeinde hat Sitz an Ort"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a parish to its place where it has its seat at."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:Parish](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Parish); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [elodzh:Place](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Place). |
## personHasFirstNameLiteral
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "person has first name literal"@en, "Person hat Vornamenliteral"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a person to the literal of its first name"""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:Person](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Person); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal). |
## personHasLastNameLiteral
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "person has last name literal"@en, "Person hat Nachnamenliteral"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a person to the literal of its last name"""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:Person](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Person); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal). |
## personHasPlaceOfOrigin
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "person has place of origin"@en, "Person hat Herkunftsort"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a person to its place of origin"""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:Person](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Person); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [elodzh:Place](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Place). |
## personHasEncyclopediaArticleURL
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "person has encyclopedia article URL"@en, "Person hat Lexikonartikel URL"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a person to its encyclopedia article URL."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:EncyclopediaArticle](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#EncyclopediaArticle); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI). |
## placeHasNameLiteral
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "place has name literal"@en, "Ort hat Namensliteral"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a place to the literal of its name."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:Place](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#Place); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [rdfs:Literal](http://www.w3.org/2000/01/rdf-schema#Literal). |
## marriageEntryHasRecordWebpageURI
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "marriage entry has record webpage URI"@en, "Eheeintrag hat Archivkatalogeintrag-URI"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a marriage entry to the record webpage uri of the entry in an archive information system."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:MarriageEntry](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#MarriageEntry); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI). |
## parishBodkHasRecordWebpageURI
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:DatatypeProperty](http://www.w3.org/2002/07/owl#DatatypeProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "parish book has record webpage URI"@en, "Pfarrbuch hat Archivkatalogeintrag-URI"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a parish book to the record webpage uri of the entry in an archive information system."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [elodzh:ParishBook](https://github.com/stazh/sw-ehedaten/tree/main/ontology/elodzh#ParishBook); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [xsd:anyURI](http://www.w3.org/2001/XMLSchema#anyURI). |
