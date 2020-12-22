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
        print(Back.RED + " Error happened when opening the input file " + Style.RESET_ALL)
        exit(1)

    filelinelist = fileraw.read().split('\n')
    fileraw.close()

    observationliststart = []
    satelliteliststart = []

    try:
        idcounter = 0

        for obscoord in re.sub('([OBS: ]|[()])', '', filelinelist[0]).split(';'):
            idcounter += 1
            obscoordlist = list(map(int, obscoord.split(',')))
            observationliststart.append(Observation.observation(idcounter, obscoordlist[0], obscoordlist[1]))
            #print("obs", idcounter, obscoordlist[0], obscoordlist[1])

        idcounter = 0

        for position in range(1, len(filelinelist)):
            idcounter += 1
            poscoordlist = list(map(int, re.sub('(SAT)\w+: {1}', '', filelinelist[position]).split(';')))
            satelliteliststart.append(Satellite.satellite(idcounter, (idcounter), 0, "iddle", poscoordlist))
            #print("pos", idcounter, (idcounter), 0, "iddle", poscoordlist)

    except:
        print(Back.RED + " Object creation failed: Invalid file contents " + Style.RESET_ALL)
        exit(1)

    satellitelistgoal = []
    observationlistgoal = []

    InitialNode = Node.node(None, satelliteliststart, observationliststart)
    FinalNode = Node.node(None, satellitelistgoal, observationlistgoal)
    astar = AStar.astar(InitialNode, FinalNode)

    stdout_fileno = sys.stdout
    sys.stdout = open('{0}.output'.format(sys.argv[1]), 'w')
    astar.algorithm()
    sys.stdout.close()
    sys.stdout = stdout_fileno



if __name__ == '__main__':
    main()
