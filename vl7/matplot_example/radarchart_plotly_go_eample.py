import pandas as pd
import plotly.graph_objects as go

covid_data = pd.read_csv('flask/static/covid_berlin.csv',
                         sep=';',
                         decimal=',',
                         quotechar="'",
                         encoding="UTF-8")

# parse datetime
covid_data['datum'] = pd.to_datetime(covid_data['datum'])
# parse to specific type
covid_data['rel_veraenderung_der_7_tage_inzidenz'] = covid_data['rel_veraenderung_der_7_tage_inzidenz'].astype(float)
# drop a column
covid_data.drop('id', axis=1, inplace=True)

# manipulate column data
covid_data["todesfaelle"] = [ value/1000 for value in covid_data["todesfaelle"]]
covid_data["neue_faelle"] = [ value/1000 for value in covid_data["neue_faelle"]]
covid_data["genesene"] = [ value/100000 for value in covid_data["genesene"]]
covid_data["fallzahl"] = [ value/100000 for value in covid_data["fallzahl"]]

#select date
covid_data = covid_data.query('datum == "2022-08-17" | datum == "2021-08-17"')

#drop unneeded data
covid_data.drop('datum', axis=1, inplace=True)
covid_data.drop('rel_veraenderung_der_7_tage_inzidenz', axis=1, inplace=True)
covid_data.drop('7_tage_inzidenz', axis=1, inplace=True)

header = covid_data.columns
values = covid_data.values

fig = go.Figure()
for data in covid_data.values:
    fig.add_trace(go.Scatterpolar(
        r=data,
        theta=header,
        fill='toself'
    ))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True
        )),
    showlegend=False
)
fig.show()