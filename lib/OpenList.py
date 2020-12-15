import lib.Node as Node

#this class represents the implementation of the open list that will be used in the A* algorithm

class openlist:
    _rootNode = None


    #CONSTRUCTOR

    def __init__(self): 
        self.setRootNode(Node.node())


    #INSERT AT EVALUATION    

    def insertAtEvaluation(self, newElem):
       # newElem = Node.node()                    #CHECK THIS!!!
        newNode = Node.node(newElem)
        posNode = None
        nodeIt = self._rootNode.getNextNode()
        if (nodeIt == None):
            self._rootNode.setNextNode(newNode)
        elif (nodeIt.getEvaluation() > newNode.getEvaluation()):
            newNode.setNextNode(nodeIt)
            self._rootNode.setNextNode(newNode)
        else:
            while (nodeIt != None):
                posNode = nodeIt
                nodeIt = nodeIt.getNextNode()
                if (nodeIt == None):
                    posNode.setNextNode(newNode)
                    break
                elif (nodeIt.getEvaluation() > newNode.getEvaluation()):
                    newNode.setNextNode(nodeIt)
                    posNode.setNextNode(newNode)
                    break

        
    #method that extracts the first node from the list and retuns it
    def pullFirst(self):
        node = self._rootNode.getNextNode()
        self._rootNode.setNextNode(node.getNextNode())
        return node


    #method that adds a new node at the beggining of the list

    def addFirst(self, newElem):
        newNode = Node.node(newElem)  #creating the new node with the other constructor
        oldNode = self._rootNode.getNextNode()  #last node
        self._rootNode.setNextNode(newNode)
        newNode.setNextNode(oldNode)


     #method that adds a new node at the end of the list

    def addLast(self, newElem):
        newNode = Node.node(newElem)
        lastNode = None
        nodeIt = self._rootNode.getNextNode()
        while (nodeIt != None):
            lastNode = nodeIt
            nodeIt = nodeIt.getNextNode()
        if (lastNode == None):
            self._rootNode.setNextNode(newNode)
        else: lastNode.setNextNode(newNode)


    def isEmpty(self):
        return (self._rootNode.getNextNode() == None)


    def getSize(self):
        size = 0
        nodeIt = self._rootNode.getNextNode()
        while (nodeIt != None):
            size += 1
            nodeIt = nodeIt.getNextNode()
        return size
    
    def getRootNode(self):
        return self._rootNode
    
    def setRootNode(self, rootnode):
        self._rootNode = rootnode



