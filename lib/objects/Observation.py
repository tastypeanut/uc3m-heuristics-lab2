#this class represents the observations that the satellites will have to measure
class observation:

	#each observation is characterized by an id, a variables than indicated whether it has already
	#been measure or not, the band where it is located, and its location in the x axis (0-12)
	__idNumber = None
	__measured = None
	__band = None
	__position = None
	

#CONSTRUCTOR

#It receives an id, a band and a position
	def __init__(self, idNumber, band, position):
		self.setIdNumber(idNumber)
		self.setMeasured(False)  #by default, an observation will be initially set to "false"
		self.setBand(band)
		self.setPosition(position)
		


	#SETTERS
	
	def setIdNumber(self, idNumber):
		self.__idNumber = idNumber

	
	def setMeasured(self, measured):
		self.__measured = measured

	
	def setBand(self, band):
		self.__band = band


	def setPosition(self, position):
		self.__position = position


	#GETTERS

	def getIdNumber(self):
		return self.__idNumber

	def getBand(self):
		return self.__band

	def getPosition(self):
		return self.__position

	def getMeasured(self):
		return self.__measured

	




    



