class HashMap():
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()

    def create_buckets(self):
        return [[] for i in range(self.size)]

    def __getHashKey(self, key):
        hash_key = 0
        for char in key:
            hash_key += ord(char)

        return hash_key % self.size

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

    # does not work

    def search(self, key):
        hash_key = self.__getHashKey(key)
        if not self.hash_table[hash_key]:
            return None
        else:
            for pair in self.hash_table[hash_key]:
                if pair[0] == key:
                    return pair[1]

            return None

    def searchByIndex(self, index):
        if self.hash_table[index]:
            for pair in self.hash_table[index]:
                return pair[1]
        else:
            pass

    def getAllItems(self):
        for kvp in self.hash_table:
            return kvp[1]

    def remove(self, key):
        hash_key = self.__getHashKey(key)
        if not self.hash_table[hash_key]:
            return False
        else:
            for i in range(len(self.hash_table[hash_key])):
                if self.hash_table[hash_key][i][0] == key:
                    self.hash_table[hash_key].pop(i)
                    return True

    # checkers
    def printAll(self):
        for pair in self.hash_table:
            print(pair)

    def printList(self):
        print(self.hash_table)
