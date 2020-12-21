import time
import lib.OpenList as OpenList
import lib.Node as Node
import lib.objects.Satellite as Satellite
import lib.objects.States as States
import lib.objects.Observation as Observation

#this class represents the A* algorithm
class astar:



    #the fields of this class are an open list, a closed list, an intial node,
    #a goal node and a boolena find goal
    
    __openList = OpenList.openlist() #list of nodes to explore
    __closedList = None #list of nodes that have already been explored
    __initialNode = None #initial node of the problem
    __goalNode = None #goal node
    __findGoal = None #this variable is used to check if the goal has been found
   


    #CONSTRUCTOR

    #it receives the initial and goal states
    def __init__(self, initialNode, goalNode):
    
       
        self.setInitialNode(initialNode)
        self.setGoalNode(goalNode)
        self.setFindGoal(False) #the findGoal variable is set to "false" 


        #computing heuristics and initial costs

        self.__initialNode.computeHeuristic(self.__goalNode,'manhattan')     #CORRECT THIS!!!
        self.__initialNode.setCost(0)
        self.__initialNode.computeEvaluation()
        self.__goalNode.computeHeuristic(self.__goalNode, 'manhattan' )

       
        #generating a list of explored and unexplored nodes

        self.__closedList = []   

        self.__openList = OpenList.openlist()
      
        self.__openList.insertAtEvaluation(self.__initialNode)
        
        #self.__openList.setRootNode(self.__initialNode)

        


    #ADD ADJACENT 
    
    #method that inserts in the open list all the nodes of the observations that can be taken in this moment
    def addAdjacentNodes(self,currentNode):
        satelliteList = currentNode.getListSatellites()     #list of satellites
        observationList = currentNode.getListObservations() #list of observations


        for satellite in satelliteList:        #this loop will make that all the satellites are in the same time (position)
            if (satellite.getPosition() >= -1 and satellite.getPosition() < 23):                         #CORRECT THIS!!!
                satellite.setPosition(satellite.getPosition() + 1)
            elif (satellite.getPosition() >= 23 or satellite.getPosition() < 0):
                satellite.setPosition(0)
                
            #satellite.setObservation(None)      #setting the observations to "None"
            print("Satellite {0} position is : {1}".format(satellite.getIdNumber(),satellite.getPosition()))

            
        for satellite in satelliteList:  #moving through the list of satellites to 
            if (satellite.getPosition() > 11): #satellites can only do activies from 0 to 11 
                continue  #it won't do anything during this time
               
            print("SAT: {0}".format(satellite.getIdNumber()))
            countObservations = 0
            for observation in observationList:     #moving through the list of observations
                childNode = Node.node(currentNode)  #creating  child node

                #MEASURE
                print("Observation position is : {0}".format(observation.getPosition()))
                #checking that the observation has not been measured and that it has energy
                if (satellite.getPosition() == observation.getPosition() and not(observation.getMeasured()) and satellite.getEnergy() >= satellite.states.measurement):      #checking that they are in the same position (x axis
 
                        if (satellite.getBand() == 0 or satellite.getBand() == 2): #CASE for bands 0 and 2
                            if (satellite.getBand() == observation.getBand() or satellite.getBand() + 1 == observation.getBand()):
                                satellite.measure(observation)  #measuring
                                #if (satellite.getActivity() == "measurement"):   #making sure that the measurement has been performed
                                    #observationList.remove(observation)   #removing the observation from the list
                                if (self.checkNode(childNode)):
                                    childNode.computeHeuristic(None,"manahattan")
                                    childNode.computeEvaluation()
                                    childNode.setParent(currentNode)
                                    childNode.setNextNode(None)
                                    print("CASE 1: observation {0} is measured by satellite {1} ".format(observation.getIdNumber(), satellite.getIdNumber()))
                                    print("OpenList size was:{0}".format(self.__openList.getSize()))
                                    self.__openList.insertAtEvaluation(childNode)
                                    print("Now it is:{0}".format(self.__openList.getSize()))
                                    break       #it has already done an activity, so the rest do not need to be checked

                        if (satellite.getBand() == 1 or satellite.getBand() == 3): # CASE for bands 1 and 3
                            if(satellite.getBand() == observation.getBand() or satellite.getBand() - 1 == observation.getBand()): 
                                satellite.measure(observation)  #measuring
                                #if (satellite.getActivity() == "measurement"):   #making sure that the measurement has been performed
                                # observationList.remove(observation)  #removing the observation from the list
                                if (self.checkNode(childNode)):
                                    childNode.computeHeuristic(None,"manahattan")
                                    childNode.computeEvaluation()
                                    childNode.setParent(currentNode)
                                    childNode.setNextNode(None)
                                    print("CASE 2: observation {0} is measured by satellite {1} ".format(observation.getIdNumber(), satellite.getIdNumber()))
                                    print("OpenList size was:{0}".format(self.__openList.getSize()))
                                    self.__openList.insertAtEvaluation(childNode)
                                    print("Now it is:{0}".format(self.__openList.getSize()))
                                    break   #it has already done an activity, so the rest do not need to be checked


                #DOWLINK    

                elif (satellite.getActivity() == "measurement" and satellite.getEnergy() >= satellite.states.downlink):    #the last activity performed by the satellite was "measure", so now it needs to downlink the observation
                    obs = satellite.getObservation()
                    satellite.downlink()   #the satellite performs the downlinking of the observation
                    if (self.checkNode(childNode)):
                                childNode.computeHeuristic(None,"manahattan")
                                childNode.computeEvaluation()
                                childNode.setParent(currentNode)
                                childNode.setNextNode(None)
                                print("CASE 3: observation {0} is downlinked by satellite {1} ".format(obs.getIdNumber(), satellite.getIdNumber()))
                                print("OpenList size was:{0}".format(self.__openList.getSize()))
                                self.__openList.insertAtEvaluation(childNode)
                                print("Now it is:{0}".format(self.__openList.getSize()))
                                break   #it has already done an activity, so the rest do not need to be checked




                #CHARGE

                elif (satellite.getEnergy() < satellite.states.measurement or satellite.getEnergy() < satellite.states.downlink):
                    satellite.charge()
                    if (self.checkNode(childNode)):
                                childNode.computeHeuristic(None,"manahattan")
                                childNode.computeEvaluation()
                                childNode.setParent(currentNode)
                                childNode.setNextNode(None)
                                print("CASE 5: Satellite {0} is charging ".format(satellite.getIdNumber()))
                                print("OpenList size was:{0}".format(self.__openList.getSize()))
                                self.__openList.insertAtEvaluation(childNode)
                                print("Now it is:{0}".format(self.__openList.getSize()))
                                break
                    

                
                #IDDLE                  #CHECK!!!

                else:
                    satellite.iddle()       #do nothing
                    if (self.checkNode(childNode)):
                                childNode.computeHeuristic(None,"manahattan")
                                childNode.computeEvaluation()
                                childNode.setParent(currentNode)
                                childNode.setNextNode(None)
                                print("CASE 4: satellite {0} is iddle ".format(satellite.getIdNumber()))
                                print("OpenList size was:{0}".format(self.__openList.getSize()))
                                self.__openList.insertAtEvaluation(childNode)
                                print("Now it is:{0}".format(self.__openList.getSize()))
                                
                
                countObservations = countObservations +1
               

                



    #ALGORITHM

    #implementation of the A* algorithm
    def algorithm(self):
       # time1 = int(time.time() * 1000) 
       # initialTime = int(round(time1 * 1000)) #this will be used to take the execution time

        currentNode = None  #defining a node

        while not(self.__openList.isEmpty()):    #checking that the open list is not empty
            currentNode = self.__openList.pullFirst()   #getting the first node from the open list
            if self.checkNode(currentNode):  #checking that the node has not been expanded
                if(self.isGoalNode(currentNode)):  #checking if its the goal node
                    print("IT HAS FOUND THE GOAL NODE")
                    self.setGoalNode(currentNode) 
                    for node in self.getPath(currentNode):
                        for satellite in node.getListSatellites():
                            print("------")
                            print(satellite.getActivity())
                            print("------")
                    self.setFindGoal(True)
                    break                   #as the goal has been found, we can stop
                self.addAdjacentNodes(currentNode)
                self.__closedList.append(currentNode)  #including the node in the closed list
       # finalTime = int(round(time.time()))   #final time
        

       # time = (finalTime - initialTime)  #computing the difference
        return 5
        #return time



    #CHECK NODE

    #method that checks if the node has already been explored. It receives a node an it's compared with all the nodes from the closed list
    #it returns "false" if the node has already been expanded
    def checkNode(self, currentNode):
        expandNode = True       #variable that will be returned
        for node in self.__closedList:  #looping through the list of nodes that have already been expaned 
            #print(node.getListObservations())
           # print("Checking node: {0} (closed list) against {1} (current node)".format(node, currentNode))
            #print(currentNode.equals(node))
            if(currentNode.equals(node)):  #checking if they are equal
                expandNode = False      #in that case, our result variable is set to "false"
                break
            #print("expand node: {0}".format(expandNode))
        return expandNode



            

    #IS GOAL

    #method that checks if the goal has been reached. That means that all the observations have been measured and dowlinked
    def isGoalNode(self, currentNode):
        for observation in currentNode.getListObservations():       #checking that all the observations have been measured
            if (observation.getMeasured() == False):
                return False
        for satellite in currentNode.getListSatellites():       #checking that it has been downlinked (if variable activity equals "measurement", 
            if (satellite.getActivity() == "measurement"):      # it means that there's a satellite that has not finished downlinking)
                return False   
        return True





    #PRINT OPEN LIST

    #method that prints the open list size
    def printOpenList(self):
        print(self.__openList.getSize())




    #GET PATH

    #method that returns the path followed to reach the received node
    def getPath(self,currentNode):
        path = []
        path.append(currentNode)
        parent = currentNode.getParent()
        while parent != None:
            path.insert(0,parent)
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

   

