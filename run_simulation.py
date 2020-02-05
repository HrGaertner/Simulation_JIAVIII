import time
import osm_parse  # Other Project files
import car        # Other Project files
import queue
from flask import Flask, render_template
from flask_socketio import SocketIO
from multiprocessing import Process

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def create_cars(car_number):  # Creates car_number cars where the ID is the current iteration
    cars = []
    for i in range(car_number):
        a = car.Car(i, streets)
        cars.append(a)
    return cars

car_amount = 5

streets = osm_parse.create_streetnetwork("JiaVII_Sep19.osm")  # Creates streetnetwork
cars = create_cars(car_amount)  # Creates cars

all_lats = queue.Queue()
all_lons = queue.Queue()
def run(all_lats, all_lons):
    try:
        while True:  # Updates the simulation
            lats = []
            lons = []
            for c in cars:
                #if c.id == 0:
                #     print(str(c.id) + ' ' + str(c.distance) + ' ' + str(c.current))
                latA = streets.node[c.current]['lat']
                lonA = streets.node[c.current]['lon']
                latB = streets.node[c.next]['lat']
                lonB = streets.node[c.next]['lon']
                # length_between_points = osm_parse.haversine(lon1, lat1, lon2, lat2)
                length = streets[c.current][c.next]['length']
                progress = c.distance / length
                lats.append(latA + (latB - latA) * progress)
                lons.append(lonA + (lonB - lonA) * progress)
                c.drive()
                # time.sleep(0.3)
            all_lats = lats
            all_lons = lons
    except KeyboardInterrupt:
        pass

@app.route(‘/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    thread1 = threading.Thread(target=run, args=(all_lons, all_lats))
    thread2 = threading.Thread(target=, args=(app))
    thread1.start()
    thread2.start()
    socketio.run(app)