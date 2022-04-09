from Wilk import Wilk
from Zajac import Zajac
from Plansza import Plansza

w = Wilk(3) #wilk
z2 = Zajac(2)
z = Zajac(3) #zajac
zbiorniczek=Plansza(5,5)
# zbiorniczek=Plansza(int(input("Podaj szerokość planszy:\n")),int(input("Podaj wysokość planszy:\n")))
# for zbiornik in zbiorniczek.Pola:
#     for zbioreczek in zbiornik:
#         print(zbioreczek)

zbiorniczek.Pola[3][4].wskocz(w)
zbiorniczek.Pola[3][4].wskocz(z)
zbiorniczek.Pola[2][4].wskocz(z2)
print(str(zbiorniczek.Pola[3][4])+"\n\n\n"+str(zbiorniczek.Pola[2][4]))
zbiorniczek.Pola[3][4].coSieDziejeNaPolu()