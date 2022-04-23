mozliweStany = ["Trawa", "Pustynia"]
from random import choice
from Wilk import Wilk
from Zajac import Zajac


class Pole:
    x = 0
    y = 0
    stan = 0
    zwierzeta = None
    poleZLewej = None
    poleZPrawej = None
    poleZGory = None
    poleZDolu = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stan = choice(mozliweStany)
        self.zwierzeta = []

    def __str__(self):
        return "x=" + str(self.x) + "\ty=" + str(self.y) + "\t stan=" + self.stan + "\n" + \
               "Zwierzeta na polu: " + str(self.zwierzeta) + "\n" \
 \
    # Zwraca tablicę ze zwierzętami znajdującymi się na polu
    def jakieZwierzetaNaPolu(self):
        return self.zwierzeta

    def coSieDziejeNaPolu(self):
        ileWilkow = 0
        ileWilczyc = 0
        ileZajecy = 0
        ileZajeczyc = 0

        for zwierze in self.zwierzeta:
            if isinstance(zwierze, Wilk):
                if zwierze.poziomTluszczu <= 0:
                    zwierze.__del__()
                    continue
                if zwierze.plec == "M":
                    ileWilkow += 1
                else:
                    ileWilkow += 1
                    ileWilczyc += 1
            if isinstance(zwierze, Zajac):
                if zwierze.plec == "M":
                    ileZajecy += 1
                else:
                    ileZajecy += 1
                    ileZajeczyc += 1

        print("\nWilków:" + str(ileWilkow) + "\nZajęcy:" + str(ileZajecy))
        while (ileZajecy > 0 and ileWilkow > 0):
            wilk = None
            zajac = None
            for zwierze in self.zwierzeta:
                if isinstance(zwierze, Wilk):
                    wilk = zwierze
                    break
            for zwierze in self.zwierzeta:
                if isinstance(zwierze, Zajac):
                    zajac = zwierze
                    break
            wilk.zezera(zajac)
            ileZajecy -= 1

        # ROZMNAŻANIE ZAJĘCY
        if (ileZajecy > 1 and ileZajeczyc > 0 and ileZajecy != ileZajeczyc):
            # Z KAŻDEJ ZAJĘCZYCY POWSTAJE DWA NOWE ZAJĄCZKI
            for i in range(0, ileZajeczyc * 2):
                nowy = Zajac(2)
                ileZajecy += 1
                self.wskocz(nowy)

        # ROZMNAŻANIE WILKÓW
        if (ileWilkow == 2 and ileWilczyc == 1):
            wilk = None
            wilczyca = None
            for zwierze in self.zwierzeta:
                if isinstance(zwierze, Wilk):
                    if zwierze.plec == "F":
                        wilczyca = zwierze
                    else:
                        wilk = zwierze
            if wilk.poziomTluszczu > 50 and wilczyca.poziomTluszczu > 50:
                wilk.poziomTluszczu -= 20
                wilczyca.poziomTluszczu -= 20
                nowy = Wilk(3)
                ileWilkow += 1
                self.wskocz(nowy)

        # ODMNAŻANIE WILKÓW (WALKI W KLATKACH)
        if (ileWilkow >= 2 and ileWilkow - ileWilczyc >= 2):
            samce = []
            for zwierze in self.zwierzeta:
                if zwierze.plec == "M":
                    samce.append(zwierze)

            minPoziomTluszczu = 200
            minWilk = None
            for wilczur in samce:
                if wilczur.poziomTluszczu < minPoziomTluszczu:
                    minPoziomTluszczu = wilczur.poziomTluszczu
                    minWilk = wilczur
                wilczur.poziomTluszczu -= 30
            minWilk.__del__()

    def wskocz(self, zwierz):
        self.zwierzeta.append(zwierz)
        zwierz.gdzieJestem(self)
        print("!skoczyłem")

    def wyskocz(self, zwierz):
        self.zwierzeta.remove(zwierz)
        zwierz.gdzieJestem(None)
        print("wyskczylesm")
