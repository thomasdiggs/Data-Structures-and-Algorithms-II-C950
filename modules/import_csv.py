import csv
from modules.packages import *
from modules.hash_table import *

# instantiate the class ChainingHashTable
hash_table = ChainingHashTable()
distance_data = []
address_data = []


# parse the packages csv file
def import_packages(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        # loop through each row in the csv file
        # O(n)
        for row in reader:
            # storing values into variables to pass into insert function and package object
            pid = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = int(row[4])
            deadline = row[5]
            weight = int(row[6])
            notes = row[7]
            # insert package id as an integer for the key and a package object as the value
            hash_table.insert(pid, Package(pid, address, city, state, zip_code, deadline, weight, notes))


# parse the distance csv file
def import_distances(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        # store each row from csv file into distance_data list
        # O(n)
        for row in reader:
            distance_data.append(row)
        # iterate over the rows and columns to fill in the missing values from the csv
        # this creates a complete distance table
        # O(n^2)
        for i in range(len(distance_data)):
            for j in range(len(distance_data)):
                distance_data[i][j] = distance_data[j][i]
        # return distance_data


# parse the address csv file
def import_addresses(filename):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        # loop through each row in the csv file
        # O(n)
        for row in reader:
            # append only the address (element 3, index 2) to the list
            address_data.append(row[2])
        # return address_data
