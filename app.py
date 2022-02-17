from audioop import add
from HashMap import HashMap
from Graph import Graph
from LoadTrucks import loadTruck
from Package import Package
import csv
from Truck import Truck

# create a hashMap of packages
package_list = HashMap(64)

# store all the addresses in a list
addressList = []

# create a function to load package data into a hash table


def loadPackageData(fileName):

    # read data from wgups_package_file.csv
    with open(fileName) as file:
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
            package_list.insert(
                current_package.address, current_package)

            # create a list of all the addresses
            addressList.append(current_package.address)


# call the loadPackageData to store the csv data into the declared hashmap
loadPackageData("wgups_package_file.csv")

# tests to see if hashmap works
package_1 = package_list.search('4300 S 1300 E')

print(package_1)

print(package_1.address)

print(package_list.hash_table)
package_list.printAllItems()
for i in range(package_list.size):
    print(package_list.hash_table[i])


# TODO: Using the Graph class:
# 1. Load the addresses in Column A in the Graph's vertex list
# 2. Load the address_2 it's corresponding distance to address_1 as a 2-item list appended to a list of

distanceGraph = Graph()


def loadDistanceData(fileName):
    rows = []
    with open(fileName) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            rows.append(row)

    # load the addresses to the vertex list
    for row in rows:
        distanceGraph.addVertex(row[0])

    # # load contents for adjacency list
    for i in range(len(distanceGraph.vertex_list_a)):
        for j in range(len(distanceGraph.vertex_list_a)):
            distanceGraph.addEdgeWeights(
                distanceGraph.vertex_list_a[i], distanceGraph.vertex_list_a[j], rows[i][j+1])


fileName = "wgups_distance_table.csv"
loadDistanceData(fileName)
distanceGraph.printEdgeWeights()

truck1 = Truck(1)
truck2 = Truck(2)

loadTruck(addressList, package_list, truck1)
print("\n")
loadTruck(addressList, package_list, truck2)
