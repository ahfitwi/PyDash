#******************************************************************************
# Dash App Skeleton
#******************************************************************************
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ahf1="""
Created on Wed Jun 24 22:42:42 2020

@author: alem fitwi
"""
#******************************************************************************
#******************************************************************************
# 1. Import all necessary libraries and packages 
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
from utils import app_layout
from utils import df_ver


#******************************************************************************
#******************************************************************************
# 2. System and Python Information
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
#******************************************************************************
# 3. System and Python Information
#******************************************************************************


#******************************************************************************
#******************************************************************************
# 4. The Dashboard
#***************************
#******************************************************************************

app = dash.Dash(__name__)
auth = dash_auth.BasicAuth(app,VALID_USERNAME_PASSWORD_PAIRS)
app.layout = app_layout

#******************************************************************************
#******************************************************************************
#                            ~End~
#******************************************************************************
 
