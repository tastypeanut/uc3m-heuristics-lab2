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
    __heuristicType = None  #heuristic type that has to be calculated
    __totalCost = None #total cost from reaching the goal state
   
    counter = 0     #auxuliary counter used for printing the step number



    #CONSTRUCTOR
    #------------------------------------------------------------------------------------------------------------------------------ 

    #it receives the initial and goal states and the heuristic types 
    def __init__(self, initialNode, goalNode, heuristicType):
    
       
        self.setInitialNode(initialNode)
        self.setGoalNode(goalNode)
        self.setFindGoal(False)  #the findGoal variable is set to "false" 
        self.setHeuristicType(heuristicType)
        self.setTotalCost(0) #the initial total cost is 0
       


        #computing heuristics and initial costs

        self.__initialNode.computeHeuristic(self.__goalNode,self.__heuristicType)     
        self.__initialNode.setCost(0)
        self.__initialNode.computeEvaluation()
        self.__goalNode.computeHeuristic(self.__goalNode, self.__heuristicType)

       
        #generating a list of explored and unexplored nodes

        self.__closedList = []   

        self.__openList = OpenList.openlist()
      
        self.__openList.insertAtEvaluation(self.__initialNode)
        
        #self.__openList.setRootNode(self.__initialNode)

        

    
    #ADD ADJACENT 
    #------------------------------------------------------------------------------------------------------------------------------
    
    #method that inserts in the open list all the nodes of the observations that can be taken in this moment
    def addAdjacentNodes(self,currentNode):
        satelliteList = currentNode.getListSatellites()     #list of satellites
        observationList = currentNode.getListObservations() #list of observations


        for satellite in satelliteList:        #this loop will make that all the satellites are in the same time (position
            if (satellite.getHasStartedMoving()):
                if (satellite.getPosition() >= 0 and satellite.getPosition() < 23):                     
                    satellite.setPosition(satellite.getPosition() + 1)
                elif (satellite.getPosition() >= 23 or satellite.getPosition() < 0):
                    satellite.setPosition(0)
                
            if(satellite.getIdNumber() == 1):         
                print("{0}.".format(self.counter), end='')        #printing current position
            self.counter = self.counter + 0.5

            
        for satellite in satelliteList:  #moving through the list of satellites to 
            childNode = Node.node(currentNode)
            satellite.setHasStartedMoving(True)
               
            print("SAT{0}: ".format(satellite.getIdNumber()), end='')        #printing SAT Id number   

            if (satellite.getPosition() > 11):  #satellites can only do activies from 0 to 11       #CASE FOR POSITION > 11
                 satellite.iddle()   #the satellite performs the downlinking of the observation
                 if(satellite.getIdNumber() == 1):
                    print("IDLE, ", end='') #printing a comma if it is SAT1
                 if(satellite.getIdNumber() == 2):
                    print("IDLE ") #printing a new line if it is SAT2

                 if (self.checkNode(childNode)):         #checking if the node has already been expanded
                    self.createChildNode(currentNode, childNode, satelliteList, observationList)
                 continue  #it won't do anything during this time                        
            countObservations = 0   #auxiliary variable to count the number of observations

            
            for observation in observationList:     #moving through the list of observations
            

                #MEASURE

                #checking that the observation and the satellite are in the same position,also that the observation has not been measured, 
                #that it has energy, and that is does not have an observation  that needs to be dowlinked
                if (satellite.getPosition() == observation.getPosition() and not(observation.getMeasured()) and satellite.getEnergy() >= satellite.states.measurement and satellite.getObservation() == None):  


                        if (satellite.getIdNumber() == 1):      # CASE for SAT 1
                            if(satellite.getBand() == observation.getBand() or satellite.getBand() - 1 == observation.getBand()):   #it can access its current band an one below
                                satellite.measure(observation)  #measuring
                                self.setTotalCost(self.getTotalCost() + satellite.states.measurement) #updating total cost
    
                                if(satellite.getIdNumber() == 1):
                                    print("Measure O{0}, ".format(observation.getIdNumber()), end='')#printing a comma if it is SAT1
                                if(satellite.getIdNumber() == 2):
                                    print("Measure O{0} ".format(observation.getIdNumber())) #printing a new line if it is SAT2

                                if (self.checkNode(childNode)):     #checking if the node has already been expanded
                                    self.createChildNode(currentNode, childNode, satelliteList, observationList)
                                    break      #it has already done an activity, so the rest do not need to be checked

                        if (satellite.getIdNumber() == 2):      #CASE for SAT 2
                            if (satellite.getBand() == observation.getBand() or satellite.getBand() + 1 == observation.getBand()):  #it can access its current band an one above
                                satellite.measure(observation)  #measuring
                                self.setTotalCost(self.getTotalCost() + satellite.states.measurement) #updating total cost
                                
                                if(satellite.getIdNumber() == 1):
                                    print("Measure O{0}, ".format(observation.getIdNumber()), end='')#printing a comma if it is SAT1
                                if(satellite.getIdNumber() == 2):
                                    print("Measure O{0} ".format(observation.getIdNumber())) #printing a new line if it is SAT2

                                if (self.checkNode(childNode)):     #checking if the node has already been expanded
                                    self.createChildNode(currentNode, childNode, satelliteList, observationList)
                                    break      #it has already done an activity, so the rest do not need to be checked


                #DOWLINK    

                elif (satellite.getActivity() == "measurement" and satellite.getEnergy() >= satellite.states.downlink):    #the last activity performed by the satellite was "measure", so now it needs to downlink the observation
                    satellite.downlink()   #the satellite performs the downlinking of the observation
                    self.setTotalCost(self.getTotalCost() + satellite.states.downlink) #updating total cost
                   
                    if(satellite.getIdNumber() == 1):
                        print("Downlink O{0}, ".format(observation.getIdNumber()), end='')     #printing a comma if it is SAT1
                    if(satellite.getIdNumber() == 2):
                            print("Downlink O{0} ".format(observation.getIdNumber())) #printing a new line if it is SAT2

                    if (self.checkNode(childNode)):         #checking if the node has already been expanded
                        self.createChildNode(currentNode, childNode, satelliteList, observationList)
                        break      #it has already done an activity, so the rest do not need to be checked
                          




                #CHARGE

                #checking that there's no energy to perform some activity. As we are using "if else", this case will be executed if others haven't been executed before 
                elif (satellite.getEnergy() < satellite.states.measurement or satellite.getEnergy() <  satellite.states.downlink):  

                    satellite.charge()  #charging
                    self.setTotalCost(self.getTotalCost() + satellite.states.charge) #updating total cost
                    
                    if(satellite.getIdNumber() == 1):
                        print("Charge, ", end='')   #printing a comma if it is SAT1
                    if(satellite.getIdNumber() == 2):
                        print("Charge ")   #printing a new line if it is SAT2

                    if (self.checkNode(childNode)):         #checking if the node has already been expanded
                        self.createChildNode(currentNode, childNode, satelliteList, observationList)
                        break       #it has already done an activity, so the rest do not need to be checked


                 #TURN

                #it will turn into another band if it has enough energy, the previous activity was not "measurent" (it should downlink it), and there's no 
                #observation that can be measured at the moment
                elif (satellite.getEnergy() >= satellite.states.turn and satellite.getActivity() != "measurement" and satellite.getPosition() != observation.getPosition() and satellite.getBand() != observation.getBand()
                and( (satellite.getIdNumber() == 1 and satellite.getBand() - 1 != observation.getBand()) or (satellite.getIdNumber() == 2 and satellite.getBand() + 1 != observation.getBand()) ) 
                and ((satellite.getPosition() +1 != observation.getPosition() and not(observation.getMeasured())) )):
                   
                    satellite.turn()    #turning
                    self.setTotalCost(self.getTotalCost() + satellite.states.turn) #updating total cost

                    if(satellite.getIdNumber() == 1):
                        print("Turn, ", end='')    #printing a comma if it is SAT1
                    if(satellite.getIdNumber() == 2):
                        print("Turn ")  #printing a new line if it is SAT2

                    if (self.checkNode(childNode)):         #checking if the node has already been expanded
                        self.createChildNode(currentNode, childNode, satelliteList, observationList)
                        break       #it has already done an activity, so the rest do not need to be checked   

                 

                
                #IDLE                  

                #in any other case, it do nothing
                else:#(satellite.getEnergy() >= satellite.states.turn and satellite.getActivity() != "measurement" and satellite.getPosition() != observation.getPosition()):
                    if(countObservations == len(observationList) -1):   #we only want it to be "iddle" if it's the last observation from the list (in IDDLE we are not including "break")
                        satellite.iddle()       #do nothing

                        if(satellite.getIdNumber() == 1):
                            print("IDLE, ", end='') #printing a comma if it is SAT1
                        if(satellite.getIdNumber() == 2):
                            print("IDLE ") #printing a new line if it is SAT2      

                        if (self.checkNode(childNode)):  #checking if the node has already been expanded
                            self.createChildNode(currentNode, childNode, satelliteList, observationList)
                        
                                   


                                
                
                countObservations = countObservations + 1  #updaating auxiliary counter

        
        self.__openList.insertAtEvaluation(childNode)       #inserting the child node into the open list, taking into account its evaluation value




    #CREATE CHILD NODE
    #------------------------------------------------------------------------------------------------------------------------------

    #method that sets the properties of the new node (childNode)
    def createChildNode(self,currentNode,childNode, newListSatellites,newListObservations):
            childNode.setParent(currentNode)    #the parent will be the current node
            childNode.setNextNode(None)         #the next node is currently null
            childNode.setListSatellites(newListSatellites)
            childNode.setListObservations(newListObservations)
            childNode.computeHeuristic(self.__goalNode,self.__heuristicType)  #computing heurstic        
            childNode.computeEvaluation()       #computing evalution
           # print("OpenList size was:{0}".format(self.__openList.getSize()))                #REMOVE!!!
            #self.__openList.insertAtEvaluation(childNode)       #inserting in the open list taking into account the evaluation
           # print("Now it is:{0}".format(self.__openList.getSize()))                        #REMOVE!!!
                 



    #ALGORITHM
    #------------------------------------------------------------------------------------------------------------------------------

    #implementation of the A* algorithm
    def algorithm(self):
        initialTime = time.time()   #this will be used to take the execution time
       
        currentNode = None  #defining a node

        while not(self.__openList.isEmpty()):    #checking that the open list is not empty
            currentNode = self.__openList.pullFirst()  #getting the first node from the open list
            
            #currentNode.getListSatellites()[0].setPosition(3)
            #if self.checkNode(currentNode):  #checking that the node has not been expanded
            if(self.isGoalNode(currentNode)):  #checking if its the goal node
                print("IT HAS FOUND THE GOAL NODE")
                self.setGoalNode(currentNode) 
                #for node in self.getPath(currentNode):
                    #for satellite in node.getListSatellites():
                       # print("------")
                        #print(satellite.getActivity())                                         #REMOVE!!!
                        #print("------")
                print("Length of solution path: {0}".format(len(self.getPath(currentNode))))
                self.setFindGoal(True)
                break                   #as the  goal has been found, we can stop
            self.addAdjacentNodes(currentNode)
            self.__closedList.append(currentNode)  #including the node in the closed list

        finalTime = time.time()  #final time 
        resultTime = abs(finalTime - initialTime)  #computing the difference

        return resultTime       #returning the time
        




    #CHECK NODE
    #------------------------------------------------------------------------------------------------------------------------------

    #method that checks if the node has already been explored. It receives a node an it's compared with all the nodes from the closed list
    #it returns "false" if the node has already been expanded
    def checkNode(self, currentNode):
        expandNode = True       #variable that will be returned
        for node in self.__closedList:  #looping through the list of nodes that have already been expaned 
            #print(node.getListObservations())
           # print("Checking node: {0} (closed list) against {1} (current node)".format(node, currentNode))
            #print(currentNode.equals(node))
            if(currentNode.equals(node)):  #checking if they are equal
                expandNode = True      #in that case, our result variable is set to "false"
                break
            #print("expand node: {0}".format(expandNode))
        return expandNode



            

    #IS GOAL
    #------------------------------------------------------------------------------------------------------------------------------

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
    #------------------------------------------------------------------------------------------------------------------------------

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
    #------------------------------------------------------------------------------------------------------------------------------ 

 
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

    def setHeuristicType(self, heuristicType):
        self.__heuristicType = heuristicType

    def setTotalCost(self,totalCost):
        self.__totalCost = totalCost


    
        
    #GETTERS
    #------------------------------------------------------------------------------------------------------------------------------ 

    def getInitialNode(self):
        return self.__initialNode

    def getGoalNode(self):
        return self.__goalNode

    def getOpenList(self):
        return self.__openList

    def getClosedList(self):
        return self.__closedList

    def getHeuristicType(self):
        return self.__heuristicType

    def getTotalCost(self):
        return self.__totalCost