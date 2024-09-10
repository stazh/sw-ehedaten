import requests
from bs4 import BeautifulSoup
import csv

class HLS_Scraper():
    """
    Dieses Script extrahiert Daten von HLS-Webseiten, welche für den Abgleich mit den Ehedaten relevant sind. 
    Die URLs der abzufragenden Webseite und weitere Metadaten werden in der Funktion import_articles - filename mitgegeben. 
    Ausgabe ist eine HLS-Checklist, mit den Feldern in fieldnames (Zeile 15).
    """
    def __init__(self):

        input_list = self.import_articles()
        with open('hls_checklist.csv', 'w', newline='') as csvfile:
            fieldnames = ['hls_id', 'url','title','gender','starttimerange','endtimerange','timeprecision','vorname','nachname','gbdatum','tddatum','heiratsdatum','heiratspartner','text']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            counter = 0
            for item in input_list:
                hls_id = item[0]
                url = item[2]
                title = item[1]
                gender = item[6]
                starttimerange = item[3]
                endtimerange = item[4]
                timeprecision = item[5]
                vorname, nachname, gbdatum, tddatum, heiratsdatum, heiratspartner,text = self.get_article_data(url)
                counter += 1
                print(counter)
                writer.writerow({'hls_id':hls_id, 'url':url,'title':title,'gender':gender,'starttimerange':starttimerange,'endtimerange':endtimerange,'timeprecision':timeprecision,'vorname':vorname,'nachname':nachname,'gbdatum':gbdatum,'tddatum':tddatum,'heiratsdatum':heiratsdatum,'heiratspartner':heiratspartner,'text':text})
        return

    def import_articles(self):
        filename = 'ZH_Bio.csv'
        url_list = []
        with open(filename, 'r') as csvfile:
            datareader = csv.reader(csvfile)
            for row in datareader:
                if len(row) > 10:
                    url_list.append([row[0],row[1],row[2],row[3],row[4],row[9],row[11]])
        url_list.pop(0)
        return url_list

    def get_article_data(self, url):
        page = requests.get(url)
        soup = BeautifulSoup(page.text, features="html.parser")
        find_vorname = soup.find('span', itemprop='givenName')
        vorname = find_vorname.text if find_vorname else ""
        find_nachname = soup.find('span', itemprop='familyName')
        nachname = find_nachname.text if find_nachname else ""
        find_gbdatum = soup.find('span', itemprop='birthDate')
        gbdatum = find_gbdatum.text if find_gbdatum else ""
        find_tddatum = soup.find('span', itemprop='deathDate')
        tddatum = find_tddatum .text if find_tddatum else ""
        find_heiratsdatum = soup.find('span', class_='hls-alli')
        heiratsdatum = find_heiratsdatum.text if find_heiratsdatum else ""
        find_text = soup.find('div', class_='hls-article-text-unit frontend-container')
        text = find_text.text if find_text else ""
        heiratspartner = ""
        if find_heiratsdatum:
            text_nach_heirat = find_heiratsdatum.next_sibling
            heiratspartner = text_nach_heirat[:text_nach_heirat.find(".")]
            if len(heiratspartner) > 0 and heiratspartner[0] == " ":
                heiratspartner = heiratspartner[1:]
        raw_text = text.replace('\n', ' ').replace('\r', '')      
        return vorname, nachname, gbdatum, tddatum, heiratsdatum, heiratspartner, raw_text


if __name__ == "__main__":
  
    HLS = HLS_Scraper()
