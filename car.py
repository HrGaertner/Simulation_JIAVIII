#Class Car will be imported and used in main.py
import random

class Car():
    def __init__(self, ID, streets, max_v=120):  # May be expanded
        self.id = ID
        self.distance = 0.0
        self.current = 'A'  # First Street
        self.next = 'B'  # Second Street
        self.streets = streets
        self.streets[self.current][self.next]['cars'][self.next].append(self)
        self.max_v = max_v
        self.v = 0

    def drive(self):  # Defines how the car drives and when it changes the street
        if self.streets[self.current][self.next]["length"] <= self.distance:  # if the car reached the end of its current street, then change it

            self.streets[self.current][self.next]["cars"][self.next].remove(self)  # Deletes this car from the street
            self.current = self.next
            self.next = random.choice(list(self.streets[self.current].keys()))  # Selects randomly a new street
            self.streets[self.current][self.next]['cars'][self.next].append(self)  # Appends this car to the current street
            self.distance = 0.0
        else:
            if not self.streets[self.current][self.next]['cars'][self.next] == [self]:  # Checks whether there is another car on the street
                next_car = False
                event = False
                for c in self.streets[self.current][self.next]['cars'][self.next]:  # Gets the succeeding car
                    if event:
                        next_car = c
                    if self == c:
                        event = True
                if not next_car:
                    self.distance += 1
                else:
                    delta_v = self.v - next_car.v
                    
                    if self.distance + 1 >= next_car.distance:  # Looks whether the next car is more than one unit away
                        pass
                    else:
                        self.distance += 1
            else:
                self.distance += 1
