# Thomas Diggs 010815435

import csv
import packages


class Main:
    with open('packages.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        packageList = []
        for row in csv_reader:
            packageList.append(row)
        for i in range(len(packageList)):
            print(packageList[i])


    print(type(packageList[0][0]))