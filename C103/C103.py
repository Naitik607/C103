import pandas as pd
import plotly.express as px

df = pd.read_csv("F:\F Drive\coding\projects\C103\Copy+of+data+-+data.csv")
fig = px.scatter(df,x = 'date',y = 'cases',color = 'country')
fig.show()