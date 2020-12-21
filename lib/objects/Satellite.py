import lib.objects.States as States

#this class represents each of the satellites that there are in the problem
class satellite:
	#a satellite is characterized for having an id, its current level of energy and position
	__idNumber = None
	__band = None
	__position = None
	__energy = None    #energy levels that the satellite has at the moment

	__observation = None  #this variable indicates the satellite's current  observation (if any)
	__activity = None  #current state (activity) being performed by the satellite
	__energyCostList = [] #list with the costs of each of the activities, following the same order as received in the input
	states = None  #object from the States class, which included the associated cost for each activity

	



#CONSTRUCTOR

#it receives and id, position and a list with the energy levels (costs and initial energy of the satellite)
	def __init__(self, idNumber, band, position, activity, energyCostList):
		self.setIdNumber(idNumber)
		self.setPosition(position)
		self.setBand(band)
		self.setEnergy(energyCostList[4])
		self.setActivity(activity)
		self.setEnergyCostList(energyCostList)
		#self.setHasObervation(False) #initially, the satellite has not taken any observation




	#CHANGE BAND

	#this method performs the activity of changing the band of a satellite. 
	#It is important to take into account that, in the case of the SAT1, we are assuming that it can always access the current band and one less (__band - 1)
	#It will initially be located in ban 1, so it will be able to access band 0 as well. If it wants to change to the next band, it will move to band 2, being able
	#to access band 2 - 1 = 1 as well.
	#In the case of the REST of the satellites, they can access its current band and one more (__band + 1). For instance, satellite 2 is intially located in band 2,
	# and it can also access band 2 + 1 = 3. If it changes to the other band, it will be able to access bands 2 and 2-1= 1.
	def turn(self):
		if (self.__observation == None and self.__energy >= self.states.turn):   #cheking there's enough energy
			#SAT1
			if self.__idNumber == 1:
				if self.__band == 1:	#currently located in bands 1-2
					self.setBand(0)		#changing to bands 0-1
				else: self.setBand(1)	#currently located in bands 0-1, and changing to bands 1-2 

			#Rest of the satellites			CHECK THIS!!!
			elif self.__band == self.__idNumber:	#currently located in bands idNumber and idNumber + 1
				self.setBand(self.__idNumber - 1)		#changing to bands idNumber and idNumber - 1
			else: self.setBand(self.__idNumber)	#currently located in bands idNumber and idNumber - 1, and changing to bands idNumber and idNumber + 1

			self.setEnergy(self.__energy - self.states.turn)  #updating the energy level
			self.__activity = "turn"       #updating the state to "turn"
		else:
			print ("There is not enough energy to change band")   #in the case there is not enough energy to perform the activity
			self.charge()   #as there is not enough energy, the satellite must be charged



	#CHARGE

	#method that charges the satellite's energy
	def charge(self):
		self.setEnergy(self.__energy + self.states.charge)
		self.__activity = "charge"       #updating the state to charge
		print("Charging with energy: {0}".format(self.__energy))


	#MEASURE

	#this method simply allows the satellite to take a measurent if it does not have one at the moment
	def measure(self,observation):
	#not(self.__observation) and					
		if (self.__observation == None and self.__energy >= self.states.measurement and not(observation.getMeasured()) ):    #cheking there's enough energy
			self.setObservation(observation)  #indicating which observation has been measured
			observation.setMeasured(True)
			self.setEnergy(self.__energy - self.states.measurement)  #calculating the new energy level
			self.__activity = "measurement"       #updating the state to measurement   

		else:
			print("There is not enough energy or a measurement has already been taken")  #in the case there is not enough energy to perform the activity
			self.charge()   #as there is not enough energy, the satellite must be charged



	#DOWNLINK

	#when a satellite downlinks the observation (if it has one), we set its variable to "false" and substract the cost
	def downlink (self):
		if (self.__observation != None and self.__energy >= self.states.downlink):   #cheking that it has an observation and that there's enough energy
			self.setEnergy(self.__energy - self.states.downlink)		#calculating the new energy level
			self.__activity = "downlink"      #updating the state to downlink
			self.setObservation(None)     
		
		else: 
			print("There's no observation to be downlinked or there is not enough energy")  #in the case there is not enough energy to perform the activity
			self.charge()    #as there is not enough energy, the satellite must be charged


	
	#IDDLE

	def iddle(self):
		self.__activity = "iddle"



	#def executeNextAction(self):




	#SETTERS
	
	def setIdNumber(self, idNumber):
		self.__idNumber = idNumber

	def setPosition(self, position):
		self.__position = position

	def setEnergy(self, energy):
		self.__energy = energy

	def setBand(self, band):
		self.__band = band

	def setObservation(self,observation):
		self.__observation = observation

	def setActivity(self, activity):
		self.__activity = activity

	def setEnergyCostList(self, energyCostList):
		self.__energyCostList = energyCostList
		self.states = States.states(energyCostList)
	
	

	#GETTERS

	def getIdNumber(self):
		return self.__idNumber

	def getBand(self):
		return self.__band

	def getPosition(self):
		return self.__position

	def getEnergy(self):
		return self.__energy

	def getObservation(self):
		return self.__observation

	def getActivity(self):
		return self.__activity

	def getEnergyCostList(self):
		return self.__energyCostList