from kps import KPS
from tekoaly_parannettu import tekoaly_parannettu

class KPSParempiTekoaly(KPS):
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = tekoaly_parannettu.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        tekoaly_parannettu.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto
