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
        self.setInitialNode(initialNode)
        self.setGoalNode(goalNode)
        self.setFindGoal(False) #the findGoal variable is set to "false" 

        #computing heuristics and initial costs

       # self.computeCosts()        #CORRECT THIS!!!

        self.__openList = OpenList.openlist()
        self.__openList.insertAtEvaluation(self.__initialNode)
        
        

    #auxiliary method to calculate the heuristics and initial costs
    #def computeCosts(self):
        #self.__initialNode.computeHeuristic(self.__goalNode,'manhattan')     #CORRECT THIS!!!
     #   self.__initialNode.setCost(0)
        #self.__initialNode.computeEvaluation()
      #  self.__goalNode.computeHeuristic(self.__goalNode)



        




     #SETTERS

 
    def setInitialNode(self, initialNode):
        self.__initialNode = initialNode


 
    def setGoalNode(self, goalNode):
        self.__goalNode = goalNode


    def setFindGoal(self, findGoal):
        self.__findGoal = findGoal

   
    def setPrintDebug(self, printDebug):
        printDebug = printDebug

    def setOpenList(self, openList):
        self.__openList = openList

    def setClosedList(self, closedList):
        self.__closedList = closedList


    
        
     #GETTERS

    def getInitialNode(self):
        return self.__initialNode

    def getGoalNode(self):
        return self.__goalNode

    def getOpenList(self):
        return self.__openList

    def getClosedList(self):
        return self.__closedList

   

