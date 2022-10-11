from random import random

import plotly.express as px
import pandas as pd

covid_data = pd.read_csv('flask/static/covid_berlin.csv',
                         sep=';',
                         decimal=',',
                         quotechar="'",
                         encoding="UTF-8")

# parse to specific type
covid_data['rel_veraenderung_der_7_tage_inzidenz'] = covid_data['rel_veraenderung_der_7_tage_inzidenz'].astype(float)
covid_data['datum'] = pd.to_datetime(covid_data['datum'], infer_datetime_format=True)

fig = px.scatter(covid_data, x="genesene", y="fallzahl") # korrelation und Kausalität
fig = px.scatter(covid_data, x="todesfaelle", y="its_belegung") # nur korrelation

covid_data["random"] = [ random() for value in covid_data["datum"]]
fig = px.scatter(covid_data, x="datum", y="random") # nix

fig.show()