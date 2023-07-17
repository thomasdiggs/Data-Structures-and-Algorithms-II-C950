class Package:
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

    # F. Develop a look-up function that takes the following components as input and returns the
    # corresponding data elements:
    # package ID number, delivery address, delivery deadline, delivery city, delivery zip code,
    # package weight, delivery status (i.e., "at the hub", "en route", or "delivered"), including
    # delivery time
    # note: Your function should output all data elements for the package ID number.
    # O(1)
    def get_details(self, user_time):
        if user_time >= self.delivered_time:
            time = self.delivered_time
            status = "Satus: delivered\t Delivered Time: " + str(time)
        elif self.delivered_time > user_time > self.departure_time:
            status = "Status: en route"
        else:
            status = "Status: at hub"

        return "Package ID: %s \t Address: %s \t City: %s \t State: %s \t Zip Code: %s" \
               "\t Deadline: %s \t Weight(kg): %s \t %s \t %s" % (
                self.pid, self.address, self.city, self.state, self.zip_code,
                self.deadline, self.weight, status, self.notes)
