import lib.Node as Node

#this class represents the implementation of the open list that will be used in the A* algorithm

class openlist:
    _rootNode = None


    #CONSTRUCTOR

    #it does not receive any parameters, and it initializes the root node
    def __init__(self): 
        self.setRootNode(Node.node())





    #INSERT AT EVALUATION    
    
    #this method inserts a node in the open list depending on its evaluation value (from smaller to greater)
    def insertAtEvaluation(self, newElem):
    
        newNode = Node.node(newElem)       #new node to be inserted
        posNode = None
        nodeIt = self._rootNode.getNextNode()    #auxiliary node, which  is the next one after the root node
        if (nodeIt == None):                     #checking if it is null
            self._rootNode.setNextNode(newNode)    #in that case, we simply place there our new node
        elif (nodeIt.getEvaluation() > newNode.getEvaluation()):
            newNode.setNextNode(nodeIt)
            self._rootNode.setNextNode(newNode)
        else:
            while (nodeIt != None):                 #moving along the list
                posNode = nodeIt
                nodeIt = nodeIt.getNextNode()
                if (nodeIt == None):                #checking if it is null   
                    posNode.setNextNode(newNode)
                    break
                elif (nodeIt.getEvaluation() > newNode.getEvaluation()):
                    newNode.setNextNode(nodeIt)
                    posNode.setNextNode(newNode)
                    break



    #PULL FIRST

    #method that extracts the first node from the list and retuns it
    def pullFirst(self):
        node = self._rootNode.getNextNode()
        self._rootNode.setNextNode(node.getNextNode())
        return node




    #ADD FIRST

    #method that adds a new node at the beggining of the list

    def addFirst(self, newElem):
        newNode = Node.node(newElem)  #creating the new node with the 1-parameter constructor
        oldNode = self._rootNode.getNextNode()  #copy of the original top node
        self._rootNode.setNextNode(newNode)
        newNode.setNextNode(oldNode)




    #ADD LAST

     #method that adds a new node at the end of the list

    def addLast(self, newElem):
        newNode = Node.node(newElem)     #creating the new node that will be inserted
        lastNode = None
        nodeIt = self._rootNode.getNextNode()   #auxiliary node
        while (nodeIt != None):             #moving along the list until we find the lsat position
            lastNode = nodeIt
            nodeIt = nodeIt.getNextNode()
        if (lastNode == None):
            self._rootNode.setNextNode(newNode)
        else: lastNode.setNextNode(newNode)


    #IS EMPTY

    #checking if the open list is empty. It returns false in that case
    def isEmpty(self):
        return (self._rootNode.getNextNode() == None)



    #GET SIZE

    #it returns the size of the list
    def getSize(self):
        size = 0
        nodeIt = self._rootNode.getNextNode()
        while (nodeIt != None):
            size += 1
            nodeIt = nodeIt.getNextNode()
        return size
    


    #GET ROOT NODE

    #returning the root node
    def getRootNode(self):
        return self._rootNode
    


    #SET ROOT NODE

    #species which is the root node
    def setRootNode(self, rootnode):
        self._rootNode = rootnode



