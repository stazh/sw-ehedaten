# Ontology belief-value

| Predicate | Object |
|:-------- |:-------- |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [owl:Ontology](http://www.w3.org/2002/07/owl#Ontology); |
| [dct:license](http://purl.org/dc/terms/license) | <http://creativecommons.org/licenses/by/3.0/>; |
| [dct:title](http://purl.org/dc/terms/title) | "An ontology about belief value"@en; |
| [dct:description](http://purl.org/dc/terms/description) | """Formal description of belief value, general subclasses, related classes and properties. This ontology adopts the majority of the concepts of the unpublished ontology belief-value created in the project NIE-INE by Hans Cools and Roberta Padlina: https://github.com/nie-ine/Ontologies/blob/master/Nie-ontologies/Generic-ontologies/belief-value.ttl"""@en; |
| [dct:creator](http://purl.org/dc/terms/creator) | "Rebekka Plüss, research assistant and software developer, States Archive canton of Zürich"@en; |
| [dct:publisher](http://purl.org/dc/terms/publisher) | "States Archive canton of Zürich"@en; |
| [owl:versionInfo](http://www.w3.org/2002/07/owl#versionInfo) | "2021-11-26"^^xsd:date. |
# CLASSES
## BeliefValue
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/belief-value#BeliefValue>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "belief value"@en, "Glaubenswert"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Value of a belief in a proposition by a certain agent in a certain time."""@en; |
| [rdfs:subClassOf](http://www.w3.org/2000/01/rdf-schema#subClassOf) | [cidoc-inf:I2_Belief](http://www.ics.forth.gr/isl/CRMinf/I2_Belief); |
| [owl:oneOf](http://www.w3.org/2002/07/owl#oneOf) | (belief-value:Certain belief-value:Uncertain belief-value:VeryLikely belief-value:Likely belief-value:LessLikely belief-value:Neutral belief-value:LessUnlikely belief-value:Unlikely belief-value:VeryUnlikely belief-value:Impossible). |
# INSTANCES
## Certain
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/belief-value#Certain>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class, belief-value:BeliefValue](http://www.w3.org/2000/01/rdf-schema#Class, belief-valu); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "certain"@en, "sicher"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Belief value representing being 'true'."""@en. |
## Uncertain
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/belief-value#Uncertain>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class, belief-value:BeliefValue](http://www.w3.org/2000/01/rdf-schema#Class, belief-valu); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "uncertain"@en, "unsicher"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Belief value representing that being 'true' can not be assured."""@en. |
## VeryLikely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/belief-value#VeryLikely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class, belief-value:BeliefValue](http://www.w3.org/2000/01/rdf-schema#Class, belief-valu); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "very likely"@en, "sehr warscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Belief value representing a high probability of being true."""@en. |
## Likely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <hhttps://github.com/stazh/sw-ehedaten/tree/main/ontology/belief-value#Likely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class, belief-value:BeliefValue](http://www.w3.org/2000/01/rdf-schema#Class, belief-valu); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "likely"@en, "warscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Belief value representing a moderate probability of being true."""@en. |
## LessLikely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/belief-value#LessLikely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class, belief-value:BeliefValue](http://www.w3.org/2000/01/rdf-schema#Class, belief-valu); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "less likely"@en, "wenig warscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Belief value representing a low probability of being true."""@en. |
## Neutral
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/belief-value#Neutral>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class, belief-value:BeliefValue](http://www.w3.org/2000/01/rdf-schema#Class, belief-valu); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "neutral"@en, "neutral"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Belief value representing being neither true nor false."""@en. |
## LessUnlikely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/belief-value#LessUnlikely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class, belief-value:BeliefValue](http://www.w3.org/2000/01/rdf-schema#Class, belief-valu); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "less unlikely"@en, "wenig unwarscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Belief value representing a low probability of being false."""@en. |
## Unlikely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/belief-value#Unlikely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class, belief-value:BeliefValue](http://www.w3.org/2000/01/rdf-schema#Class, belief-valu); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "unlikely"@en, "unwarscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Belief value representing a moderate probability of being false."""@en. |
## VeryUnlikely
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/belief-value#VeryUnlikely>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class, belief-value:BeliefValue](http://www.w3.org/2000/01/rdf-schema#Class, belief-valu); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "very unlikely"@en, "sehr unwarscheinlich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Belief value representing a high probability of being false."""@en. |
## Impossible
| Predicate | Object |
|:-------- |:-------- |
| [rdfs:isDefinedBy](http://www.w3.org/2000/01/rdf-schema#isDefinedBy) | <https://github.com/stazh/sw-ehedaten/tree/main/ontology/belief-value#Impossible>; |
| [rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | [rdfs:Class](http://www.w3.org/2000/01/rdf-schema#Class); |
| [rdfs:label](http://www.w3.org/2000/01/rdf-schema#label) | "impossible"@en, "unmöglich"@de; |
| [rdfs:comment](http://www.w3.org/2000/01/rdf-schema#comment) | """Belief value representing being 'false'."""@en. |