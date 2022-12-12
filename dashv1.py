#******************************************************************************
# Dash App Skeleton
#******************************************************************************
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 22:22:17 2022
@author: alem fitwi
"""
#******************************************************************************
### Standard, Third-party, and user-defined packages
#******************************************************************************
#Files, I/O, regular expressions and OS
import os
import io
import shutil
import glob
import sys
import re
#*************************************
# Data Structures
import numpy as np
import pandas as pd
#*************************************
# Database
import sqlite3
from sqlalchemy import create_engine
from IPython.display import Image
import base64
#*************************************
# Time and Dates
import time
from datetime import datetime as dtt
from datetime import date,timedelta
#*************************************
# Dash and Dash Components
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output, State
import dash_table as dt
import dash_daq as daq
import dash_auth
#*************************************
# Otherss
import random
import warnings
warnings.simplefilter("ignore")
import platform
import flask
import urllib
from math import ceil, floor
import getpass
import socket
#import netifaces
import re, uuid
import multiprocessing

#*************************************
# user defined

#******************************************************************************
# System and Python Information
#******************************************************************************
# Check your systems and version of your environment
def def_ver():
    df_ver1 = pd.DataFrame({'System Attribute': ['Date', 'User Name', 'System', 
                       'Node', 'Release','Version', 'Machine', 'Processor', 
                       'Python Version', '# of CPU Cores'], 
                       'Description':[dtt.now().strftime("%Y-%B-%d %H:%M:%S"),
                        platform.uname(), platform.system(),
                        platform.node(),platform.release(), platform.version(),
                        platform.machine(), platform.processor(),
                        platform.python_version(), 
                        multiprocessing.cpu_count()]
                       })
    return df_ver1

#******************************************************************************
# 4. The Dashboard
#***************************
#******************************************************************************
# Initialise the dash app
app = dash.Dash(__name__)
#auth = dash_auth.BasicAuth(app,VALID_USERNAME_PASSWORD_PAIRS)
#******************************************************************************
### app.html function
#******************************************************************************
#-----------------------------------------------------------------------------
#~START
#-----------------------------------------------------------------------------
def serve_layout():
    return html.Div([
            #-----------------------------------------------------
            html.Div([
                 html.A([
                      html.Img(src=encode_image(image_file),
                               style={'width':'100%'},)])]),
            #-----------------------------------------------------


            #-----------------------------------------------------
            html.Hr(),  # add a horizontal rule
            html.Hr(),  # add a horizontal rule
            #-----------------------------------------------------
            #-----------------------------------------------------
            #Section: Header and Date
            #-----------------------------------------------------
            html.Div([
                    html.H1(children='COURSES DASHBOARD',
                            style={'textAlign': 'center','fontWeight':'bold',
                                      'color':colors['txt1']}),

                    html.H1(dtt.today().strftime('%Y-%m-%d'),
                            dtt.today().strftime('%H:%M:%S'),
                            style={'opacity': '1','color': 'black',
                                   'fontWeight':'bold', 'fontSize': 40,
                                   'textAlign' : 'right',
                                   'margin-right': '10px'}),
                   ], style ={'background-color':colors['bgd2']}),
	        # End of header
            #-----------------------------------------------------

            #-----------------------------------------------------
            html.Hr(),  # add a horizontal rule
            html.Hr(),  # add a horizontal rule
            #-----------------------------------------------------


            #-----------------------------------------------------
            #Section: Dash update: around right top region
            #-----------------------------------------------------
            html.Div([
             html.Div([
               html.Div([
                html.Button('Input, Insert and Query Data (New)', id='submit-val', n_clicks=0,
                style = {'height': '220px','width': '500px','fontSize': 20,
                         'fontWeight':'bold','textAlign': 'center',
                         'margin-left': '250px','border': '10px solid green'}),
                 html.Div(id='container-button-basic')
                 ], className="row"),

                html.Div([
                  html.Div(id='update_status')
                         ],className="row"), # , style={'color':colors['txt3'],
                                              #'textAlign' : 'left', 'margin-left': '250px'}

                ], className="five columns"),

                html.Div([
                 html.Div([
                 html.Button('Update Table Records (Existing)', id='submit-val2', n_clicks=0,
                  style = {'height': '220px','width': '500px','fontSize': 20,
                         'fontWeight':'bold','textAlign': 'center',
                         'margin-left': '350px','border': '10px solid red'}),
                         html.Div(id='container-button-basic2')
                   ],className="row"),
                html.Div([
                    html.Div(id="replace_status")
                ], className="row"),
                html.Div([
                    html.Div(id="error_status")
                ], className="row"),

                ], className="five columns"),

                ], className="row",
                   style={'border': '1px solid white',
                             'margin-left': '150px',
                             'margin-right': '50px',
                             'margin-top': '20px',
                             'margin-bottom': '20px'}),

	        # End of dash update
            #-----------------------------------------------------
            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),
            #-----------------------------------------------------
            #-----------------------------------------------------
            # Section: Links to Data Sources
            #-----------------------------------------------------
            html.Div([
                html.Div([
                html.Div([
                    html.Div([
                            html.H1(children='Links to Data Sources',
                                    style={'color':colors['txt3']}),
                           ], className="four columns"),

                    html.Div([
                        dcc.Markdown('''
            > [Contact_Constant](https://www.constantcontact.com/account-home).
                               '''),
                        dcc.Markdown('''
            > [MyCourses_Login](https://cas.cc.binghamton.edu/cas/login).
                                        '''),
                              ], className="two columns"),

                    html.Div([
                        html.H4("Number of Courses offered in "+str(yrc)),
                        ], className="four columns"),

                    html.Div([
                       daq.LEDDisplay(id='course-number', value=cyc,
                                      color='blue'),
                       ], className="one columns")

                   ], className="row")
               ],style={'border': '1px solid white',
                         'margin-left': '10px',
                         'margin-right': '5px',
                         'margin-top': '10px',
                         'margin-bottom': '10px'})
             ],style={'border': '1px solid red',
                       'margin-left': '50px',
                       'margin-right': '50px',
                       'margin-top': '20px',
                       'margin-bottom': '20px'}),
            # End of links
            #-----------------------------------------------------


            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),
            #-----------------------------------------------------




#-----------------------------------------------------------------------------
  ])
app.layout = serve_layout
#~END
#-----------------------------------------------------------------------------

#******************************************************************************
# @app.callbacks to add interactive functionalities to the app
#******************************************************************************


#******************************************************************************
# Run the app by adding the server clause
#******************************************************************************
#******************************************************************************
# Run the app
# Add the server clause:
if __name__ == '__main__':
    app.run_server(port = 55555)
    #using public IP Address
    #app.run_server(debug=True, host='0.0.0.0')
    #app.run_server(port = 55555, host='0.0.0.0')
#******************************************************************************
#                  ~End of Program~
#******************************************************************************