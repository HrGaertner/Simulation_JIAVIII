#Class Car will be imported and used in main.py
import random
import math

__license__ = "GNU GENERAL PUBLIC LICENSE"
__authors__ = "Ole Schmidt, Matthias Andres, Jonathan Gärtner"
__version__ = "0.6 Alpha - '27'"

class Car():
    def __init__(self, ID, streets, tick_waiting, current=None, s_0=2.0, T=1.5, a=0.3, b=3.0):  # May be expanded
        if current == None:
            current = random.choice(list(streets.nodes.keys()))
        self.id = ID
        self.distance = 0.0
        self.current = current  # First Street
        self.streets = streets
        self.next = random.choice(list(self.streets[self.current].keys()))  # Second Street
        self.streets[self.current][self.next]['cars'][self.next].append(self)
        self.v = 0.1
        self.s_0 = s_0 #Minimum bumper distant
        self.T = T/tick_waiting# Desired safety time headway T when following other vehicles
        self.a = a/(tick_waiting**2)# Acceleration a in every-day traffic
        self.b = b/(tick_waiting**2)# Comfortable (braking) deceleration b in every-day traffic

    def drive(self):  # Defines how the car drives and when it changes the street
        if self.streets[self.current][self.next]["length"] <= self.distance:  # if the car reached the end of its current street, then change it
            try:
                self.streets[self.current][self.next]["cars"][self.next].remove(self)  # Deletes this car from the street
            except:
                print("I am confused")
            former_current = self.current
            self.current = self.next
            while True: #Against oneway roads
                self.next = random.choice(list(self.streets[self.current].keys()))  # Selects randomly a new street
                if self.next == former_current and not len(list(self.streets[self.current].keys())) == 1:
                    continue
                try:
                    self.streets[self.current][self.next]['cars'][self.next].append(self)  # Appends this car to the current street
                except:
                    continue
                break
            self.distance = 0.0
        else:
            a_free = (self.v / float(self.streets[self.current][self.next]["max_v"])) ** 4  # See at the paper of Martin Treiber
            #if self.id == 0:
            #    print(a_free)
            if not self.streets[self.current][self.next]['cars'][self.next] == [self]:  # Checks whether there is another car on the street
                next_car = False
                event = False
                for c in self.streets[self.current][self.next]['cars'][self.next]:  # Gets the succeeding car
                    if event:
                        next_car = c
                    if self == c:
                        event = True
                if not next_car:
                    self.distance += self.v + a_free
                else:
                    gap_s = next_car.distance - self.distance
                    if gap_s == 0:
                        gap_s = 0.1
                    delta_v = self.v - next_car.v
                    a_int = ((self.s_0*max(0, (self.v*self.T + (self.v*delta_v/2*math.sqrt(self.a*self.b)))))/gap_s)**2# See at the paper of Martin Treiber
                    dt = a_free - a_int

                    self.distance += self.v + dt
            else:
                self.distance += self.v + a_free