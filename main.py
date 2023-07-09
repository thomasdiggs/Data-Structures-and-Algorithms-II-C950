# Thomas Diggs 010815435

from hashtable import *
from import_csv import *
from menu import *


class Main:
    # Instantiate the class ChainingHashTable
    hash_table = ChainingHashTable()

    # Call import_packages from the import-csv.py module
    import_packages('packages.csv', hash_table)

    # Start of program's user interface
    start_ui(hash_table)
