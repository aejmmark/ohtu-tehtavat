from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Pelinvalitsija:
    def __init__(self):
        self._komennot = {
            "a": KPSPelaajaVsPelaaja(),
            "b": KPSTekoaly(),
            "c": KPSParempiTekoaly()
        }
    
    def valitse_peli(self, vastaus):
        if vastaus in self._komennot:
            return self._komennot[vastaus]
        return None