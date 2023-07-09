# Name: Thomas Diggs
# Student ID: 010815435

from modules.import_csv import *
from modules.menu import *
from modules.delivery import *


class Main:
    # instantiate the class ChainingHashTable
    # hash_table = ChainingHashTable()

    # begin calling import functions from the import-csv.py module
    # import package objects into the newly created hash_table
    import_packages("csv_files/packages.csv")

    # import addresses into a one-dimensional list
    import_addresses("csv_files/addresses.csv")

    # import distances to all addresses into a two-dimensional list
    # distance_data[2][6] is the same as distance_data[6][2]
    import_distances("csv_files/distances.csv")

    # Start of program's user interface
    start_ui(hash_table)