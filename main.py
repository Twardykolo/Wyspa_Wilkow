from Zwierze import *
from Plansza import Plansza
from Cel import Cel

# TODO: LOGIKA GRY
# 1 - lista wszystkich pól, z niej wybieramy pola i wywołujemy ich "co się dzieje na polu"
# 2 - w co się dzieje na polu musimy dla każdego zwierzęcia wywołać jego logikę z zaznaczeniem, że
#     jak się poruszą na inne pole, to już nie mogą wykonać akcji w tej turze, jeśli np. już jadły
#     czyt tura = akcja + krok MAX
# 3 - pętla w której to wszystko się będzie odbywać i warunki jej przerwania/zakończenia np. jeśli wciśniemy ESC

# 4 - jakieś ustawienia gry (w pliku albo na sztywno w kodzie), na podstawie których generujemy ilość pól i zwierząt

# TODO: GRAFIKA / OKIENKA


w = Wilk(3, "M")  # wilk
w2 = Wilk(3, "F")  # wilk
w3 = Wilk(3, "M")  # wilk

z2 = Zajac(2)
z = Zajac(2)  # zajac
z3 = Zajac(2)
# z4 = Zajac(2)
# z5 = Zajac(2)
zbiorniczek = Plansza(7, 7)
# zbiorniczek=Plansza(int(input("Podaj szerokość planszy:\n")),int(input("Podaj wysokość planszy:\n")))
# for zbiornik in zbiorniczek.Pola:
#     for zbioreczek in zbiornik:
#         print(zbioreczek)

zbiorniczek.Pola[3][3].wskocz(w)
zbiorniczek.Pola[3][2].wskocz(z)
zbiorniczek.Pola[3][4].wskocz(z2)
zbiorniczek.Pola[5][3].wskocz(z3)
zbiorniczek.Pola[3][4].wskocz(w2)
zbiorniczek.Pola[3][4].wskocz(w3)

print("hmhmhmhm.. " + str(zbiorniczek.Pola[3][3]))
zbiorniczek.Pola[3][3].coSieDziejeNaPolu()
print("REWELACJA ŁUCJA:     " + str(zbiorniczek.Pola[3][3]))

# w2.poziomTluszczu = 5
# zbiorniczek.Pola[3][3].wskocz(w)
# zbiorniczek.Pola[1][5].wskocz(w2)
# zbiorniczek.Pola[1][5].wskocz(w3)

# print("HMHMHM.. " + str(zbiorniczek.Pola[1][5]))
# zbiorniczek.Pola[1][5].coSieDziejeNaPolu()
# print("czesc, czesc: " + str(zbiorniczek.Pola[1][5]))
# print(w2.poziomTluszczu)
# print(w3.poziomTluszczu)

print("Przed " + str(w))
# w.ruchZwierza(zbiorniczek.Pola[2][4])
# zbiorniczek.Pola[2][4].coSieDziejeNaPolu()
print("Po " + str(w))

print(w.czyZyje)
print(z2.czyZyje)
z2.patrze()
w.patrze()
# print(str(zbiorniczek.Pola[3][4])+"\n\n\n"+str(zbiorniczek.Pola[2][4]))
zbiorniczek.Pola[3][5].coSieDziejeNaPolu()

w.poziomTluszczu = 20
w.ruchZwierza(zbiorniczek.Pola[1][4])
w.gdzieWykonacRuch()
w.ruchZwierza(w.cel.sciezkaDo.pop(0))
print(w)
print("QQQQQQQQ: " + str(w.cel.sciezkaDo))
print("Obrany cel: " + str(w.cel.sciezkaDo.pop(0)))
print("RRRRRRRR: " + str(w.cel.sciezkaDo))
