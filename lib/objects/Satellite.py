#this class represents each of the satellites that there are in the problem
class satellite:
	#a satellite is characterized for having an id, its current level of energy and position
	idNumber = None
	position = None
	energy = None



#CONSTRUCTOR

#it receives and id, position and energy level
	def __init__(self, idN, pos, ener):
		self.idNumber = idN
		self.position = pos
		self.energy = ener