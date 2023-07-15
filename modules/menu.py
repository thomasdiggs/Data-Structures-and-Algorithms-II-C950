from modules.delivery import *


def start_ui():
    print("Western Governors University Parcel Service Program\n")
    total_distance = truck_two.miles_traveled + truck_two.miles_traveled + truck_three.miles_traveled
    print("Total distance traveled for all trucks: {} miles".format(total_distance))
    print("\ntype an option to:")
    is_quit = True
    while is_quit:
        print("\n[1] get package details")
        print("[2] enter a time")
        print("[0] quit program")
        option = int(input("[?]: "))
        if option == 1:
            lookup_id = int(input("input package ID: "))
            print(hash_table.search(lookup_id).get_details())
        elif option == 0:
            print("stay sweet parakeet")
            is_quit = False
        elif option == 2:
            lookup_time = input("Enter format, HH:MM")
            h, m = lookup_time.split(":")
            h = int(h)
            m = int(m)
            converted_time = datetime.time(hour=h, minute=m)
            print(converted_time)
        else:
            print("invalid option")
