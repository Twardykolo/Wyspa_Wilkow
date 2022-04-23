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

    #TODO: LOGIKA PORUSZANIA SIE
