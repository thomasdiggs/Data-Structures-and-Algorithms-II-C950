class Package:
    def __init__(self, pid, address, city, state, zip_code, deadline, weight):
        self.pid = pid
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = "at the hub"

    def get_properties(self):
        return [self.pid,
                self.address,
                self.city,
                self.state,
                self.zip_code,
                self.deadline,
                self.weight,
                self.status]
