from flask import Flask, render_template
import datetime
app = Flask(__name__)

name = "Rockhopper-penguin"
date = datetime.datetime.now()

@app.route("/")
def menu():
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    minute = date.minute
    second = date.second
    return render_template("index.html", name = name, year = year, month = month, day = day, hour = hour, minute = minute, second = second)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)