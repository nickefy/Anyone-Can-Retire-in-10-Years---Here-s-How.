import pandas as pd

# Standard plotly imports
import plotly as py
import plotly.tools as tls
from plotly.offline import iplot, init_notebook_mode
import plotly.graph_objs as go
import cufflinks

# Using plotly + cufflinks in offline mode
init_notebook_mode(connected=True)
cufflinks.go_offline(connected=True)

df = pd.read_csv("ActualData.csv")
df2 = pd.read_csv("ActualData2.csv")
df3 = pd.read_csv("ActualData3.csv")


data= [
go.Scatter(x=df['Date'], y=df['Expense'],
                mode='lines',
                name='Yearly Expense'),
go.Scatter(x=df['Date'], y=df2['Expense'],
                mode='lines',
                name='Yearly Expense'),
go.Scatter(x=df['Date'], y=df3['Expense'],
                mode='lines',
                name='Yearly Expense'),
go.Scatter(x=df['Date'], y=df['Annual Returns'],
                    mode='lines+markers',
                    name='Annual Returns'),
go.Scatter(x=df['Date'], y=df2['Annual Returns'],
                    mode='lines+markers',
                    name='Annual Returns'),
go.Scatter(x=df['Date'], y=df3['Annual Returns'],
                    mode='lines+markers',
                    name='Annual Returns')]

#defining list_updatemenus
list_updatemenus = [{'label': '50k Income',
  'method': 'update',
  'args': [{'visible': [True, False, False, True, False, False]}, {'title': 'Yearly Expense vs Annual Returns over 10 Years'}]},
 {'label': '30k Income',
  'method': 'update',
  'args': [{'visible': [False, True, False, False, True, False]}, {'title': 'Yearly Expense vs Annual Returns over 10 Years'}]},
  {'label': '100k Income',
  'method': 'update',
  'args': [{'visible': [False, False, True, False, False, True]}, {'title': 'Yearly Expense vs Annual Returns over 10 Years'}]}]

#defining layout
layout=go.Layout(title='Yearly Expense vs Annual Returns over 10 Years',updatemenus=list([dict(buttons= list_updatemenus)]))
#defining figure and plotting
fig = go.Figure(data,layout)
iplot(fig)