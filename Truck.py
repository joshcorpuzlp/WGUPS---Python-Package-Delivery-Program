# the truck will be used as the container for packages
from package import Package
import datetime


class Truck:
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.container = []  # list of packages
        self.address_list = []
        self.route = []
        self.speed = 18
        self.miles_travelled = 0.0
        self.capacity = 16
        self.status = "AT_HUB"
        self.start_time = datetime.datetime(
            2022, 2, 21, hour=8, minute=0, second=0)
        self.end_time = None
        self.is_truck_optimized = False

    def add_package(self, package):
        self.container.append(package)
        self.__add_to_address_list(package)

    def remove_package(self, package):
        self.container.remove(package)
        self.__remove_from_address_list(package)

    def get_package(self, package_id):
        for package in self.container:
            if package.id == package_id:
                return package

    def add_miles(self, miles_travelled):
        self.miles_travelled += miles_travelled

    def calculate_miles_travelled(self):
        for kvp in self.route:
            self.add_miles(float(kvp[0]))

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

    def __remove_from_address_list(self, package):
        self.address_list.remove(package.address)

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
                  package.delivery_deadline, "---", package.notes, "---", package.status, "---", package.datetime_delivered)

        return loaded_packages

    # marks each package in the truck.container as delivered if the package has the same address as the current location

    def deliver_packages(self):
        route = self.route
        container = self.container

        for location in route:
            for package in container:
                if package.address == location[1]:
                    package.status = "DELIVERED"
                    # calls the method get_miles_travelled_to_location to calculate miles travelled from HUB to provided location address
                    package.miles_travelled = self.get_miles_travelled_to_location(
                        package.address)
                    # converts the miles travelled to the # of hours it takes to get to that location
                    package.time_elapsed = self.convert_distance_to_time(
                        package.address)
                    # creates a timedelta object from the time_elapsed value
                    time_delta = datetime.timedelta(hours=package.time_elapsed)
                    # sets the package delivery time to the truck's start time + time_delta.
                    package.datetime_delivered = self.start_time + time_delta

        # set end time for the truck's delivery
        time_elapsed = self.convert_distance_to_time('HUB')
        total_time_delta = datetime.timedelta(hours=time_elapsed)
        self.end_time = self.start_time + total_time_delta

        for package in container:
            print(package.id, package.address, package.status,
                  package.miles_travelled, package.time_elapsed, package.datetime_delivered)

    # calculate the miles travelled to get to that location
    def get_miles_travelled_to_location(self, address_to_get_to):
        distance_to_location = 0.00
        current_address = 'HUB'

        for location in self.route[1:]:
            edge_weight = float(location[0])
            distance_to_location += edge_weight
            current_address = location[1]
            if current_address == address_to_get_to:
                return distance_to_location
            else:
                continue
        # return distance_to_location

    # calcualtes time_elapsed to get to the given address
    def convert_distance_to_time(self, address_to_get_to):
        miles_travelled = self.get_miles_travelled_to_location(
            address_to_get_to)
        time_elapsed = miles_travelled / 18  # 18 miles per hour

        return time_elapsed

    def get_package_status_at_time(self, datetime_input):
        container = self.container

        for package in container:
            if datetime_input <= package.datetime_delivered:
                if datetime_input > self.start_time:
                    package.status = "EN_ROUTE"
                else:
                    package.status = "AT HUB"
            else:
                package.status = "DELIVERED"

        for package in container:
            print(package.id, package.address, package.status,
                  package.miles_travelled, package.time_elapsed, package.datetime_delivered)
