from random import choice
from Zwierze import Zwierze, dostepnePlci
from Zajac import Zajac


class Wilk(Zwierze):
    poziomTluszczu = 100

    def __init__(self, zasiegWidzenia, plec=choice(dostepnePlci)):
        Zwierze.__init__(self, plec, zasiegWidzenia)

    def __del__(self):
        # TODO:Zdycha
        # print("Wilk też umarł")
        pass

    def __str__(self):
        return "Poziom tłuszczu wilka: " + str(self.poziomTluszczu)

    def zezera(self, zajac):
        print("*Kłap kłap*")
        self.poziomTluszczu += 10
        zajac.__del__()

    def ruchZwierza(self, pole):
        self.poziomTluszczu -= 5
        super().ruchZwierza(pole)