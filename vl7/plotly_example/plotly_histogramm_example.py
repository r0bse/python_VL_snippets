import plotly.express as px
import pandas as pd

covid_data = pd.read_csv('flask/static/covid_berlin.csv',
                         sep=';',
                         decimal=',',
                         quotechar="'",
                         encoding="UTF-8")

fig = px.histogram(covid_data, x='neue_faelle')
fig.show()