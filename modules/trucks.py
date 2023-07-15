class Truck:
    def __init__(self, packages, depart_time):
        self.capacity = 16
        self.speed = 18
        self.miles_traveled = float(0.0)
        self.not_delivered = packages
        self.delivered = []
        self.start_address = "4001 South 700 East"
        self.current_address = self.start_address
        self.end_address = "4001 South 700 East"
        self.depart_time = depart_time
        self.current_time = self.depart_time
