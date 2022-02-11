from hashMap import HashMap
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
            current_package.status = ""

            # add the package object in the list
            package_list.insert(
                current_package.id, current_package)


# call the loadPackageData to store the csv data into the declared hashmap
loadPackageData("wgups_package_file.csv")

# test to see if hashmap works
package_1 = package_list.search("10")
package_2 = package_list.search("11")
package_3 = package_list.search("20")

print(package_1)
print(package_2)
print(package_3)

print(package_1.address)
print(package_3.address)

# for i in range(len(package_list.hash_table)):
#     print(package_list.searchByIndex(i))

print(package_list.hash_table)
