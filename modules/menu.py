from modules.delivery import *


# function to convert a user input of time in string format into a datetime object
# O(1)
def convert_time(user_time):
    (h, m, s) = user_time.split(":")
    h = int(h)
    m = int(m)
    s = int(s)
    return datetime.timedelta(hours=h, minutes=m, seconds=s)


def start_ui():
    # printing and calculating then rounding the total distance traveled for all trucks
    total_distance = truck_two.miles_traveled + truck_two.miles_traveled + truck_three.miles_traveled
    rounded_total_distance = round(total_distance, 1)
    print("Total distance traveled for all trucks: {} miles".format(rounded_total_distance))
    print("\nPackage IDs on " + truck_one.truck_id + ":")
    print(truck_one.delivered)
    print("\nPackage IDs on " + truck_two.truck_id + ":")
    print(truck_two.delivered)
    print("\nPackage IDs on " + truck_three.truck_id + ":")
    print(truck_three.delivered)
    print("\ntype an option to:")
    is_quit = True
    # O(1)
    while is_quit:
        print("[1] get SINGLE package STATUS details at a specific time")
        print("[2] get ALL package FULL details at a specific time")
        print("[0] quit program")
        try:
            option = int(input("[?]: "))
            if option == 0:
                try:
                    print("stay sweet parakeet")
                    is_quit = False
                except:
                    print("Invalid input, try again")
            elif option == 1:
                try:
                    # take the user input for a time in the correct format, else send error message
                    user_time = input("enter time with format, HH:MM:SS: ")
                    # convert the user input from string to a datetime object
                    converted_time = convert_time(user_time)
                    # take the user input for package ID
                    lookup_id = int(input("enter package ID: "))
                    # search hash table for the package object
                    package = hash_table.search(lookup_id)
                    # print details to the screen
                    print(package.get_details(converted_time))
                except:
                    print("Invalid input, try again")
            elif option == 2:
                try:
                    user_time = input("enter time with format, HH:MM:SS: ")
                    converted_time = convert_time(user_time)
                    # loop through all packages in hash table
                    for element in range(1, 41):
                        package = hash_table.search(element)
                        print(package.get_details(converted_time))
                except:
                    print("Invalid input, try again")
            else:
                print("invalid input, try again")
        except:
            print("invalid input, try again")