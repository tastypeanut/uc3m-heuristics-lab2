import sys
import re
from colorama import Fore, Back, Style 
import lib.Node as Node
import lib.OpenList as OpenList
import lib.AStar as AStar
import lib.objects.Satellite as Satellite
import lib.objects.Observation as Observation
import lib.objects.States as States

def main():

    #Try catch for opening file
    try:
        fileraw = open(sys.argv[1], 'r')
    except:
        print(Back.RED + " Error happened when opening the input file " + Style.RESET_ALL)  #error if problem with the input file
        exit(1)

    filelinelist = fileraw.read().split('\n')   #spliting the input file by lines
    fileraw.close()

    observationListStart = []   #initial list of observations
    satelliteListStart = []     #initial list of satellites

    try:
        idcounter = 0

        for obscoord in re.sub('([OBS: ]|[()])', '', filelinelist[0]).split(';'):
            idcounter += 1
            obscoordlist = list(map(int, obscoord.split(',')))
            observationListStart.append(Observation.observation(idcounter, obscoordlist[0], obscoordlist[1]))   #including observations
            #print("obs", idcounter, obscoordlist[0], obscoordlist[1])

        idcounter = 0

        for position in range(1, len(filelinelist)):
            idcounter += 1
            poscoordlist = list(map(int, re.sub('(SAT)\w+: {1}', '', filelinelist[position]).split(';')))
            satelliteListStart.append(Satellite.satellite(idcounter, (idcounter), 0, "iddle", poscoordlist))    #including satellites
            #print("pos", idcounter, (idcounter), 0, "iddle", poscoordlist)

    except:
        print(Back.RED + " Object creation failed: Invalid file contents " + Style.RESET_ALL)   #error if the input file format is not correct
        exit(1)

    satelliteListGoal = []      #final list of satellites
    observationListGoal = []    #finallist of observations

    InitialNode = Node.node(None, satelliteListStart, observationListStart)     #creating the initial node
    FinalNode = Node.node(None, satelliteListGoal, observationListGoal)         #creating the final node
    astar = AStar.astar(InitialNode, FinalNode, sys.argv[2])                    #creating A* object (sys.argv[2] is the heurtistic type)

    stdout_fileno = sys.stdout
    sys.stdout = open('{0}.output'.format(sys.argv[1]), 'w')
    statoutput = open('{0}.statistics'.format(sys.argv[1]), 'w')
    print("Total execution time: ", astar.algorithm(), " seconds.", file=statoutput)  #calling the A* algorithm method
    print("#Steps: ", astar.getPath(astar.getGoalNode()), file=statoutput)
   # print("#Expansions: ", astar.getCountExpansion(), file = statoutput) 
    sys.stdout.close()
    sys.stdout = stdout_fileno



if __name__ == '__main__':
    main()
