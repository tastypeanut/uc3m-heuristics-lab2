import lib.OpenList as OpenList
import lib.objects.Satellite as Satellite
import lib.objects.Observation as Observation

class node:
    __cost = None
    __heuristic = None       #heuristic value comming from the function associated to this node
    __evaluation = None      #Evaluation value. It gives preferences when ordering the open list
    __parent = None          #parent node
    __nextNodeList = None    #next element of the open list
    __listSatellites = []    #list of satellites
    __listObservations = []  #list of observations that need to be measured




    #CONSTRUCTOR
    #------------------------------------------------------------------------------------------------------------------------------ 


    def __init__(self, *args): 
    
    #in python it is not possible to create several constructors, so we include different cases
    #depending on the number of received parameters

        #if a node is received (just 1 single argument)
        if len(args) == 1: 
            self.setCost(args[0].getCost())
            self.setHeuristic(args[0].getHeuristic())
            self.setEvaluation(args[0].getEvaluation())
            self.setParent(args[0].getParent())
            self.setNextNode(args[0].getNextNode())
            self.setListSatellites(args[0].getListSatellites())
            self.setListObservations(args[0].getListObservations())
        
        #receiving 3 paremeters: parentNode, list of satellites and list of observations
        if len(args) == 3:
            self.setParent(args[0])
            self.setListSatellites(args[1])
            self.setListObservations(args[2])




    #COMPUTE HEURISTIC
    #------------------------------------------------------------------------------------------------------------------------------ 


    #method that computes the heuristic
    #it receives the final node to where to the heuristics will be calculated and 
    #the heuristic function that will be employed. There are two options: Manhattan and Hamming distance
    def computeHeuristic(self, finalNode, heuristicType):
        self.setHeuristic(0)

        if(heuristicType == "manhattan"):       #Manhattan distance
            for satellite in self.__listSatellites:
                for observation in self.__listObservations:
                    self.setHeuristic(abs(satellite.getPosition() - observation.getPosition()) + abs(satellite.getBand() - observation.getBand()))

        elif(heuristicType == "hamming"):       #Hamming distance
            for n in range(len(finalNode.getListSatellites())):
                if (self.getListSatellites()[n] != finalNode.getListSatellites()[n]):
                    self.setHeuristic(self.getHeuristic() +1 )
			       
                    
            



    #EQUALS
    #------------------------------------------------------------------------------------------------------------------------------ 


    #method that checks if the information from another node is equal to the one we have
    def equals (self,otherNode):
        #print("In method equals, observations: {0} {1}".format(len(self.__listObservations), range(len(self.__listObservations))))
        #checking that the lists of observations are equal, but looping through through them
        for x in range(len(self.__listObservations)):
            if (self.__listObservations[x].getIdNumber() != otherNode.getListObservations()[x].getIdNumber()
            or self.__listObservations[x].getBand() != otherNode.getListObservations()[x].getBand()
            or self.__listObservations[x].getPosition() != otherNode.getListObservations()[x].getPosition()
            or self.__listObservations[x].getMeasured() != otherNode.getListObservations()[x].getMeasured()):
                return False

        #checking that the lists of satellites are equal, but looping through through them
        #print("In method equals, satellites: {0} {1}".format(len(self.__listObservations), range(len(self.__listObservations))))
        for x in range(len(self.__listSatellites)):
            if (self.__listSatellites[x].getIdNumber() != otherNode.getListSatellites()[x].getIdNumber()
            or self.__listSatellites[x].getBand() != otherNode.getListSatellites()[x].getBand()
            or self.__listSatellites[x].getPosition() != otherNode.getListSatellites()[x].getPosition()
            or self.__listSatellites[x].getEnergy() != otherNode.getListSatellites()[x].getEnergy() ):
                return False

        return True  #otherwise, they are equal, so "true" is returned 



    
    #COMPUTE EVALUATION
    #------------------------------------------------------------------------------------------------------------------------------ 
    
    #method that executes the evaluation function of the problem for the node
    def computeEvaluation(self):
        self.__evaluation = self.__cost + self.__heuristic


    




    #SETTERS
    #------------------------------------------------------------------------------------------------------------------------------ 

 
    def setCost(self, cost):
        self.__cost = cost

    def setHeuristic(self, heuristic):
        self.__heuristic = heuristic

    def setEvaluation(self, evaluation):
        self.__evaluation = evaluation

    def setParent(self, parent):
        self.__parent = parent

    def setNextNode(self, nextNodeList):
        self.__nextNodeList = nextNodeList

    def setListSatellites (self, satellites):
        self.__listSatellites = satellites

    def setListObservations (self, observations):
        self.__listObservations = observations


   
     #GETTERS
     #------------------------------------------------------------------------------------------------------------------------------ 

     
    def getCost(self):
        return self.__cost

    def getHeuristic(self):
        return self.__heuristic

    def getEvaluation(self):
        return self.__evaluation

    def getParent(self):
        return self.__parent

    def getNextNode(self):
        return self.__nextNodeList

    def getListSatellites(self):
        return self.__listSatellites

    def getListObservations(self):
        return self.__listObservations





        

