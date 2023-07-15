import datetime

from modules.trucks import *
from modules.import_csv import *

# MANUALLY LOAD ADDRESS THAT ARE CLOSE TO EACH OTHER AFTER LOADING THE ONES WITH CONSTRAINTS
# My way: [1, 2, 4, 5, 7, 8, 10, 11, 12, 16, 17, 21, 22, 23, 24, 26]
# Not my way: [1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40]
truck_one = Truck([1, 2, 4, 5, 7, 8, 10, 11, 12, 16, 17, 21, 22, 23, 24, 26], datetime.timedelta(hours=8, minutes=00))
# My way: [3, 13, 14, 15, 18, 19, 20, 36, 38, 27, 29, 30, 31, 33, 34, 35]
# Not my way: [3, 12, 17, 18, 19, 21, 22, 23, 24, 26, 27, 35, 36, 38, 39]
truck_two = Truck([3, 13, 14, 15, 18, 19, 20, 36, 38, 27, 29, 30, 31, 33, 34, 35], datetime.timedelta(hours=8, minutes=00))
# My way: [6, 9, 25, 28, 32, 37, 39, 40]
# Not my way: [2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33]
truck_three = Truck([6, 9, 25, 28, 32, 37, 39, 40], datetime.timedelta(hours=10, minutes=30))


def distance_between(address1, address2):
    return float(distance_data[address_data.index(address1)][address_data.index(address2)])


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
    # set packages in truck as en route
    for element in truck.not_delivered:
        hash_table.search(element).status = "en route"
    # loop through every package on the truck in the not_delivered array
    # for element in truck.not_delivered:
    while len(truck.not_delivered) > 0:
        # find the shortest distance from current_address of truck to any package
        index_of_nearest, shortest_distance = min_distance(truck)
        truck.current_address = hash_table.search(truck.not_delivered[index_of_nearest]).address
        # add mileage to package to truck's total milage
        truck.miles_traveled += shortest_distance
        # update current time as each package is delivered
        truck.current_time += datetime.timedelta(hours=shortest_distance / 18)
        hash_table.search(truck.not_delivered[index_of_nearest]).delivered_time = truck.current_time
        # mark package as delivered
        hash_table.search(truck.not_delivered[index_of_nearest]).status = "delivered"
        # move package to delivered and remove from not_delivered
        truck.delivered.append(truck.not_delivered[index_of_nearest])
        truck.not_delivered.remove(truck.not_delivered[index_of_nearest])
    # add mileage from last package on truck back to the hub
    truck.miles_traveled += distance_between(hash_table.search(truck.delivered[len(truck.delivered) - 1]).address, truck.end_address)
    truck.miles_traveled = round(truck.miles_traveled, 1)
