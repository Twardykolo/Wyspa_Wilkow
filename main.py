from Wilk import Wilk
from Zajac import Zajac
from Plansza import Plansza

w = Wilk(3) #wilk
z2 = Zajac(2)
z = Zajac(2) #zajac
z3 = Zajac(2)
z4 = Zajac(2)
z5 = Zajac(2)
zbiorniczek=Plansza(6,6)
# zbiorniczek=Plansza(int(input("Podaj szerokość planszy:\n")),int(input("Podaj wysokość planszy:\n")))
# for zbiornik in zbiorniczek.Pola:
#     for zbioreczek in zbiornik:
#         print(zbioreczek)

zbiorniczek.Pola[3][4].wskocz(w)
zbiorniczek.Pola[3][4].wskocz(z)
zbiorniczek.Pola[2][4].wskocz(z2)
zbiorniczek.Pola[4][4].wskocz(z3)
zbiorniczek.Pola[3][3].wskocz(z4)
zbiorniczek.Pola[3][5].wskocz(z5)
#.ruchZwierza(zbiorniczek.Pola[2][4])
w.patrze()
#print(str(zbiorniczek.Pola[3][4])+"\n\n\n"+str(zbiorniczek.Pola[2][4]))
zbiorniczek.Pola[3][4].coSieDziejeNaPolu()
