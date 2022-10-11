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

fig = px.line(covid_data, x='datum', y='rel_veraenderung_der_7_tage_inzidenz')
#fig = px.area(covid_data, x='datum', y='rel_veraenderung_der_7_tage_inzidenz')

fig.show()