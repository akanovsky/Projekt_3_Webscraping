##1. Popis projektu

Program sberac.py projde výsledky voleb pro vybraný volební okrsek a uloží do výstupního csv souboru vybrané data pro jednotlivé obce z daného okrsku.
Data čerpá z odkazu, který musí směrovat na stránky ČSÚ, viz ukázka projektu.   
data, která program sběrač u každé obce načte a uloží do výstupního souboru :
- kód obce
- název obce
- voliči v seznamu
- vydané obálky
- platné hlasy
- kandidující strany


##2. Instalace potřebných knihoven

Před spuštěním je třeba stáhnout extra moduly, které program pro běh využívá. Jejich seznam je uveden v souboru requirements.txt.
Instalaci provedete následujícím příkazem :

`pip install -r requirements.txt`

##3. Ukázka projektu

Výsledky voleb pro okrsek Uherské Hradiště

    1. argument - https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202
    2. argument - vysledky_UH.csv

   Spuštění programu :
    
    python sberac.py "https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=13&xnumnuts=7202" vysledky_UH.csv
    
Průběh stahování:


Ukázka výstupu :

    Kód obce,Název obce,Voliči v seznamu,Vydané obálky,Platné hlasy,Kandidující strany...
    592013,Babice,1452,873,866,Občanská demokratická strana,Řád národa - Vlastenecká unie,...
    592021,Bánov,1707,1070,1063,Občanská demokratická strana,Řád národa - Vlastenecká unie,...
    592030,Bílovice,1473,1018,1008,Občanská demokratická strana,Řád národa - Vlastenecká unie,..

