from random import choice
from Zwierze import Zwierze, dostepnePlci


class Zajac(Zwierze):

    def __init__(self, zasiegWidzenia, plec=None):
        if plec == None:
            plec = choice(dostepnePlci)
        Zwierze.__init__(self, plec, zasiegWidzenia)

    # ZDECHNIĘCIE ZAJĄCA
    def __del__(self):
        super().__del__()

    def zezera(self, ileZajecy):
        self.poziomTluszczu += 10 / ileZajecy

        super().zezera()

    # PORUSZANIE SIĘ (spalanie tłuszczu przy ruchu)
    def ruchZwierza(self, pole):
        self.poziomTluszczu -= 3
        super().ruchZwierza(pole)

    # TODO: LOGIKA PORUSZANIA SIE
