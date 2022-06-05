from Pole import *
from random import choice
import pygame


class Plansza:
    Pola = []
    zwierzeta = []

    def __init__(self, a, b):
        for i in range(a):
            x = []
            for j in range(b):
                pole = Pole(i, j)
                x.append(pole)
            self.Pola.append(x)

        for i in range(a):
            for j in range(b):
                pole = self.Pola[i][j]
                if (i > 0):
                    pole.poleZLewej = self.Pola[i - 1][j]
                if (i < a - 1):
                    pole.poleZPrawej = self.Pola[i + 1][j]
                if (j > 0):
                    pole.poleZGory = self.Pola[i][j - 1]
                if (j < b - 1):
                    pole.poleZDolu = self.Pola[i][j + 1]
        # print("Zrobiono planszę")
        self.generujIRozmiescNaPolachZwierzeta()

    def wykonajTureWilk(self):
        for pola in self.Pola:
            for pole in pola:
                pole.rysowanko(self.zwierzetaSprite)
                pole.coSieDziejeNaPolu()
        for pola in self.Pola:
            for pole in pola:
                pole.wilki()

    def wykonajTureZajac(self):
        for pola in self.Pola:
            for pole in pola:
                pole.rysowanko(self.zwierzetaSprite)
                pole.coSieDziejeNaPolu()
        for pola in self.Pola:
            for pole in pola:
                pole.zajace()


    def generujIRozmiescNaPolachZwierzeta(self, ileWilkow=None, ileZajecy=None):
        ile_pol = len(self.Pola) * len(self.Pola[0])
        if (ile_pol < 27):
            zajetePola = 0
        else:
            zajetePola = int(ile_pol * 0.15) - 3
        self.zwierzeta.append(Wilk(3, "M"))
        self.zwierzeta.append(Wilk(3, "F"))
        self.zwierzeta.append(Zajac(2, "M"))
        self.zwierzeta.append(Zajac(2, "F"))

        # - generowanie brakujących zwierzów
        gatunek = ("Wilk", "Zajac")
        for i in range(zajetePola-1):
            los = choice(gatunek)
            if (los == "Wilk"):
                self.zwierzeta.append(Wilk(3))
            elif (los == "Zajac"):
                self.zwierzeta.append(Zajac(2))

        # - rozmieszczanie zwierzów
        self.zwierzetaSprite = pygame.sprite.Group()
        for zwierz in self.zwierzeta:
            zwierz = self.zwierzeta.pop(0)
            choice(choice(self.Pola)).wskocz(zwierz)
            # zwierz.pygameInit()
            self.zwierzetaSprite.add(zwierz)

    def __str__(self):
        wynik = ""
        for pola in self.Pola:
            for pole in pola:
                wynik += " | "+str(pole)+""
            wynik+="\n"
        return wynik