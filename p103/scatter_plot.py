import pandas as pd
import plotly.express as px

cd = pd.read_csv("data.csv")

fig = px.scatter (cd,x="date",y="cases",color="country")
fig.show()