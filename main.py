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
        print(Back.RED + " Error happened when opening the file " + Style.RESET_ALL)
        exit(1)

    filelinelist = fileraw.read().split('\n')

    observationlist = []
    satellitelist = []

    try:
        idcounter = 0

        for obscoord in re.sub('([OBS: ]|[()])', '', filelinelist[0]).split(';'):
            idcounter += 1
            obscoordlist = obscoord.split(',')
            observationlist.append(Observation.observation(idcounter, obscoordlist[0], obscoordlist[1]))
            #print("obs", idcounter, obscoordlist[0], obscoordlist[1])
        idcounter = 0

        for position in range(1, len(filelinelist)):
            idcounter += 1
            poscoordlist = re.sub('(SAT)\w+: {1}', '', filelinelist[position]).split(';')
            satellitelist.append(Satellite.satellite(idcounter, (idcounter), 0, "iddle", poscoordlist))
            #print("pos", idcounter, (idcounter), 0, "iddle", poscoordlist)
    except:
        print(Back.RED + " Object creation failed: Invalid file contents " + Style.RESET_ALL)
        exit(1)
    

    InitialNode = Node.node(None, satellitelist, observationlist)
    FinalNode = Node.node(None, None, None)
    astar = AStar.astar(InitialNode, FinalNode)
    astar.algorithm()
    fileraw.close()



if __name__ == '__main__':
    main()
