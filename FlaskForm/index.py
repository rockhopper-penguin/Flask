from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        name = request.form['name']
        return render_template("result.html", name = name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
    # app.run(host="192.168.0.2", debug=True)