# Wissensnetz der Zürcher Ehedaten 16. - 18. Jh. (angereicherte Version) 

Die Daten liegen im Moment auf keinem öffentlichen Tripplestore. Sie können aber problemlos in einen lokalen Tripplestore geladen und abgefragt werden. Am besten eignet sich dafür Appache Jena Fuseki:

Lade die Fuseki-Distribution von der offiziellen [Apache Jena Webseite](https://jena.apache.org/download/index.cgi) herunter (zum Zeitpunkt der Erstellung dieser Anleitung: *apache-jena-fuseki-5.1.0.zip*). Entzippe die zip-Datei in einem Verzeichnis deiner Wahl.

Öffne ein Terminal oder eine Eingabeaufforderung und navigiere zu dem Verzeichnis, in dem du Fuseki entpackt hast. Starte den Server mit:

```bash
./fuseki-server
```
Ruf nun folgenden Link im Browser auf:

```
http://localhost:3030/
```

Über *manage* kannst du nun ein neues Datenset erstellen (am besten mit Option *persistent*), alle [Daten](data) und Turtle-Dateien aller [Ontologien](ontology) hochladen und mit den [Beispielabfragen](queries) starten.

