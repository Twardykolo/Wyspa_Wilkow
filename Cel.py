class Cel:
    pole = None
    koszt = 0
    sciezkaDo = None

    def __init__(self, poleAktualne, pole):
        self.pole = pole
        self.sciezkaDo = []
        poleSprawdzane = poleAktualne
        # print("siemanko przed pętlą \n")
        while (poleSprawdzane.x != pole.x or poleSprawdzane.y != pole.y):
            # print("siemanko w pętli\n")
            if (poleSprawdzane.x == pole.x):
                if (poleSprawdzane.y < pole.y):
                    # - cel u dołu
                    # print("siemanko w dół\n")
                    # print("Pole sprawdzam 1:\n" + str(poleSprawdzane))
                    poleSprawdzane = poleSprawdzane.poleZDolu
                    # print("Pole sprawdzam 2:\n" + str(poleSprawdzane))
                    self.sciezkaDo.append(poleSprawdzane)
                    self.koszt += 1
                    pass
                else:
                    # - cel u góry
                    # print("siemanko w górę\n")
                    poleSprawdzane = poleSprawdzane.poleZGory
                    self.sciezkaDo.append(poleSprawdzane)
                    self.koszt += 1
                    pass
            elif (poleSprawdzane.y == pole.y):
                if (poleSprawdzane.x > pole.x):
                    # - cel po lewej
                    # print("siemanko w lewo \n")
                    # print("Pole sprawdzam 1:\n" + str(poleSprawdzane))
                    poleSprawdzane = poleSprawdzane.poleZLewej
                    # print("Pole sprawdzam 2:\n" + str(poleSprawdzane))
                    self.sciezkaDo.append(poleSprawdzane)
                    self.koszt += 1
                    pass
                else:
                    # - cel po prawej
                    # print("siemanko w prawo\n")
                    poleSprawdzane = poleSprawdzane.poleZPrawej
                    self.sciezkaDo.append(poleSprawdzane)
                    self.koszt += 1
                    pass
            else:
                # print("Koniec imprezy, zamykamy ten burdel")
                break

    def __str__(self):
        return "Koszt: " + str(self.koszt) + \
               "\nSciezka do celu: " + str(self.sciezkaDo)
