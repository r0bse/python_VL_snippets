from flask import Flask, render_template
import pandas as pd
import json, requests
import plotly
import plotly.express as px
from pandas import DataFrame

app = Flask(__name__)

url  = "https://www.berlin.de/lageso/gesundheit/infektionskrankheiten/corona/tabelle-indikatoren-gesamtuebersicht/index.php/index/all.json?q="

@app.route('/')
def index():
    response = requests.request("get", url).json()
    df = DataFrame(response["index"])

    fig = px.bar(df, x='Fruit', y='Amount', color='City', barmode='group')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJSON=graphJSON)


if __name__ == "__main__":

    app.run(debug = True)