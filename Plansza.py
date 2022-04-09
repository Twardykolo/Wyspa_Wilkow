from Pole import Pole


class Plansza:
    Pola=[]

    def __init__(self,a,b):
        for i in range (a):
            x=[]
            for j in range(b):
                x.append(Pole(i+1,j+1))
            self.Pola.append(x)
        # print("Zrobiono planszę")