import plotly.express as px

if __name__ == "__main__":
    labels = ['One','Two','Three']
    value =  [10,50,100]
    fig = px.bar(x=labels,y=value, height=400, width=500)
    fig.show()