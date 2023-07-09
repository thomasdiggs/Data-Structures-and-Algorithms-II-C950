import csv
from packages import Package


# parse the packages csv file
def import_packages(filename, hash_table):
    with open(filename) as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        # loop through each row in the csv file
        for row in reader:
            # storing values into variables to pass into insert function and package object
            pid = int(row[0])
            address = row[1]
            city = row[2]
            state = row[3]
            zip_code = int(row[4])
            deadline = row[5]
            weight = int(row[6])
            # insert package id as an integer for the key and a package object as the value
            hash_table.insert(pid, Package(pid, address, city, state, zip_code, deadline, weight))

# parse the distance csv file
