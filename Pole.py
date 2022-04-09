mozliweStany=["Trawa","Pustynia"]
from random import choice
from Wilk import Wilk
from Zajac import Zajac


class Pole:
    x=0
    y=0
    stan=0
    zwierzeta=None
    poleZLewej=None
    poleZPrawej=None
    poleZGory=None
    poleZDolu=None

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.stan=choice(mozliweStany)
        self.zwierzeta=[]

    def __str__(self):
        return "x="+str(self.x)+"\ty="+str(self.y)+"\t stan="+self.stan+"\n"+\
            "Zwierzeta na polu: "+str(self.zwierzeta)+"\n"\
            "poleZLewej="+str(self.poleZLewej)+"\n"

    def coSieDziejeNaPolu(self):
        ileWilkow=0
        ileWilczyc=0
        ileZajecy=0
        ileZajeczyc=0

        for zwierze in self.zwierzeta:
            if isinstance(zwierze, Wilk):
                if zwierze.plec=="M":
                    ileWilkow+=1
                else:
                    ileWilkow+=1
                    ileWilczyc+=1
            if isinstance(zwierze, Zajac):
                if zwierze.plec=="M":
                    ileZajecy+=1
                else:
                    ileZajecy+=1
                    ileZajeczyc+=1

        print("\nWilków:"+str(ileWilkow)+"\nZajęcy:"+str(ileZajecy))
        while(ileZajecy>0 and ileWilkow>0):
            wilk=None
            zajac=None
            for zwierze in self.zwierzeta:
                if isinstance(zwierze, Wilk):
                    wilk = zwierze
                    break
            for zwierze in self.zwierzeta:
                if isinstance(zwierze, Zajac):
                    zajac = zwierze
                    break
            wilk.zezera(zajac)
            ileZajecy-=1

        if(ileZajecy>1 and ileZajeczyc>0 and ileZajecy!=ileZajeczyc):
            #TODO: zajonce +18
            pass

        if(ileWilkow>1 and ileWilczyc>0 and ileWilkow!=ileWilczyc):
            #TODO: wilki +18
            pass

    def wskocz(self,zwierz):
        self.zwierzeta.append(zwierz)