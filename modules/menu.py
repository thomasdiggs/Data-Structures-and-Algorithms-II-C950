from modules.delivery import *


def start_ui():
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
    while is_quit:
        print("\n[1] get SINGLE package FULL details after delivery")
        print("[2] get SINGLE package STATUS details at a specific time")
        print("[3] get ALL package FULL details after delivery")
        print("[4] get ALL package FULL details at a specific time")
        print("[0] quit program")
        try:
            option = int(input("[?]: "))
            if option == 0:
                print("stay sweet parakeet")
                is_quit = False
            elif option == 1:
                try:
                    lookup_id = int(input("enter package ID: "))
                    print(hash_table.search(lookup_id).get_details() + "Notes: " + hash_table.search(lookup_id).notes)
                except:
                    print("Invalid input, try again")
            elif option == 2:
                try:
                    lookup_time = input("enter time with format, HH:MM:SS: ")
                    (h, m, s) = lookup_time.split(":")
                    h = int(h)
                    m = int(m)
                    s = int(s)
                    converted_time = datetime.timedelta(hours=h, minutes=m, seconds=s)
                    lookup_id = int(input("enter package ID: "))
                    package = hash_table.search(lookup_id)
                    print(package.get_status(converted_time))
                except:
                    print("Invalid input, try again")
            elif option == 3:
                for element in range(1, 41):
                    print(hash_table.search(element).get_details() + "Notes: " + hash_table.search(element).notes)
            elif option == 4:
                try:
                    lookup_time = input("enter time with format, HH:MM:SS: ")
                    (h, m, s) = lookup_time.split(":")
                    h = int(h)
                    m = int(m)
                    s = int(s)
                    converted_time = datetime.timedelta(hours=h, minutes=m, seconds=s)
                    for element in range(1, 41):
                        print(hash_table.search(element).get_details_at_time() + hash_table.search(element).get_status(
                            converted_time))
                except:
                    print("Invalid input, try again")
            else:
                print("invalid input, try again")
        except:
            print("invalid input, try again")