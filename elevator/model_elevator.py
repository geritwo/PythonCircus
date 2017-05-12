# Create an "elevator" class
# The class should track the following things:
#  - elevator position
#  - elevator direction
#  - people in the elevator
#  - add people
#  - remove people
#
# Please remeber that negative amount of people would be troubling

class Elevator():

    def __init__(self):
        self.position = 0
        self.passengers = 0
        self.capacity = 8
        self.floors = 11
        self.message = "-"

    def setPosition(self, n):
        if self.position + n in range(self.floors + 1):
            self.position += n
        else:
            self.message = "ERROR! Can't move further!"

    def addPeople(self, people_in):
        if people_in + self.passengers > self.capacity:
            print("Can't move" + str(people_in) + "people in! Over capacity!")
            self.message = "ERROR! Over capacity!"
        else:
            self.passengers += people_in

    def rmPeople(self, people_out):
        if people_out > self.passengers:
            self.message = "ERROR! No more people!"
        else:
            self.passengers -= people_out

    def getFloors(self):
        return self.floors

    def getPosition(self):
        return self.position

    def getPassengers(self):
        return self.passengers

    def getMessage(self):
        return self.message

    def resetMessage(self):
        self.message = "-"

    def setMessage(self, msg):
        self.message = msg
