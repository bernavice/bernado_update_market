from dash import Dash, html, dcc
import plotly.express as px
import plotly.graph_objects as px
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import numpy as np

app = Dash(__name__) # criando o seu aplicativo Dash
server = app.server

fig = make_subplots(specs=[[{"secondary_y": True}]])

#Gráfico com todas as premissas
#Gráfico com todas as premissas
#Gráfico com todas as premissas
#Gráfico com todas as premissas

fig.add_trace(
    go.Scatter(x=['data1', 'data2', 'data3'], y=['1000', '1200', '1250'], name="Afluência Brasil (MWm)"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=['data1', 'data2', 'data3'], y=['1000', '1000', '1000'], name="Afluência mlt Brasil (MWm)"),
    secondary_y=False,)

fig.add_trace(
    go.Scatter(x=['data1', 'data2', 'data3'], y=['200', '150', '120'], name="PLD (R$/MWh)"),
    secondary_y=True,)

#Add figure title
fig.update_layout(title_text="PLD (R$/MWh), Geração e Afluência (MWm)", template='plotly')
#Set x-axis title
#fig.update_xaxes(title_text="xaxis title")
#Set y-axes titles
fig.update_yaxes(title_text="<b>Energia</b> (MWm)", secondary_y=False)
fig.update_yaxes(title_text="<b>PLD</b> (R$/MMh)", secondary_y=True)
#fig.show()#(fig, filename="C:\\Users\\Bernardo\\Downloads\\ena_carga_pld.html")
#py.offline.plot(fig, filename="C:\\Users\\Bernardo\\Downloads\\ena_carga_pld.html")

# css
app.layout = html.Div(children=[

    #html.Img(src=r'assets/vale3.png', alt='image', width='650'),

    # html.H1(children='RDH - IPDO - PLD', style={"text-align": "center"}),

    # html.h2(children='''
    #    Dashboard de Vendas em Python
    # '''),

    # html.H3(children="Vendas de cada Produto por Loja"),

    dcc.Graph(id='grafico2', figure=fig),

])

# callbacks


# colocando o seu site (seu dashboard) no ar
if __name__ == '__main__':
    app.run_server(debug=False)