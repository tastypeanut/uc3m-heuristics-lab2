import AStar
import OpenList

class node:
    cost = None
    heuristic = None
    evaluation = None
    parent = None
    nextNodeList = None

    def __init__(self, c, h, ev, par, nextN): 
        self.cost = c
        self.heuristic= h
        self.evaluation = ev
        self.parent = par
        self.nextNodeList = nextN