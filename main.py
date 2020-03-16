import time
import osm_parse  # Other Project files
import car        # Other Project files
import xml.etree.ElementTree as ET
from decimal import *
getcontext().prec = 40

__license__ = "GNU GENERAL PUBLIC LICENSE"
__authors__ = "Ole Schmidt, Matthias Andres, Jonathan Gärtner"
__version__ = "0.6 Alpha - '27'"

def create_cars(car_number):  # Creates car_number cars where the ID is the current iteration
    cars = []
    for i in range(car_number):
        a = car.Car(i, streets, 1/3)
        cars.append(a)
    return cars

car_amount = 40

file = "JiaVII_Sep19.osm"

streets, bus_stops = osm_parse.create_streetnetwork(file)  # Creates streetnetwork
cars = create_cars(car_amount)  # Creates cars

tree = ET.parse(file)
root = tree.getroot()
for child in root:
    if child.tag == "bounds":
        outer__coord = child.attrib

center = {}
center = [float(outer__coord["minlat"]) + (float(outer__coord["maxlat"]) - float(outer__coord["minlat"]))]
center.append(float(outer__coord["minlon"]) + (float(outer__coord["maxlon"]) - float(outer__coord["minlon"""])))

def tick():
    coord = {"type": "MultiPoint", "coordinates": []}
    for c in cars:
        #if c.id == 0:
        #    print(str(c.id) + ' ' + str(c.distance) + ' ' + str(c.current))
        latA = Decimal(streets.node[c.current]['lat'])
        lonA = Decimal(streets.node[c.current]['lon'])
        latB = Decimal(streets.node[c.next]['lat'])
        lonB = Decimal(streets.node[c.next]['lon'])
        length = streets[c.current][c.next]['length']
        progress = c.distance / Decimal(length)
        latC = float(latA + (latB - latA) * progress)
        lonC = float(lonA + (lonB - lonA) * progress)

        coord["coordinates"].append([lonC, latC])
        c.drive()
    return coord

if __name__ == "__main__":
    #try:
        while True:  # Updates the simulation
            data = tick()
            time.sleep(1/3)
            print(str(cars[0].id), str(cars[0].distance), str(cars[0].current), str(cars[0].v))
    #except KeyboardInterrupt:
    #    pass