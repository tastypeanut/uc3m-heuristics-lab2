#this class represents the observations that the satellites will have to measure
class observation:

	#each observation is characterized by an id, a variables than indicated whether it has already
	#been measure or not, the band where it is located, and its location in the x axis (0-12)
	idNumber = None
	measured = None
	band = None
	position = None
	

#CONSTRUCTOR

#It receives an id, a band and a position
	def __init__(self, idN, band, pos):
		self.idNumber = idN
		#by default, an observation will be initially set to "false"
		self.measured = False
		self.band = band
		self.position = pos
		