class Bus:
    def __init__(self, route_number, destination, price, capacity):
        self.route_number = route_number
        self.capacity = capacity
        self.destination = destination
        self.price = price
        self.passengers = []
        self.total_cash = 0

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)

    def remaining_capacity(self):
        return self.capacity - self.passenger_count()

    def pick_up(self, passenger):
        self.passengers.append(passenger)

    def drop_off(self, passenger):
        self.passengers.remove(passenger)

    def empty(self):
        self.passengers = []

    def pick_up_from_stop(self, bus_stop):

        for person in bus_stop.queue:
            if (self.remaining_capacity() > 0 and person.destination == self.destination):
                self.pick_up(person)
                
        for person in self.passengers:
            if person in bus_stop.queue:
                bus_stop.queue.remove(person)