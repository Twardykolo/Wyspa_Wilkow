from random import choice
from Zwierze import Zwierze,dostepnePlci


class Zajac(Zwierze):
    def __init__(self,zasiegWidzenia,plec=choice(dostepnePlci)):
        Zwierze.__init__(self,plec,zasiegWidzenia)

    def __del__(self):
        #TODO: królik umiera
        #mordo ale to był zajac
        self.czyZyje=False
        # print("O Boże, umarłem")
        pass