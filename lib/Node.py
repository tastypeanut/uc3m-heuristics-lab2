import OpenList
import objects.Satellite

class node:
    cost = None
    heuristic = None
    evaluation = None
    parent = None
    nextNodeList = None

    #constructor
    def __init__(self, *args): 
        if len(args) == 5:
            self.cost = args[0]
            self.heuristic= args[1]
            self.evaluation = args[2]
            self.parent = args[3]
            self.nextNodeList = args[4]



    #method that computes the heuristic
    def computeHeuristic(self,finalNode):
        self.heuristic = 0


    #method that checks if the information from another node is equal to the one we have
    #def equals (otherNode):

        

