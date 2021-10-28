# Ontology archiving
| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:Ontology](http://www.w3.org/2002/07/owl#Ontology); |
| [dct:license](http://purl.org/dc/terms/license) | <http://creativecommons.org/licenses/by/3.0/>; |
| [dct:title](http://purl.org/dc/terms/title) | "An ontology about archiving"@en; |
| [dct:description](http://purl.org/dc/terms/description) | """Formal description of a record, general subclasses, related classes and properties."""@en; |
| [dct:creator](http://purl.org/dc/terms/creator) | "Rebekka Plüss, research assistant and software developer, States Archive canton of Zürich"@en; |
| [dct:contributor](http://purl.org/dc/terms/contributor) | "Hans Cools, MD, knowledge engineer, ontologist, software developer, University of Basel, Switzerland"@en; |
| [dct:publisher](http://purl.org/dc/terms/publisher) | "States Archive canton of Zürich"@en; |
| [owl:versionInfo](http://www.w3.org/2002/07/owl#versionInfo) | "2021-10-17"^^xsd:date. |
# CLASSES
## Record
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record"@en, "Archiveinheit"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """A record as an entry in an Archive Information System with metadata, which describe the instantiation of the record."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [rico:Record](https://www.ica.org/standards/RiC/ontology#Record). |
## RecordPart
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record part"@en, "Teil einer Archiveinheit"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """A record part as an entry in an Archive Information System with metadata, which describe the instantiation of the record part."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [rico:RecordPart](https://www.ica.org/standards/RiC/ontology#RecordPart). |
## Title
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "title"@en, "Titel"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """The title of the record or the record part."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [rico:Tilte](https://www.ica.org/standards/RiC/ontology#Tilte). |
## CarrierType
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Carrier type"@en, "Trägertyp"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """The physical or electronical carrier of the instantiation of the record, the archival material type. This can be, f. e. paper, digital image,..."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [rico:CarrierType](https://www.ica.org/standards/RiC/ontology#CarrierType). |
## Provenance
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "provenance"@en, "Provenienz"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """The agent (f.e. organization, person), which created the record originally for its own purposes."""@en. |
## Instantiation
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "instantiation"@en, "Ausprägung"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """The archived thing to which the record or the record part refers."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [rico:Instantiation](https://www.ica.org/standards/RiC/ontology#Instantiation). |
## Volume
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "volume"@en, "Band"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Volume as type of the carrier resp. the archival material type. It is also a special book: One book of a serie of books. One serie is a set of books which are mostly created for the same purpose by the same provenance."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [archiving:CarrierType](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#CarrierType). |
## DescriptiveNote
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "descriptive Note"@en, "Zusatzinformation"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Some information about a record or record part. Can be of any kind."""@en. |
## Identifier
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "identifier"@en, "Identifikator"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """The identifying mark with which a record or an record part or instantiation of it can be clearly identified and referenced. In the context of an archive information system, this is usually the signature."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [rico:Identifier](https://www.ica.org/standards/RiC/ontology#Identifier). |
## Title
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "title"@en, "Titel"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [rico:Title](https://www.ica.org/standards/RiC/ontology#Title). |
## Date
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "date"@en, "Entstehungszeitraum"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """The date when the archived item was originally created."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [rico:Date](https://www.ica.org/standards/RiC/ontology#Date). |
## Webpage
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "webpage"@en, "Webseite"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Webpage of the record or record part in an archive information system."""@en. |
## Reference
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "reference"@en, "Referenz"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """A reference to the instantiation of a record or record part."""@en. |
# PROPERTIES
## recordHasRecordPart
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record has record part"@en, "Archiveinheit hat Archiveinheitteil"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:Record](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Record); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:RecordPart](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#RecordPart); |
| [rdfs:subPropertyOf](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) | [rico:hasOrHadPart](https://www.ica.org/standards/RiC/ontology#hasOrHadPart). |
## recordHasInstantiation
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record has webpage"@en, "Archiveinheit hat Webseite"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a record to its instantiation."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:Record](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Record); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Instantiation](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Instantiation); |
| [rdfs:subPropertyOf](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) | [rico:hasInstantiation](https://www.ica.org/standards/RiC/ontology#hasInstantiation). |
## recordPartHasInstantiation
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record part has webpage"@en, "Archiveinheitteil hat Webseite"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a record part to its instantiation."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:RecordPart](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#RecordPart); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Instantiation](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Instantiation); |
| [rdfs:subPropertyOf](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) | [rico:hasInstantiation](https://www.ica.org/standards/RiC/ontology#hasInstantiation). |
## instantiationHasCarrierType
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "instantiation has carrier type"@en, "Ausprägung hat Trägertyp"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a archive record to its physical or electronical carrier."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:Instantiation](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Instantiation); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:CarrierType](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#CarrierType); |
| [rdfs:subPropertyOf](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) | [rico:hasCarrierType](https://www.ica.org/standards/RiC/ontology#hasCarrierType). |
## recordHasTitle
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record has title"@en, "Archiveinheit hat Titel"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:Record](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Record); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Title](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Title); |
| [rdfs:subPropertyOf](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) | [rico:hasOrHadTitle](https://www.ica.org/standards/RiC/ontology#hasOrHadTitle). |
## recordPartHasTitle
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record part has title"@en, "Archiveinheitteil hat Titel"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:RecordPart](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#RecordPart); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Title](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Title); |
| [rdfs:subPropertyOf](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) | [rico:hasOrHadTitle.](https://www.ica.org/standards/RiC/ontology#hasOrHadTitle.)  |
## recordIsIdentifiedByIdentifier 
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record is identified by identifier"@en, "Archiveinheit wird identifiziert mit Identifikator."@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:Record](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Record); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Identifier](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Identifier). |
## recordPartIsIdentifiedByIdentifier 
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record part is identified by identifier"@en, "Archiveinheiteil wird identifiziert mit Identifikator."@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:RecordPart](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#RecordPart); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Identifier](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Identifier). |
## instantiationIsIdentifiedByIdentifier 
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "instantiation is identified by identifier"@en, "Ausprägung wird identifiziert mit Identifikator."@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:Instantiation](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Instantiation); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Identifier](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Identifier). |
## recordIsheldbyArchive
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record is held by archive"@en, "Archivdatensatz wird geführt von Archiv"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a record to its archive in which it is stored and recorded. The archive is responsible for the publishing and managing of the record."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:Record](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Record); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Archive. #TOD](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Archive. #TOD)O |
## recordHasProvenance
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record has provenance"@en, "Archiveinheit hat Provenienz"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a record to the agent, which originally created the record for its own purposes."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:Record](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Record); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Provenance](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Provenance); |
| [rdfs:subPropertyOf](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) | [rico:hasProvenance](https://www.ica.org/standards/RiC/ontology#hasProvenance). |
## recordPartHasProvenance
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record part has provenance"@en, "Archiveinheitteil hat Provenienz"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a record part to the agent, which originally created the record part for its own purposes."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:RecordPart](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#RecordPart); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Provenance](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Provenance); |
| [rdfs:subPropertyOf](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) | [rico:hasProvenance](https://www.ica.org/standards/RiC/ontology#hasProvenance). |
## recordHasWebpage
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record has webpage"@en, "Archiveinheit hat Webseite"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a record to the webpage of the entry in an archive information system."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:Record](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Record); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Webpage](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Webpage). |
## recordPartHasWebpage
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record part has webpage"@en, "Archiveinheitteil hat Webseite"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a record part to the webpage of the entry in an archive information system."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:RecordPart](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#RecordPart); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Webpage](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Webpage). |
## recordHasDescriptiveNote
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record has descriptive note"@en, "Archiveinheit hat Zusatzinformation"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a record to the some further information about it, which can be of any kind."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:Record](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Record); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:DescriptiveNote](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#DescriptiveNote); |
| [rdfs:subPropertyOf](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) | [rico:descriptiveNote](https://www.ica.org/standards/RiC/ontology#descriptiveNote). |
## recordHPartHasDescriptiveNote
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record part has descriptive note"@en, "Archiveinheitteil hat Zusatzinformation"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating a record part to the some further information about it, which can be of any kind."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:RecordPart](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#RecordPart); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:DescriptiveNote](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#DescriptiveNote); |
| [rdfs:subPropertyOf](http://www.w3.org/2000/01/rdf-schema#subPropertyOf) | [rico:descriptiveNote](https://www.ica.org/standards/RiC/ontology#descriptiveNote). |
## isRepresentedByRecord
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "is represented by record"@en, "wird durch Archiveinheit dargestellt"; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating something in the world (an event, a thing...) to the record it is represented by."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [archiving:Record](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Record); |
| [owl:inverseOf](http://www.w3.org/2002/07/owl#inverseOf) | [archiving:recordRepresents](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#recordRepresents). |
## recordRepresents
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:ObjectProperty](http://www.w3.org/2002/07/owl#ObjectProperty); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "record represents"@en, "Archiveinheit stellt dar"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Relating an record to what (an event, a thing...) it represents."""@en; |
| [rdfs:domain](http://www.w3.org/2000/01/rdf-schema#domain) | [archiving:Record](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#Record); |
| [rdfs:range](http://www.w3.org/2000/01/rdf-schema#range) | [rdfs:Resource](http://www.w3.org/2000/01/rdf-schema#Resource); |
| [owl:inverseOf](http://www.w3.org/2002/07/owl#inverseOf) | [archiving:isRepresentedByRecord](https://github.com/stazh/sw-ehedaten/tree/main/ontology/archiving#isRepresentedByRecord). |
