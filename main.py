import time
import osm_parse  # Other Project files
import car        # Other Project files
import xml.etree.ElementTree as Et

__license__ = "GNU GENERAL PUBLIC LICENSE"
__authors__ = "Ole Schmidt, Matthias Andres, Jonathan Gärtner"
__version__ = "1.0 - 'Heart's On Fire'"


def create_cars(car_number):  # Creates car_number cars where the ID is the current iteration
    cars_created = []
    for i in range(car_number):
        a = car.Car(i, streets, 1/3)
        cars_created.append(a)
    return cars_created


car_amount = 15

file = "JiaVII_Sep19.osm"

streets, bus_stops = osm_parse.create_streetnetwork(file)  # Creates streetnetwork
cars = create_cars(car_amount)  # Creates cars

tree = Et.parse(file)
root = tree.getroot()
for child in root:
    if child.tag == "bounds":
        outer__coord = child.attrib

center = [float(outer__coord["minlat"]) + (float(outer__coord["maxlat"]) - float(outer__coord["minlat"])),
          float(outer__coord["minlon"]) + (float(outer__coord["maxlon"]) - float(outer__coord["minlon"""]))]


def tick():
    coord = {"type": "MultiPoint", "coordinates": []}
    for c in cars:
        # if c.id == 0:
        #    print(str(c.id) + ' ' + str(c.distance) + ' ' + str(c.current))
        lat_a = streets.node[c.current]['lat']
        lon_a = streets.node[c.current]['lon']
        lat_b = streets.node[c.next]['lat']
        lon_b = streets.node[c.next]['lon']
        length = streets[c.current][c.next]['length']
        progress = c.distance / length
        lat_c = float(lat_a + (lat_b - lat_a) * progress)
        lon_c = float(lon_a + (lon_b - lon_a) * progress)

        coord["coordinates"].append([lon_c, lat_c])
        c.drive()
    return coord


if __name__ == "__main__":
    while True:  # Updates the simulation
        data = tick()
        time.sleep(1/3)
        print(str(cars[0].id), str(cars[0].distance), str(cars[0].current), str(cars[0].v))
