# Truck class used to represent a package and store its details
# Truck class also contain methods that allow for its properties to be accessed.

from package import Package
import datetime


class Truck:
    def __init__(self, truck_id):
        self.truck_id = truck_id
        self.container = []  # list of packages
        self.address_list = []
        self.route = []
        self.speed = 18
        self.miles_traveled = 0.0
        self.capacity = 16
        self.status = "AT_HUB"
        self.start_time = datetime.datetime(
            2022, 2, 21, hour=8, minute=0, second=0)
        self.end_time = None

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

    def add_miles(self, miles_traveled):
        self.miles_traveled += miles_traveled

    def calculate_miles_traveled(self):
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

    # Function delivers packages by marking each package in the truck.container as delivered if the package has the same address as the current location
    # O(n^2)
    def deliver_packages(self):
        route = self.route
        container = self.container

        for location in route:
            for package in container:
                if package.address == location[1]:
                    package.status = "DELIVERED"
                    # calls the method get_miles_travelled_to_location to calculate miles travelled from HUB to provided location address
                    package.miles_traveled = self.get_miles_traveled_to_location(
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
            print(
                f'Package Id: {package.id}, Miles Traveled: {package.miles_traveled:.2f}, Date and Time Delivered: {package.datetime_delivered}')

    # Function calculate the miles travelled to get to that location
    # O(n)
    def get_miles_traveled_to_location(self, address_to_get_to):
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

    # Function calcualtes time_elapsed to get to the given address
    def convert_distance_to_time(self, address_to_get_to):
        miles_traveled = self.get_miles_traveled_to_location(
            address_to_get_to)
        time_elapsed = miles_traveled / 18  # 18 miles per hour

        return time_elapsed

    
    # Function that returns all the package and details at the given time
    # O(n)
    def get_all_packages_status_at_time(self, datetime_input):
        container = self.container

        for package in container:
            if datetime_input <= self.start_time or None:
                package.status = "AT HUB"
                show_datetime_as = datetime.datetime(
                    2022, 2, 21, hour=0, minute=0, second=0)
            if datetime_input > self.start_time and datetime_input < package.datetime_delivered:
                package.status = "EN ROUTE"
            if datetime_input >= package.datetime_delivered:
                package.status = "DELIVERED"

        for package in container:
            if datetime_input <= self.start_time or None:
                print(
                    f'Package Id: {package.id}, Status: {package.status}, Miles Traveled: {package.miles_traveled:.2f}, Scheduled Delivery Date and Time: {show_datetime_as}')
            else:
                print(
                    f'Package Id: {package.id}, Status: {package.status}, Miles Traveled: {package.miles_traveled:.2f}, Scheduled Delivery Date and Time: {package.datetime_delivered}')

    # Function prints all the contents of the truck's container
    # O(n)
    def print_container_contents(self):
        print(f"Truck #{self.truck_id} Packages")
        for package in self.container:
            print(package.id, package.address,
                  package.delivery_deadline, "---", package.notes)
