from WidokPola import WidokPola

dostepnePlci = ("M", "F")


class Zwierze:
    plec = "M"
    czyZyje = True
    zasiegWidzenia = 5
    pole = None
    arr_zwierz = None
    poziomTluszczu = 100

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

    #TODO: LOGIKA PORUSZANIA SIE

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

        for widok in self.arr_zwierz:
            print(str(widok))

    def zezera(self):
        pass