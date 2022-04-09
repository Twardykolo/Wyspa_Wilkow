dostepnePlci=("M","F")

class Zwierze:
    plec="M"
    czyZyje=True
    zasiegWidzenia=5
    pole=None

    def __init__(self,plec,zasiegWidzenia):
        self.plec=plec
        self.zasiegWidzenia=zasiegWidzenia

    #setter
    def gdzieJestem(self, pole):
        self.pole=pole

    #getter
    def gdzieJest(self):
        return self.pole

    #TODO: ruch zwierzów
    def ruchZwierza(self, pole):
        self.pole.wyskocz(self)
        pole.wskocz(self)
        print("ide sie ruszyc")