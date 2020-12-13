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
    op = OpenList.openlist() #unused variable, only for tests
    astar1 = AStar.astar(1, 2, 3) #unused variable, only for tests

    print("Number of lines of file {0}: {1}\nFirst line: {2}\nParent of node2: {3}".format(sys.argv[1], numlines, obsraw, node2.getParent()))
    fileraw.close()

if __name__ == '__main__':
    main()
