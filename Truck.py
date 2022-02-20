# the truck will be used as the container for packages
from package import Package


class Truck:
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.container = []  # list of packages
        self.address_list = []
        self.route = []
        self.speed = 18
        self.miles_travelled = 0
        self.capacity = 16
        self.status = "AT_HUB"
        self.start_time = "8:00 AM"
        self.end_time = "8:00 AM"
        self.is_truck_optimized = False

    def add_package(self, package):
        self.container.append(package)
        self.__add_to_address_list(package)
        

    def remove_package(self, package):
        self.container.remove(package)

    def add_miles(self, miles_travelled):
        self.miles_travelled += miles_travelled

    def set_status(self, status):
        self.status = status

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_end_time(self, end_time):
        self.end_time = end_time

    def set_route(self, route):
        self.route = route
    
    def __add_to_address_list(self, package):
        self.address_list.append(package.address)
    

    def optimize(self):
        if (len(self.address_list) == 0 and len(self.route) > 0):
            self.is_truck_optimized = True
            return self.is_truck_optimized
        else:
            self.is_optimized = False
            return self.is_truck_optimized
    
    def load_truck(self, package_list, loaded_package_list=[]):
        loaded_packages = loaded_package_list
        package = Package()

    # create a list of all addresses
    # determine which truck is passed

        if self.truck_id == 1:
            for i in range(1, package_list.item_counter + 1):
                package = package_list.search_by_id(f"{i}")
                if package in loaded_packages:
                    pass
                else:
                    if len(self.container) < 16:
                        # conditions to load into truck 1
                        if (package.delivery_deadline == "9:00 AM"):
                            loaded_packages.append(package)
                            package.status = "LOADED ON TRUCK 1"
                            self.add_package(package)
                            

                        if (package.delivery_deadline == "10:30 AM" and package.notes != "" and package.notes != "Wrong Address listed" and package.notes != "Delayed on flight---will not arrive to depot until 9:05 am"):
                            loaded_packages.append(package)
                            package.status = "LOADED ON TRUCK 1"
                            self.add_package(package)

                        if (package.delivery_deadline == "10:30 AM" and package.notes == ""):
                            loaded_packages.append(package)
                            package.status = "LOADED ON TRUCK 1"
                            self.add_package(package)

                        if (len(self.container) < 16 and package.delivery_deadline == "EOD" and package.notes == ""):
                            loaded_packages.append(package)
                            package.status = "LOADED ON TRUCK 1"
                            self.add_package(package)

        if self.truck_id == 2:
            for i in range(1, package_list.item_counter + 1):
                package = Package()
                package = package_list.search_by_id(f"{i}")
                if package in loaded_packages:
                    pass
                else:
                    if len(self.container) < 16:
                        # conditions to load into truck 2
                        if (package.delivery_deadline == "10:30 AM" and package.notes == "Delayed on flight---will not arrive to depot until 9:05 am"):
                            loaded_packages.append(package)
                            package.status = "LOADED ON TRUCK 2"
                            self.add_package(package)

                        if (package.delivery_deadline == "EOD" and package.notes == "Delayed on flight---will not arrive to depot until 9:05 am"):
                            loaded_packages.append(package)
                            package.status = "LOADED ON TRUCK 2"
                            self.add_package(package)

                        if (package.delivery_deadline == "EOD" and package.notes == "Wrong address listed"):
                            loaded_packages.append(package)
                            package.status = "LOADED ON TRUCK 2"
                            self.add_package(package)

                        if (package.delivery_deadline == "EOD" and package.notes == "Can only be on truck 2"):
                            loaded_packages.append(package)
                            package.status = "LOADED ON TRUCK 2"
                            self.add_package(package)

                        if (len(self.container) < 16 and package.delivery_deadline == "EOD" and package.notes == ""):
                            loaded_packages.append(package)
                            package.status = "LOADED ON TRUCK 2"
                            self.add_package(package)

        if self.truck_id == 3:
            for i in range(1, package_list.item_counter + 1):
                package = Package()
                package = package_list.search_by_id(f"{i}")
                if package in loaded_packages:
                    pass
                else:
                    if len(self.container) < 16:
                        if (len(self.container) < 16):
                            loaded_packages.append(package)
                            package.status = "LOADED ON TRUCK 3"
                            self.add_package(package)

        # checker
        for package in self.container:
            print(package.id, package.address,
                  package.delivery_deadline, "---", package.notes, "---", package.status, "---", )

        return loaded_packages
