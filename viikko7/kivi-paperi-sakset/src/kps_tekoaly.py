from kps import KPS
from tekoaly import tekoaly

class KPSTekoaly(KPS):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
