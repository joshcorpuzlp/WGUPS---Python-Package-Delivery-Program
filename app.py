import csv
import datetime
from xmlrpc.client import _datetime_type
from hash_map import HashMap
from graph import Graph
from loading_process import LoadingProcess
from package import Package
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


# TODO: Using the Graph class:
# 1. Load the addresses in Column A in the Graph's vertex list
# 2. Load the address_2 it's corresponding distance to address_1 as a 2-item list appended to a list of

distance_graph = Graph()


def load_distance_data(file_name):
    rows = []
    with open(file_name) as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            rows.append(row)

    # load the addresses to the vertex list
    for row in rows:
        distance_graph.add_vertex(row[0])

    # # load contents for adjacency list
    for i in range(len(distance_graph.vertex_list_a)):
        for j in range(len(distance_graph.vertex_list_a)):
            distance_graph.add_edge_weights(
                distance_graph.vertex_list_a[i], distance_graph.vertex_list_a[j], rows[i][j+1])


# load distance data from csv
file_name = "wgups_distance_table.csv"
load_distance_data(file_name)


# create the three trucks
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)

# store trucks in a list
trucks = [truck1, truck2, truck3]

# pass the list of trucks as a parameter to create a loading process object
loading_process = LoadingProcess(trucks)
# load the trucks with the passed package_list
trucks = loading_process.load_trucks(package_list)

# optimize truck1 and truck3's routes
loading_process.nearest_neighbor(truck=truck1, distance_graph=distance_graph)
loading_process.nearest_neighbor(truck=truck3, distance_graph=distance_graph)


# FIXING THE WRONG ADDRESS for PACKAGE_9 before optimizing truck2
# retrieve package 9 from truck container and save it to a local variable
package_9 = truck2.get_package("9")
# remove package 9 from truck's container and address_list
truck2.remove_package(truck2.get_package('9'))

# update package_9 values
package_9.set_address('410 S State St')
package_9.set_city('Salt Lake City')
package_9.set_zip('84111')

# add package_9 to the container and address_list
truck2.add_package(package_9)

# Optimize truck2's route
loading_process.nearest_neighbor(truck=truck2, distance_graph=distance_graph)
print('\n')

print('Truck 1 summary')
truck1.deliver_packages()
print('Start:', truck1.start_time)
print('End:', truck1.end_time)

print('\n')
print('Truck 3 summary')
truck3.deliver_packages()
print('Start:', truck3.start_time)
print('End:', truck3.end_time)

print('\n')
print('Truck 2 summary')
truck2.start_time = truck1.end_time
truck2.deliver_packages()
print('Start:', truck2.start_time)
print('End:', truck2.end_time)

print('\n')


truck1.calculate_miles_traveled()
truck2.calculate_miles_traveled()
truck3.calculate_miles_traveled()


print("Truck 1 travelled:", truck1.miles_traveled, "miles")
print("Truck 2 travelled:", truck2.miles_traveled, "miles")
print("Truck 3 travelled:", truck3.miles_traveled, "miles")

print("Total miles travelled:", truck1.miles_traveled +
      truck2.miles_traveled + truck3.miles_traveled, "miles")


print('\n')
print('Status of packages in trucks at: 09:10:00')
datetime_input = datetime.datetime(
    2022, 2, 21, hour=9, minute=10, second=00)

print('\n')
print('Truck 1 status')
truck1.get_all_packages_status_at_time(datetime_input)
print('\n')
print('Truck 2 status')
truck2.get_all_packages_status_at_time(datetime_input)
print('\n')
print('Truck 3 status')
truck3.get_all_packages_status_at_time(datetime_input)

print('\n')
print('Status of packages in trucks at: 10:15:00')
datetime_input = datetime.datetime(
    2022, 2, 21, hour=10, minute=15, second=00)

print('\n')
print('Truck 1 status')
truck1.get_all_packages_status_at_time(datetime_input)
print('\n')
print('Truck 2 status')
truck2.get_all_packages_status_at_time(datetime_input)
print('\n')
print('Truck 3 status')
truck3.get_all_packages_status_at_time(datetime_input)

print('\n')
print('Status of packages in trucks at: 12:30:00')
datetime_input = datetime.datetime(
    2022, 2, 21, hour=12, minute=30, second=00)

print('\n')
print('Truck 1 status')
truck1.get_all_packages_status_at_time(datetime_input)
print('\n')
print('Truck 2 status')
truck2.get_all_packages_status_at_time(datetime_input)
print('\n')
print('Truck 3 status')
truck3.get_all_packages_status_at_time(datetime_input)
# print('\n')
# print(truck2.get_miles_travelled_to_location("5383 South 900 East #104"))
# print(truck2.convert_distance_to_time("HUB"))


# print(truck2.convert_distance_to_time("5383 South 900"))
# print(truck3.convert_distance_to_time("HUB"))


# CHECKERS
# result = truck1.load_truck(package_list)
# print("\n")
# result = truck2.load_truck(package_list, loaded_package_list=result)
# print("\n")
# result = truck3.load_truck(package_list, loaded_package_list=result)

# print("\n")
# print(truck1.container[1])

# print('\n')
# print(truck1.container)

# print('\n')
# print(truck1.address_list)

# print('\n')
# print(truck2.container)

# print('\n')
# print(truck2.address_list)
# print('\n')


# print(truck3.container)

# print('\n')
# print(truck3.address_list)
# print('\n')

# Checker
# print(truck2.get_package('9'))
# print('\n')


# tests to see if hashmap works
# package_1 = package_list.search_by_id('1')
# package_2 = package_list.search_by_id('2')
# package_3 = package_list.search_by_id('3')

# print(package_1)
# print(package_2)
# print(package_3)

# print(package_1.address)
# print(package_2.address)
# print(package_3.address)

# # print(package_list.hash_table)
# package_list.print_all_items()

# #prints all the contents of the hash table
# for i in range(package_list.size):
#     print(package_list.hash_table[i])

# #prints all the edge_weights
# distanceGraph.print_edge_weights()


# #checkers to see miles travelled before calculating miles travelled
# print(truck1.miles_travelled)
# print(truck2.miles_travelled)
# print(truck3.miles_travelled)
