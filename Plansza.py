from Pole import Pole


class Plansza:
    Pola=[]

    def __init__(self,a,b):
        for i in range (a):
            x=[]
            for j in range(b):
                pole=Pole(i,j)
                x.append(pole)
            self.Pola.append(x)

        for i in range(a):
            for j in range(b):
                pole=self.Pola[i][j]
                if(i>0):
                    pole.poleZLewej=self.Pola[i-1][j]
                if(i<a-1):
                    pole.poleZPrawej=self.Pola[i+1][j]
                if(j>0):
                    pole.poleZGory=self.Pola[i][j-1]
                if(j<b-1):
                    pole.poleZDolu=self.Pola[i][j+1]
        # print("Zrobiono planszę")

