import lib.OpenList as OpenList
import lib.objects.Satellite as Satellite
import lib.objects.Observation as Observation

class node:
    __cost = None
    __heuristic = None
    __evaluation = None
    __parent = None
    __nextNodeList = None

    #list of satellites
    listSatellites = []

    #list of observations that need to be measured
    listObservations = []


    #CONSTRUCTOR


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
        
        #receiving 3 paremeters: parentNode, list of satellites and list of observations
        if len(args) == 3:
            self.setParent(args[0])
            self.listSat = args[1]
            self.listObs = args[2]




    #COMPUTE HEURISTIC


    #method that computes the heuristic
    #it receives the final node to where to the heuristics will be calculated and 
    #the heuristic function that will be employed. There are two options: Manhattan and Hamming distance
    def computeHeuristic(self,finalNode,heuristicType):
        self.heuristic = 0

        for obs in self.listObservations:
            if heuristicType == 'manhattan':
                result = 5

        #Manhattan distance
        



    #EQUALS


    #method that checks if the information from another node is equal to the one we have
    def equals (self,otherNode):
        
        #checking that the lists of observations are equal, but looping through through them
        for x in range(len(self.listObservations)):
            if(self.listObservations[x].getIdNumber != otherNode.listObservations[x].getIdNumber ):
                return False

        
        #checking that the lists of satellites are equal, but looping through through them
        for x in range(len(self.listSatellites)):
            if(self.listSatellites[x].getIdNumber != otherNode.listSatellites[x].getIdNumber ):
                return False



    
    #COMPUTE EVALUATION
    
    #method that executes the evaluation function of the problem for the node
    def computeEvaluation(self):
        self.__evaluation = self.__cost + self.__heuristic


    




    #SETTERS

 
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


   
     #GETTERS

     

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





        

