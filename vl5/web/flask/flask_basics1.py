from flask import Flask

app = Flask(__name__) # muss vor den Annotierungen stehen!

@app.route("/")
def hello_flask():
    return "Hello Flask!"

@app.route("/hello")
def hello_world():
    return "Hello World!"

if __name__ == "__main__":

    app.run(debug = True)

