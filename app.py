from turtle import distance
from HashMap import HashMap
from Graph import Graph
from package import Package
import csv

# create a hashMap of packages
package_list = HashMap(64)

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
            current_package.status = ""

            # add the package object in the list
            package_list.insertById(
                current_package.id, current_package)


# call the loadPackageData to store the csv data into the declared hashmap
loadPackageData("wgups_package_file.csv")

# tests to see if hashmap works
# package_1 = package_list.searchById("10")
# package_2 = package_list.searchById("11")
# package_3 = package_list.searchById("20")
# print(package_1)
# print(package_2)
# print(package_3)
# print(package_1.address)
# print(package_3.address)
# print(package_list.hash_table)
# package_list.printAllItems()
# for i in range(package_list.size):
#     print(package_list.hash_table[i])


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

    # for row in rows:
    #     print(row, "\n")

    # print(rows)

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
# distanceGraph.getGraph()
#distanceGraph.getEdgeWeights('1330 2100 S\n(84106)')
distanceGraph.printEdgeWeights()
