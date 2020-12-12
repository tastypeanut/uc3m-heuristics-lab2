import sys
from colorama import Fore, Back, Style 
sys.path.append("lib")
import Node
import OpenList

def main():
    try:
        fileraw = open(sys.argv[1], 'r')
    except:
        print(Back.RED + " Error happened when opening the file " + Style.RESET_ALL)
        exit(1)
    numlines = sum(1 for line in fileraw)
    filearray = fileraw.read().split('\n')
    obsraw = filearray[0]
    node1 = Node.node("test", "test", "test", "test", "test")
    op = OpenList.openList()
    print(node1.cost)
    fileraw.close()

if __name__ == '__main__':
    main()
