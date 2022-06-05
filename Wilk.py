from random import choice
from Zwierze import Zwierze, dostepnePlci
from Cel import Cel
from Zajac import Zajac


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
        return "Poziom tłuszczu wilka: " + str(self.poziomTluszczu) + \
               "\nx: " + str(self.pole.x) + "    y: " + str(self.pole.y) + "\n"

    # ZJEDZENIE ZAJĄCA
    def zezera(self, zajac):
        self.poziomTluszczu += 10
        zajac.__del__()
        super.zezera()

    # PORUSZANIE SIĘ (spalanie tłuszczu przy ruchu)
    def ruchZwierza(self, pole):
        self.poziomTluszczu -= 5
        super().ruchZwierza(pole)

    # LOGIKA (cały algorytm) PORUSZANIA SIE WILKÓW
    def gdzieWykonacRuch(self):
        dostepneCele = []
        self.patrze()

        # poziom tłuszczu < 40 -> goń zająca
        if (self.poziomTluszczu <= 40):
            for widok in self.arr_zwierz:
                for zwierze in widok.zwierzetaNaPolu:
                    if isinstance(zwierze, Zajac):
                        dostepneCele.append(Cel(self.pole, widok.pole))
            pass

        # poziom tłuszczu > 40 && poziom tłuszczu < 60 -> chodź
        if (self.poziomTluszczu > 40 and self.poziomTluszczu <= 60):
            if (self.pole.poleZDolu):
                dostepneCele.append(Cel(self.pole, self.pole.poleZDolu))
            if (self.pole.poleZGory):
                dostepneCele.append(Cel(self.pole, self.pole.poleZGory))
            if (self.pole.poleZLewej):
                dostepneCele.append(Cel(self.pole, self.pole.poleZLewej))
            if (self.pole.poleZPrawej):
                dostepneCele.append(Cel(self.pole, self.pole.poleZPrawej))

        # poziom tłuszczu > 60 -> goń wilka
        if (self.poziomTluszczu > 60):
            for widok in self.arr_zwierz:
                for zwierze in widok.zwierzetaNaPolu:
                    if isinstance(zwierze, Wilk):
                        dostepneCele.append(Cel(self.pole, widok.pole))

        # wyznaczanie trasy do obranego Celu
        min_koszt = 100
        cele_arr = []
        for cel in dostepneCele:
            if cel.koszt < min_koszt:
                min_koszt = cel.koszt
        for cel in dostepneCele:
            if (cel.koszt == min_koszt):
                cele_arr.append(cel)
        self.cel = choice(cele_arr)
        pass

    # WYKOWNYWANIE KROKU W TURZE
    def wykonajRuch(self):
        if self.cel.sciezkaDo:
            self.ruchZwierza(self.cel.sciezkaDo.pop(0))
        self.gdzieWykonacRuch()
