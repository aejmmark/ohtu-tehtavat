KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, luku):
        for i in range(0, self.alkioiden_lkm):
            if luku == self.ljono[i]:
                return True
        return False

    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.ljono[self.alkioiden_lkm] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1
            if self.alkioiden_lkm % len(self.ljono) == 0:
                aputaulukko = self.ljono
                self.ljono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(aputaulukko, self.ljono)
            return True
        return False

    def poista(self, luku):
        for i in range(0, self.alkioiden_lkm):
            if luku == self.ljono[i]:
                self.ljono[i] = 0
                for j in range(i, self.alkioiden_lkm - 1):
                    self.ljono[j] = self.ljono[j + 1]
                self.alkioiden_lkm = self.alkioiden_lkm - 1
                return True
        return False

    def kopioi_taulukko(self, taulukko_a, taulukko_b):
        for i in range(0, len(taulukko_a)):
            taulukko_b[i] = taulukko_a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm
        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]
        return taulu

    @staticmethod
    def yhdiste(joukko_a, joukko_b):
        uusi = IntJoukko()
        for i in range(0, max(joukko_a.mahtavuus(),
        joukko_b.mahtavuus())):
            uusi.lisaa(joukko_a.ljono[i])
            uusi.lisaa(joukko_b.ljono[i])
        return uusi

    @staticmethod
    def leikkaus(joukko_a, joukko_b):
        uusi = IntJoukko()
        for i in range(0, max(joukko_a.mahtavuus(),
        joukko_b.mahtavuus())):
            if (joukko_b.kuuluu(joukko_a.ljono[i])):
                uusi.lisaa(joukko_a.ljono[i])
        return uusi

    @staticmethod
    def erotus(joukko_a, joukko_b):
        uusi = IntJoukko()
        for i in range(0, joukko_a.mahtavuus()):
            if not (joukko_b.kuuluu(joukko_a.ljono[i])):
                uusi.lisaa(joukko_a.ljono[i])
        return uusi

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        tuloste = "{"
        for i in range(0, self.alkioiden_lkm - 1):
            tuloste = tuloste + str(self.ljono[i]) + ", "
        tuloste = tuloste + str(self.ljono[self.alkioiden_lkm - 1]) + "}"
        return tuloste
