from flask import Flask, render_template
import main
import threading
import time
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

__license__ = "GNU GENERAL PUBLIC LICENSE"
__authors__ = "Ole Schmidt, Matthias Andres, Jonathan Gärtner"
__version__ = "1.0 - 'Heart's On Fire'"

# variables that are accessible from anywhere
data = {}
last_website_access = 0.0
running = True

def Simulation():
    global data
    global running
    while True:  # Updates the simulation
        if last_website_access + 3 <= time.time():
            running = False
            break
        data = main.tick()
        time.sleep(0.3)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", bus_stops=main.bus_stops, center=main.center)

@app.route("/update")
def update():
    global running
    global last_website_access
    last_website_access = time.time()
    if running:
        return data
    else:
        simu = threading.Thread(target=Simulation)
        simu.start()
        running = True
        return data

if __name__ == "__main__":
    # lock to control access to variable
    dataLock = threading.Lock()
    # thread handler
    simu = threading.Thread(target=Simulation)
    simu.start()

    app.run(debug=True)