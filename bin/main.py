import sys
import Node
import OpenList

def main():
    try:
        fileraw = open(sys.argv[1], 'r')
        numlines = sum(1 for line in fileraw)
        filearray = fileraw.read().split('\n')
        obsraw = filearray[0]
        node1 = Node.node("test", "test", "test", "test", "test")
        op= OpenList.openList()
        print(node1.cost)
    finally:
        fileraw.close()

if __name__ == '__main__':
    main()
