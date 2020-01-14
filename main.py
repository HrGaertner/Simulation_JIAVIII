import time
import osm_parse, car #Other Project files

def create_cars(car_number):  # Creates car_number cars where the ID is the current iteration
    cars = []
    for i in range(car_number):
        a = car.Car(i, streets)
        cars.append(a)
    return cars

streets = osm_parse.create_streetnetwork("JiaVII_Sep19.osm")  # Creates streetnetwork
car = create_cars(5)  # Creates cars

while True:  # Updates the simulation
    for c in car:
        if c.id == 0:
            print(str(c.id) + ' ' + str(c.distance) + ' ' + str(c.current))
        c.drive()
        time.sleep(0.3)
