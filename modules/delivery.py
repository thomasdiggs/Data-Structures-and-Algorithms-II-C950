from modules.address_lookup import *
from modules.import_csv import distance_data, address_data, hash_table
from modules.trucks import *
from modules.import_csv import *
#
# # MANUALLY LOAD ADDRESS THAT ARE CLOSE TO EACH OTHER AFTER LOADING THE ONES WITH CONSTRAINTS
# # [1, 2, 4, 5, 7, 8, 10, 11, 12, 16, 17, 21, 22, 23, 24, 26]
truck_one = Truck([1, 13, 14, 15])
# , 16, 20, 29, 30, 31, 34, 37, 40
# # [3, 13, 14, 15, 18, 19, 20, 36, 38, 27, 29, 30, 31, 33, 34, 35]
# truck2 = Truck([3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39])
# # [6, 9, 25, 28, 32, 37, 39, 40]
# truck3 = Truck([2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33])
#
#
# def deliver(truck):
#     for element in truck.packages:
#         print(hash_table.search(element).get_details())


def distance_between(address1, address2):
    return distance_data[address_data.index(address1)][address_data.index(address2)]


def min_distance(truck):
    distances = []
    for element in truck.not_delivered:
        dist = distance_between(truck.current_address, hash_table.search(element).address)
        distances.append(float(dist))
    minimum_distance = min(distances)
    index_of_minimum = distances.index(minimum_distance)
    #     package_address = hash_table.search(element).address
    #     dist = distance_between(truck.start_address, package_address)
    #     package_list.append(dist)
    # float_package_list = list(map(float, package_list))
    # return min(float_package_list)
    # print(distances)
    # print(min(distances))
    # print(distances)
    # print(index_of_minimum)
    # print(minimum_distance)
    return index_of_minimum, minimum_distance


def delivery(truck):
    for element in truck.not_delivered:
        while len(truck.not_delivered) > 0:
            print(truck.not_delivered)
            index_of_nearest, shortest_distance = min_distance(truck)
            print(shortest_distance)
            print(index_of_nearest)
            truck.delivered.append(truck.not_delivered[index_of_nearest])
            truck.not_delivered.remove(truck.not_delivered[index_of_nearest])
            truck.miles_traveled += shortest_distance
            print(truck.miles_traveled)
            print(truck.not_delivered)
            print(truck.delivered)
            print("---")
    print(truck.not_delivered)
    print(truck.delivered)
