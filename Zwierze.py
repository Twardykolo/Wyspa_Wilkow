from WidokPola import WidokPola
dostepnePlci=("M","F")

class Zwierze:
    plec="M"
    czyZyje=True
    zasiegWidzenia=5
    pole=None
    arr_zwierz=None

    def __init__(self,plec,zasiegWidzenia):
        self.plec = plec
        self.zasiegWidzenia = zasiegWidzenia

    #setter
    def gdzieJestem(self, pole):
        self.pole=pole

    #getter
    def gdzieJest(self):
        return self.pole

    #FUNKCJA ODPOWIEDZIALNA ZA PRZESKOK Z POLA NA POLE
    def ruchZwierza(self, pole):
        self.pole.wyskocz(self)
        pole.wskocz(self)

    #FUNKCJA ODPOWIEDZIALNA ZA ROZPOZNAWANIE
    #ZWIERZĄT W ZASIĘGU WIDZENIA
    def patrze(self):
        here = self.gdzieJest() #pole
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
