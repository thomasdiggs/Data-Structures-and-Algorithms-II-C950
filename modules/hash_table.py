# D. Identify a self-adjusting data structure, such as a hash table, that can be used with the algorithm
# identified in part A to store the package data. 1. Explain how your data structure accounts for the relationship
# between the data points you are storing.
# Note: Use only appropriate built-in data structures, except dictionaries. You must design, write, implement,
# and debug all code that you turn in for this assessment. Code downloaded from the Internet or acquired from
# another student or any other source may not be submitted and will result in automatic failure of this assessment.

# E. Develop a hash table, without using any additional libraries or classes, that has an insertion function that
# takes the following components as input and inserts the components into the hash table:
# packageIDnumber, deliveryaddress, deliverydeadline, deliverycity, deliveryzipcode, packageweight,
# deliverystatus(e.g., delivered, enroute)

# HashTable class using chaining.
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts either a new item into or updates an item in the hash table.
    def insert(self, key, item):
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket.
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        for key_value in bucket_list:
            if key_value[0] == key:
                # if found return the key's value that is in the bucket list.
                # return after calling the getter function for the value in bucket list.
                return key_value[1]

        # the key is not found.
        return None
