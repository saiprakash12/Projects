import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input,Output,State
import dash_bootstrap_components as dbc
import numpy 

import pickle

app = dash.Dash(external_stylesheets =[dbc.themes.FLATLY])

server=app.server


form=html.Div([
                    html.H1("Air Quality Index Prediction",style={
                                                                    'textAlign': 'center'
                                                                }
                            ),
                    #dbc.Label("Enter the Values for the below Input Attributes:"),
                    html.Hr(),
                    dbc.FormGroup([
                                    dbc.Label("Average Temperature:",html_for="T",width=2,style={
                                                                                    'padding':'0px 0px 0px 70px',
                                                                                    'font-weight':'bold'
                                                                                }),
                                    dbc.Col(
                                    dbc.Input(id="T", type="number", placeholder="Enter Value"),width=2,
                                    ),
                                    ],row=True,),
                    dbc.FormGroup([
                                    dbc.Label("Maximum Temperature:",html_for="TM",width=2,style={
                                                                                'padding':'0px 0px 0px 70px',
                                                                                'font-weight':'bold'
                                                                                }),
                                    dbc.Col(
                                    dbc.Input(id="TM", type="number", placeholder="Enter Value"),width=2,
                                    ),
                                    ],row=True,),
                    dbc.FormGroup([
                                    dbc.Label("Minimum Temperature:",html_for="Tm",width=2,style={
                                                                                'padding':'0px 0px 0px 70px',
                                                                                'font-weight':'bold'
                                                                                }),
                                    dbc.Col(
                                    dbc.Input(id="Tm", type="number", placeholder="Enter Value"),width=2,
                                    ),
                                    ],row=True,),
                    dbc.FormGroup([
                                    dbc.Label("Atmospheric Pressure at Sea Level:",html_for="SLP",width=2,style={
                                                                                'padding':'0px 0px 0px 70px',
                                                                                'font-weight':'bold'
                                                                                }),
                                    dbc.Col(
                                    dbc.Input(id="SLP", type="number", placeholder="Enter Value"),width=2,
                                    ),
                                    ],row=True,),
                    dbc.FormGroup([
                                    dbc.Label("Average Relative Humidity:",html_for="H",width=2,style={
                                                                                'padding':'0px 0px 0px 70px',
                                                                                'font-weight':'bold'
                                                                                }),
                                    dbc.Col(
                                    dbc.Input(id="H", type="number", placeholder="Enter Value"),width=2,
                                    ),
                                    ],row=True,),
                    dbc.FormGroup([
                                    dbc.Label("Average Visibility:",html_for="VV",width=2,style={
                                                                                'padding':'0px 0px 0px 70px',
                                                                                'font-weight':'bold'
                                                                                }),
                                    dbc.Col(
                                    dbc.Input(id="VV", type="number", placeholder="Enter Value"),width=2,
                                    ),
                                    ],row=True,),
                    dbc.FormGroup([
                                    dbc.Label("Average Wind Speed:",html_for="V",width=2,style={
                                                                                'padding':'0px 0px 0px 70px',
                                                                                'font-weight':'bold'
                                                                                }),
                                    dbc.Col(
                                    dbc.Input(id="V", type="number", placeholder="Enter Value"),width=2,
                                    ),
                                    ],row=True,),
                    dbc.FormGroup([
                                    dbc.Label("Maximum Sustained Wind Speed:",html_for="VM",width=2,style={
                                                                                'padding':'0px 0px 0px 70px',
                                                                                'font-weight':'bold'
                                                                                }),
                                    dbc.Col(
                                    dbc.Input(id="VM", type="number", placeholder="Enter Value"),width=2,
                                    ),
                                    ],row=True,),
                    html.Br(),
                    html.Div([dbc.Button('Submit', id='submit-val', n_clicks=0
                                                                )],style={
                                                                         'padding': '0px 0px 0px 200px',
                                                                        'text-align': 'center',
                                                                        'text-decoration': 'none',
                                                                        'display': 'inline-block',
                                                                        'float':'center'}),
                    html.Hr(),
                    html.Div([dbc.Label('The Predicted Result is:')],style={
                             'padding': '0px 0px 0px 50px',
                             'font-weight': 'bold'}),
                    html.Div(id='PM',style={'padding=left':'50px'}),
                    html.Br(),
                    dcc.Markdown('''Developed by **A.V. Sai Prakash**''',className='text-right text-primary mb-4',style={'padding-right':'50px'})

                    ])

app.layout=html.Div([form])

@app.callback(
Output("PM","children"),
Input("submit-val","n_clicks"),
State("T","value"),
State("TM","value"),
State("Tm","value"),
State("SLP","value"),
State("H","value"),
State("VV","value"),
State("V","value"),
State("VM","value"),

)



def update_output(n_clicks,T,TM,Tm,SLP,H,VV,V,VM):
    if (n_clicks)>0:
        data=[T,TM,Tm,SLP,H,VV,V,VM]
        df=pd.DataFrame([data],columns=['T','TM','Tm','SLP','H','VV','V','VM'])
            #print(df)
        loaded_model=pickle.load(open('Random_Fores_model.pkl','rb'))
        my_prediction=loaded_model.predict(df)
        return my_prediction

if __name__=="__main__":
    print("Air Quality Index Prediciton")
    app.run_server(debug=False,dev_tools_hot_reload_interval=6000)
