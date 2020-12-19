#this class represents each of the activities that the satellites can do on each of the bands
from enum import Enum

class states():

    #activity type: idle, measurement, downlink, turn, charge with cost wich right now is set to None
    idle = None
    measurement = None
    downlink = None
    turn = None
    charge = None

    #CONSTRUCTOR

    #it recevies a list with the energy costs of each activity
    def __init__(self, energyCostList):
        self.measurement = energyCostList[0]
        self.downlink = energyCostList[1]
        self.turn = energyCostList[2]
        self.charge = energyCostList[3]
        self.iddle = 0