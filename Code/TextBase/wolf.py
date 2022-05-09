from .monster import Monster

class Wolf(Monster):

	def __init__(self) :
		super().__init__(name="LeLoup",hp=5,atk=2,dfc=1,mag=0)