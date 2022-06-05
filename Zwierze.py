from WidokPola import WidokPola
from random import choice
from Cel import Cel
dostepnePlci = ("M", "F")


class Zwierze:
    plec = "M"
    czyZyje = True
    zasiegWidzenia = 5
    pole = None
    arr_zwierz = None
    poziomTluszczu = 100
    cel = None

    def __init__(self, plec, zasiegWidzenia):
        self.plec = plec
        self.zasiegWidzenia = zasiegWidzenia

    # ZDECHNIĘCIE ZWIERZA
    def __del__(self):
        self.czyZyje = False
        if self.pole:
            self.pole.zwierzeta.remove(self)
        self.pole = None

    # setter
    def gdzieJestem(self, pole):
        self.pole = pole

    # getter
    def gdzieJest(self):
        return self.pole

    # FUNKCJA ODPOWIEDZIALNA ZA PRZESKOK Z POLA NA POLE
    def ruchZwierza(self, pole):
        if self.czyZyje:
            self.pole.wyskocz(self)
            pole.wskocz(self)

    # TODO: LOGIKA PORUSZANIA SIE

    # FUNKCJA ODPOWIEDZIALNA ZA ROZPOZNAWANIE
    # ZWIERZĄT W ZASIĘGU WIDZENIA
    def patrze(self):
        if not self.czyZyje:
            return

        here = self.gdzieJest()  # pole
        self.arr_zwierz = []

        # WIDOK W LEWO
        terazSprawdzane = here.poleZLewej

        for i in range(0, self.zasiegWidzenia):
            if not terazSprawdzane:
                break
            zwierzetaNaPolu = terazSprawdzane.jakieZwierzetaNaPolu()
            if zwierzetaNaPolu:
                self.arr_zwierz.append(WidokPola(terazSprawdzane, zwierzetaNaPolu))
            terazSprawdzane = terazSprawdzane.poleZLewej

        # WIDOK W PRAWO
        terazSprawdzane = here.poleZPrawej

        for i in range(0, self.zasiegWidzenia):
            if not terazSprawdzane:
                break
            zwierzetaNaPolu = terazSprawdzane.jakieZwierzetaNaPolu()
            if zwierzetaNaPolu:
                self.arr_zwierz.append(WidokPola(terazSprawdzane, zwierzetaNaPolu))
            terazSprawdzane = terazSprawdzane.poleZPrawej

        # WIDOK W GÓRE
        terazSprawdzane = here.poleZGory

        for i in range(0, self.zasiegWidzenia):
            if not terazSprawdzane:
                break
            zwierzetaNaPolu = terazSprawdzane.jakieZwierzetaNaPolu()
            if zwierzetaNaPolu:
                self.arr_zwierz.append(WidokPola(terazSprawdzane, zwierzetaNaPolu))
            terazSprawdzane = terazSprawdzane.poleZGory

        # WIDOK W DÓL
        terazSprawdzane = here.poleZDolu

        for i in range(0, self.zasiegWidzenia):
            if not terazSprawdzane:
                break
            zwierzetaNaPolu = terazSprawdzane.jakieZwierzetaNaPolu()
            if zwierzetaNaPolu:
                self.arr_zwierz.append(WidokPola(terazSprawdzane, zwierzetaNaPolu))
            terazSprawdzane = terazSprawdzane.poleZDolu

    def zezera(self):
        pass


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
        self.gdzieWykonacRuch()
        if self.cel.sciezkaDo:
            self.ruchZwierza(self.cel.sciezkaDo.pop(0))


class Zajac(Zwierze):
    arr_trawa = None

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

    # PATRZENIE CZY ROŚNIE TRAWA NA POLU
    def patrze(self):
        print("NIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCH")

        super().patrze()
        here = self.gdzieJest()
        self.arr_trawa = []

        # WIDOK W LEWO
        terazSprawdzane = here.poleZLewej
        for i in range(0, self.zasiegWidzenia):
            if not terazSprawdzane:
                break
            if terazSprawdzane.stan == "Trawa":
                self.arr_trawa.append(terazSprawdzane)
            terazSprawdzane = terazSprawdzane.poleZLewej

        # WIDOK W PRAWO
        terazSprawdzane = here.poleZPrawej

        for i in range(0, self.zasiegWidzenia):
            if not terazSprawdzane:
                break
            if terazSprawdzane.stan == "Trawa":
                self.arr_trawa.append(terazSprawdzane)
            terazSprawdzane = terazSprawdzane.poleZPrawej

        # WIDOK W GÓRE
        terazSprawdzane = here.poleZGory

        for i in range(0, self.zasiegWidzenia):
            if not terazSprawdzane:
                break
            if terazSprawdzane.stan == "Trawa":
                self.arr_trawa.append(terazSprawdzane)
            terazSprawdzane = terazSprawdzane.poleZGory

        # WIDOK W DÓL
        terazSprawdzane = here.poleZDolu

        for i in range(0, self.zasiegWidzenia):
            if not terazSprawdzane:
                break
            if terazSprawdzane.stan == "Trawa":
                self.arr_trawa.append(terazSprawdzane)
            terazSprawdzane = terazSprawdzane.poleZDolu

        for widok in self.arr_zwierz:
            print(str(widok))

        for widok in self.arr_trawa:
            print(str(widok))

        print("NIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCHNIOCH2")
        pass

    # TODO: LOGIKA PORUSZANIA SIE
    def gdzieWykonacRuch(self):
        dostepneCele = []
        self.patrze()

        # poziom tłuszczu < 40 -> szukaj trawy
        if (self.poziomTluszczu <= 40):
            for widok in self.arr_trawa:
                byl_wilk = False
                for zwierze in widok.zwierzeta:
                    if isinstance(zwierze, Wilk):
                        byl_wilk = True
                if not byl_wilk:
                    dostepneCele.append(Cel(self.pole, widok))
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

        # poziom tłuszczu > 60 -> goń zająca
        if (self.poziomTluszczu > 60):
            for widok in self.arr_zwierz:
                byl_wilk = False
                byla_zajeczyca = False
                for zwierze in widok.zwierzetaNaPolu:
                    if isinstance(zwierze, Wilk):
                        byl_wilk = True
                    if isinstance(zwierze, Zajac):
                        if (zwierze.plec != self.plec):
                            byla_zajeczyca = True
                if (byla_zajeczyca and not byl_wilk):
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


    def wykonajRuch(self):
        self.gdzieWykonacRuch()
        if self.cel.sciezkaDo:
            self.ruchZwierza(self.cel.sciezkaDo.pop(0))
