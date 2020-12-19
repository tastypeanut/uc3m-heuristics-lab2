#this class represents each of the activities that the satellites can do on each of the bands
from enum import Enum

class states(Enum):

    #activity type: idle, measurement, downlink, turn, charge with cost wich right now is set to None
    IDLE = None
    MEASUREMENT = None
    DOWNLINK = None
    TURN = None
    CHARGE = None

    #CONSTRUCTOR

    #it recevies a list with the energy costs of each activity
    def __init__(self, energyCostList):
        print ("TEST")
        