# -- INFO ---------------
# First Name: Joshua
# Last Name: Corpuz
# Student id#: 001196484
# -- INFO ---------------


from collections import UserList
import csv
import datetime
from unittest import skip
from hash_map import HashMap
from graph import Graph
from loading_process import LoadingProcess
from package import Package
from truck import Truck


def exit_program():
    print("System exited, goodbye!")
    SystemExit


def wgups_routing_program():
    packages_delivered = False

    print("""
    *****************************************
    * Welcome to the WGUPS Routing Program! *
    *****************************************
    """)
    print("Press: 1 - to enter program")
    print("Press: 0 - to exit program")
    user_input = input("Input: ")

    # create a hashMap of packages
    package_list = HashMap(64)

    # create a list of all the addresses
    address_list = []

    # create a function to load package data into a hash table
    def load_package_data(file_name):

        # read data from wgups_package_file.csv
        with open(file_name) as file:
            reader = csv.reader(file)
            package_data = list(reader)

            # create a package object using each row of from package_list
            # skipped the first row of headers
            for i in range(1, len(package_data)):
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
                    current_package.id, current_package)

                # store all the addresses in a list
                address_list.append(current_package.address)

    # create a method to load data from wgups_distance_table.csv into graph
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
        for i in range(len(distance_graph.vertex_list)):
            for j in range(len(distance_graph.vertex_list)):
                distance_graph.add_edge_weights(
                    distance_graph.vertex_list[i], distance_graph.vertex_list[j], rows[i][j+1])

    # call the load_package_data to store the csv data into the declared hashmap
    load_package_data("wgups_package_file.csv")

    # Create a Graph object
    distance_graph = Graph()

    # load distance data from csv
    file_name = "wgups_distance_table.csv"

    # call function
    load_distance_data(file_name)

    # create the three trucks
    truck1 = Truck(1)
    truck2 = Truck(2)
    truck3 = Truck(3)

    # store trucks in a list
    trucks = [truck1, truck2, truck3]

    print("""
    ************************************************************
    * Package data loaded!                                     *
    * Distance data loaded!                                    *
    *                                                          *
    *  - The time is 8:00 AM. What you would you like to do? - *
    * Would you like to view the details of all the packages?  *
    ************************************************************
    """)
    print("Press: 1 - to skip and continue with the program")
    print("Press: 2 - to view package details")
    print("Press: 0 - to exit program")
    user_input = input("Input: ")

    while user_input == '2':
        print("""
        *************************************************************************
        *                                                                       *
        * Reminder: All packages are either at the hub or on its way to the hub *
        *                                                                       *
        *************************************************************************
        """)
        user_input_2 = input(
            "Enter the package id # for the package that you would like to view: ")

        try:
            package_result = package_list.search(user_input_2)

        except:
            print("""
            PACKAGE WITH THE PROVIDED ID DOES NOT EXIST!!
            """)
        else:
            print(f"""Package Details: 
            {package_result}
            """)

        print("""
        ****************************************************
        *                                                   *
        * Would you like to view another package's details? *
        *                                                   *
        ****************************************************
        """)
        print("Press: 1 - to continue with the program")
        print("Press: 2 - to view another package's details")
        print("Press: 0 - to exit program")
        user_input = input("Input: ")

    if user_input == "1":
        print('\n')
        print("""
        --- Assign packages to trucks? ---
        """)
        print("Press: 1 - to assign packages to trucks")
        print("Press: 0 - to exit program")
        user_input = input("Input: ")

        if user_input == "1":

            # pass the list of trucks as a parameter to create a loading process object
            loading_process = LoadingProcess(trucks)
            print('\n')
            # load the trucks with the passed package_list
            trucks = loading_process.load_trucks(package_list)

            # Message to note end of process
            print("""
            --- Packages have been assigned to trucks! ---
            """)

            # OPTIMIZE? y/n
            print('\n')
            print("""
            --- Would you like to optimize each of the truck\'s routes? ---
            """)
            print("Press: 1 to optimize truck routes")
            print("Press: 0 to exit program")
            user_input = input("Input: ")

            if user_input == '1':
                print('\n')
                # optimize truck1 and truck3's routes
                loading_process.nearest_neighbor(
                    truck=truck1, distance_graph=distance_graph)
                loading_process.nearest_neighbor(
                    truck=truck2, distance_graph=distance_graph)
                loading_process.nearest_neighbor(
                    truck=truck3, distance_graph=distance_graph)

                print('Truck routes optimized!\n')

                # DELIVER PACKAGES PROMPT
                print("""
                --- Would you like to deliver packges? ---
                """)
                print("Press: 1 to deliver packages")
                print("Press: 0 to exit program")
                user_input = input("Input: ")

                if user_input == '1':

                    print('\n')
                    truck1.deliver_packages()
                    print('\n')
                    truck3.start_time = truck1.end_time
                    truck3.deliver_packages()

                    print('\n')
                    print("""
                    --- Corrected address for package 9 was received at 10:20 AM! ---

                    --- Would you like to correct the address for package 9? ---
                    """)

                    print("Press: 1 - to correct address for package 9")
                    print("Press: 0 - to exit program")
                    user_input = input("Input: ")

                    if user_input == '1':
                        print('\n')
                        print('Correcting the address for package_9...\n')

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
                        print("""
                        --- Package 9 address corrected! ---
                        """)

                        # OPTIMIZE Route for Truck2 Y/N?
                        print("""
                        --- Would you like to optimize route for truck 2? ---
                        """)
                        print("Press: 1 to optimize route for truck 2")
                        print("Press: 0 to exit program")
                        user_input = input("Input: ")

                        if user_input == '1':

                            # re-optimize truck2's route
                            loading_process.nearest_neighbor(
                                truck=truck2, distance_graph=distance_graph)
                            # print truck 2's contents

                            print("""
                            --- Would you like to view truck 2's package details? ---
                            """)
                            print("Press: 1 - to view packages for truck 2")
                            print("Press: 0 - to skip")
                            user_input = input("Input: ")

                            # Skipped if the user enters 0
                            if user_input == '1':
                                truck2.print_container_contents()
                                print('\n')
                            else:
                                print("")

                            # DELIVER Truck 2 packages y/n?
                            print("""
                            --- Deliver Truck 2's packages? ---
                            """)
                            print("Press: 1 - Deliver Truck 2's packages?")
                            print("Press: 0 - to exit program")
                            user_input = input("Input: ")

                            if user_input == '1':
                                print('\n')
                                truck2.start_time = datetime.datetime(
                                    2022, 2, 21, hour=9, minute=5, second=0)
                                truck2.deliver_packages()

                                print("""
                                *************************************
                                * All packages have been delivered! *
                                *************************************
                                """)
                                packages_delivered = True
                            else:
                                exit_program()
                        else:
                            exit_program()
                    else:
                        exit_program()
                else:
                    exit_program()
            else:
                exit_program()

            # Checker will only run if packages have been delivered.
            if packages_delivered == True:
                # Would you like to look up the status at a specific time?
                print("""
                -- Would you like to look up the system status at a specific time? ---
                """)
                print("Press: 1 - to look up system status at a specific time")
                print("Press: 0 - to exit system status lookup")
                user_input = input("Input: ")

                while user_input == '1':
                    if user_input == '1':
                        print('Please input the time you would like to lookup:')
                        input_hour = int(
                            input('Hour (Enter hour values from 1-24): '))
                        input_minute = int(
                            input('Minutes (Enter values from 00-60): '))
                        print('\n')
                        print('Status of packages in trucks at:',
                              input_hour, ':', input_minute)
                        datetime_input = datetime.datetime(
                            2022, 2, 21, hour=input_hour, minute=input_minute, second=00)

                        print('\n')
                        print('Truck 1 Status:')
                        truck1.get_all_packages_status_at_time(datetime_input)
                        print('\n')
                        print('Truck 2 Status:')
                        truck2.get_all_packages_status_at_time(datetime_input)
                        print('\n')
                        print('Truck 3 Status:')
                        truck3.get_all_packages_status_at_time(datetime_input)

                        print(
                            "Would you like to look up the system status at another specific time?")
                        print("Press: 1 to look up another time")
                        print("Press: 0 to exit lookup function")
                        user_input = input("Input: ")
                    else:
                        print("System lookup function exited!")
                        continue

                # Would you like to print the summary for specific time requirements
                print("""
                --- Would you like to print the summary for specific time requirements:
                    Status for a time between 8:35 a.m. and 9:25 a.m
                    Status for a time between 9:35 a.m. and 10:25 a.m
                    Status for a time between 12:03 p.m. and 1:12 p.m
                """)
                print("Press: 1 for Yes")
                print("Press: 0 to exit program")
                user_input = input("Input: ")

                if user_input == '1':
                    # SUMMARY FOR SPECIFIC PROJECT TIME REQUIREMENTS
                    print('\n')
                    print('Status of packages in trucks at: 09:10:00')
                    datetime_input = datetime.datetime(
                        2022, 2, 21, hour=9, minute=10, second=00)

                    print('\n')
                    print('Truck 1 Status:')
                    truck1.get_all_packages_status_at_time(datetime_input)
                    print('\n')
                    print('Truck 2 Status:')
                    truck2.get_all_packages_status_at_time(datetime_input)
                    print('\n')
                    print('Truck 3 Status:')
                    truck3.get_all_packages_status_at_time(datetime_input)

                    print('\n')
                    print('Status of packages in trucks at: 10:15:00')
                    datetime_input = datetime.datetime(
                        2022, 2, 21, hour=10, minute=15, second=00)

                    print('\n')
                    print('Truck 1 Status:')
                    truck1.get_all_packages_status_at_time(datetime_input)
                    print('\n')
                    print('Truck 2 Status:')
                    truck2.get_all_packages_status_at_time(datetime_input)
                    print('\n')
                    print('Truck 3 Status:')
                    truck3.get_all_packages_status_at_time(datetime_input)

                    print('\n')
                    print('Status of packages in trucks at: 12:30:00')
                    datetime_input = datetime.datetime(
                        2022, 2, 21, hour=12, minute=30, second=00)

                    print('\n')
                    print('Truck 1 Status:')
                    truck1.get_all_packages_status_at_time(datetime_input)
                    print('\n')
                    print('Truck 2 Status:')
                    truck2.get_all_packages_status_at_time(datetime_input)
                    print('\n')
                    print('Truck 3 Status:')
                    truck3.get_all_packages_status_at_time(datetime_input)

                else:
                    print("Program time lookup exited")
                    SystemExit

                print('\n')

                # Would you like to look to print the system summary?
                print("""
                *******************************************************
                * Would you like to look to print the system summary? *
                *******************************************************
                """)
                print("Press: 1 to print system summary")
                print("Press: 0 to exit program")
                user_input = input("Input: ")

                if user_input == '1':
                    print('\n')

                    # calcualtes the total miles traveled for each truck.
                    truck1.calculate_miles_traveled()
                    truck2.calculate_miles_traveled()
                    truck3.calculate_miles_traveled()

                    print("""
                    *******************
                    * PROGRAM SUMMARY *
                    *******************
                    """)
                    print('Truck 1 Summary:')
                    print('Start:', truck1.start_time)
                    print('End:', truck1.end_time)
                    print("Truck 1 travelled:", truck1.miles_traveled, "miles")

                    print('\n')
                    print('Truck 2 Summary:')
                    print('Start:', truck2.start_time)
                    print('End:', truck2.end_time)
                    print("Truck 3 travelled:", truck3.miles_traveled, "miles")

                    print('\n')
                    print('Truck 3 Summary:')
                    print('Start:', truck3.start_time)
                    print('End:', truck3.end_time)
                    print("Truck 2 travelled:", truck2.miles_traveled, "miles")

                    # aggregates the total miles traveled by all three trucks
                    total_miles_traveled = truck1.miles_traveled + \
                        truck2.miles_traveled + truck3.miles_traveled
                    summary_message = '''\
                    *********************************
                    * TOTAL MILES TRAVELED: {miles} *
                    *********************************\
                    '''.format(miles=total_miles_traveled)

                    print(summary_message)
                else:
                    exit_program()
            else:
                SystemExit
        else:
            exit_program()

    else:
        exit_program()


if __name__ == "__main__":
    wgups_routing_program()
