from flask import Flask, render_template
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route("/")
def hello_plot():
    plt.bar([1,3,5,7,9],[5,2,7,8,2], label="Example one", color="#00cc00")
    plt.bar([2,4,6,8,10],[8,6,2,5,6], label="Example two", color='g')

    plt.legend()
    plt.xlabel('bar number')
    plt.ylabel('bar height')

    plt.title('Epic Graph')

    path = "static/plot.png" # speichert die Datei im Projektordner!
    plt.savefig(path)

    return render_template("statistics.html", img_path=path)


if __name__ == "__main__":

    app.run(debug = True)