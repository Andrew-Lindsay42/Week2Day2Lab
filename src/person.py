class Person:
    def __init__(self, name, age, cash):
        self.name = name
        self.age = age
        self.cash = cash

    def pay_for_bus(self, bus):
        self.cash -= bus.price
        bus.total_cash += bus.price