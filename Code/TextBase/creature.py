from abc import ABC,abstractmethod

class Creature(ABC) :

    red = '\033[91m'
    green = '\033[92m'
    blue = '\033[94m'
    bold = '\033[1m'
    italics = '\033[3m'
    underline = '\033[4m'
    end = '\033[0m'

    def __init__(self, name, hp=1, atk=2, dfc=3, mag=4, lck=0) :
        self.name = name #Name
        self.hp = hp #Health Points
        self.atk = atk #Attack
        self.dfc = dfc #Defence
        self.mag = mag #Magic
        self.lck = lck #Luck

    def getName(self) :
        return self.name
    def getHp(self) :
        return self.hp
    def getAtk(self) :
        return self.atk
    def getDfc(self) :
        return self.dfc
    def getMag(self) :
        return self.mag
    def getLck(self) :
        return self.lck

    def setHp(self,hp) :
        self.hp = hp
    def setAtk(self,atk) :
        self.atk = atk
    def setDfc(self,dfc) :
        self.dfc = dfc
    def setMag(self,mag) :
        self.mag = mag
    def setLck(self,lck) :
        self.lck = lck

    def blabla(self) :
        print(self.getName()+" : Mes stats (Hp,Atk,Dfc,Mag,Lck) : "+str(self.getHp())+" "+str(self.getAtk())+" "+str(self.getDfc())+" "+str(self.getMag())+" "+str(self.getLck()))

    @abstractmethod
    def attackSomeone(c) :
        ...

    @abstractmethod
    def getAttacked(self,dmg) :
        ...
