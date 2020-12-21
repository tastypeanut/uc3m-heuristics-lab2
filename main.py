import sys
from colorama import Fore, Back, Style 
import lib.Node as Node
import lib.OpenList as OpenList
import lib.AStar as AStar
import lib.objects.Satellite as Satellite
import lib.objects.Observation as Observation
import lib.objects.States as States

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
    listenergy = [1, 2, 3, 4, 20]

    l1 = []
    l1.append (Satellite.satellite(1,1,1, "measurement",listenergy))
    l1.append (Satellite.satellite(2,2,2,"measurement",listenergy))

    l3 = []
    l3.append (Satellite.satellite(1,1,1,"measurement",listenergy))
    l3.append (Satellite.satellite(2,2,2,"measurement",listenergy))


    l2 = []
    l2.append (Observation.observation(1,1,1))
    l2.append (Observation.observation(2,2,2))

    print(len(l1))

    childNode3 = Node.node(parentNode, l1, l2)
    print(len(childNode3.getListSatellites()))
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


#Change band tests

    print ("---------------------------------------")
    listenergy = [1, 2, 3, 4, 20]
    sat = Satellite.satellite(2, 1, 4, "measurement",listenergy)
    obs = Observation.observation(3,2,1)
    print(sat.getBand())
    sat.turn()
    print(sat.getBand())
    sat.measure(obs)
    sat.downlink()
    print(sat.getEnergy())
    sat.charge()
    print(sat.getEnergy())

    print ("---------------------------------------")


    #TEST FOR REACHING OBSERVATIONS

    sat2 = Satellite.satellite(2,2,0,"measurement",listenergy) 
    
    l4 = []
    l4.append (Observation.observation(1,1,1))
    l4.append (Observation.observation(4,2,2))
    l4.append (Observation.observation(2,5,2))
    l4.append (Observation.observation(3,1,2))

    for x in range (70):        #moving along the position (x axis)
        for observation in l4:  #moving along the observations
           # print(sat2.getPosition())
            if ( (sat2.getBand() == observation.getBand() or sat2.getBand() + 1 == observation.getBand() )      #checking conditions
            and sat2.getPosition() == observation.getPosition() and not(observation.getMeasured()) ):
               # print("hi")
                sat2.measure(observation)  #measuring
                break                                   #nothing else can be measured in that position at the moment
        sat2.setPosition(sat2.getPosition() + 1)       #moving to the next position
        if(sat2.getPosition() == 24):   #if the day has finished, we start again
            sat2.setPosition(0) 


        

    for observations in  l4:
        print(observations.getMeasured())


    print("---------------------------------------")

    listenergy = [50, 1, 3, 4, 4]

    satelliteliststart = []
    satelliteliststart.append(Satellite.satellite(1,1,-1,"",listenergy))
    satelliteliststart.append(Satellite.satellite(2,2,-1,"",listenergy))
    #satelliteliststart[0].setHasObservation(True)

    satellitelistgoal = []
    #satellitelistgoal.append(Satellite.satellite(1,1,5,"charge",listenergy))
    #satellitelistgoal.append(Satellite.satellite(2,2,7,"charge",listenergy))

    observationliststart = []
    observationliststart.append (Observation.observation(1,1,0))
    observationliststart.append (Observation.observation(2,2,2))
    observationliststart.append (Observation.observation(3,2,3))
    observationliststart.append (Observation.observation(4,1,4))
    observationliststart.append (Observation.observation(5,1,5))
    observationliststart.append (Observation.observation(6,1,5))
    observationliststart.append (Observation.observation(7,1,5))

    observationlistgoal = []
    #observationlistgoal.append (Observation.observation(1,1,11))
    #observationlistgoal.append (Observation.observation(2,2,3))

    InitialNode = Node.node(None, satelliteliststart, observationliststart)
    FinalNode = Node.node(None, satellitelistgoal, observationlistgoal)
    astar = AStar.astar(InitialNode, FinalNode)

    astar.algorithm()
    print("Size of OpenList: {0}\n".format(astar.getOpenList().getSize()))
    print("Size of ClosedList: {0}\n".format(len(astar.getClosedList())))
    print("------------------------------------------")
    print("Length of path: {0}".format(len(astar.getPath(FinalNode))))

    for obs in InitialNode.getListObservations():
        print(obs.getMeasured())
        #if (i.getListSatellites() != None):
            #print(i.getParent().getListSatellites())
          #  print(i.getListSatellites()[0].getEnergy())
           # print(i.getListSatellites()[0].getActivity())

    print("------------------------------------------")
    #testpull1 = astar.getOpenList().pullFirst().getListSatellites()
    #testpull2 = astar.getOpenList().pullFirst().getListSatellites()
    #print(testpull1[0].getActivity())
    #print(testpull1[1].getActivity())
    #print(testpull2[0].getActivity())
    #print(testpull2[1].getActivity())


    #print("Number of lines of file {0}: {1}\nFirst line: {2}\nParent of node2: {3}".format(sys.argv[1], numlines, obsraw, node2.getParent()))
    fileraw.close()

if __name__ == '__main__':
    main()
