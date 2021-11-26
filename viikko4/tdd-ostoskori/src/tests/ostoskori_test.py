import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_hinta_on_sama_kuin_tuotteen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        banaani = Tuote("Banaani", 6)
        self.kori.lisaa_tuote(banaani)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteiden_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        banaani = Tuote("Banaani", 6)
        self.kori.lisaa_tuote(banaani)
        self.assertEqual(self.kori.hinta(), 9)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_on_tuotteiden_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), 6)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_ostos_jolla_on_sama_nimi_ja_lukumaara_on_yksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 1)
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        banaani = Tuote("Banaani", 6)
        self.kori.lisaa_tuote(banaani)
        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_ostos(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 1)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_yksi_ostos_jolla_on_sama_nimi_ja_lukumaara_on_kaksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 2)
    
    def test_kahden_saman_tuotten_lisaamisen_ja_yhden_poistamisen_jalkeen_tuotteiden_lukumaara_on_yksi(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].lukumaara(), 1)
    
    def test_tuotteen_lisaamisen_ja_poistamisen_jalkeen_kori_on_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(len(self.kori.ostokset()), 0)