import time
import osm_parse  # Other Project files
import car        # Other Project files
import pickle


def create_cars(car_number):  # Creates car_number cars where the ID is the current iteration
    cars = []
    for i in range(car_number):
        a = car.Car(i, streets)
        cars.append(a)
    return cars

car_amount = 5

streets = osm_parse.create_streetnetwork("JiaVII_Sep19.osm")  # Creates streetnetwork
cars = create_cars(car_amount)  # Creates cars
values = []
for i in range(car_amount):
    values.append([])
ts = 0
try:
    while ts < 100:  # Updates the simulation
        for c in cars:
            # if c.id == 0:
            #     print(str(c.id) + ' ' + str(c.distance) + ' ' + str(c.current))
            latA = streets.node[c.current]['lat']
            lonA = streets.node[c.current]['lon']
            latB = streets.node[c.next]['lat']
            lonB = streets.node[c.next]['lon']
            # length_between_points = osm_parse.haversine(lon1, lat1, lon2, lat2)
            length = streets[c.current][c.next]['length']
            progress = c.distance / length
            latC = latA + (latB - latA) * progress
            lonC = lonA + (lonB - lonA) * progress
            values[c.id].append([ts, lonC, latC])

            c.drive()
            # time.sleep(0.3)
        ts += 1
except KeyboardInterrupt:
    pass

with open('daten.pickle', 'wb') as file:
    pickle.dump(values, file)