from pickle import TRUE
from package import Package
from truck import Truck
from graph import Graph


class LoadingProcess():
    def __init__(self, trucks=[]):
        self.trucks = []
        for truck in trucks:
            self.trucks.append(truck)

    def load_trucks(self, package_list):
        loaded_packages = []
        package = Package()
        is_package_loaded = False

        for i in range(1, package_list.item_counter + 1):
            package = package_list.search_by_id(f"{i}")
            is_package_loaded = False

            if package in loaded_packages:
                pass
            else:
                while is_package_loaded == False:

                    # truck_1: (packages with 9:00 AM or 10:30 AM deadline) AND no notes
                    if ((package.delivery_deadline == "9:00 AM" or package.delivery_deadline == "10:30 AM") and package.notes == "" and len(self.trucks[0].container) < 16):
                        loaded_packages.append(package)
                        package.status = "LOADED ON TRUCK 1"
                        self.trucks[0].add_package(package)
                        is_package_loaded = True

                    # truck_1 which will exclude those with notes: can only be truck 2, wrong address listed, delayed, -- This will invariably allow those with package_dependencies
                    if (package.notes != "" and package.notes != "Wrong address listed" and package.notes != "Delayed on flight---will not arrive to depot until 9:05 am" and package.notes != "Can only be on truck 2" and len(self.trucks[0].container) < 16):
                        loaded_packages.append(package)
                        package.status = "LOADED ON TRUCK 1"
                        self.trucks[0].add_package(package)
                        is_package_loaded = True

                    # truck2: if notes say: "wrong address listed" or "Can only be on truck 2"
                    if (package.notes == "Wrong address listed" or package.notes == "Can only be on truck 2" and len(self.trucks[1].container) < 16):
                        loaded_packages.append(package)
                        package.status = "LOADED ON TRUCK 2"
                        self.trucks[1].add_package(package)
                        is_package_loaded = True

                    #truck2: (deadine is 1030 or EOD) and Delayed
                    elif ((package.delivery_deadline == "10:30 AM" or package.delivery_deadline == "EOD") and package.notes == "Delayed on flight---will not arrive to depot until 9:05 am" and len(self.trucks[1].container) < 16):
                        loaded_packages.append(package)
                        package.status = "LOADED ON TRUCK 2"
                        self.trucks[1].add_package(package)
                        is_package_loaded = True

                    # packages without deadline and no notes and will be placed to the first truck with less than 16 packages
                    if (len(self.trucks[2].container) < 16 and package.delivery_deadline == "EOD" and package.notes == "" and package not in loaded_packages):
                        loaded_packages.append(package)
                        package.status = "LOADED ON TRUCK 3"
                        self.trucks[2].add_package(package)
                        is_package_loaded = True

                    elif (len(self.trucks[0].container) < 16 and package.delivery_deadline == "EOD" and package.notes == "" and package not in loaded_packages):
                        loaded_packages.append(package)
                        package.status = "LOADED ON TRUCK 1"
                        self.trucks[0].add_package(package)
                        is_package_loaded = True

                    elif (len(self.trucks[1].container) < 16 and package.delivery_deadline == "EOD" and package.notes == "" and package not in loaded_packages):
                        loaded_packages.append(package)
                        package.status = "LOADED ON TRUCK 2"
                        self.trucks[1].add_package(package)
                        is_package_loaded = True

        # print(truck.container)
        # print(len(truck.container))
        # print(truck.container)

        # checker
        # for truck in self.trucks:
        #     for package in truck.container:
        #         print(package.id, package.address,
        #               package.delivery_deadline, "---", package.notes, "---", package.status, "---", )

        print("Truck #1")
        for package in self.trucks[0].container:
            print(package.id, package.address,
                  package.delivery_deadline, "---", package.notes, "---", package.status, "---", )

        print("Truck #2")
        for package in self.trucks[1].container:
            print(package.id, package.address,
                  package.delivery_deadline, "---", package.notes, "---", package.status, "---", )

        print("Truck #3")
        for package in self.trucks[2].container:
            print(package.id, package.address,
                  package.delivery_deadline, "---", package.notes, "---", package.status, "---", )

        return self.trucks

    def greedy_algorithm(self, truck, distance_graph):
        min_distance = float('inf')
        nearest_neighbor = "HUB"
        truck.route.append("HUB")
        vertex_a = "HUB"
        adjacency_list = distance_graph.get_edge_weights(vertex_a)

        for location in adjacency_list:
            if location[0] not in truck.container:
                pass
            else:
                if location[1] < min_distance and location[1] != 0:
                    min_distance = location[1]
                    nearest_neighbor = location[0]

        truck.route.append(nearest_neighbor)
        vertex_a = nearest_neighbor

        print(nearest_neighbor)
