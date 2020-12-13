import OpenList
import objects.Satellite

class node:
    cost = None
    heuristic = None
    evaluation = None
    parent = None
    nextNodeList = None

    #list of satellites
    listSat = []

    #list of obserations that need to be measured
    listObs = []


    #constructor
    def __init__(self, *args): 
    
    #in python it is not possible to create several constructors, so we include different cases
    #depending on the number of received parameters

        #if a node is received (just 1 single argument)
        if len(args) == 5:
            self.cost = args[0]
            self.heuristic= args[1]
            self.evaluation = args[2]
            self.parent = args[3]
            self.nextNodeList = args[4]
        
        #receiving 3 paremeters: parentNode, list of satellites and list of observations
        if len(args) == 3:
            self.parent = args[0]
            self.listSat = args[1]
            self.listObs = args [2]



    #method that computes the heuristic
    def computeHeuristic(self,finalNode):
        self.heuristic = 0


    #method that checks if the information from another node is equal to the one we have
    #def equals (otherNode):

        

