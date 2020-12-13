import lib.OpenList as OpenList
import lib.Node as Node

#this class represents the A* algorithm
class astar:

# 0: nothing, 1: basic information, 2: complete information
    printDebug = None

    #the fields of this class are an open list, a closed list, an intial node,
    #a goal node and a boolena find goal
    
    __openList = OpenList.openlist() #list of nodes to explore
    __closedList = [] #list of nodes that have already been explored
    __initialNode = None #initial node of the problem
    __goalNode = None #goal node
    __findGoal = None #this variable is used to check if the goal has been found



    #CONSTRUCTOR

    #it receives the initial and goal states
    def __init__(self, printDebug, initialNode, goalNode):
    
        self.printDebug = printDebug
        self.__initialNode = initialNode
        self.__goalNode = goalNode
        self.__findGoal = False #the findGoal variable is set to "false" 

    

      #  initialNode.computeHeuristic(goalNode)

        




    
        
