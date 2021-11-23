import unittest
from src.person import Person
from src.bus import Bus

class TestPerson(unittest.TestCase):
    def setUp(self):
        self.person = Person("Guido van Rossum", 64, 20, "Somewhere")

    # @unittest.skip("Delete this line to run the test")
    def test_person_has_name(self):
        self.assertEqual("Guido van Rossum", self.person.name)

    # @unittest.skip("Delete this line to run the test")
    def test_person_has_age(self):
        self.assertEqual(64, self.person.age)

    # @unittest.skip("Delete this line to run the test")
    def test_person_has_cash(self):
        self.assertEqual(20, self.person.cash)

    def test_person_has_paid(self):
        bus = Bus(22, "Ocean Terminal", 2, 5)
        self.person.pay_for_bus(bus)
        self.assertEqual(18, self.person.cash)
        self.assertEqual(2, bus.total_cash)

    def test_person_has_destination(self):
        self.assertEqual("Somewhere", self.person.destination)