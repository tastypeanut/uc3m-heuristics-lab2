#this class represents each of the satellites that there are in the problem
class satellite:
	#a satellite is characterized for having an id, its current level of energy and position
	__idNumber = None
	__band = None
	__position = None
	__energy = None
	__activities = []  #list of activities that the satellite can do
	



#CONSTRUCTOR

#it receives and id, position and energy level
	def __init__(self, idNumber,band, position, energy):
		self.setIdNumber(idNumber)
		self.setPosition(position)
		self.setBand(band)
		self.setEnergy(energy)



#SETTERS
	
	def setIdNumber(self, idNumber):
		self.__idNumber = idNumber

	def setPosition(self, position):
		self.__position = position

	def setEnergy(self, energy):
		self.__energy = energy

	def setBand(self, band):
		self.__band = band

	#GETTERS

	def getIdNumber(self):
		return self.__idNumber

	def getBand(self):
		return self.__band

	def getPosition(self):
		return self.__position

	def getEnergy(self):
		return self.__energy
