import flask
import werkzeug.exceptions

app = flask.Flask(__name__)


@app.teardown_request
def teardown(exc):
    print("Teardown: {}".format(exc))


@app.route("/")
def index():
    return "Home"


@app.route("/httpexception")
def httpexception():
    return werkzeug.exceptions.BadRequest("HttpException occured")


@app.route("/exception")
def exception():
    raise Exception("internal Exception occurred")


if __name__ == "__main__":
    app.run(port=5000)

