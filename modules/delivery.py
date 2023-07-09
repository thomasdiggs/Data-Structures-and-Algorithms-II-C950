from modules.import_csv import distance_data, address_data, hash_table
from modules.trucks import *

# [1, 2, 4, 5, 7, 8, 10, 11, 12, 16, 17, 21, 22, 23, 24, 26]
truck1 = Truck([1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40])
# [3, 13, 14, 15, 18, 19, 20, 36, 38, 27, 29, 30, 31, 33, 34, 35]
truck2 = Truck([3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39])
# [6, 9, 25, 28, 32, 37, 39, 40]
truck3 = Truck([2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33])


def distance_between(address1, address2):
    return distance_data[address_data.index(address1)][address_data.index(address2)]


def min_distance(start_address, truck_packages):
    package_list = []
    for i in truck_packages:
        package_address = hash_table.search(i).address
        dist = distance_between(start_address, package_address)
        package_list.append(dist)
    float_package_list = list(map(float, package_list))
    return min(float_package_list)
