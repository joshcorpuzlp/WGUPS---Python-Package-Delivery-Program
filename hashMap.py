# might be a good idea to try and use a different hash_map
# Hash_map will be used for storing all the package objects

class HashMap():
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
        self.item_counter = 0

    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # The hash key is calculated by the sum of the char values of the key % the size of the hashmap
    def __getHashKey(self, key):
        hash_key = 0
        for char in key:
            hash_key += ord(char)

        return hash_key % self.size

    # method inserts a key value pair to the hashmap
    def insert(self, key, value):

        # Create the hash_key from from passed key
        hash_key = self.__getHashKey(key)

        # Check if hash_table is not empty,
        if (self.hash_table[hash_key]):

            # loop through the contents at that specific hash_table, check the passed key if it matches any of the stored keys
            # if it matches, update the value with the passed value
            # if it does not match, append
            for pair in self.hash_table[hash_key]:
                if pair[0] == key:
                    pair[1] = value
                    return True
                else:
                    self.hash_table[hash_key].append([key, value])

        # if the hash_key is empty, add the key value pair into that list
        else:
            self.hash_table[hash_key].append([key, value])
        
        #add 1 to counter
        self.item_counter += 1

    # creates a hash key by converting the id (string) to an integer
    def __convertIdToHashKey(self, key):
        return int(key)

    # same logic as insert but instead of creating the hash_key function, it just uses the package id as the hash_function
    def insertById(self, key, value):
        hash_key = self.__convertIdToHashKey(key)

        if (self.hash_table[hash_key]):
            for pair in self.hash_table[hash_key]:
                if pair[0] == hash_key:
                    pair[1] = value
                    return True
                else:
                    self.hash_table[hash_key].append([key, value])
        else:
            self.hash_table[hash_key].append([key, value])
        
        #add 1 to counter
        self.item_counter += 1

    # Method removes an item from th hashmap

    def remove(self, key):
        hash_key = self.__getHashKey(key)
        if not self.hash_table[hash_key]:
            return False
        else:
            for i in range(len(self.hash_table[hash_key])):
                if self.hash_table[hash_key][i][0] == key:
                    self.hash_table[hash_key].pop(i)

                    # subtracts 1 from item counter
                    self.item_counter -= 1
                    return True

    def search(self, key):
        hash_key = self.__getHashKey(key)
        if not self.hash_table[hash_key]:
            return None
        else:
            for pair in self.hash_table[hash_key]:
                if pair[0] == key:
                    return pair[1]

            return None

    def searchById(self, key):
        hash_key = self.__convertIdToHashKey(key)
        if not self.hash_table[hash_key]:
            return None
        else:
            for pair in self.hash_table[hash_key]:
                if pair[0] == key:
                    return pair[1]

            return None

    # # does not work
    # def searchByIndex(self, index):
    #     if self.hash_table[index]:
    #         for pair in self.hash_table[index]:
    #             return pair[1]
    #     else:
    #         pass

    # prints all items within the hashtable
    def printAllItems(self):
        for bucket in self.hash_table:
            for kvp in bucket:
                print(kvp[1])
