from flask import Flask
app = Flask(__name__)


application = app

@app.route("/")
def hello():
    return "This is Hello World!\n"

@app.route("/dv")
def hello():
    return "Development on Progress!"


if __name__ == "__main__":
    app.run(debug=True)