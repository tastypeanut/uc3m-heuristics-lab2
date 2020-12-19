import lib.objects.States as States

#this class represents each of the satellites that there are in the problem
class satellite:
	#a satellite is characterized for having an id, its current level of energy and position
	__idNumber = None
	__band = None
	__position = None
	__energy = None    #energy levels that the satellite has at the moment
	__hasObservation = None  #this variable indicates if the satellite currently has an observation that needs to be dowlinked
	#__state = None  #current state (activity) being performed by the satellite
	__energyCostList = [] #list with the costs of each of the activities, following the same order as received in the input
	states = None   #object from the States class, which included the associated cost for each activity



#CONSTRUCTOR

#it receives and id, position and a list with the energy levels (costs and initial energy of the satellite)
	def __init__(self, idNumber,band, position, energyCostList):
		self.setIdNumber(idNumber)
		self.setPosition(position)
		self.setBand(band)
		print("HELLO")
		print(len(energyCostList))
		#self.setEnergyCostList(energyCostList)
		self.setHasObervation(False) #initially, the satellite has not taken any observation




	#CHANGE BAND

	#this method performs the activity of changing the band of a satellite. 
	#It is important to take into account that, in the case of the SAT1, we are assuming that it can always access the current band and one less (__band - 1)
	#It will initially be located in ban 1, so it will be able to access band 0 as well. If it wants to change to the next band, it will move to band 2, being able
	#to access band 2 - 1 = 1 as well.
	#In the case of the REST of the satellites, they can access its current band and one more (__band + 1). For instance, satellite 2 is intially located in band 2,
	# and it can also access band 2 + 1 = 3. If it changes to the other band, it will be able to access bands 2 and 2-1= 1.
	def changeBand(self):
		if self.__energy > self.states.TURN:   #cheking there's enough energy


			#SAT1
			if self.__idNumber == 1:
				if self.__band == 1:	#currently located in bands 1-2
					self.setBand(0)		#changing to bands 0-1
				else: self.setBand(1)	#currently located in bands 0-1, and changing to bands 1-2 


			#Rest of the satellites			CHECK THIS!!!
			elif self.__band == self.__idNumber:	#currently located in bands idNumber and idNumber + 1
				self.setBand(self.__idNumber - 1)		#changing to bands idNumber and idNumber - 1
			else: self.setBand(self.__idNumber)	#currently located in bands idNumber and idNumber - 1, and changing to bands idNumber and idNumber + 1

		


			

			self.setEnergy(self.__energy - self.states.TURN)  #updating the energy levels
		
		else: print ("There is not enough energy to change band")   #in the case there is not enough energy to perform the activity




	#CHARGE

	#method that charges the satellite's energy
	def charge(self, energyGained):
		self.setEnergy(self.__energy + energyGained )



	#TAKE MEASUREMENT

	#this method simply allows the satellite to take a measurent if it does not have one at the moment
	def takeMeasurement(self,observation):
	#not(self.__hasObservation) and  ADD IT!!!
		if (  self.__energy > self.states.MEASUREMENT and not(observation.getMeasured()) ):    #cheking there's enough energy
			self.setHasObervation(True)
			observation.setMeasured(True)
			self.setEnergy(self.__energy - self.states.MEASUREMENT) 	#calculating the new energy level

		else: print ("There is not enough energy or a measurement has already been taken")  #in the case there is not enough energy to perform the activity



	#DOWNLINK

	#when a satellite downlinks the observation (if it has one), we set its variable to "false" and substract the cost
	def downlink (self):
		if (self.__hasObservation and self.__energy > self.states.DOWNLINK):   #cheking that it has an observation and that there's enough energy
			self.setHasObervation(False)  #setting the variable to "false"
			self.setEnergy(self.__energy - self.states.DOWNLINK)		#calculating the new energy level
			self.__state = self.states.state.DOWNLINK      #updating the state to downlink
		else: print ("There's no observation to downlink or there is not enough energy")  #in the case there is not enough energy to perform the activity



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

	def setHasObervation(self,observation):
		self.__hasObservation = observation

	def setState(self, state):
		self.__state = state

	def setEnergyCostList(self, energyCostList):
		self.__energyCostList = energyCostList
		#self.states = States.states(energyCostList)
		self.__energy = energyCostList[4]
	

	#GETTERS

	def getIdNumber(self):
		return self.__idNumber

	def getBand(self):
		return self.__band

	def getPosition(self):
		return self.__position

	def getEnergy(self):
		return self.__energy

	def getHasObservation(self):
		return self.__hasObservation

	def getState(self):
		return self.__state

	def getEnergyCostList(self):
		return self.__energyCostList