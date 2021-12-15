from pelinvalitsija import Pelinvalitsija

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        pelinvalitsija = Pelinvalitsija()
        vastaus = input()
        peli = pelinvalitsija.valitse_peli(vastaus)
        
        if peli is not None:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen \
                    siirron eli jonkun muun kuin k, p tai s"
            )
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
