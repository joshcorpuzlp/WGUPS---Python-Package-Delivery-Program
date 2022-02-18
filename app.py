from turtle import distance
from hash_map import HashMap
from graph import Graph
from load_trucks import load_truck
from loading_process import LoadingProcess
from package import Package
import csv
from truck import Truck

# create a hashMap of packages
package_list = HashMap(64)

# store all the addresses in a list
address_list = []

# create a function to load package data into a hash table


def load_package_data(file_name):

    # read data from wgups_package_file.csv
    with open(file_name) as file:
        reader = csv.reader(file)
        package_data = list(reader)

        # create a package object using each row of from package_list
        for i in range(1, len(package_data)):  # skipped the first row of headers
            current_package = Package()
            current_package.id = package_data[i][0]
            current_package.address = package_data[i][1]
            current_package.city = package_data[i][2]
            current_package.state = package_data[i][3]
            current_package.zip = package_data[i][4]
            current_package.delivery_deadline = package_data[i][5]
            current_package.mass_kg = package_data[i][6]
            current_package.notes = package_data[i][7]
            current_package.status = "AT_HUB"

            # add the package object in the list
            package_list.insert_by_id(
                current_package.id, current_package)

            # create a list of all the addresses
            address_list.append(current_package.address)


# call the load_package_data to store the csv data into the declared hashmap
load_package_data("wgups_package_file.csv")

# tests to see if hashmap works
package_1 = package_list.search_by_id('1')
package_2 = package_list.search_by_id('2')
package_3 = package_list.search_by_id('3')

print(package_1)
print(package_2)
print(package_3)

print(package_1.address)
print(package_2.address)
print(package_3.address)

# print(package_list.hash_table)

package_list.print_all_items()

for i in range(package_list.size):
    print(package_list.hash_table[i])


# TODO: Using the Graph class:
# 1. Load the addresses in Column A in the Graph's vertex list
# 2. Load the address_2 it's corresponding distance to address_1 as a 2-item list appended to a list of

distanceGraph = Graph()


def load_distance_data(file_name):
    rows = []
    with open(file_name) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            rows.append(row)

    # load the addresses to the vertex list
    for row in rows:
        distanceGraph.add_vertex(row[0])

    # # load contents for adjacency list
    for i in range(len(distanceGraph.vertex_list_a)):
        for j in range(len(distanceGraph.vertex_list_a)):
            distanceGraph.add_edge_weights(
                distanceGraph.vertex_list_a[i], distanceGraph.vertex_list_a[j], rows[i][j+1])


file_name = "wgups_distance_table.csv"
load_distance_data(file_name)
distanceGraph.print_edge_weights()

truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)

trucks = [truck1, truck2, truck3]

loading_process = LoadingProcess(trucks)
trucks = loading_process.load_trucks(package_list)

# result = truck1.load_truck(package_list)
# print("\n")
# result = truck2.load_truck(package_list, loaded_package_list=result)
# print("\n")
# result = truck3.load_truck(package_list, loaded_package_list=result)

# print("\n")
# print(truck1.container[1])

loading_process.greedy_algorithm(truck1, distanceGraph)
