from Package import Package


def loadTruck(allAddresses, hashTable, truck, usedAddresses = []):
    unassignedAddresses = allAddresses
    assignedAddresses = usedAddresses

    # create a list of all addresses
    # determine which truck is passed

    if truck.truckId == 1:
        for address in unassignedAddresses:
            if address in assignedAddresses:
                pass
            else:
                packageToCheck = Package()
                packageToCheck = hashTable.search(address)

                # conditions to load into truck 1
                if (packageToCheck.delivery_deadline == "9:00 AM"):
                    assignedAddresses.append(address)
                    truck.addPackage(packageToCheck)

                if (packageToCheck.delivery_deadline == "10:30 AM" and packageToCheck.notes != "" and packageToCheck.notes != "Wrong Address listed" and packageToCheck.notes != "Delayed on flight---will not arrive to depot until 9:05 am"):
                    assignedAddresses.append(address)
                    truck.addPackage(packageToCheck)

                if (packageToCheck.delivery_deadline == "10:30 AM" and packageToCheck.notes == ""):
                    assignedAddresses.append(address)
                    truck.addPackage(packageToCheck)

                if (len(truck.container) < 16 and packageToCheck.delivery_deadline == "EOD" and packageToCheck.notes == ""):

                    assignedAddresses.append(address)
                    truck.addPackage(packageToCheck)

    if truck.truckId == 2:
        for address in unassignedAddresses:
            if address in assignedAddresses:
                pass
            else:
                packageToCheck = Package()
                packageToCheck = hashTable.search(address)

                # conditions to load into truck 2
                if (packageToCheck.delivery_deadline == "10:30 AM" and packageToCheck.notes == "Delayed on flight---will not arrive to depot until 9:05 am"):
                    assignedAddresses.append(address)
                    truck.addPackage(packageToCheck)

                if (packageToCheck.delivery_deadline == "EOD" and packageToCheck.notes == "Delayed on flight---will not arrive to depot until 9:05 am"):
                    assignedAddresses.append(address)
                    truck.addPackage(packageToCheck)

                if (packageToCheck.delivery_deadline == "EOD" and packageToCheck.notes == "Wrong address listed"):
                    assignedAddresses.append(address)
                    truck.addPackage(packageToCheck)

                if (packageToCheck.delivery_deadline == "EOD" and packageToCheck.notes == "Can only be on truck 2"):
                    assignedAddresses.append(address)
                    truck.addPackage(packageToCheck)

                if (len(truck.container) < 16 and packageToCheck.delivery_deadline == "EOD" and packageToCheck.notes == ""):
                    assignedAddresses.append(address)
                    truck.addPackage(packageToCheck)
    
    if truck.truckId == 3:
        for address in unassignedAddresses:
            if address in assignedAddresses:
                pass
            else:
                packageToCheck = Package()
                packageToCheck = hashTable.search(address)

                if (len(truck.container) < 16):
                    assignedAddresses.append(address)
                    truck.addPackage(packageToCheck)


    # print(truck.container)
    # print(len(truck.container))
    # print(truck.container)

    for package in truck.container:
        print(package.address)

    return assignedAddresses

    # if truck.id == 1
    # load packages that are to be delivered at 9:00
    # load packages that are 10:30 deadline but with other package dependencies, make sure to exclude those with notes other than package dependencies
    # load packages that are 10:30 deadline without notes
    # load packages that are EOD deadline without notes until packages reach 16
    # must be < 16 packages

    # if truck.id == 2
    # load package that is 10:30 deadline but has a 9:05 hub arrival in the special notes
    # load packages that has a EOD deadline AND has 9:05 hub arrival in the special notes
    # load packages that has an EOD deadline and a wrong address
    # load packages that are notes to be on truck #2
    # load packages that are EOD deadline without notes until packages reach 16

    # if alladdress
    # if truck.id == 3
    # load all that is left in the allAddressList

    # must have a way to track unloaded packages, update the list being passed in the parameter before it is called again

    # priority list:
    # truck 1
    # container can not be > 16 packages
    # 1. delivery deadline: 9:00
    # 2. delivery deadline: 10:30
    # 3. Must not have any notes

    # truck 2
    # container can not be > 16 packages
    # 1. Must be on truck 2
    # 2. Must be [13, 14, 15, 16, 19, 20]

    #truck #
    # container can not be > 16 packages
    # 1. Can not load leave until 9:05AM
    # 2.

    # Function to load the trucks with the "correct" packages and get the best route to take
    # "Correct" packages were first sorted by hand, and I determined what the priorities would be.
    # Priority 1: Packages that have to be delivered by 9:00 -- truck 1
    # Priority 2: Packages that have to be delivered by 10:30 and are delayed_on_flight or have deliver_with special notes
    # Priority 3: Packages that have to be delivered by 10:30 with no special notes
    # Priority 4: Packages that have to be delivered by EOD (17:00) and delayed_on_flight, truck2_only, or wrong_address
    # Priority 5: Packages that are EOD with no special notes, but cannot exceed the load of the trucks (16 packages)
    # After all trucks are loaded, the greedy_path_algorithm changes the route to make it more efficient
    # O(N^2)

    # TODO
    # fix the checker to see if the package has been assigned already. It needs to keep track of all the assigned addresses already
    # BIG DESIGN FLAW!!! You should refactor your program:
        #1. You should not use address as the key, instead use packageId as the key for the hash table
        #2. refactor code to use the same naming convention, use underscores
        #3. No need to create the an address list checker.
