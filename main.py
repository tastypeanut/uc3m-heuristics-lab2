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

    #print(filelinelist[0].replace('OBS: ', '').split(';'))
    #print(re.sub('([OBS: ]|[()])', '', filelinelist[0]).split(';'))
    observationlist = []
    satellitelist = []
    idcounter = 0

    for obscoord in re.sub('([OBS: ]|[()])', '', filelinelist[0]).split(';'):
        idcounter += 1
        obscoordlist = obscoord.split(',')
        observationlist.append(Observation.observation(idcounter, obscoordlist[0], obscoordlist[1]))

    idcounter = 0

    for position in range(1, len(filelinelist)):
        idcounter += 1
        #for satellite in re.sub('(SAT)\w+: {1}', '', filelinelist[position]).split(';'):
        #print(re.sub('(SAT)\w+: {1}', '', filelinelist[position]).split(';'))
        poscoordlist = re.sub('(SAT)\w+: {1}', '', filelinelist[position]).split(';')
        #print(idcounter, (2*idcounter-2), 0, "iddle", poscoordlist)
        satellitelist.append(Satellite.satellite(idcounter, (2*idcounter-2), 0, "iddle", poscoordlist))

    try:
       exit()
    except:
        print(Back.RED + " Object creation failed: Invalid file contents " + Style.RESET_ALL)
        exit(1)
    


    fileraw.close()



if __name__ == '__main__':
    main()
