from flask import Flask, render_template
import matplotlib.pyplot as plt
import pandas as pd

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

@app.route("/covid/pandas")
def covid():

    df = pd.read_csv('static/covid_berlin.csv', sep=';', decimal=',')
    plt.bar(df["datum"], df["7_tage_hosp_inzidenz"], label="7 Tage Incidenz", color="#00cc00")

    plt.legend()
    plt.xlabel('7 Tage Inzidenz')
    plt.ylabel('Datum')
    plt.title('Covid / Tage Inzidenz Graph')

    filename = "covid.png" # speichert die Datei im Projektordner!
    plt.savefig("static/"+filename)
    return render_template("statistics.html", filename=filename)

if __name__ == "__main__":

    app.run(debug = True)