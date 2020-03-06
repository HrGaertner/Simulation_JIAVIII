from flask import Flask, render_template
import main
import threading
import time

# variables that are accessible from anywhere
data = {}

def Simulation():
    global data
    while True:  # Updates the simulation
        data = main.tick()
        time.sleep(0.3)
        #main.time.sleep(1/60)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", bus_stops=main.bus_stops, center=main.center)

@app.route("/update")
def update():
    return data

if __name__ == "__main__":
    # lock to control access to variable
    dataLock = threading.Lock()
    # thread handler
    simu = threading.Thread(target=Simulation)
    simu.start()

    app.run(debug=True)