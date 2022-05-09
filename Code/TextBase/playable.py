from .creature import Creature
import random

class Playable(Creature):
    def __init__(self,name,hp,atk,dfc,mag,lck):
        super().__init__(name,hp,atk,dfc,mag,lck)

    def isCrit(self) :
        if(random.random()*100 <= self.getLck()) :
            return True
        else :
            return False

    def attackSomeone(self,c) :
        if(self.isCrit()) :
            print("Un coup critique de "+self.getName()+ " !")
            c.getAttacked(self.getAtk()*2)
        else :
            print(self.getName()+" attaque !")
            c.getAttacked(self.getAtk())

    def getAttacked(self,dmg) :
        if(self.isCrit()) :
            print("Une parade critique de "+self.getName()+ " !")
            trueDamage = dmg - self.getDfc()*2
        else :
            print(self.getName()+" se défend !")
            trueDamage = dmg - self.getDfc()
        if trueDamage < 0 :
            trueDamage = 0
        self.setHp(self.getHp() - trueDamage)
        if self.getHp() <= 0 :
            self.setHp(0)

