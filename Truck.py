# the truck will be used as the container for packages

class Truck:
    def __init__(self):
        self.container = []
        self.speed = 18
        self.milesTravelled = 0
        self.capacity = 16
        self.status = "AT_HUB"

    def addPackage(self, package):
        self.container.append(package)

    def removePackage(self, package):
        self.container.remove(package)

    def addMiles(self, milestravelled):
        self.milesTravelled += milestravelled

    def setStatus(self, status):
        self.status = status
