from hashMap import hashMap
from package import package
import csv


# create a function to load package data into a hash table
def loadPackageData(fileName):
    # create a hashMap of packages
    package_list = hashMap(64)

    # read data from wgups_package_file.csv
    with open(fileName) as file:
        reader = csv.reader(file)

        package_data = list(reader)

        # create a package object using each row of from package_list
        for i in range(1, len(package_data)):
            current_package = package()
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
            package_list.addKeyValuePair(
                current_package.id, current_package)

    return package_list


package_list = loadPackageData("wgups_package_file.csv")

# test to see if hashmap works
found_package = package_list.getValue("10")
package_1 = package_list.getValue("11")
package_3 = package_list.getValue("20")

print(found_package)
print(package_1)
print(package_3)

# package_2 = package_list.getValue("10")


print(package_1.address)
print(package_3.address)

# package_list.printAll()
# package_list.printList()


# package_list.deleteKeyValuePair("10")

# package_list.printAll()
# package_list.printList()
