from Wilk import Wilk
from Zajac import Zajac
from Plansza import Plansza

# TODO: LOGIKA GRY
# TODO: GRAFIKA / OKIENKA

w = Wilk(3, "M")  # wilk
w2 = Wilk(3, "F")  # wilk
w3 = Wilk(3, "M")  # wilk

z2 = Zajac(2)
z = Zajac(2)  # zajac
z3 = Zajac(2)
z4 = Zajac(2)
z5 = Zajac(2)
zbiorniczek = Plansza(6, 6)
# zbiorniczek=Plansza(int(input("Podaj szerokość planszy:\n")),int(input("Podaj wysokość planszy:\n")))
# for zbiornik in zbiorniczek.Pola:
#     for zbioreczek in zbiornik:
#         print(zbioreczek)

zbiorniczek.Pola[3][4].wskocz(w)
zbiorniczek.Pola[3][5].wskocz(z)
zbiorniczek.Pola[3][5].wskocz(z2)
zbiorniczek.Pola[3][5].wskocz(z3)
zbiorniczek.Pola[3][5].wskocz(z4)
zbiorniczek.Pola[3][5].wskocz(z5)

print("hmhmhmhm.. " + str(zbiorniczek.Pola[3][5]))
zbiorniczek.Pola[3][5].coSieDziejeNaPolu()
print("REWELACJA ŁUCJA:     " + str(zbiorniczek.Pola[3][5]))

# w2.poziomTluszczu = 5
zbiorniczek.Pola[1][5].wskocz(w)
zbiorniczek.Pola[1][5].wskocz(w2)
zbiorniczek.Pola[1][5].wskocz(w3)

print("HMHMHM.. " + str(zbiorniczek.Pola[1][5]))
zbiorniczek.Pola[1][5].coSieDziejeNaPolu()
print("czesc, czesc: " + str(zbiorniczek.Pola[1][5]))
print(w2.poziomTluszczu)
print(w3.poziomTluszczu)

print("Przed " + str(w))
w.ruchZwierza(zbiorniczek.Pola[2][4])
zbiorniczek.Pola[2][4].coSieDziejeNaPolu()
print("Po " + str(w))

w.patrze()
# print(str(zbiorniczek.Pola[3][4])+"\n\n\n"+str(zbiorniczek.Pola[2][4]))
zbiorniczek.Pola[3][4].coSieDziejeNaPolu()
