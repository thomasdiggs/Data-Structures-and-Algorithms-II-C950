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

    # F. Develop a look-up function that takes the following components as input and returns the corresponding data elements:
    # package ID number, delivery address, delivery deadline, delivery city, delivery zip code,
    # package weight, delivery status (i.e., "at the hub", "en route", or "delivered"), including delivery time
    # note: Your function should output all data elements for the package ID number.
    def get_details_after_delivery(self):
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
    # the return value is concatenated with the return value from get_details_at_time
    def get_status(self, user_time):
        if user_time >= self.delivered_time:
            status = "Status: delivered\t"
            time = self.delivered_time
            return status + "Delivered Time: " + str(time)
        elif self.delivered_time > user_time > self.departure_time:
            return "Status: en route"
        else:
            return "Status: at hub"

    def get_details(self, user_time):
        if user_time >= self.delivered_time:
            time = self.delivered_time
            status = "Satus: delivered\t Delivered Time: " + str(time)
        elif self.delivered_time > user_time > self.departure_time:
            status = "Status: en route"
        else:
            status = "Status: at hub"

        return "Package ID: %s \t Address: %s \t City: %s \t State: %s \t Zip Code: %s" \
               "\t Deadline: %s \t Weight(kg): %s \t %s" % (
                self.pid, self.address, self.city, self.state, self.zip_code,
                self.deadline, self.weight, status)
