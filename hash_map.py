# This hashmap is a data structure built from scratch without the use of dictionaries
# It will be used for storing all the package objects

class HashMap():
    def __init__(self, size):
        self.size = size
        self.hash_table = self.create_buckets()
        self.item_counter = 0

    #creates the number of hash 'containers' or 'buckets' that will hold the values
    def create_buckets(self):
        return [[] for _ in range(self.size)]

    # creates a hash key by converting the id (string) to an integer
    def create_hash_key(self, key):
        return int(key)

    # Inserts the given value to the hash table at the given key
    # uses the create_hash_key method to create the index where the values will be stored\
    # O(n)
    def insert(self, key, value):
        hash_key = self.create_hash_key(key)

        # If the bucket is not empty
        if (self.hash_table[hash_key]):
            for pair in self.hash_table[hash_key]:
                #if the passed key matches the current key, then we should update the value
                if pair[0] == hash_key:
                    pair[1] = value
                    return True
                #if the passed key does not match the current key, then we should append the value
                else:
                    self.hash_table[hash_key].append([key, value])
        # Else, add the key value pair into the empty bucket
        else:
            self.hash_table[hash_key].append([key, value])

        # add 1 to counter
        self.item_counter += 1

    # Function removes an item from the hashmap based on the passed key
    # O(n)
    def remove(self, key):
        hash_key = self.create_hash_key(key)
        if not self.hash_table[hash_key]:
            return False
        else:
            for i in range(len(self.hash_table[hash_key])):
                if self.hash_table[hash_key][i][0] == key:
                    self.hash_table[hash_key].pop(i)

                    # subtracts 1 from item counter
                    self.item_counter -= 1
                    return True

    # Function searches and returns an item from the hashmap based on the passed key
    # O(n)
    def search(self, key):
        hash_key = self.create_hash_key(key)
        if not self.hash_table[hash_key]:
            return None
        else:
            for pair in self.hash_table[hash_key]:
                if pair[0] == key:
                    return pair[1]

            return None

    # Function prints all items within the hashtable
    # Used mainly during the development process to review data
    # O(n^2)
    def print_all_items(self):
        for bucket in self.hash_table:
            for kvp in bucket:
                print(kvp[1])
