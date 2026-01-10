class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passengers(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} has boarded the bus")
        else:
            print("Bus full, cannot board more passengers")
        
    def remove_passengers(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} has dropped the bus")
        else:
            print(f"{person.name} isn't in the bus")

class Person:
    def __init__(self, name):
        self.name = name

person_1 = Person("Ana")
person_2 = Person("Juan")
person_3 = Person("Jose")

bus_1 = Bus(2)

bus_1.add_passengers(person_1)
bus_1.add_passengers(person_2)
bus_1.add_passengers(person_3)

bus_1.remove_passengers(person_1)
bus_1.remove_passengers(person_2)
