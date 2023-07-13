# Packages class
class Package:
    # package constructor to create package objects that will be inserted into hash table
    def __init__(self, pid, address, city, state, zip_code, deadline, weight, notes):
        self.pid = pid
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

        # self.status = "at the hub"
        # self.delivery_time = "00:00:00"

    # method to be called on any package object within hash table
    # this prints a human-readable string of package information
    def get_details(self):
        return "Package ID: %s \t Address: %s \t City: %s \t State: %s \t " \
               "Zip Code: %s \t Deadline: %s \t Weight(kg): %s \t Notes: %s" % (
                self.pid, self.address, self.city, self.state,
                self.zip_code, self.deadline, self.weight, self.notes)

    # CREATE AN UPDATE STATUS FUNCTION HERE
    # THIS FUNCTION WILL UPDATE FROM "at the hub" TO "en route" OR "delivered"
    # def update_status(self, x):
