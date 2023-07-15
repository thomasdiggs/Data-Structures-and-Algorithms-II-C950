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
        self.departure_time = None
        self.delivered_time = None
        self.status = "at hub"

    # method to be called on any package object within hash table
    # this prints a human-readable string of package information
    def get_details(self):
        return "Package ID: %s \t Address: %s \t City: %s \t State: %s \t Zip Code: %s" \
               "\t Deadline: %s \t Weight(kg): %s \t Delivered Time: %s \t" % (
                self.pid, self.address, self.city, self.state, self.zip_code,
                self.deadline, self.weight, self.delivered_time)

    def get_details_at_time(self):
        return "Package ID: %s \t Address: %s \t City: %s \t State: %s \t Zip Code: %s" \
               "\t Deadline: %s \t Weight(kg): %s \t" % (
                self.pid, self.address, self.city, self.state, self.zip_code,
                self.deadline, self.weight)

    # method that will return the status at any given time
    def get_status(self, user_time):
        if user_time >= self.delivered_time:
            status = "Status: delivered\t"
            time = self.delivered_time
            return status + "Delivered Time: " + str(time)
        elif self.delivered_time > user_time > self.departure_time:
            return "Status: en route"
        else:
            return "Status: at hub"
