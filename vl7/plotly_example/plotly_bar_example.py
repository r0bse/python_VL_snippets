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

#select date
covid_data = covid_data.query('datum == "2022-08-17" | datum == "2021-08-17"')

print(covid_data)

fig = px.bar(covid_data, x='datum', y='fallzahl')
fig.show()