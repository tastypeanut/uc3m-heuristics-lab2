#this class represents each of the activities that the satellites can do on each of the bands

class activity:
    __type = None  #activity type: idle, measurement, dowlink, turn, charge
    __cost = None #cost of permforming the activity




    #CONSTRUCTOR

    #it receives the type and cost of the activity
    def __init__(self, typ, cost):
        self.setType(typ)
        self.setCost(cost)





    #SETTERS

    def setType(self,typ):
        self.__type = typ


    def setCost(self,cost):
        self.__cost = cost



    #GETTERS

    def getType(self):
        return self.__type

    def getCost(self):
        return self.__cost

