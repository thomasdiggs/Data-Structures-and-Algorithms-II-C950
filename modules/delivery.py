import datetime

from modules.trucks import *
from modules.import_csv import *

# manually loading trucks and inputting departure times
truck_one = Truck([13, 14, 15, 16, 19, 20, 1, 29, 30, 31, 34, 37, 40],
                  datetime.timedelta(hours=8, minutes=0, seconds=0), "Truck One")
truck_two = Truck([3, 6, 18, 25, 28, 32, 36, 38, 27, 35, 39], datetime.timedelta(hours=9, minutes=5, seconds=0),
                  "Truck Two")
truck_three = Truck([9, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 24, 26, 33],
                    datetime.timedelta(hours=10, minutes=20, seconds=0), "Truck Three")


# function to return the index of an address from the address table
# O(1)
def address_lookup(address):
    return address_data.index(address)


# function to return the distance between two addresses based on the distance table
# O(1)
def distance_between(address1, address2):
    return float(distance_data[address_lookup(address1)][address_lookup(address2)])


# function to return the minimum value in an array
# O(n)
def min_distance(truck):
    distances = []
    # loop through elements in truck's array of packages not delivered
    for element in truck.not_delivered:
        # find the distance between the truck's current address and every other element in the array
        dist = distance_between(truck.current_address, hash_table.search(element).address)
        # add that distance in miles to the distances array
        distances.append(float(dist))
    # find the minimum value in the array of distances
    minimum_distance = min(distances)
    # find the index of the next closest address
    index_of_minimum = distances.index(minimum_distance)
    return index_of_minimum, minimum_distance


# algorithm used for delivery can be defined as a Nearest Neighbor algorithm
def delivery(truck):
    # set packages in truck as en route
    # O(n)
    for element in truck.not_delivered:
        hash_table.search(element).status = "en route"
        hash_table.search(element).departure_time = truck.depart_time
        truck.current_time = truck.depart_time
    # loop through every package on the truck in the not_delivered array
    # O(n)
    while len(truck.not_delivered) > 0:
        # find the shortest distance from current_address of truck to any package
        index_of_nearest, shortest_distance = min_distance(truck)
        truck.current_address = hash_table.search(truck.not_delivered[index_of_nearest]).address
        # add mileage to package to truck's total milage
        truck.miles_traveled += shortest_distance
        # update current time as each package is delivered
        truck.current_time += datetime.timedelta(hours=shortest_distance / 18)
        # mark package as delivered
        hash_table.search(truck.not_delivered[index_of_nearest]).status = "delivered"
        hash_table.search(truck.not_delivered[index_of_nearest]).delivered_time = truck.current_time
        # move package to delivered and remove from not_delivered
        truck.delivered.append(truck.not_delivered[index_of_nearest])
        truck.not_delivered.remove(truck.not_delivered[index_of_nearest])
    # add mileage from last package on truck back to the hub
    dist_back_to_hub = distance_between(hash_table.search(truck.delivered[len(truck.delivered) - 1]).address,
                                        truck.end_address)
    truck.miles_traveled += dist_back_to_hub
    truck.miles_traveled = round(truck.miles_traveled, 1)
    truck.current_time += datetime.timedelta(hours=dist_back_to_hub / 18)
    print(truck.truck_id + " departed hub at: " + str(truck.depart_time))
    print(truck.truck_id + " returned to hub at: " + str(truck.current_time))
    print(truck.truck_id + " traveled " + str(truck.miles_traveled) + " miles")
