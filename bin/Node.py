import OpenList

class node:
    cost = None
    heuristic = None
    evaluation = None
    parent = None
    nextNodeList = None

    #constructor
    def __init__(self, c, h, ev, par, nextN): 
        self.cost = c
        self.heuristic= h
        self.evaluation = ev
        self.parent = par
        self.nextNodeList = nextN


    #method that computes the heuristic
    def computeHeuristic(self,finalNode):
        self.heuristic = 0


    #method that checks if the information from another node is equal to the one we have
    #def equals (otherNode):

        

