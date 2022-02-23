# -- INFO ---------------
# First Name: Joshua
# Last Name: Corpuz
# Student id#: 001196484
# -- INFO ---------------

from pickle import TRUE
from package import Package
from truck import Truck
from graph import Graph


# the loading process is abstracted as its own class
class LoadingProcess():
    def __init__(self, trucks=[]):
        self.trucks = []
        for truck in trucks:
            self.trucks.append(truck)

    # non-heuristic algorithm to load each package in a truck depending on their notes, delivery deadlines and other package dependencies
    def load_trucks(self, package_list):
        loaded_packages = []
        package = Package()
        is_package_loaded = False

        for i in range(1, package_list.item_counter + 1):
            package = package_list.search(f"{i}")
            is_package_loaded = False

            if package in loaded_packages:
                pass
            else:
                while is_package_loaded == False:

                    # truck_1: (packages with 9:00 AM or 10:30 AM deadline) AND no notes
                    if ((package.delivery_deadline == "9:00 AM" or package.delivery_deadline == "10:30 AM") and package.notes == "" and len(self.trucks[0].container) < 16):
                        loaded_packages.append(package)
                        package.status = "AT HUB"
                        self.trucks[0].add_package(package)
                        is_package_loaded = True

                    # truck_1 which will exclude those with notes: can only be truck 2, wrong address listed, delayed, -- This will invariably allow those with package_dependencies
                    if (package.notes != "" and package.notes != "Wrong address listed" and package.notes != "Delayed on flight---will not arrive to depot until 9:05 am" and package.notes != "Can only be on truck 2" and len(self.trucks[0].container) < 16):
                        loaded_packages.append(package)
                        package.status = "AT HUB"
                        self.trucks[0].add_package(package)
                        is_package_loaded = True

                    # truck2: if notes say: "wrong address listed" or "Can only be on truck 2"
                    if (package.notes == "Wrong address listed" or package.notes == "Can only be on truck 2" and len(self.trucks[1].container) < 16):
                        loaded_packages.append(package)
                        package.status = "AT HUB"
                        self.trucks[1].add_package(package)
                        is_package_loaded = True

                    #truck2: (deadine is 1030 or EOD) and Delayed
                    elif ((package.delivery_deadline == "10:30 AM" or package.delivery_deadline == "EOD") and package.notes == "Delayed on flight---will not arrive to depot until 9:05 am" and len(self.trucks[1].container) < 16):
                        loaded_packages.append(package)
                        package.status = "AT HUB"
                        self.trucks[1].add_package(package)
                        is_package_loaded = True

                    # packages without deadline and no notes and will be placed to the first truck with less than 16 packages
                    if (len(self.trucks[2].container) < 16 and package.delivery_deadline == "EOD" and package.notes == "" and package not in loaded_packages):
                        loaded_packages.append(package)
                        package.status = "AT HUB"
                        self.trucks[2].add_package(package)
                        is_package_loaded = True

                    elif (len(self.trucks[0].container) < 16 and package.delivery_deadline == "EOD" and package.notes == "" and package not in loaded_packages):
                        loaded_packages.append(package)
                        package.status = "AT HUB"
                        self.trucks[0].add_package(package)
                        is_package_loaded = True

                    elif (len(self.trucks[1].container) < 16 and package.delivery_deadline == "EOD" and package.notes == "" and package not in loaded_packages):
                        loaded_packages.append(package)
                        package.status = "AT HUB"
                        self.trucks[1].add_package(package)
                        is_package_loaded = True

        # Checkers used for reviewing data
        print("Truck #1 Packages:")
        for package in self.trucks[0].container:
            print(package.id, package.address,
                  package.delivery_deadline, "---", package.notes)
        print('\n')

        print("Truck #2 Packages:")
        for package in self.trucks[1].container:
            print(package.id, package.address,
                  package.delivery_deadline, "---", package.notes)
        print('\n')

        print("Truck #3 Packages:")
        for package in self.trucks[2].container:
            print(package.id, package.address,
                  package.delivery_deadline, "---", package.notes)
        print('\n')

        return self.trucks

    # Nearest neighbor algorithm used to sort the truck's packages into a route
    # uses the nearest neighbor algorithm to create an optimal route for each truck
    # O(n^2)
    def nearest_neighbor(self, truck, distance_graph):
        min_distance = 99999.99
        nearest_neighbor = []
        vertex_a = "HUB"
        address_list_temp = []
        adjacency_list = distance_graph.get_edge_weights(vertex_a)

        # always clear the contents of the route so it can be run again without duplicating the HUBs
        truck.route.clear()

        while (len(truck.address_list) > 0):
            for location in adjacency_list:
                if location[0] not in truck.address_list:
                    pass
                elif location[0] == vertex_a:
                    # removes the found nearest_neighbor from address_list
                    truck.address_list.remove(location[0])
                    # adds the found nearest_neighbor to temp_address_list, to reset the truck's address_list when the algorithm is over
                    address_list_temp.append(location[0])
                    pass

                else:
                    distance = float(location[1])
                    if (distance < min_distance) and distance != 0:
                        min_distance = distance
                        nearest_neighbor = location

            # removes the found nearest_neighbor from address_list
            truck.address_list.remove(nearest_neighbor[0])
            # adds the found nearest_neighbor to temp_address_list, to reset the truck's address_list when the algorithm is over
            address_list_temp.append(nearest_neighbor[0])
            # adds the nearest_neighbor and it's distance from vertex_a to the route
            truck.route.append([nearest_neighbor[1], nearest_neighbor[0]])

            # sets vertex_a to the current nearest_neighbor
            vertex_a = nearest_neighbor[0]
            min_distance = 99999.99  # resets min_distance to an absurdly high number
            # resets the adjacency list using the new vertex_a
            adjacency_list = distance_graph.get_edge_weights(vertex_a)

        # once the loop is exited
        # inserts the HUB as the first location
        truck.route.insert(0, ["0", "HUB"])
        # retrieves the distance from the last vertex_a to HUB
        distance_to_hub = distance_graph.get_edge_weight(vertex_a, "HUB")
        # inserts the distance from the last vertex_a to HUB into the route
        truck.route.append(distance_to_hub)

        # resets the contents of the address_list so that the method can be run again
        truck.address_list = address_list_temp
