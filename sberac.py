from bs4 import BeautifulSoup
import requests
import sys
import csv

HLAVICKA = ["Kód obce","Název obce","Voliči v seznamu","Vydané obálky", "Platné hlasy"]
BASE_URL = "https://volby.cz/pls/ps2017nss/"
kody_list=[]
jmena_list=[]
komplet_list=[]
strany_seznam = []

# nacteni argumentu z prikazove radky a jejich kontrola
def nacti_parametry():
    parametry = sys.argv
    if len(parametry) != 3:
        print("Nebyly zadány všechny parametry ! Konec programu.")
    elif "https://volby.cz/pls/ps2017nss/" not in parametry[1]:
            print("Na první pozici není odkaz na stránku voleb.")

    elif ".csv" not in parametry[2]:
            print("Nezadán výstupní csv soubor.")
    else:
        return parametry[1],parametry[2]

# nacteni vsech obci z daneho okrsku a ulozeni do listu
def nacti_obce(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    obce = soup.find_all(class_="cislo")
    obce_jmena = soup.find_all(class_="overflow_name")
    for i in obce:
        temp=[]
        kod_obce = i.getText()
        link_obce = BASE_URL + i.find("a").get("href")
        temp.append(kod_obce)
        temp.append(link_obce)
        kody_list.append(temp)

    for i in obce_jmena:
       jmeno_obce = i.getText()
       jmena_list.append(jmeno_obce)

# vytazeni vybranych dat ze stranky pro kazdou obec
def seber_strany(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    strany = soup.find_all(class_="overflow_name")
    for s in strany:
        strany_seznam.append(s.getText())

    # print(strany_seznam)



def seber_data(url):
    temp = []

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')

    volici = soup.find(class_="cislo", headers="sa2").getText()
    temp.append(int(volici.replace(u'\xa0', '')))
    obalky = soup.find(class_="cislo", headers="sa3").getText()
    temp.append(int(obalky.replace(u"\xa0","")))

    hlasy = soup.find(class_="cislo", headers="sa6").getText()
    temp.append(int(hlasy.replace(u"\xa0","")))

    for x in range(1,4):
        try:
            strany_pocty =  soup.find_all(class_="cislo", headers=f"t{x}sa2 t{x}sb3")
            for sp in strany_pocty:
                #print(sp)
                cislo = sp.getText()
                temp.append(int(cislo.replace(u"\xa0","")))
        except:
            pass
    return temp


# stazeni dat pro jednotlive obce
def napln_data():
    print("Stahuji data...")
    obce_list = []
    seber_strany(kody_list[1][1])
    for i in range(0,len(kody_list)):
        detail = []
        obce_list.extend(kody_list[i])
        obce_list.pop(1) # odstraneni http odkazu na obec

        detail = seber_data(kody_list[i][1])
        obce_list.append(jmena_list[i])
        obce_list.extend(detail)
        komplet_list.append(obce_list)
        obce_list = []

# ulozeni sebranych vysledku do zvoleneho souboru
def uloz_data(soubor):
    temp=[]
    temp.extend(HLAVICKA)
    temp.extend(strany_seznam)
    print(f"Ukladám data do souboru {soubor}.")
    with open(soubor, "w", newline='', encoding='utf-8') as file:
        wr = csv.writer(file)

        wr.writerow(temp)
        wr.writerows(komplet_list)
    print("Data uložena. Konec programu.")

# hlavni fce pro beh programu
def ziskej_data():
        url, soubor = nacti_parametry()
        nacti_obce(url)
        napln_data()
        uloz_data(soubor)

if __name__ == "__main__":
    ziskej_data()
