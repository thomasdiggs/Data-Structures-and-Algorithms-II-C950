# Thomas Diggs 010815435

from truck import Truck
from hashtable import ChainingHashTable
from importcsv import import_packages


class Main:
    # Instantiate the class ChainingHashTable
    hash_table = ChainingHashTable()

    # Call import_packages from the importcsv.py module
    import_packages('packages.csv', hash_table)

    # instantiate truck objects and manually load packages
    truck1 = Truck(hash_table.table[1])

    print("Western Governors University Parcel Service (WGUPS) Program")
    print("Lookup by Package ID: ")
    command = int(input())
    print(hash_table.search(command).get_details())

    # print(truck1.packages)
    