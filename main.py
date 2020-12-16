import sys
from colorama import Fore, Back, Style 
import lib.Node as Node
import lib.OpenList as OpenList
import lib.AStar as AStar
import lib.objects.Satellite as Satellite
import lib.objects.Observation as Observation

def main():
    try:
        fileraw = open(sys.argv[1], 'r')
    except:
        print(Back.RED + " Error happened when opening the file " + Style.RESET_ALL)
        exit(1)
    
    filearray = fileraw.read().split('\n')
    numlines = len(filearray)
    
    obsraw = filearray[0]

    node1 = Node.node("test", "test", "test")
    node2 = Node.node(node1)
    #unused variable, only for tests
    #astar1 = AStar.astar(1, 2, 3) #unused variable, only for tests

    ##TESTS


    #OpenList.py
    op = OpenList.openlist()   #creating an open list
    nodeopenlist1 = Node.node(None, None, None)    #node1
    nodeopenlist1.setEvaluation(3)
    op.insertAtEvaluation(nodeopenlist1)
    nodeopenlist2 = Node.node(None, None, None)    #node2
    nodeopenlist2.setEvaluation(2)
    op.insertAtEvaluation(nodeopenlist2)
    nodeopenlist3 = Node.node(None, None, None)     #node3
    nodeopenlist3.setEvaluation(5)
    op.insertAtEvaluation(nodeopenlist3)
    print(op.pullFirst().getEvaluation()) #Si imprime 2 insertAtEvaluation funciona
    print(op.getSize()) #Si imprime 2 getSize funciona
    #print(op.getRootNode()) #Esto cambia el nodo raíz, y si no tiene hijos asignados, la openlist estará vacía, comentamos esto para que funcionen las pruebas de después
    #op.setRootNode(node1)
    #print(op.getRootNode())
    print(op.isEmpty())
    nodeopenlist4 = Node.node(None, None, None)
    nodeopenlist4.setEvaluation(1)
    nodeopenlist5 = Node.node(None, None, None)
    nodeopenlist5.setEvaluation(1)
    op.addFirst(nodeopenlist4)
    op.addLast(nodeopenlist5)
    print(op.getSize())
    print(op.pullFirst().getEvaluation())
    print(op.pullFirst().getEvaluation())
    print(op.pullFirst().getEvaluation())
    print(op.pullFirst().getEvaluation())
    #print(op.pullFirst().getEvaluation())


    #PARENT-CHILD TESTS

    parentNode = Node.node(None, None, None)
    childNode = Node.node(parentNode, None, None)
    childNode2 = Node.node(parentNode, None, None)
    print(parentNode.getParent())
    print(childNode.getParent())
    print(childNode2.getParent())  #the parent of these two should be the same



    #Checking the creation of lists and nodes works properly

    l1 = []
    l1.append (Satellite.satellite(1,1,1,1))
    l1.append (Satellite.satellite(2,2,2,2))

    l3 = []
    l3.append (Satellite.satellite(1,1,1,1))
    l3.append (Satellite.satellite(2,2,2,2))


    l2 = []
    l2.append (Observation.observation(1,1,1))
    l2.append (Observation.observation(2,2,2))

    print(len(l1))

    childNode3 = Node.node(parentNode, l1, l2)
    print(len(childNode3.listSatellites))
    childNode4 = Node.node(parentNode, l3, l2)

    print(childNode3.equals(childNode4))


    print ("---------------------------------------")
    op2 = OpenList.openlist()   #creating an open list
    print(op2.getRootNode())
    node3 = Node.node(op.getRootNode(), None, None)  
    node4 = Node.node(None, None, None) 
    print(op2.getRootNode().getNextNode())
    op2.addFirst(node4)
    print(node4) 
    print(op2.getRootNode().getNextNode())
    print(node4.getNextNode())
    print(node3)
    op2.addLast(node3)
    print(op2.getRootNode().getNextNode().getNextNode())
    #op2.addFirst(node3)
    #print(node3.getParent())
    #print(node3)  
    #print(op2.getRootNode().getNextNode())
    #print(op2.getSize())



    print("Number of lines of file {0}: {1}\nFirst line: {2}\nParent of node2: {3}".format(sys.argv[1], numlines, obsraw, node2.getParent()))
    fileraw.close()

if __name__ == '__main__':
    main()
