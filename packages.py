class Package:
    def __init__(self, pid, address, city, state, zipcode, deadline, weight):
        self.pid = pid
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = "at the hub"

