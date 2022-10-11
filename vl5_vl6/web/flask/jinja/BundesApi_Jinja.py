import json

import requests as requests
from flask import Flask, render_template, request

app = Flask(__name__)  # muss vor den Annotierungen stehen!
baseUrl = "https://warnung.bund.de/api31/appdata/covid/covidrules/DE/{0}.json"


@app.route("/")
def index():
    return render_template("registrationform.html",
                           title="Registration Form",
                           post_url="/select-example")

@app.route("/select-example", methods=["POST"])
def select_example() -> 'html':
    regions = []
    with(open("static/regionKeys.json", 'r')) as file:
        unsorted = json.load(file)["daten"]
        regions = sorted(unsorted, key=lambda unsorted: unsorted[1])
    return render_template("select-example.html",
                           title="Corona nach Gebieten",
                           post_url="/result",
                           regions=regions)


@app.route("/result", methods=["POST"])
def get_covid_ticker() -> 'html':
    selected_region_id =  request.form["selected_region"]
    # Die Letzten 7 Stellen müssen dabei mit "0000000" ersetzt werden, weil die Daten nur auf Kreisebene bereitgestellt werden.
    replacementStr = '0000000'
    shortened_id = selected_region_id[:-len(replacementStr)] + replacementStr
    url = baseUrl.format(shortened_id)
    response = requests.get(url)
    json = response.json()
    headline = json["level"]["headline"]
    incicdence = json["level"]["range"]
    return render_template("result.html",
                           title=headline,
                           ticker=incicdence)


if __name__ == "__main__":
    app.run(debug=True)
