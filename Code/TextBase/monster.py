from .creature import Creature

class Monster(Creature) :
    def __init__(self,name,hp,atk,dfc,mag) :
        super().__init__(name,hp,atk,dfc,mag,lck=0)

    def attackSomeone(self,c) :
            print(self.getName()+" attaque !")
            c.getAttacked(self.getAtk())

    def getAttacked(self,dmg) :
        print(self.getName()+" se défend !")
        trueDamage = dmg - self.getDfc()
        if trueDamage < 0 :
            trueDamage = 0
        self.setHp(self.getHp() - trueDamage)
        if self.getHp() <= 0 :
            self.setHp(0)
