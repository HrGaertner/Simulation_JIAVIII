from flask import Flask, render_template
import main

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/update")
def update():
    return main.tick()

if __name__ == "__main__":
    app.run(debug=True)