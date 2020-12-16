import lib.OpenList as OpenList
import lib.Node as Node

#this class represents the A* algorithm
class astar:

# 0: nothing, 1: basic information, 2: complete information
    printDebug = None

    #the fields of this class are an open list, a closed list, an intial node,
    #a goal node and a boolena find goal
    
    __openList = OpenList.openlist() #list of nodes to explore
    __closedList = None #list of nodes that have already been explored
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

        self.__initialNode.computeHeuristic(self.__goalNode,'manhattan')     #CORRECT THIS!!!
        self.__initialNode.setCost(0)
        self.__initialNode.computeEvaluation()
        self.__goalNode.computeHeuristic(self.__goalNode)

       
        #generating a list of explored and unexplored nodes

        self.__closedList = []   #CHECK THIS!

        self.__openList = OpenList.openlist()
      
        self.__openList.insertAtEvaluation(self.__initialNode)
        
        

        


    #CHECK NODE

    #method that checks if the node has already been explored. It receives a node an it's compared with all the nodes from the closed list
    def checkNode(self,currentNode):
        expandNode = True       #variable that will be returned
        for node in self.__closedList:  #looping through the list of nodes that have already been expaned 
            if(currentNode.equals(node)):  #checking ig they are equal
                expandNode = False      #in that case, our result variable is set to "false"
                break

        return expandNode




    #PRINT OPEN LIST

    #method that prints the open list size
    def printOpenList(self):
        print(self.__openList.getSize)




    #GET PATH

    #methos that re
    def getPath(self,currentNode):
        path = []
        path.append(currentNode)
        parent = currentNode.getParent()
        while  parent != None :
            path.append(0,parent)
            currentNode = parent
            parent = currentNode.getParent()

        return path




        


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

   

