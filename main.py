import sys
from colorama import Fore, Back, Style 
import lib.Node as Node
import lib.OpenList as OpenList
import lib.AStar as AStar

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
    op = OpenList.openlist()
    nodeopenlist1 = Node.node(None, None, None)
    nodeopenlist1.setEvaluation(3)
    op.insertAtEvaluation(nodeopenlist1)
    nodeopenlist2 = Node.node(None, None, None)
    nodeopenlist2.setEvaluation(2)
    op.insertAtEvaluation(nodeopenlist2)
    nodeopenlist3 = Node.node(None, None, None)
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



    print("Number of lines of file {0}: {1}\nFirst line: {2}\nParent of node2: {3}".format(sys.argv[1], numlines, obsraw, node2.getParent()))
    fileraw.close()

if __name__ == '__main__':
    main()
