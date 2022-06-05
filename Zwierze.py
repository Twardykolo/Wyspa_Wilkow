from WidokPola import WidokPola
from random import choice
from Cel import Cel
import pygame

dostepnePlci = ("M", "F")


class Tile(pygame.sprite.Sprite):
    def __int__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft=pos)
        pass


class Zwierze(Tile):
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
        super().__init__()

    # def pygameInit(self):
    #     if self.pole:
    #         super().__init__((self.pole.x,self.pole.y),32)

    # ZDECHNIĘCIE ZWIERZA
    def __del__(self):
        self.czyZyje = False
        # self.kill()
        if self.pole:
            self.pole.wyskocz(self)

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

    # FUNKCJA ODPOWIEDZIALNA ZA ROZPOZNAWANIE
    # ZWIERZĄT W ZASIĘGU WIDZENIA
    def patrze(self):
        if not self.czyZyje:
            return

        here = self.gdzieJest()
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

    def __str__(self):
        return "Aktualny cel: \n" + str(self.cel)


class Wilk(Zwierze):

    def __init__(self, zasiegWidzenia, plec=None):
        if plec == None:
            plec = choice(dostepnePlci)
        Zwierze.__init__(self, plec, zasiegWidzenia)

    # ZDECHNIĘCIE WILKA
    def __del__(self):
        super().__del__()

    def __str__(self):
        return "Poziom tłuszczu wilka: " + str(self.poziomTluszczu) + \
               "\nx: " + str(self.pole.x) + "    y: " + str(
            self.pole.y) + "\n plec: " + self.plec + "\n" + super().__str__()

    # ZJEDZENIE ZAJĄCA
    def zezera(self, zajac):
        self.poziomTluszczu += 15
        zajac.__del__()

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
        #
        # # poziom tłuszczu > 40 && poziom tłuszczu < 60 -> chodź
        # elif (self.poziomTluszczu > 40 and self.poziomTluszczu <= 60):
        #

        # poziom tłuszczu > 60 -> goń wilka
        elif (self.poziomTluszczu > 60):
            for widok in self.arr_zwierz:
                for zwierze in widok.zwierzetaNaPolu:
                    if isinstance(zwierze, Wilk):
                        dostepneCele.append(Cel(self.pole, widok.pole))

        if not dostepneCele:
            if (self.pole.poleZDolu):
                dostepneCele.append(Cel(self.pole, self.pole.poleZDolu))
            if (self.pole.poleZGory):
                dostepneCele.append(Cel(self.pole, self.pole.poleZGory))
            if (self.pole.poleZLewej):
                dostepneCele.append(Cel(self.pole, self.pole.poleZLewej))
            if (self.pole.poleZPrawej):
                dostepneCele.append(Cel(self.pole, self.pole.poleZPrawej))

        # wyznaczanie trasy do obranego Celu
        min_koszt = 100
        cele_arr = []
        for cel in dostepneCele:
            if cel.koszt < min_koszt:
                min_koszt = cel.koszt
        for cel in dostepneCele:
            if (cel.koszt == min_koszt):
                cele_arr.append(cel)
        if cele_arr:
            self.cel = choice(cele_arr)

    # WYKOWNYWANIE KROKU W TURZE
    def wykonajRuch(self):
        self.gdzieWykonacRuch()
        if self.cel:
            if self.cel.sciezkaDo:
                ruch = self.cel.sciezkaDo[0]
                print(str(self.cel.sciezkaDo[0]))
                self.ruchZwierza(ruch)
                self.cel.sciezkaDo.remove(ruch)


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

    # PORUSZANIE SIĘ (spalanie tłuszczu przy ruchu)
    def ruchZwierza(self, pole):
        self.poziomTluszczu -= 3
        super().ruchZwierza(pole)

    # PATRZENIE CZY ROŚNIE TRAWA NA POLU
    def patrze(self):
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

    # LOGIKA PORUSZANIA SIE
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

        # poziom tłuszczu > 40 && poziom tłuszczu < 60 -> chodź
        # else:
        #     if (self.pole.poleZDolu):
        #         dostepneCele.append(Cel(self.pole, self.pole.poleZDolu))
        #     if (self.pole.poleZGory):
        #         dostepneCele.append(Cel(self.pole, self.pole.poleZGory))
        #     if (self.pole.poleZLewej):
        #         dostepneCele.append(Cel(self.pole, self.pole.poleZLewej))
        #     if (self.pole.poleZPrawej):
        #         dostepneCele.append(Cel(self.pole, self.pole.poleZPrawej))

        # poziom tłuszczu > 60 -> goń zająca
        elif (self.poziomTluszczu > 60):
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
        if not dostepneCele:
            if (self.pole.poleZDolu):
                dostepneCele.append(Cel(self.pole, self.pole.poleZDolu))
            if (self.pole.poleZGory):
                dostepneCele.append(Cel(self.pole, self.pole.poleZGory))
            if (self.pole.poleZLewej):
                dostepneCele.append(Cel(self.pole, self.pole.poleZLewej))
            if (self.pole.poleZPrawej):
                dostepneCele.append(Cel(self.pole, self.pole.poleZPrawej))

        # wyznaczanie trasy do obranego Celu
        min_koszt = 100
        cele_arr = []
        for cel in dostepneCele:
            if cel.koszt < min_koszt:
                min_koszt = cel.koszt
        for cel in dostepneCele:
            if (cel.koszt == min_koszt):
                cele_arr.append(cel)
        if cele_arr:
            self.cel = choice(cele_arr)
        pass

    def wykonajRuch(self):
        self.gdzieWykonacRuch()
        if self.cel:
            if self.cel.sciezkaDo:
                # print(str(self))
                ruch = self.cel.sciezkaDo[0]
                self.ruchZwierza(ruch)
                self.cel.sciezkaDo.remove(ruch)
