from random import choice
from Zwierze import Zwierze, dostepnePlci


class Wilk(Zwierze):

    def __init__(self, zasiegWidzenia, plec=None):
        if plec == None:
            plec = choice(dostepnePlci)
        Zwierze.__init__(self, plec, zasiegWidzenia)
        print(plec)

    # ZDECHNIĘCIE WILKA
    def __del__(self):
        super().__del__()

    def __str__(self):
        return "Poziom tłuszczu wilka: " + str(self.poziomTluszczu)

    # ZJEDZENIE ZAJĄCA
    def zezera(self, zajac):
        self.poziomTluszczu += 10
        zajac.__del__()
        super.zezera()

    # PORUSZANIE SIĘ (spalanie tłuszczu przy ruchu)
    def ruchZwierza(self, pole):
        self.poziomTluszczu -= 5
        super().ruchZwierza(pole)

    #TODO: LOGIKA (cały algorytm) PORUSZANIA SIE
