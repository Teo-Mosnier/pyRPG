from .playable import Playable

class Knight(Playable) :
	
    def __init__(self,name="Sir Gontrand",hp=10,atk=2,dfc=3,mag=0,lck=0):
        super().__init__(name,hp,atk,dfc,mag,lck)

    def berserkerSlash(self,c):
    	print(self.getName()+" : BERSERKER SLAAAAASH !")
    	self.setHp(self.getHp()-1)
    	self.setAtk(self.getAtk()*2)
    	self.attackSomeone(c)
    	self.setAtk(self.getAtk()//2)