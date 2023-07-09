# Thomas Diggs 010815435

import csv
from hashtable import ChainingHashTable


class Main:
    with open('packages.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        package_list = []
        for row in reader:
            package_list.append(row)

    # Instantiate the class ChainingHashTable
    my_hash = ChainingHashTable()

    for element in package_list:
        my_hash.insert(element[0], element[1])
    print(my_hash.table)

    print(my_hash.search("35"))