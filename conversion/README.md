
Die Skripte sind in folgender Reihenfolge anzuwenden:

1. python/create_dictionaries.py (mit Parameter [OGD-Datensatz](https://www.zh.ch/de/politik-staat/opendata.html?keyword=ogd#/details/468@staatsarchiv-kanton-zuerich))

2. python/convert_archiving.py (mit Parameter [OGD-Datensatz](https://www.zh.ch/de/politik-staat/opendata.html?keyword=ogd#/details/468@staatsarchiv-kanton-zuerich) und [Daten zu den Pfarrbüchern](https://github.com/stazh/sw-ehedaten/blob/main/sourcedata/csv/Ehedaten_Baende.CSV))

3. python/convert_basic.py (mit Parameter [OGD-Datensatz](https://www.zh.ch/de/politik-staat/opendata.html?keyword=ogd#/details/468@staatsarchiv-kanton-zuerich) und [Daten zu den Pfarrbüchern](https://github.com/stazh/sw-ehedaten/blob/main/sourcedata/csv/Ehedaten_Baende.CSV))

4. python/convert_use_case_3_weekday.py (mit Parameter [OGD-Datensatz](https://www.zh.ch/de/politik-staat/opendata.html?keyword=ogd#/details/468@staatsarchiv-kanton-zuerich) und [Daten zu den Pfarrbüchern](https://github.com/stazh/sw-ehedaten/blob/main/sourcedata/csv/Ehedaten_Baende.CSV))


python/convert_default_empty.py dienst als Vorlage für weitere Anwendungsfälle 



