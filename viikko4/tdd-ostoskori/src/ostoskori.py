from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoslista = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        sum = 0
        for x in self.ostoslista.values():
            sum = sum + x.lukumaara()
        return sum
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        sum = 0
        for x in self.ostoslista.values():
            sum = sum + x.hinta()
        return sum
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        if self.ostoslista.get(lisattava.nimi()) == None:
            self.ostoslista[lisattava.nimi()] = Ostos(lisattava)
        else:  
            self.ostoslista[lisattava.nimi()].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        self.ostoslista[poistettava.nimi()].muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        values = self.ostoslista.values()
        return list(values)
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on