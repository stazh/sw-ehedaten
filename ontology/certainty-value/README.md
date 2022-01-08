# Ontology certainty-value

<div align="center"><img src="archiving.jpg" width="600"></div>

| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:Ontology](http://www.w3.org/2002/07/owl#Ontology); |
| [dct:license](http://purl.org/dc/terms/license) | <http://creativecommons.org/licenses/by/3.0/>; |
| [dct:title](http://purl.org/dc/terms/title) | "An ontology about certainty value"@en; |
| [dct:description](http://purl.org/dc/terms/description) | """Formal description of certainty value, general subclasses, related classes and properties. This ontology adopts the majority of the concepts of the unpublished ontology belief-value created in the project NIE-INE by Hans Cools and Roberta Padlina: https://github.com/nie-ine/Ontologies/blob/master/Nie-ontologies/Generic-ontologies/belief-value.ttl"""@en; |
| [dct:creator](http://purl.org/dc/terms/creator) | "Rebekka Plüss, research assistant and software developer, States Archive canton of Zürich"@en; |
| [dct:publisher](http://purl.org/dc/terms/publisher) | "States Archive canton of Zürich"@en; |
| [owl:versionInfo](http://www.w3.org/2002/07/owl#versionInfo) | "2021-11-26"^^xsd:date. |
# CLASSES
## CertaintyValue
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#CertaintyValue>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "Certainty value"@en, "Glaubenswert"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Value of a certainty in a proposition by a certain agent in a certain time."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [cidoc-inf:I2_Belief](http://www.ics.forth.gr/isl/CRMinf/I2_Belief); |
| [owl:oneOf](http://www.w3.org/2002/07/owl#oneOf) | (certainty-value:Certain, certainty-value:Uncertain, certainty-value:VeryLikely, certainty-value:Likely, certainty-value:LessLikely, certainty-value:Neutral, certainty-value:LessUnlikely, certainty-value:Unlikely, certainty-value:VeryUnlikely, certainty-value:Impossible). |
# INSTANCES
## Certain
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#Certain>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [certainty-value:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "certain"@en, "sicher"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing being 'true'."""@en. |
## Uncertain
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#Uncertain>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [certainty-value:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "uncertain"@en, "unsicher"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing that being 'true' can not be assured."""@en. |
## VeryLikely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#VeryLikely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [certainty-value:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "very likely"@en, "sehr warscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a high probability of being true."""@en. |
## Likely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <hhttps://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#Likely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [certainty-value:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "likely"@en, "warscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a moderate probability of being true."""@en. |
## LessLikely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#LessLikely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [certainty-value:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "less likely"@en, "wenig warscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a low probability of being true."""@en. |
## Neutral
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#Neutral>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [certainty-value:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "neutral"@en, "neutral"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing being neither true nor false."""@en. |
## LessUnlikely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#LessUnlikely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [certainty-value:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "less unlikely"@en, "wenig unwarscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a low probability of being false."""@en. |
## Unlikely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#Unlikely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [certainty-value:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "unlikely"@en, "unwarscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a moderate probability of being false."""@en. |
## VeryUnlikely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#VeryUnlikely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [certainty-value:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "very unlikely"@en, "sehr unwarscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing a high probability of being false."""@en. |
## Impossible
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#Impossible>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [certainty-value:CertaintyValue](https://github.com/stazh/sw-ehedaten/tree/main/ontology/certainty-value#CertaintyValue); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "impossible"@en, "unmöglich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Certainty value representing being 'false'."""@en. |
