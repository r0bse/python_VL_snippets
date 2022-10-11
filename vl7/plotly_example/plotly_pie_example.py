import plotly.express as px

users = [80, 40, 1000, 300, 50, 80, 10]
os = ['MacOS', 'Chrome', 'Windows', 'Linux', 'Devian', 'Ubuntu', 'Arch Linux']

fig = px.pie(values=users, names=os,
             color_discrete_sequence=px.colors.sequential.RdBu)

fig.update_traces(textposition='outside',
                  textinfo='percent+label+value',
                  marker=dict(line=dict(color='#FFFFFF', width=2)),
                  textfont_size=12)

fig.show()

