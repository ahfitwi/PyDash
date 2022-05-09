# cd /home/alem/Desktop/dash/py_and_db/
#******************************************************************************
#cd /home/alem/Desktop/dash/
#******************************************************************************
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ahf1="""
Created on Wed Jun 24 22:42:42 2020

@author: alem fitwi
"""
ahf2='\nCreated on Wed Jun 24 22:42:42 2020\n\n@author: alem fitwi\n'
#******************************************************************************
#******************************************************************************
# 0. Columns and paths Setting for reporting storing
#******************************************************************************
#******************************************************************************
### 0.1 Columns
#******************************************************************************
# All Course List Columns
allCourses_columns = ['course_name', 'acronym', 'cost_model']
    # Registrants columns: two are missing (Education Level and Country)
registrant_columns1 = ['First Name:','Last Name:','Email Address:','Address 1:',
                          'City:','State:', 'Education Level:', 'Country:',
                          'ZIP Code:', 'Phone:','Company/School:', 'Job Title:',
                          'Department:', 'How did you hear about this course?',
                          'Registration Date', 'Registration Status',
                          'Payment Status','Payment Type','Fee Type',
                          'Promo Code', 'Code Type', 'Discount Percent',
                          'Discount Amount', 'Total Price']
registrant_columns = ['course_id','course_abb','startDate','course_type',
                      'First Name:','Last Name:','Email Address:','Address 1:',
                      'City:','State:', 'Education Level:', 'Country:',
                      'ZIP Code:','Phone:','Company/School:', 'Job Title:',
                      'Department:','How did you hear about this course?',
                      'Registration Date','Registration Status',
                      'Payment Status','Payment Type','Fee Type', 'Promo Code',
                      'Code Type', 'Discount Percent','Discount Amount',
                      'Total Price']
#Grade columns
grade_columns1 =['Last Name', 'First Name', 'Username',
                     'Student ID','Last Access', 'Availability', 'Final Exam']
grade_columns = ['course_id','course_abb','startDate','course_type','Last Name',
                 'First Name', 'Username', 'Student ID','Last Access',
                 'Availability', 'Final Exam', 'Final Grade']
grade_columns3 = ['course_id','Last Name','First Name', 'Username',
                  'Student ID','Last Access','Availability',
                  'Final Exam']
grade_columns4 = grade_columns3+['year']
# Cost-model
cost_columns1 = ['Name', 'Role', 'Pay', 'Type', 'Location']
cost_columns = ['course_id','course_abb','startDate','course_type','Name','Role',
                'Pay','Type','Location']
# Survey
sur_columns1 = ['course_id','course_type','questions','opinion','count']
sur_columns = ['course_id','course_abb','startDate','course_type','questions',
               'opinion','scores','count']

# Others
bunbu_columns = ['course_id','course_type','Fee Type']
city_columns = ['course_id','course_type','City:']
state_columns = ['course_id','course_type','State:']
dept_columns = ['course_id','course_type','Department:']
jt_columns = ['course_id','course_type','job_title']
ctry_columns = ['course_id','course_type','Country:']
edu_columns = ['course_id','course_type','Education Level:']
cpy_columns = ['course_id','course_type','Company/School:']
hw_columns = ['course_id','course_type','How did you hear about this course?']
regdt_coluumns = ['course_id','course_type','Registration Date']
procd_columns = ['course_id','course_type','Promo Code']
demog_columns = ['course_id', 'course_abb','startDate', 'course_type', 'object',
                 'by', 'count']

profit_columns = ['course_id', 'course_abb', 'startDate', 'course_type', 'Name',
                  'Role', 'Pay', 'Type', 'Location','Amount']
psmry_col = ['course_id', 'course_abb','startDate','total_income', 'total_cost',
             'profit', 'profit%'] 
type_col =['Total Income', 'Total Salaries', 'State Fringe', 'Credit Card Fees',
           'Marketing Cost', 'Total Direct Cost', 'RF Overhead Indirect Cost',
           'Total Costs', 'Profit']      

sort_dict = {'Total Income': 'A',
             'percent': 'B',
             'actual': 'C',
             'Total Salaries': "D",
             'State Fringe' : 'E',
             'Credit Card Fees' : 'F',
             'Marketing Cost' : 'G',
             'Total Direct Cost' : 'H',
             'RF Overhead Indirect Cost' : 'I',
             'Total Costs': 'J',
             'Profit': 'K',
             'Profit%': 'L'}
sort_dict2 = {'Total Income': 'A',
             'Total Salaries': "B",
             'State Fringe' : 'C',
             'Credit Card Fees' : 'D',
             'Marketing Cost' : 'E',
             'Total Direct Cost' : 'F',
             'RF Overhead Indirect Cost' : 'G',
             'Total Costs': 'H',
             'Profit': 'I'}
# For the survey data analysis
suvy1_cols1 = ['Timestamp',
 "Participant's Name (Optional)",
 'Contribution to learning [Level of skill/knowledge at start of course]',
 'Contribution to learning [Level of skill/knowledge at end of course]',
 'Contribution to learning [Level of skill/knowledge required to'+
               ' complete the course]',
 'Contribution to learning [Contribution of course to your skill/knowledge]',
 'Skill and responsiveness of the instructors [Instructor  an effective'+
               ' lecturer/demonstrator]',
 'Skill and responsiveness of the instructors [Presentations were clear'
               ' and organized]',
 'Skill and responsiveness of the instructors [Instructor stimulated' +
               ' student interest]',
 'Skill and responsiveness of the instructors [Instructor effectively'+
               ' used time during class periods]',
 'Course content [Learning objectives were clear]',
 'Course content [Course content was organized and well planned]',
 'Course content [Course workload was appropriate]',
 'Course content [Course organized to allow all students to participate fully]',
 'Course content [Hands-on activities aided in your learning]',
 'What aspects of this course were most useful or valuable?',
 'How would you improve this course?',
 'Intention to apply your new knowledge',
 'Satisfaction of Registration/Payment Process [Registration process]',
 'Satisfaction of Registration/Payment Process [Payment process]',
 'Overall Course Satisfaction',
 'Your Likelihood to Recommend this course?',
 'Why or Why Not?']

c_new=['1.1 Level of skill/knowledge at start of course',
       '1.2 Level of skill/knowledge at end of course',
       '1.3 Level of skill/knowledge required to complete the course',
       '1.4 Contribution of course to your skill/knowledge',
       '2.1 Instructor  an effective lecturer/demonstrator',
       '2.2 Presentations were clear and organized',
       '2.3 Instructor stimulated student interest',
       '2.4 Instructor effectively used time during class periods',
       '3.1 Learning objectives were clear',
       '3.2 Course content was organized and well planned',
       '3.3 Course workload was appropriate',
       '3.4 Course organized to allow all students to participate fully',
       '3.5 Hands-on activities aided in your learning',
       '7.1 Registration process',
       '7.2 Payment process',
       '8.1 Overall Course Satisfaction',
       '9.1 Your Likelihood to Recommend this Course?',
       'Keys to Survey Questions 1 through 9.']

colcon =['Contribution to learning',
         'Skill and responsiveness of the instructors',
         'Course content',
         'What aspects of this course were most useful or valuable?',
         'How would you improve this course?',
         'Intention to apply your new knowledge',
         'Satisfaction of Registration',
         'Overall Course Satisfaction',
         'Your Likelihood to Recommend this course?',
         'Why or Why Not?'
        ]

colcon1 = ['Contribution To Learning','Skill and Responsiveness',
           'Course Content', 'Most Useful Aspects',
           'How To Improve This Course', 'Apply New Knowledge',
           'Satisfaction Registration','Overall Course Satisfaction',
           'Likelihood to Recommend','Whyor Why Not']


c1_new =['Level of skill/knowledge at start of course',
         'Level of skill/knowledge at end of course',
         'Level of skill/knowledge required to complete the course',
         'Contribution of course to your skill/knowledge']

c2_new = ['Instructor  an effective lecturer/demonstrator',
          'Presentations were clear and organized',
          'Instructor stimulated student interest',
          'Instructor effectively used time during class periods']
c3_new = ['Learning objectives were clear',
          'Course content was organized and well planned',
          'Course workload was appropriate',
          'Course organized to allow all students to participate fully',
          'Hands-on activities aided in your learning']
c4_new = ['What aspects of this course were most useful or valuable?']
c5_new = ['How would you improve this course?']
c6_new = ['Intention to apply your new knowledge']
c7_new = ['Registration process',
          'Payment process']
c8_new = ['Overall Course Satisfaction']
c9_new = ['Your Likelihood to Recommend this course?']

remarks ={'Excellent':[5], 'Very good':[4], 'Satisfactory':[3],
          'Fair':[2],'Limited':[1],'Strongly disagree':[1],
          'Disagree':[2], 'Neutral':[3], 'Agree':[4], 'Strongly agree':[5],
          'Very Dissatisfied':[1], 'Dissatisfied':[2],
          'Neutral':[3], 'Satisfied':[4], 'Very Satisfied':[5]}

keysvy = ['Excellent', 'Very good', 'Satisfactory', 'Fair', 'Limited',
          'Strongly disagree', 'Disagree', 'Neutral', 'Agree', 'Strongly agree',
           'Very Dissatisfied', 'Dissatisfied', 'Neutral','Satisfied',
           'Very Satisfied']

dest_cols = ['percentage_name','Short_name','update_percent']

#cklst_col = ['course_id', 'year']
cklst_col = ['course_id','year','Registrants','Grades','Surveys','Costs']

colhdh=['course_id','course_abb','startDate','How did you hear about this course?']
colhdh2=['Courses','Start Date','How did you hear about this course?','count']
colregin=['Courses','Start Date','Month/Year','Enrollees', 'Income','Notes']

# Dictionary of Columns
dupcols = {'acl':['course_name', 'acronym'],
           'reg':['course_id','First Name:','Last Name:','Email Address:'],
           'dem':['course_id','object','by','count'],
           'cml':['course_id','Name','Role', 'Pay', 'Type','Location'],
           'gra':['course_id','Last Name', 'First Name'],
           'svy':['course_id','questions', 'opinion', 'count'],
           'set':['percentage_name','Short_name'],
           'pft': profit_columns,
           'pfs': psmry_col}
querycol = {'acl': allCourses_columns, 'reg':registrant_columns,
            'dem': demog_columns, 'cml': cost_columns,
            'gra': grade_columns, 'svy': sur_columns,
            'set': dest_cols, 'pft': profit_columns, 'pfs':psmry_col}
tabmsg = {'set':'Fraction setting','acl':'All Courses List',
          'cml': 'Cost Model File', 'reg':'Registration File',
          'dem':'Demography Dataframe', 'gra':'Grade File',
          'svy':'Survey File', 'pft':'Profit', 'pfs':'Profit Summary'}
tbls  = {'acl':'course_list', 'reg':'registrants',
         'dem':'demography', 'cml':'cost_model',
         'gra':'grade_report', 'svy':'surveys', 'set': 'frac_setting',
         'pft':'profit_by_id', 'pfs': 'profit_by_abb'}

acl_col_db = ['course_name', 'acronym', 'cost_model']
reg_col_db = ['course_id', 'course_abb', 'startDate', 'course_type', 'First_Name', 'Last_Name', 
              'Email_Address', 'Address_1', 'City', 'State', 'Education_Level', 'Country', 
              'ZIP_Code', 'Phone', 'Company_School', 'Job_Title', 'Department', 
              'How_did_you_hear_about_this_course', 'Registration_Date', 'Registration_Status', 
              'Payment_Status', 'Payment_Type', 'Fee_Type', 'Promo_Code', 'Code_Type', 
              'Discount_Percent', 'Discount_Amount', 'Total_Price']
dem_col_db = ['course_id', 'course_abb', 'startDate', 'course_type', 'object', 'by', 'count']
cml_col_db = ['course_id', 'course_abb', 'startDate', 'course_type', 'Name', 'Role', 'Pay', 
              'Type', 'Location']
gra_col_db = ['course_id', 'course_abb', 'startDate', 'course_type', 'Last_Name', 'First_Name', 
              'Username', 'Student_ID', 'Last_Access', 'Availability', 'Final_Exam', 'Final_Grade']
svy_col_db = ['course_id', 'course_abb', 'startDate', 'course_type', 'questions', 'opinion', 
              'scores', 'count']
set_col_db = ['percentage_name', 'Short_name', 'update_percent']
#******************************************************************************
#******************************************************************************
# 1. Import all necessary libraries and packages and Check Versions
    # All of them must be installe in the machine where this pm runs
#******************************************************************************
#******************************************************************************
#******************************************************************************
### 1.1 Packages
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
#*************************************
# Paths and user defined Packages
from sys import path
#Linux OS
"""cpath = "/home/alem/Desktop/dash/"
pathmdl = os.path.join(cpath,'replacemdl/')
rpath = os.path.join(cpath,"Replace/")
apath = os.path.join(cpath,"All_Datasets/")
dbpath = os.path.join(cpath,"py_and_db/DashProjDB.db")
path.append(pathmdl)"""
dtdate = [dtt.now().strftime("%Y-%B-%d %H:%M:%S")]
#------------------------------------------
#Marketing Cost percentage
mrkt = 0.04
#------------------------------------------
#Windows OS
#Windows OS
#cpath="D:\\DashProject02June20\\"
cpath = "/home/alem/Documents/ReadingMaterial/PastProj/Dash-20220327T002430Z-001/Dash/Dash_August03_2021/DashProject02June20"
pathmdl = os.path.join(cpath,"PythonAndSqlite/py_and_db/replacemdl/")
rpath = os.path.join(cpath, "DatasetsAndReprots/Replace/")
apath = os.path.join(cpath,"DatasetsAndReprots/All_Datasets/")
dbpath = os.path.join(cpath,'PythonAndSqlite/py_and_db/DashProjDB.db')
path.append(pathmdl)
#******************************************************************************
### 1.2 Versions Check
#******************************************************************************
# Check your systems and version of your environment
errors = []
def gen_warning():
    print("*******************************************************************")
    print("****************Warning Messages and Instructions!*****************")
    print("*******************************************************************")
    print("*******************************************************************")
    print('User Name:', platform.uname())
    print('System:', platform.system())
    print('Node:', platform.node())
    print('Release:', platform.release())
    print('Version:', platform.version())
    print('Machine:', platform.machine())
    print('Processor:', platform.processor())
    print('Python Version:', platform.python_version())
    print("*******************************************************************")
    ver = platform.python_version()
    if int(ver[0])>=3 and int(ver[2])>=7:
        print("Your Python Version Meets the minimum Requirement!")
        print("***************************************************************")
    else:
        print("Exited!. Your Python Version should be at least 3.7.4!")
        errors.append("Exited!. Your Python Version should be at least 3.7.4!")
        print("***************************************************************")
        exit()
#%%%%
#gen_warning()

#******************************************************************************
### 1.3 Paths Setting
#******************************************************************************
#Windows OS
"""
path_1 = os.path.join(cpath,"DatasetsAndReprots\\InputDatasets\\")
path_2 = os.path.join(cpath,"PythonAndSqlite\\py_and_db\\")
path_3 = os.path.join(cpath,"DatasetsAndReprots\\Reports\\")
path_4 = os.path.join(cpath,"DB_Backups\\")
path_5 = os.path.join(cpath,"DatasetsAndReprots\\All_Datasets\\")
path_6 = os.path.join(cpath,"settings\\")
path_7 = os.path.join(cpath,"DatasetsAndReprots\\DB_Tables\\")
path_8 = os.path.join(cpath,"DatasetsAndReprots\\checklist\\")
path_9 = os.path.join(cpath,"DatasetsAndReprots\\Replace\\")
chklstpath = glob.glob(path_8+'*.xlsx')
chklstpath = chklstpath[0]"""


# Linux OS
path_1 = os.path.join(cpath,"DatasetsAndReprots/InputDatasets/")
path_2 = os.path.join(cpath,"PythonAndSqlite/py_and_db/")
path_3 = os.path.join(cpath,"DatasetsAndReprots/Reports/")
path_4 = os.path.join(cpath,"DB_Backups/")
path_5 = os.path.join(cpath,"DatasetsAndReprots/All_Datasets/")
path_6 = os.path.join(cpath,"settings/")
path_7 = os.path.join(cpath,"DatasetsAndReprots/DB_Tables/")
path_8 = os.path.join(cpath,"DatasetsAndReprots/checklist/")
path_9 = os.path.join(cpath,"DatasetsAndReprots/Replace/")
chklstpath = glob.glob(path_8+'*.xlsx')
chklstpath = chklstpath[0]

def set_paths():
    try:
        df = pd.read_excel(path_6+'pathssetting.xlsx')
        path_dict = dict(zip(df['path_name'].tolist(),
                         df['Actual_path'].tolist()))
    except:
        return False
    else:
        return path_dict
path_dict = set_paths()

def set_path(path_dict):
    if bool(path_dict):
        if bool(path_dict['path_1'])!=False:
            path_1 = os.path.join(cpath,path_dict['path_1'])
        if bool(path_dict['path_2'])!=False:
            path_2 = os.path.join(cpath,path_dict['path_2'])
        if bool(path_dict['path_3'])!=False:
            path_3 = os.path.join(cpath,path_dict['path_3'])
        if bool(path_dict['path_4'])!=False:
            path_4 = os.path.join(cpath,path_dict['path_4'])
        if bool(path_dict['path_5'])!=False:
            path_5 = os.path.join(cpath,path_dict['path_5'])
        if bool(path_dict['path_6'])!=False:
            path_6 = os.path.join(cpath,path_dict['path_6'])
        if bool(path_dict['path_7'])!=False:
            path_7 = os.path.join(cpath,path_dict['path_7'])
        if bool(path_dict['path_8'])!=False:
            path_8 = os.path.join(cpath,path_dict['path_8'])
#set_path(path_dict)
#******************************************************************************
#******************************************************************************
# 2. Handle Input Files and Not Found Exceptions
#******************************************************************************
#******************************************************************************
#filenames: a list grabbed file names
# ids: holds course id of input file, extracted from the filenames
# dfall: dataframe of all_courses_list input files
# dfreg: dataframe of registrants files
# dfgra: dataframe of grade file
# dfcos: dataframe of cost Models
# dfsur: dataframe of survey files
# dfset: dataframe of cost formula setting
def extrat_id(fn, prefix, path):
    #idd = re.sub(path_1, '', fn)
    idd = fn.replace(path, '')
    idd = idd.replace(prefix,'')
    idd = idd.replace('.xlsx','')

    if 'pu_' in idd:
        return idd.replace('pu_',''), 'public'
    else:
        return idd.replace('pr_',''), 'private'

def get_filenames(filenames, path):
    fnall= '';
    fnregistrants =''; idreg = '';
    fngrades = ''; idgra = '';
    fncosts = ''; idcos = '';
    fnevals = ''; ideva = '';

    for fn in filenames:
        if 'all_' in fn:
            fnall = fn
        elif 'registrants_' in fn:
            fnregistrants = fn
            idreg = extrat_id(fn, 'registrants_',path)
        elif 'grades_' in fn:
            fngrades = fn
            idgra = extrat_id(fn, 'grades_',path)
        elif 'costs_' in fn:
            fncosts = fn
            idcos = extrat_id(fn, 'costs_',path)
        elif 'eval_' in fn:
            fnevals = fn
            ideva = extrat_id(fn, 'eval_',path)
    final_names=[fnall, fnregistrants, fngrades, fncosts, fnevals]
    ids = [idreg, idgra, idcos, ideva]
    return final_names, ids

def read_input_files(fname):
    try:
        df = pd.read_excel(fname)
    except:        
        return False
    else:
        return df

#*************************************
def read_dsets(path):
    filenames, ids =get_filenames(glob.glob(path+"*.xlsx"), path)
    dfall = read_input_files(filenames[0])
    if isinstance(dfall, bool)==False:
        try:
            dfall = dfall[allCourses_columns]
        except:
            errors.append('All_course_list has columns mismatch problem!')
    dfreg = read_input_files(filenames[1])
    if isinstance(dfreg, bool)==False:
        try:
            dfreg = dfreg[registrant_columns1]
        except:
            errors.append('Registrants file has columns mismatch problem!')
    dfgra = read_input_files(filenames[2])
    if isinstance(dfgra, bool)==False:
        try:
            dfgra = dfgra[grade_columns1]
        except:
            errors.append('Grades file has columns mismatch problem!')
    dfcos = read_input_files(filenames[3])
    if isinstance(dfcos, bool)==False:
        try:
            dfcos = dfcos[cost_columns1]
        except:
            errors.append('Costs file has columns mismatch problem!')
    dfsur = read_input_files(filenames[4])
    if isinstance(dfsur, bool)==False:
        try:
            dfsur = dfsur[suvy1_cols1]
        except:
            errors.append('Surveys file has columns mismatch problem!')
    dfset = read_input_files(path_6+"fractions.xlsx")
    if isinstance(dfset, bool)==False:
        try:
            dfset = dfset[dest_cols]
        except:
            errors.append('Cost setting file has columns mismatch problem!')
    dfcklst = read_input_files(chklstpath)
    if isinstance(dfcklst, bool)==False:
        try:
            dfcklst = dfcklst[cklst_col]
        except:
            errors.append('Checklist file has columns mismatch problem!')
    return filenames, ids, dfall, dfreg, dfgra, dfcos, dfsur, dfset, dfcklst

#%%%%
#filenames, ids, dfall, dfreg, dfgra, dfcos, dfsur, dfset = read_dsets()
#*************************************
# Write all datasets to the All_Datasets folder
def write_dsets(df, col, filename, msg):

    if  isinstance(df, bool)==False:
        if set(col).issubset(set(list(df.columns))):
            dfw = df[col]
            #dfw.to_excel(path_5+re.sub(path_1, '', filename),index=False)
            dfw.to_excel(path_5+filename.replace(path_1, ''),index=False)

        else:
            print("**********************************************************"
                  +"*********")
            var="Section-2 (write_dsets()): Error! Columns mismatch in "+msg+"!"
            errors.append(var)
            print(var)
            print("***********************************************************"
                  +"********")

    else:
        print("**************************************************************"
               + "*****")
        var = "Section-2 (write_dsets()): No " + msg + " to write to All_Datasets Folder!"
        errors.append(var)
        print(var)
        print("************************************************************"
              + "*******")

def call_writer():
    write_dsets(dfall, allCourses_columns, filenames[0],"All Courses List File")
    write_dsets(dfreg, registrant_columns1, filenames[1], "Registrants File")
    write_dsets(dfgra, grade_columns1, filenames[2], "Grades File")
    write_dsets(dfcos, cost_columns1, filenames[3], "Cost List File")
    write_dsets(dfsur, suvy1_cols1, filenames[4], "Survey File")

#%%%%
#call_writer()
#*************************************
# Empty the Current_5_Datasets folder
def remove_inputfiles():
    try:
        files = glob.glob(path_1+'*.xlsx')
        for f in files:
            os.remove(f)
    except:
        print("************************************************************"
               +"*******")
        print("Section-2 (remove_inputfiles): No files to remove!")
        errors.append("Section-2 (remove_inputfiles): No files to remove!")
        print("************************************************************"
              +"*******")
#%%%%
#remove_inputfiles()
#******************************************************************************
#******************************************************************************
#3. Preprocess Input Files
#******************************************************************************
#******************************************************************************
### 3.1 List of All courses
#******************************************************************************
# File_name: all_courses_list.xlsx
def handle_acl(dfall):
    all_bool1 = str(type(dfall))
    all_bool2 = "<class 'bool'>"
    allf = None
    if all_bool1 != all_bool2:
        try:
            dfall = dfall[allCourses_columns]
            dfall.sort_values(by='course_name', inplace=True)
        except:
            print("**********************************************************"
                   +"*********")
            print("Subsection-3.1: Column names of grade file are inconsistent")
            print("Subsection-3.1: Hence, grade file is not added to DB nor"
                  + " report")
            errors.append("Subsection-3.1: Column names of grade file are"
                          +" inconsistent")
            errors.append("Subsection-3.1: Hence, grade file is not added to "
                          +"DB nor report")
            print("**********************************************************"
                  +"*********")
            allf = False
            return dfall, allf
        else:
            return dfall, allf
    else:
        return dfall, allf

#dfall, allf = handle_acl(dfall)
#******************************************************************************
### 3.2 Registrants
#******************************************************************************
# File_name:registrants_/pu/pr_acronym_yyyy_mm.xlsx
# dfreg, buNonBU, cityreg, statereg, deptreg, jtreg, demog, rev

# Handle promocode
def promo_code(dfreg):
    promlst = dfreg['Promo Code'].tolist()
    numlst = []
    for p in promlst:
        numlst.append(any(map(str.isdigit, str(p))))

    if any(numlst) == True:
        dfreg['temp'] = dfreg['Promo Code'].str.extract('(\d+)')
        dfreg["temp"] = pd.to_numeric(dfreg["temp"])
        dfreg["temp"] = dfreg["temp"].apply(lambda x: x if x>=0 else 'x' )
        cnds1 = [(dfreg["temp"]!='x'),(dfreg["temp"]=='x')]
        vals1 = [dfreg["temp"], dfreg['Total Price']]
        dfreg['Total Price'] = np.select(cnds1,vals1)
        dfreg['Total Price'] = pd.to_numeric(dfreg['Total Price'])
        del dfreg['temp']
    return dfreg

def get_demog(df, cols):
    cols1=[c for c in cols]
    tmp = cols1[2]
    subset = df[cols1]
    cols1[2] = 'object'
    subset.columns = cols1
    subset['by']=tmp
    subset['count']=1
    cols2 = list(subset.columns)
    subset = subset.groupby(cols2[0:4]).sum().reset_index()
    return subset
# Current Course ID
def gen_demography(dfreg):
    ccid1 = None
    reg_bool1 = str(type(dfreg))
    reg_bool2 = "<class 'bool'>"
    regf = None
    if reg_bool1 != reg_bool2:
        try:
            dfreg = promo_code(dfreg)
            dfreg['course_id'] = ids[0][0]
            ccid1 = ids[0][0]
            dfreg['course_type'] = ids[0][1]
            #Demography-By BU and Non-BU
            buNonBU = get_demog(dfreg, bunbu_columns)
            #Demography-By City
            cityreg = get_demog(dfreg, city_columns)
            #Demography-By State
            statereg = get_demog(dfreg, state_columns)
            #Demography-By Dept
            deptreg = get_demog(dfreg, dept_columns)
            #Demography-By Job-Title
            jt = 'Job Title:'
            jtreg = dfreg[['course_id','course_type',jt]]
            jtreg.columns = jt_columns
            jtreg = get_demog(jtreg, jt_columns)
            #Aggregate all demography datasets
            #Demography-By Country
            ctryreg = get_demog(dfreg, ctry_columns)
            #Demography-By Education Level
            edureg = get_demog(dfreg, edu_columns)
            #Demography-By Company/School
            cpyreg = get_demog(dfreg, cpy_columns)
            #Demography-By How Did You Hear About Us
            hwreg = get_demog(dfreg, hw_columns)
            #Demography-By Registration Date
            regdtreg = get_demog(dfreg, regdt_columns)
            #Demography-By Promo Code
            procdreg = get_demog(dfreg, procd_columns)
            #Aggregate all demography datasets
            demog = pd.concat([buNonBU,cityreg,statereg,deptreg,jtreg,
                  ctryreg, edureg, cpyreg, hwreg, regdtreg, procdreg],
                          ignore_index=True)
            
            # Revenue
            rev1 = dfreg[['course_id','course_type','Promo Code','Total Price']]
        except:
            print("**********************************************************"
                  +"*********")
            print("Subsection-3.2: Column names of registrants are "
                  +"inconsistent")
            errors.append("Subsection-3.2: Column names of registrants are "
                  +"inconsistent")
            print("Subsection-3.2: Hence, registrants are not added to "
                  +"DB nor report")
            errors.append("Subsection-3.2: Hence, registrants are not added to"
                  +" DB nor report")
            print("**********************************************************"
                  +"*********")
            demog, rev1, regf = False, False, False
            return demog, rev1, regf, ccid1
        else:
            return demog, rev1, regf, ccid1
    else:
        demog, rev1 = False, False
        return demog, rev1, regf, ccid1
#%%%%
#demog, rev, regf, ccid1 = gen_demography(dfreg)
##******************************************************************************
### 3.3 Grades
#******************************************************************************
# File_name:grades_pu/pr_acronym_yyyy_mm.xlsx
# dfgra
# Current Course ID
def get_grade(dfgra):
    lstr = set(dfgra["Final Exam"].tolist())
    if 'P' in lstr or 'F' in lstr:
        dfgra["Final Exam"]=dfgra["Final Exam"].apply(lambda x:
                    'Passed' if x == 'P' else('Failed'
                    if x == 'F' else('H' if x=='H' else 'NaN')))
        dfgra["Final Grade"] = dfgra["Final Exam"]
    else:
        dfgra['tmp'] = dfgra['Final Exam'].apply(lambda x:
                                                 1000 if x=='H' else x)
        dfgra['tmp'] = dfgra['tmp'].astype('float')
        cnds2 = [((dfgra["tmp"]>=70) & (dfgra["tmp"]<=100)),
                                        (dfgra["tmp"]<70),
                                     (dfgra["tmp"]==1000),
                                (dfgra["tmp"]==pd.np.nan)]
        vals2 = ['Passed', 'Failed', 'H','NaN']
        dfgra['Final Grade'] = np.select(cnds2,vals2)
        #dfgra = dfgra[['course_id', 'Final Exam','Final Grade']]

        cnds3 = [(dfgra["Final Grade"].isin(['Passed'])),
                    (dfgra["Final Grade"].isin(['Failed'])),
                    (dfgra["Final Grade"].isin(['H'])),
                    (~dfgra["Final Grade"].isin(['Passed','Failed','H']))]

        vals3 = ['Passed', 'Failed', 'H','NaN']
        dfgra['Final Grade'] = np.select(cnds3,vals3)
        del dfgra['tmp']
    return dfgra


def gen_grades(dfgra, ids):
    ccid2 = None
    gra_bool1 = str(type(dfgra))
    gra_bool2 = "<class 'bool'>"
    graf = None
    if gra_bool1 != gra_bool2:
        try:
            dfgra['course_id'] = ids[1][0]
            ccid2 = ids[1][0]
            dfgra['course_type'] = ids[1][1]
            dfgra = get_grade(dfgra)
        except:
            print("*********************************************************"
                  +"**********")
            print("Subsection-3.3: Column names/values of grade file are inconsistent")
            errors.append("Subsection-3.3: Column names of grade file are"
                          +" inconsistent")
            print("Subsection-3.3: Hence, grade file is not added to DB nor"
                  +" report")
            errors.append("Subsection-3.3: Hence, grade file is not added to"
                          +" DB nor report")
            print("**********************************************************"
                  +"*********")
            graf = False
            return dfgra, ccid2, graf
        else:
            return dfgra, ccid2, graf
    else:
        return dfgra, ccid2, graf
#%%%%
#dfgra, ccid2, graf = gen_grades(dfgra)
#******************************************************************************
### 3.4 Cost-Models
#******************************************************************************
# costs_pu/pr_acronym_yyyy_mm.xlsx
# dfcos
# Current Course ID
def gen_costModels(dfcos):
    ccid3 = None
    cosf = None
    if isinstance(dfcos, bool)==False:
        try:
            dfcos['course_id'] = ids[2][0]
            ccid3 = ids[2][0]
            dfcos['course_type'] = ids[2][1]
            #dfcos = dfcos[cost_columns]
        except:
            print("**********************************************************"
                   +"*********")
            print("Subsection-3.4: Column names of grade file are inconsistent")
            errors.append("Subsection-3.4: Column names of grade file are"
                          + " inconsistent")
            print("Subsection-3.4: Hence, grade file is not added to DB nor"
                  +" report")
            errors.append("Subsection-3.4: Hence, grade file is not added to"
                          +" DB nor report")
            print("***********************************************************"
                  +"********")
            cosf = False
            return dfcos, ccid3, cosf
        else:
            return dfcos, ccid3, cosf
    return dfcos, ccid3, cosf
#%%%%
#dfcos, ccid3, cosf = gen_costModels(dfcos)
#******************************************************************************
### 3.5 Survey-Data
#******************************************************************************
# Current Course ID
def change_col(df):
    pat_col1 = 'Your Likelihood to Recommend this course?'
    pat_col2 = ' (Would you recommend it to a friend or colleague?)'
    pat_col = pat_col1 + pat_col2
    sur_col_all = list(df.columns)
    for i, col in enumerate(sur_col_all):
        if 'Your Likelihood to Recommend this' in col:
            sur_col_all[i] = pat_col
    df.columns = sur_col_all
    return df

def proc(df,c,i):
    q1c1 = df[[c[i],'count']].groupby(c[i]).sum().reset_index()
    q1c1['x']=c[i]
    q1c1 = q1c1[['x',c[i],'count']]
    q1c1.columns = ['questions','opinion','count']
    return q1c1

def ext_col(df, cn):
    cc = [df.columns[i] for i in range(len(df.columns))
          if cn in df.columns[i]]
    return cc

def gen_toot(dfsur):
    sur1f, ccid4 = None, None
    sur_bool1 = str(type(dfsur))
    sur_bool2 = "<class 'bool'>"
    if sur_bool1 != sur_bool2:
        try:
            ev11 = change_col(dfsur)
            c1, c2 = ext_col(ev11, colcon[0]), ext_col(ev11, colcon[1])
            c3 = ext_col(ev11, colcon[2])
            c4, c5 = ext_col(ev11, colcon[3]), ext_col(ev11, colcon[4])
            c6 = ext_col(ev11, colcon[5])
            c7, c8 = ext_col(ev11, colcon[6]), ext_col(ev11, colcon[7])
            c9 = ext_col(ev11, colcon[8])
            dfsur_cols = c1+c2+c3+c4+c5+c6+c7+c8+c9
            ev11 = ev11[dfsur_cols]

            dfc1, dfc2, dfc3, dfc4 = ev11[c1], ev11[c2], ev11[c3], ev11[c4]
            dfc5, dfc6, dfc7, dfc8 = ev11[c5], ev11[c6], ev11[c7], ev11[c8]
            dfc9 = ev11[c9]

            qpt1 = []
            for cl in list(dfc2.columns):
                if 'Instructor were available and helpful' not in cl:
                    qpt1.append(cl)
            dfc2 = dfc2[qpt1]

            dfc1.columns, dfc2.columns, dfc3.columns = c1_new,c2_new,c3_new
            dfc4.columns, dfc5.columns, dfc6.columns = c4_new,c5_new, c6_new
            dfc7.columns, dfc8.columns, dfc9.columns = c7_new,c8_new, c9_new

            dfc1['count'], dfc2['count'], dfc3['count']=1, 1, 1
            dfc4['count'], dfc5['count'], dfc6['count']=1, 1, 1
            dfc7['count'], dfc8['count'], dfc9['count']=1, 1, 1

            q11,q12,q13,q14 = proc(dfc1,c1_new,0),proc(dfc1,c1_new,1),\
                  proc(dfc1,c1_new,2),proc(dfc1,c1_new,3)
            q21,q22,q23,q24 = proc(dfc2,c2_new,0),proc(dfc2,c2_new,1),\
                  proc(dfc2,c2_new,2),proc(dfc2,c2_new,3)
            q31,q32,q33,q34,q35 = proc(dfc3,c3_new,0),proc(dfc3,c3_new,1),\
            proc(dfc3,c3_new,2),proc(dfc3,c3_new,3), proc(dfc3,c3_new,4)

            q4 = proc(dfc4,c4_new,0)
            q5 = proc(dfc5,c5_new,0)
            q6 = proc(dfc6,c6_new,0)

            q71,q72 = proc(dfc7,c7_new,0), proc(dfc7,c7_new,1)
            q81 = proc(dfc8,c8_new,0)
            q91 = proc(dfc9,c9_new,0)

            dfsur1 = pd.concat([q11,q12,q13,q14,q21,q22,q23,q24,q31,q32,q33,
                            q34,q35,q4,q5,q6,q71,q72,q81,q91],ignore_index=True)
            dfsur1['course_id'] = ids[3][0]
            ccid4 = ids[3][0]
            dfsur1['course_type'] = ids[3][1]
            dfsur1 = dfsur1[sur_columns1]
            cndsvy = [
            (dfsur1['opinion'] == keysvy[0]),(dfsur1['opinion'] == keysvy[1]),
            (dfsur1['opinion'] == keysvy[2]),(dfsur1['opinion'] == keysvy[3]),
            (dfsur1['opinion'] == keysvy[4]),(dfsur1['opinion'] == keysvy[5]),
            (dfsur1['opinion'] == keysvy[6]),(dfsur1['opinion'] == keysvy[7]),
            (dfsur1['opinion'] == keysvy[8]),(dfsur1['opinion'] == keysvy[9]),
            (dfsur1['opinion'] == keysvy[10]),(dfsur1['opinion'] == keysvy[11]),
            (dfsur1['opinion'] == keysvy[12]),(dfsur1['opinion'] == keysvy[13]),
            (dfsur1['opinion'] == keysvy[14])]
            valuesvy = [5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
            dfsur1['scores'] = np.select(cndsvy, valuesvy)
            #dfsur1 = dfsur1[sur_columns]

        except:
            print("***********************************************************"
                  +"********")
            print("Subsection-3.5: Column names of the survey file are "
                  +"inconsistent")
            errors.append("Subsection-3.5: Column names of the survey file"
                          +" are inconsistent")
            print("Subsection-3.5: Hence, the survey file is not added to DB"
                  +" nor report")
            errors.append("Subsection-3.5: Hence, the survey file is not added"
                          +" to DB nor report")
            print("***********************************************************"
                   +"********")
            sur1f, dfsur1 = False, False
            return dfsur1, ccid4, sur1f
        else:
            return dfsur1, ccid4, sur1f
    else:
        dfsur1 = False
        return dfsur1, ccid4, sur1f
#%%%%
#dfsur1, ccid4, sur1f = gen_toot(dfsur)
#******************************************************************************
### 3.6 Add Course Acronym and MM/YYYY¶
#******************************************************************************
# ids = [idreg, idgra, idcos, ideva]
def add_abb_date(dfreg,demog,dfcos,dfgra,dfsur1, ids):
    if isinstance(dfreg, bool)==False:
        dfreg['course_abb'] = ids[0][0].split('_')[0]
        my11=ids[0][0].split('_')
        my12 = my11[1:]
        dfreg['startDate'] = '/'.join(my12[::-1])
        dfreg = dfreg[registrant_columns]
        demog['course_abb'] = ids[0][0].split('_')[0]
        demog['startDate'] = '/'.join(my12[::-1])
        demog = demog[demog_columns]
    if isinstance(dfgra, bool)==False:
        dfgra['course_abb'] = ids[1][0].split('_')[0]
        my31=ids[1][0].split('_')
        my32 = my31[1:]
        dfgra['startDate'] = '/'.join(my32[::-1])
        dfgra = dfgra[grade_columns]
    if isinstance(dfcos, bool)==False:
        dfcos['course_abb'] = ids[2][0].split('_')[0]
        my21=ids[2][0].split('_')
        my22 = my21[1:]
        dfcos['startDate'] = '/'.join(my22[::-1])
        dfcos = dfcos[cost_columns]
    if isinstance(dfsur1, bool)==False:
        dfsur1['course_abb'] = ids[3][0].split('_')[0]
        my41=ids[3][0].split('_')
        my42 = my41[1:]
        dfsur1['startDate'] = '/'.join(my42[::-1])
        dfsur1 = dfsur1[sur_columns]
    return dfreg,demog,dfcos,dfgra,dfsur1

#dfreg,demog,dfcos,dfgra,dfsur1 = \
    #add_abb_date(dfreg,demog,dfcos,dfgra,dfsur1)


#******************************************************************************
#******************************************************************************
# 4. Adding Current files to the Database
#******************************************************************************
#******************************************************************************
### 4.1 Create or update tables in DB
#******************************************************************************
#DB Name:DashprojDB.db
     #Navigate to folder of interest on CLI
     #$ sqlite3 DashprojDB.db
     #sqlite> .databases
     #sqlite> .quit, or
     #create it once using import sqlite3 & con=sqlite3.connect('DashprojDB.db')
# Tables: ['course_list', 'registrants', 'demography', 'cost_model',
#               'grade_report', 'profit', 'surveys']
#------------------------------------------------------------------------------
def check_tables(dbpath):
    table_list, msg = [], ''
    try:
        con = sqlite3.connect(dbpath)
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tab = cursor.fetchall()
        for t in list(tab):
            table_list.append(t[0])
        msg = "DB Tables were grabbed successfully!"
    except sqlite3.Error as error:
        msg = f"Tables fetching failed due to {error}."
    finally:
        if con:
            con.close()
    return table_list, msg
# table_list, ctmsg = check_tables(dpath)
#------------------------------------------------------------------------------
def querydb(dbpath, coldb, colnorm, tblname):
    try:
        tmpcol = [c for c in coldb]
        tmpcol.extend(['modifiedBy', 'MAC', 'hostname', 'Timestamp'])
        engine = create_engine('sqlite:///'+dbpath, echo=False)
        df = pd.DataFrame(engine.execute(f"Select DISTINCT * from {tblname}"),
                     columns=tmpcol)
        df = df[coldb]
        df.columns = colnorm
    except:
        msg = f"{tblname} doesn't exist or columns don't match!"
        return msg
    else:
        return df
#------------------------------------------------------------------------------
def getThoseNotInDB(df, dbtbl, cid):    
    if (isinstance(df, bool)==False)\
        and (isinstance(dbtbl, str)==False):
        try:
            dblst = dbtbl[cid].tolist()            
            inner = df[~df[cid].isin(dblst)]           
        except:
            return False
        else:
            return inner       
    else:
        return False
#------------------------------------------------------------------------------
def getstamps():
    un = getpass.getuser()
    now = dtt.now()
    dt = now.strftime("%m/%d/%Y %H:%M:%S")
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    hn = socket.gethostname()
    return un, mac, hn, dt
#------------------------------------------------------------------------------
def tosqlite(dbpath, df, dbtab, flag, tab_name, tabmsg1,label, mode, cid, coldb):
    error, replaces= [], []
    if mode == 'append':
        df = getThoseNotInDB(df, dbtab, cid)
    if isinstance(df, bool)== False and flag == None:
        try:
            con = sqlite3.connect(dbpath)
            cursor = con.cursor()
            engine = create_engine('sqlite:///'+dbpath, echo=False)
            df.columns = coldb
            un, mac, hn, dt = getstamps()    
            df['modifiedBy'],df['MAC'],df['hostname'],df['Timestamp']=un,mac,hn,dt             
            df.to_sql(tab_name, engine, if_exists=mode, index=False)
            if mode == 'append':
                error.append(f"Section-4: {tabmsg1} was successfully appended to db!")
            if mode == 'replace' and tab_name != 'frac_setting':
                error.append(f"Section-4: {tabmsg1} was successfully replaced in db!")
                replaces.append(tab_name)
            con.commit()
            cursor.close()
        except sqlite3.Error as error:
            error.append(f"{tab_name} wasn't added to DB due to {error}.")
        else:
            error.append(f"{tab_name} was added to DB!")
        finally:
            if con:
                con.close()
    elif flag == False:
        error.append(f"Section-4: Check columns mismatch in {tabmsg1} file!")
    else:
        error.append(f"Section-4: No {tabmsg1} input and nothing was iserted"
               +" to DB or table might be already in DB!")
    return error, replaces
# error, replaces = tosqlite(dbpath, df, dbtab, flag, tab_name, 
#                       tabmsg1, label, mode, cid)
#******************************************************************************
#******************************************************************************
# 5. Backup the Database in the Backup folder
#******************************************************************************
#******************************************************************************
# New Name is given to every backedup DB
# DB_name = DashProjDB_yyyy_month_dd.db
def backupDb(path_4, dbpath):
    try:
        tdy = date.today()
        y = tdy.strftime("%Y")
        m = tdy.strftime("%B")
        d = tdy.strftime("%d")
        db_name = 'DashProjDB_'+y+'_'+m+'_'+d+'.db'        
        shutil.copy(dbpath, path_4)
        path_old = path_4+'DashProjDB.db'
        path_new = path_4 + db_name
        os.rename(r''+path_old,r''+path_new)
        errors.append('Section-5: DB was successfully backed up!')
    except:
        errors.append('Section-5: DB is not backed up because the path'
                     +' is wrong!')

#backupDb(path_4)
#******************************************************************************
#******************************************************************************
# 6. Generate Reports from the db
#******************************************************************************
#******************************************************************************
# Reports: All Courses List, Demography, Grades, Profit Analysis, & Survey
# Convert DB tables to pandas tables
# acl, reg, dem, cml, gra, prof, profsmry, and  svy
#******************************************************************************
### 6.1 Read Relevant Tables from DB
#******************************************************************************
def remove_duplicate(df, col):
    try:
        df.sort_values(col, inplace = True)
        df.drop_duplicates(subset =col, keep = 'first', inplace = True)
    except:
        df = False
    return df

def sqliteTopd(dbpath1, querycol, tabname, dupcol, coldb):    
    df = querydb(dbpath1, coldb, querycol, tabname)  
    if isinstance(df, str)== False:
        df = remove_duplicate(df, dupcol)
        if isinstance(df, bool)== False:
            return df
        else:
            return False
    else:
        return False
   
# Pairing
# [al,  rl,  dl,  cl,  gl,  sl,   fs]
# [acl, reg, dem, cml, gra, svy,  fset]
#******************************************************************************
### 6.2 Cost-Profit Analysis
#******************************************************************************
# Inputs: rev from reg, dfcos from cml, and frac from fset
# Outputs: prof, profsmry
def gen_profit(reg, cml, fset, mrkt):
    tmpprof={'course_id':['xxxyz'],
             'course_abb':[''],
             'startDate':[''],
             'course_type':[''],'Name':[''], 
             'Role':[''], 'Pay':[0],
             'Type':[''],'Location':[''],
             'Amount':[0]}

    prof = pd.DataFrame(tmpprof)
    
    def gen_profall(reg, cml, fset, cid, mrkt):               
        rev = reg[['course_id', 'course_type', 
                       'Registration Status',
                       'Promo Code','Total Price']]
        rev = rev[~rev['Registration Status'].isin(
                          ['Abandoned', 'Cancelled'])]
        rev = rev[rev['course_id']==cid]
        dfcos1 = cml[cml.columns]
        dfcos1 = dfcos1[dfcos1['course_id']==cid]
        if rev.shape[0] != 0 and dfcos1.shape[0]!=0:
            try:
                frac = {}
                fset1 = fset[list(fset.columns)[1:]]
                frac ={k:v for k,v in zip(fset1['Short_name'].tolist(),
                              fset1['update_percent'].tolist())}
                tot_income = rev['Total Price'].sum()
                dfcos1['Amount']=0
                    
                income ={'course_id':[cid],
                         'course_abb':[dfcos1['course_abb'].tolist()[0]],
                         'startDate':[dfcos1['startDate'].tolist()[0]],
                         'course_type':[dfcos1['course_type'].tolist()[0]],
                         'Name':[''], 'Role':[''], 'Pay':[0],
                         'Type':['Total Income'],
                         'Location':['inex'],
                         'Amount':[tot_income]}
                inc = pd.DataFrame(income)
                cost=pd.concat([inc,dfcos1],ignore_index=True)
                int_col =['course_id','course_abb','startDate',
                              'course_type','Name', 'Role', 'Pay','Type',
                              'Location','Amount']
                cost =cost[int_col]
                cost['Amount']=cost['Amount'].fillna(0)
                conditions = [(cost['Type'] == 'percent'),
                          (cost['Type'] == 'actual'),
                          (cost['Type'] == 'Total Income')]
                values = [tot_income*cost['Pay'], cost['Pay'],tot_income]          
                cost['Amount'] = np.select(conditions, values)
                sf_sum1 = cost['Amount'][(cost['Location']=='in') &\
                                 (cost['Role']=='Instructor')].sum()
                sf_sum2 = cost['Amount'][(cost['Location']=='in') &\
                                 (cost['Role']=='TA')].sum()                    
                TI = tot_income
                salaries = cost['Amount'].sum()-TI
                state_fringe = sf_sum1*frac['SFI']+sf_sum2*frac['SFT']
                creditcard = frac['PCCF']*TI
                mrkting = mrkt*tot_income                     
                TDC = salaries + state_fringe + creditcard + mrkting
                RFOIC = 0.25*TDC
                TC = TDC + RFOIC
                profit100 = TI -TC
                profper = round(profit100/TI*100,2)
                dctcost ={
                        'course_id':[cid]*9,
                        'course_abb':[dfcos1['course_abb'].tolist()[0]]*9,
                        'startDate':[dfcos1['startDate'].tolist()[0]]*9,
                        'course_type':[dfcos1['course_type'].tolist()[0]]*9,
                        'Name':['']*9,'Role':['']*9, 'Pay':['']*9,
                        'Type':['Total Salaries', 'State Fringe', 
                                'Credit Card Fees',
                                'Marketing Cost','Total Direct Cost',
                                'RF Overhead Indirect Cost',
                                'Total Costs', 'Profit', 'Profit%'],
                        'Location':['']*9,
                        'Amount': [salaries, state_fringe,
                                   creditcard,
                                   mrkting, TDC,
                                   RFOIC,
                                   TC, profit100, profper]
                    }
                profit=pd.concat([cost,pd.DataFrame(dctcost)],
                                                ignore_index=True)
                    
            except:
                errors.append(f"Subsection-6.2: Check Column"+
                                  f" names & {sys.exc_info()[0]}") 
                print("I am in except", cid)
                return False
            else:
                    return profit.round(2)
        else:
            return False
    
    if isinstance(reg, bool) == False and\
        isinstance(cml, bool) == False and\
        isinstance(fset, bool)==False:
        regid = set(reg['course_id'].tolist())
        cmlid = set(cml['course_id'].tolist())
        interid = list(regid & cmlid)
        for cid in interid:
            profit1 = gen_profall(reg, cml, fset, cid, mrkt)
            if isinstance(profit1, bool)==False:
                prof = pd.concat([prof,profit1],ignore_index=True)
        prof = prof[prof['course_id']!='xxxyz']
        prof = remove_duplicate(prof, profit_columns)
        return prof.round(2)
    else:
        return False  
#prof = gen_profit(reg, cml, fset, mrkt)
#******************************************************************************
### 6.3 Cost-Profit Summary
#******************************************************************************
# Inputs: prof
# Outputs: profsmry
def gen_profsmry(prof):
    tmpsmry={'course_id':['xxxy'],'course_abb':[''],
             'startDate':[''],'total_income':[0],
             'total_cost':[0], 'profit':[0]}

    profsmry = pd.DataFrame(tmpsmry)
    tmpcol = ['course_id', 'course_abb',
              'startDate', 'Type', 'Amount']
    prof1 = prof[tmpcol]
    cidall = set(prof1['course_id'].tolist())
    
    for cid in cidall:
        tmp = prof1[prof1['course_id']==cid]        
        ca = tmp['course_abb'].unique().tolist()
        sd = tmp['startDate'].unique().tolist()
        ti = tmp['Amount'][tmp['Type']=='Total Income'].tolist()
        tc = tmp['Amount'][tmp['Type']=='Total Costs'].tolist()
        pt = tmp['Amount'][tmp['Type']=='Profit'].tolist()
        tmp1 = pd.DataFrame({'course_id':[cid],                             
                             'course_abb' : ca,
                             'startDate' : sd,
                             'total_income': ti, 
                             'total_cost': tc,
                             'profit': pt, 'profit%':[0]})
        profsmry = profsmry.append(tmp1)
        
    profsmry = profsmry[profsmry['course_id']!= 'xxxy']
    profsmry['startDate']= profsmry['startDate'].str.strip()    
    #profsmry = profsmry[profsmry['total_income']!= 0]
    profsmry['profit%']=\
    round(profsmry['profit']/profsmry['total_income']*100,2)
    tmpcol1 = ['course_id', 'course_abb','startDate', 
               'total_income', 'total_cost', 
               'profit', 'profit%']
    return profsmry[tmpcol1]

#profsmry = gen_profsmry(prof)
#******************************************************************************
### 6.4 Report formatting Method
#******************************************************************************
flags = ['acl3', 'acl5','gra','demtd','prof25','demall','svyall','cklst']
def save_fmt_report(df, path, fname, flag):
    allname = path + fname + '.xlsx'
    if flag == 'acl3':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 54)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()
    elif flag == 'acl5':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 54)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 24)
        worksheet1.set_column('E:E', 68)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()
    elif flag == 'gra':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 54)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 18)
        worksheet1.set_column('F:F', 54)
        worksheet1.set_column('G:G', 54)
        worksheet1.set_column('H:H', 40)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()
    elif flag == 'demtd':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 54)
        worksheet1.set_column('B:B', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()
    elif flag == 'prof25':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 54)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()
    elif flag == 'demall':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 18)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 72)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 18)
        worksheet1.set_column('F:F', 18)
        worksheet1.set_column('G:G', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()
    elif flag == 'svyall':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 18)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 54)
        worksheet1.set_column('D:D', 24)
        worksheet1.set_column('E:E', 18)
        worksheet1.set_column('F:F', 18)
        worksheet1.set_column('G:G', 18)
        worksheet1.set_column('H:H', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()
    elif flag == 'pf':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 54)
        worksheet1.set_column('B:B', 24)
        worksheet1.set_column('C:C', 24)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'cklst':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 24)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 18)
        worksheet1.set_column('F:F', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'aus':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 54)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 54)
        worksheet1.set_column('D:D', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'regin':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 54)
        worksheet1.set_column('B:B', 24)
        worksheet1.set_column('C:C', 24)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 18)
        worksheet1.set_column('F:F', 54)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)

        number_rows = len(df.index) + 1
        format1 = workbook.add_format({'bg_color': '#FFFF00'})
        format2 = workbook.add_format({'bg_color': '#FFA500'})
        worksheet1.conditional_format("$A$1:$F$%d" % (number_rows),
                             {"type": "formula",
                              "criteria": '=INDIRECT("C"&ROW())="Subtotal"',
                              "format": format1
                             })
        worksheet1.conditional_format("$A$1:$F$%d" % (number_rows),
                             {"type": "formula",
                              "criteria": '=INDIRECT("C"&ROW())="Grand Total"',
                              "format": format2
                             })
        writer.save()
    elif flag == 'ad':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 18)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 54)
        worksheet1.set_column('D:D', 24)
        worksheet1.set_column('E:E', 18)
        worksheet1.set_column('F:F', 18)
        worksheet1.set_column('G:G', 24)
        worksheet1.set_column('H:H', 18)
        worksheet1.set_column('I:I', 18)
        worksheet1.set_column('J:J', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()
#******************************************************************************
### 6.5 Save DBTables in Excel Format
#******************************************************************************
def save_dbtables(df, path, fname, flag):
    allname = path + fname + '.xlsx'
    if flag == 'course_list':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 54)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'registrants':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 18)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 18)
        worksheet1.set_column('F:F', 18)
        worksheet1.set_column('G:G', 36)
        worksheet1.set_column('H:H', 36)
        worksheet1.set_column('I:I', 36)
        worksheet1.set_column('J:J', 18)
        worksheet1.set_column('K:K', 36)
        worksheet1.set_column('L:L', 18)
        worksheet1.set_column('M:M', 18)
        worksheet1.set_column('N:N', 18)
        worksheet1.set_column('O:O', 54)
        worksheet1.set_column('P:P', 54)
        worksheet1.set_column('Q:Q', 54)
        worksheet1.set_column('R:R', 54)
        worksheet1.set_column('S:S', 36)
        worksheet1.set_column('T:T', 18)
        worksheet1.set_column('U:U', 18)
        worksheet1.set_column('V:V', 18)
        worksheet1.set_column('W:W', 54)
        worksheet1.set_column('X:X', 54)
        worksheet1.set_column('Y:Y', 24)
        worksheet1.set_column('Z:Z', 18)
        worksheet1.set_column('AA:AA', 18)
        worksheet1.set_column('AB:AB', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()


    elif flag == 'grade_report':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 18)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 18)
        worksheet1.set_column('F:F', 18)
        worksheet1.set_column('G:G', 18)
        worksheet1.set_column('H:H', 18)
        worksheet1.set_column('I:I', 18)
        worksheet1.set_column('J:J', 18)
        worksheet1.set_column('K:K', 18)
        worksheet1.set_column('L:L', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'demography':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 18)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 18)
        worksheet1.set_column('F:F', 54)
        worksheet1.set_column('G:G', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'profit_id_by':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 18)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 24)
        worksheet1.set_column('F:F', 24)
        worksheet1.set_column('G:G', 18)
        worksheet1.set_column('H:H', 18)
        worksheet1.set_column('I:I', 18)
        worksheet1.set_column('J:J', 18)        
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'profit_by_abb':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 18)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 18)
        worksheet1.set_column('F:F', 18)
        worksheet1.set_column('G:G', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()


    elif flag == 'surveys':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 18)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 54)
        worksheet1.set_column('F:F', 24)
        worksheet1.set_column('G:G', 18)
        worksheet1.set_column('H:H', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'cost_model':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 18)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 18)
        worksheet1.set_column('E:E', 36)
        worksheet1.set_column('F:F', 18)
        worksheet1.set_column('G:G', 18)
        worksheet1.set_column('H:H', 18)
        worksheet1.set_column('I:I', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'frac_setting':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 24)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()
    elif flag == 'checklist':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 24)
        worksheet1.set_column('B:B', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()
#******************************************************************************
### 6.6 Save additional files in Excel Format
#******************************************************************************
def save_additional(df, path, fname, flag):
    allname = path + fname + '.xlsx'
    if flag == 'bunbuabb':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 90)
        worksheet1.set_column('B:B', 10)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'bunbucid':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 90)
        worksheet1.set_column('B:B', 10)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()


    elif flag == 'profabb':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 36)
        worksheet1.set_column('B:B', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'profcid':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 36)
        worksheet1.set_column('B:B', 18)
        worksheet1.set_column('C:C', 18)
        worksheet1.set_column('D:D', 54)
        worksheet1.set_column('E:E', 18)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()

    elif flag == 'npstat':
        writer = pd.ExcelWriter(allname, engine='xlsxwriter')
        df.to_excel(writer, sheet_name=fname, index=False)
        workbook  = writer.book
        worksheet1 = writer.sheets[fname]
        worksheet1.set_column('A:A', 10)
        worksheet1.set_column('B:B', 10)
        worksheet1.set_column('C:C', 10)
        worksheet1.set_column('D:D', 10)
        worksheet1.set_column('E:E', 10)
        worksheet1.set_column('F:F', 10)
        worksheet1.set_column('G:G', 10)
        worksheet1.set_column('H:H', 10)
        header_format = workbook.add_format({
        'bold': True, 'fg_color': '#D7E4BC','border': 1})
        for col_num, value in enumerate(df.columns.values):
            worksheet1.write(0, col_num, value, header_format)
        writer.save()
#******************************************************************************
### 6.7 today
#******************************************************************************
def get_date():
    today = date.today()
    tday = today.strftime("%d/%m/%Y") # dd/mm/YYYY
    #Current Year and mont
    yrc = today.strftime("%Y") # YYYY
    mhc = today.strftime("%m") # Month
    dyc = today.strftime("%d") # Month
    cr=''
    cr = u"\u00a9"+yrc
    return yrc, mhc, dyc, cr
#yrc, mhc, dyc, cr = get_date()
#******************************************************************************
### 6.8 Checklist
#******************************************************************************
def get_chklst(reg,gra,cml,svy,dfcklst):
    if isinstance(reg, bool) == False:        
        reglst = reg['course_id'].tolist()
    else:
        reglst = []
    if isinstance(gra, bool) == False:        
        gralst = gra['course_id'].tolist()
    else:
        gralst  = []
    if isinstance(cml, bool) == False:        
        cmllst = cml['course_id'].tolist()
    else:
        cmllst = []
    if isinstance(svy, bool) == False:        
        svylst = svy['course_id'].tolist()
    else:
        svylst = []      
    
    if isinstance(dfcklst, bool) == False:
        chklst = dfcklst[['course_id','year',
            'Registrants','Grades','Surveys','Costs']]
        
        chklst['Registrants']=chklst.apply(lambda x:\
               'Yes' if x['course_id'] in reglst else x['Registrants'], axis=1)
        
        chklst['Grades']=chklst.apply(lambda x:\
                      'Yes' if x['course_id'] in gralst else x['Grades'], axis=1)
        chklst['Surveys']=chklst.apply(lambda x:\
                      'Yes' if x['course_id'] in svylst else x['Surveys'], axis=1)
        chklst['Costs']=chklst.apply(lambda x:\
                      'Yes' if x['course_id'] in cmllst else x['Costs'], axis=1)    
        chklst.sort_values(by='course_id',inplace=True)
        chklst = chklst.fillna('No')
    return chklst
#******************************************************************************
### 6.9 Registrants and Income
#******************************************************************************
def gen_regenr(reg,acl):
    enrolreg = reg[reg['Registration Status']=='Registered']
    enrolreg['count'] = 1
    enrcol= ['course_abb','startDate', 'count','Total Price']
    enrolreg = enrolreg [enrcol]
    enrg = enrolreg.groupby(
        ['course_abb','startDate']).sum().reset_index()
    enrg['dates'] = pd.to_datetime(enrg["startDate"],format='%d/%m/%Y')
    enrg['year'] = pd.DatetimeIndex(enrg["dates"]).year
    enrg['mm'] = pd.DatetimeIndex(enrg["dates"]).month
    mdict = {1:'Jan',2:'Feb', 3:'Mar',4:'Apr',
         5:'May', 6:'Jun',7:'Jul',8:'Aug',
         9:'Sep',10:'Oct',11:'Nov',12:'Dec'}
    enrg['month']=enrg['mm'].apply(lambda x: mdict[x])
    enrg['my']=enrg['mm'].astype(str)+'/'+enrg['year'].astype(str)
    aclm = acl[['course_name', 'acronym']]
    aclm.columns = ['course_name', 'course_abb']
    merged = aclm.merge(enrg, on ='course_abb',how='inner')
    merged.sort_values(by=['mm', 'year'], inplace = True)
    merged = merged[['my', 'course_name', "startDate",'dates','year', 'mm',
                 'month', 'count', 'Total Price']]
    container = []
    for label, _df in merged.groupby(['my']):
        _df.loc[f'{label} Subtotal']= _df[['count',
                                    'Total Price']].sum().fillna(' ')
        container.append(_df)
    ergsum = pd.concat(container)
    ergsum.loc['Grand Total'] = merged[['count', 'Total Price']].sum()
    #ergsum = ergsum.fillna('---')
    ergsum['count'] = ergsum['count'].astype(int)
    lstmy = ergsum['my'].tolist()
    lstidx= [k for k in ergsum.index]
    for i in range(len(lstmy)):
        if 'Subtotal' in str(lstidx[i]) or 'Grand Total' in str(lstidx[i]):
            lstmy[i]=lstidx[i]
    ergsum['Month/Year']=lstmy
    ergsum = ergsum[['course_name', 'dates','startDate','Month/Year', 'count',
                     'Total Price']]
    ergsum.columns = ['Courses', 'Start Date', 'startDate','Month/Year',
                      'Enrollees', 'Income']
    ergsum['startDate'] = ergsum['startDate'].fillna(method='ffill')
    ergsum = ergsum.fillna('---')
    ergsum['Notes'] = ''
    ergsum['Month/Year'] = ergsum['Month/Year'].apply(
           lambda x: 'Subtotal' if 'Subtotal' in x\
           else('Grand Total' if 'Grand Total' in x else x))
    return ergsum
#******************************************************************************
#******************************************************************************
# 7. Preparing Data for Creating Dashboard
#******************************************************************************
#******************************************************************************
### 7.1 Final Dasets for dashboard
#******************************************************************************
# [al,  rl,  dl,  cl,  gl,  pl,   psl,      sl]
# [acl, reg, dem, cml, gra, prof, profsmry, svy] 
def dash_sets1(dem, acl):
    if isinstance(dem, bool) == False :
        bnb1= dem[dem['by']=='Fee Type']  
    else:
        bnb1 = False
    if isinstance(acl, bool) == False:
        blank_colns = acl.columns
        acl1 =acl[list(acl.columns)]
        acl1["course_id"]= acl1['acronym']+'_yyyy_mm_dd'
        acl1["course_file_name"]= 'registrants/grades/costs/eval'+\
            '_pu/pr_'+ acl1['acronym']+'_yyyy_mm.xlsx'
    else:
        blank_colns, acl1 = False, False

    blank2 = pd.DataFrame({'A':[4], 'B':[1234],'C':[345],
                       'D':[456],'E':[4567],'F':[123]})
    blank3 = blank2[['A','B']]
    return bnb1, blank_colns, blank2, blank3, acl1
#bnb1, blank_colns, blank2, blank3, acl1 = dash_sets1(dem, acl)

def dash_sets2(svy,reg): 
    if isinstance(svy, bool) == False:
        dsq1 = svy[svy['questions'].isin(c1_new)]
        dsq2 = svy[svy['questions'].isin(c2_new)]
        dsq3 = svy[svy['questions'].isin(c3_new)]
        dsq7 = svy[svy['questions'].isin(c7_new)]
        dsq8 = svy[svy['questions'].isin(c8_new)]
        dsq9 = svy[svy['questions'].isin(c9_new)]
        svyg = svy[list(svy.columns)]
        svyq = svy[list(svy.columns)]
    else:
        dsq1, dsq2, dsq3, dsq7, dsq8, dsq9, svyg, svyq =\
        False, False, False, False, False, False, False, False
    if isinstance(reg, bool) == False:
        cid_list=reg['course_id'].unique().tolist()
        cid_listf = [i for i in cid_list if yrc in i]
        cyc = len(cid_listf)
    else:
        cyc = False
    return dsq1, dsq2, dsq3, dsq7, dsq8, dsq9, svyg, svyq,cyc
#dsq1, dsq2, dsq3, dsq7, dsq8, dsq9, svyg, svyq,cyc = dash_sets2(svy,reg)
#--------------------------------
#How did you hear about us?
def get_hdh(reg, acl):
    if isinstance(reg, bool) == False and isinstance(acl, bool) == False:
        hdhear = reg[colhdh]
        hdhear['count'] = 1
        hdhearg = hdhear.groupby(colhdh).sum().reset_index()
        aclhdh = acl[['acronym','course_name']]
        aclhdh.columns = ['course_abb', 'Courses']
        hdhearg1 = aclhdh.merge(hdhearg, on ='course_abb',how='inner')
        #hdhearg1 = hdhearg1[colhdh1]
        return hdhearg1
    else:
        return False
#******************************************************************************
### 7.2 Call all functions 
#******************************************************************************
gen_warning()
path_dict = set_paths()
set_path(path_dict)
filenames, ids, dfall, dfreg, dfgra, dfcos, dfsur, dfset,dfcklst = read_dsets(path_1)
call_writer()
remove_inputfiles()

def proc_dfset(dfset):
    setf = None
    if isinstance(dfset, bool) == False:
        return dfset, setf
    else:
        return False, False
dfset, setf = proc_dfset(dfset)


dfall, allf = handle_acl(dfall)
demog, rev1, regf, ccid1 = gen_demography(dfreg)
dfgra, ccid2, graf = gen_grades(dfgra,ids)
dfcos, ccid3, cosf = gen_costModels(dfcos)
#profit, profsumry, proff = analyze_costprofit(rev, dfcos, dfset)
dfsur1, ccid4, sur1f = gen_toot(dfsur)

dfreg,demog,dfcos,dfgra,dfsur1 = \
    add_abb_date(dfreg,demog,dfcos,dfgra,dfsur1, ids)

acl1 = querydb(dbpath, acl_col_db, querycol['acl'], tbls['acl'])
reg1 = querydb(dbpath, reg_col_db, querycol['reg'], tbls['reg'])
dem1 = querydb(dbpath, dem_col_db, querycol['dem'], tbls['dem'])
gra1 = querydb(dbpath, gra_col_db, querycol['gra'], tbls['gra'])
cml1 = querydb(dbpath, cml_col_db, querycol['cml'], tbls['cml'])
svy1 = querydb(dbpath, svy_col_db, querycol['svy'], tbls['svy'])
fset1 = querydb(dbpath, dest_cols, querycol['set'], tbls['set'])
#pft1 = querydb(dbpath, querycol['pft'], tbls['pft'])
#pfs1 = querydb(dbpath, querycol['pfs'], tbls['pfs'])

er1, rpc1 = tosqlite(dbpath, dfall, acl1, allf, tbls['acl'],
            tabmsg['acl'], 'acl', 'append', 'acronym', acl_col_db)
er2, rpc2 = tosqlite(dbpath, dfreg, reg1, regf, tbls['reg'],
            tabmsg['reg'],'reg', 'append', 'course_id', reg_col_db)
er3, rpc3 = tosqlite(dbpath, demog, dem1, regf, tbls['dem'],
            tabmsg['dem'], 'dem', 'append', 'course_id', dem_col_db)
er4, rpc4 = tosqlite(dbpath, dfgra, gra1, graf, tbls['gra'],
            tabmsg['gra'], 'gra', 'append', 'course_id', gra_col_db)
er5, rpc5 = tosqlite(dbpath, dfcos, cml1, cosf, tbls['cml'],
            tabmsg['cml'], 'cml', 'append', 'course_id', cml_col_db)
er6, rpc6 = tosqlite(dbpath, dfsur1, svy1, sur1f, tbls['svy'],
            tabmsg['svy'], 'svy', 'append', 'course_id', svy_col_db)
er7, rpc7 = tosqlite(dbpath, dfset, fset1, setf, tbls['set'],
            tabmsg['set'], 'set', 'replace', 'course_id', dest_cols)
errors = er1+er2+er3+er4+er5+er6+er7

table_list, msg = check_tables(dbpath)
backupDb(path_4, dbpath)

acl = sqliteTopd(dbpath, querycol['acl'], 'course_list', dupcols['acl'],
                            acl_col_db)
reg = sqliteTopd(dbpath, querycol['reg'], 'registrants', dupcols['reg'],
                            reg_col_db)
dem = sqliteTopd(dbpath, querycol['dem'], 'demography', dupcols['dem'],
                            dem_col_db)
cml = sqliteTopd(dbpath, querycol['cml'], 'cost_model', dupcols['cml'],
                            cml_col_db)
gra = sqliteTopd(dbpath, querycol['gra'], 'grade_report', dupcols['gra'],
                            gra_col_db)
svy = sqliteTopd(dbpath, querycol['svy'], 'surveys', dupcols['svy'],
                            svy_col_db)
fset = sqliteTopd(dbpath, querycol['set'], 'frac_setting', dupcols['set'],
                            dest_cols) 

#prof = pd.DataFrame(tmpprof)
prof = gen_profit(reg, cml, fset, mrkt)
#profsmry = pd.DataFrame(tmpsmry)
profsmry = gen_profsmry(prof)

yrc, mhc, dyc, cr = get_date()
bnb1, blank_colns, blank2, blank3, acl1 = dash_sets1(dem, acl)
dsq1, dsq2, dsq3, dsq7, dsq8, dsq9, svyg,svyq, cyc = dash_sets2(svy,reg)
chklstv1 = get_chklst(reg,gra,cml,svy,dfcklst)
hdhhearg = get_hdh(reg, acl)
if isinstance(reg, bool) == False and isinstance(acl, bool) == False:
    regincome = gen_regenr(reg,acl)
else:
    regincome = False

def gen_cnt(reg, gra, svy,cml):
    rc1=reg['course_id'].unique().tolist()
    rc1 = [i for i in rc1 if yrc in i]
    gc1=gra['course_id'].unique().tolist()
    gc1 = [i for i in gc1 if yrc in i]
    sc1=svy['course_id'].unique().tolist()
    sc1 = [i for i in sc1 if yrc in i]
    cc1=cml['course_id'].unique().tolist()
    cc1 = [i for i in cc1 if yrc in i]
    rc1,gc1,sc1,cc1 = len(rc1),len(gc1),len(sc1),len(cc1),
    return rc1,gc1,sc1,cc1
rc1,gc1,sc1,cc1 = gen_cnt(reg, gra, svy,cml)  

boollist = [isinstance(acl, bool), isinstance(reg, bool), isinstance(cml, bool),
   isinstance(dem, bool), isinstance(gra, bool), isinstance(svy, bool),
   isinstance(fset, bool)]
if all(boollist) == True:
    errors.append('Section-4: No Table in DB, it is empty!')
#******************************************************************************
### 7.3 List of dictionaries for Dropdown options and defaults
#******************************************************************************
# Static Vars
default_dept, default_top5 = 'None', 'None'
default_course_id2 = 'None'
default_bu = 'None'
default_bu_id = 'None'
default_cAbb = None
default_cIDr = None
default_By = None
default_cihdh = None
default_abhdh = None
profc = ['Name', 'Role', 'Pay', 'Type', 'Amount']
prof_cl=[{"name": i, "id": i} for i in profc]
default_cisvy = None
default_absvy = None
vls= [i for i in range(1,10)]
qnc = ['questions', 'qnum', 'opinion', 'scores', 'count']
# 'course_id', 'course_abb', 'startDate', 'course_type',
qnc1 = ['course_id', 'course_abb', 'startDate', 'course_type',
         'questions', 'qnum', 'opinion', 'scores', 'count']
default_qn = None
default_pc = 'None'

def get_options(df,colstr):
    opts = []
    for x in df[colstr].unique():
        opts.append({'label':str(x),'value':x})
    return opts

# Dynamic Vars
courseID_options = get_options(reg,'course_id')
buoption =  get_options(bnb1, 'course_abb')
buoption_id  = get_options(bnb1, 'course_id')
cAbb_options = get_options(dem, 'course_abb')
cAbb_options.append({'label':str(None),'value':None})
cIDr_options = get_options(dem, 'course_id')
dept_ids, top5_ids= cIDr_options,cIDr_options
cIDr_options.append({'label':str(None),'value':None})
top5_ids.append([{'label':'None','value':'None'}])

By_options = get_options(dem, 'by')
By_options.append({'label':str(None),'value':None})

demcrs = get_options(dem, 'course_abb')
demcrs.append({'label':'All','value':"All"})
default_dcrs = "All"

demid = get_options(dem, 'course_id')
demid.append({'label':str(None),'value':None})
default_demid = None

pc_options = get_options(prof, 'course_id')
pc_options.append([{'label':'None','value':'None'}])

cisvy = get_options(svyg,'course_id')
cisvy.append({'label':str(None),'value':None})
absvy = get_options(svyg,'course_abb')
absvy.append({'label':str(None),'value':None})

abhdh = get_options(hdhhearg,'course_abb')
abhdh.append({'label':str(None),'value':None})
cihdh = get_options(hdhhearg,'course_id')
cihdh.append({'label':str(None),'value':None})

cns = [(svyq['questions'].isin(c1_new)),(svyq['questions'].isin(c2_new)),
       (svyq['questions'].isin(c3_new)),(svyq['questions'].isin(c4_new)),
       (svyq['questions'].isin(c5_new)),(svyq['questions'].isin(c6_new)),
       (svyq['questions'].isin(c7_new)),(svyq['questions'].isin(c8_new)),
       (svyq['questions'].isin(c9_new))]
svyq['qnum'] = np.select(cns, vls)

cidyn = get_options(chklstv1, 'course_id')
cidyn.append([{'label':'Default','value':int(yrc)}])
cidyndft = None

chklstyroptions = get_options(chklstv1, 'year')
chklstyroptions.append([{'label':'Default','value':int(yrc)}])
defaultcklstyr = int(yrc)


regyn = get_options(chklstv1, 'Registrants')
regyn.append([{'label':'Default','value':None}])
regyndft = None


grayn = get_options(chklstv1, 'Grades')
grayn.append([{'label':'Default','value': None}])
grayndft = None

svyyn = get_options(chklstv1, 'Surveys')
svyyn.append([{'label':'Default','value': None}])
svyyndft = None

cmlyn = get_options(chklstv1, 'Costs')
cmlyn.append([{'label':'Default','value': None}])
cmlyndft = None


chklstcid  = get_options(chklstv1, 'course_id')
chklstcid.append([{'label':'Default','value':None}])
chklstciddefault = None


chklstcid  = get_options(chklstv1, 'course_id')
chklstcid.append([{'label':'Default','value':'None'}])
chklstciddefault = 'None'

#qn_options = get_options(svyq, 'qnum')
#qn_options.append({'label':str(None),'value':None})

pc_id = get_options(prof, 'course_abb')
npsab_options = get_options(svyq, 'course_abb')
npsab_options.append({'label':str(None),'value':None})
npsid_options = get_options(svyq, 'course_id')
npsid_options.append({'label':str(None),'value':None})
#npsqn_options = get_options(svyq, 'qnum')
#npsqn_options.append({'label':str(None),'value':None})

qnlst = {'1. Contribution To Learning':1, '2. Skill and Responsiveness':2,
 '3. Course Content':3, '4. Useful aspects of course':4,
 '5. Improving the course':5,'6. Intention to apply your new knowledge':6,
 '7. Satisfaction Registration':7,
 '8. Overall Course Satisfaction':8, '9. Likelihood to Recommend the Course':9,
 str(None):None}

qn_options = []
for x in list(qnlst.keys()):
    qn_options.append({'label':str(x),'value':x})

npsqn_options = []
npslst = {'1. Contribution To Learning':1, '2. Skill and Responsiveness':2,
 '3. Course Content':3, '7. Satisfaction Registration':7,
 '8. Overall Course Satisfaction':8, str(None):None, None:None}
for x in list(npslst.keys()):
    npsqn_options.append({'label':str(x),'value':x})
#npsqn_options.append({'label':str(None),'value':None})
#******************************************************************************
### 7.4 columns and heading strings
#******************************************************************************
#Profit Tables
var1 = 'Summary of a course in a single offer '
var2 = '(Select a course by a course_id)'
var3='(Select the right combinations: Acronym & Dates& By or ID & By or Dates)'
cdc1 = ['course_id', 'course_abb', 'startDate', 'course_type',
         'object', 'by', 'count']
            #'course_id', 'course_abb', 'startDate', 'course_type',
cdc2 = ['object', 'by', 'count']
pie = 'Select a course_id to display a Pie-Chart:'
tab = "Select Dates to display Count of Trainees by Departments"
mf_col = ['course_name', 'Enrolled', 'Submitted', 'Passed', 'Failed',
   'Passing rate of submitted', 'Passing rate of enrolled',
   'Submission rate']
pc_col = ['course_name','total_income','total_cost','profit','profit%']
prof5c = ['Name', 'Role', 'Pay', 'Type', 'Amount']
dpts=['Binghamton University Students and SUNY Students (must be matriculated)']
dptc = ['Department', 'Count']
npsat = "Statistics and Net Promoter Score (NPS) of a course "
npsat = npsat + "(Statistics for 1, 2, 3, 7, 8, & NPS for 9)."
keysc = ['Count', 'Mean', 'STD', 'MIN', '25%', '50%', '75%', 'MAX']
nbmsg = 'Columns (names, numbers, and orders in the case of a Survey File)'
nbmsg = nbmsg + ' and data must be 100% consistent!'

gracol = ['course_abb', 'startDate', 'Last Name','First Name', 'Final Exam',
 'Final Grade']
regcol = ['course_id', 'First Name:','Last Name:', 'Email Address:',
'Registration Date',  'Total Price']

lname_dwn = get_options(reg, 'Last Name:')
lname_dwn.append({'label':str(None),'value':None})
pfcol = ['course_name','Avg_of_passed Trainees', 'Avg_of_failed Trainees']
ckstr = 'Course Offerings Check List (R = Registrants, G = Grades, '
ckstr = ckstr + 'S = Surveys, & C = Costs in current year)'
#*************************************
### 7.5 Values for Dash settings
# https://www.webucator.com/blog/2015/03/python-color-constants-module/
colors = {'bgd1': '#111111','bgd2':'#CAFF70','txt1': '#8B0A50',
           'txt2':'#BF3EFF', 'txt3':'#2F4F4F', 'blue':'#0000FF'}

image_file = "./stylesFigs/ce.png"
def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

PAGE_SIZE, PAGE_SIZE20 = 10, 25
PAGE_SIZEacl = 10

if ahf1 != ahf2:
    print("*******************************************************************")
    print("Program was changed or tampered! Please use the original copy!")
    errors.append("Program was changed or tampered! Please use the original "
                  + "copy!")
    print("*******************************************************************")
    exit()
if all(table_list) == False:
    print("*******************************************************************")
    print("Database is incomplete! Program has been exited!")
    errors.append("Database is incomplete! Program has been exited!")
    print("Some or all sqlite tables are missing! Please check!")
    errors.append("Some or all sqlite tables are missing! Please check!")
    print("*******************************************************************")
    exit()
print("*******************************************************************")
link = "http://127.0.0.1:55555/"
print("Please press control and click the following link to open the Dash!")
print(link, "at the bottom of this screen!")
print("To stop or quit it, please press CTRL + C")
print("*******************************************************************")
dfer = pd.DataFrame(errors, columns=['Input, Insert, and Query Status'])
#er_col = get_options(dfer,'Warnings_Error_Messages')
dbdwn = []
for x in table_list:
    dbdwn.append({'label':str(x),'value':x})

#******************************************************************************
# Authentication
#******************************************************************************
def queryup(dbpath, tblname = 'auth_tbl'):
    try:
        tmpcol = ["Username", "Password"]
        tmpcol.extend(['modifiedBy', 'MAC', 'hostname', 'Timestamp'])
        engine = create_engine('sqlite:///'+dbpath, echo=False)
        df = pd.DataFrame(engine.execute(f"Select DISTINCT * from {tblname}"),
                     columns=tmpcol)
        df = df[["Username", "Password"]]       
    except:
        msg = f"{tblname} doesn't exist or columns don't match!"
        return msg
    else:
        un = df["Username"].tolist()
        pw = df["Password"].tolist()
        VALID_USERNAME_PASSWORD_PAIRS = {}
        for k,v in zip(un,pw):
            VALID_USERNAME_PASSWORD_PAIRS[k] = v
        return VALID_USERNAME_PASSWORD_PAIRS
VALID_USERNAME_PASSWORD_PAIRS = queryup(dbpath, tblname = 'auth_tbl')
#******************************************************************************
#@startofapp
#******************************************************************************
#******************************************************************************
# 8. Create the Dashboard
#******************************************************************************
#******************************************************************************
#*************************************
# 8.0 app.html function
#*************************************
# 8.1 Initialise the dash app
app = dash.Dash(__name__)
auth = dash_auth.BasicAuth(app,VALID_USERNAME_PASSWORD_PAIRS)
#*************************************
# 8.2 Define the app and the Dashboard Layout
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


            #-----------------------------------------------------
            # Section: Checklist
            #-----------------------------------------------------
            html.Div([
                html.H1(children='Check List',
                         style={'color':colors['txt3'],
                                 'margin-left': '10px',
                                 'margin-top': '10px'}),
                html.Div([
                    html.Div([
            #-----------------------------------------------------
            # Beginning of Check List
            #-----------------------------------------------------
                        html.Div([
                            html.H4(
                            children=ckstr,
                            style={'color':colors['txt3'],
                                    'margin-left': '10px',
                                    'margin-top': '10px'}),
                            #---------------------------------------------------
                            html.Hr(),
                            #---------------------------------------------------
                            #---------------------------------------------------
                            #Start of checklist summary
                            html.Div([
                            html.Div([
                            #---------------------------------------------------
                            html.Div([
                                    html.Div([
                                        html.H4("R:"),
                                        ], className="one columns"),

                                    html.Div([
                                       daq.LEDDisplay(id='reg1', value=rc1,
                                                      color='red'),
                                       ], className="one columns"),
                                    html.Div([
                                        html.H4("   G:"),
                                        ], className="one columns"),

                                    html.Div([
                                       daq.LEDDisplay(id='gra1', value=gc1,
                                                      color='brown'),
                                       ], className="one columns"),
                                   html.Div([
                                       html.H4("   S:"),
                                       ], className=" one columns"),

                                   html.Div([
                                      daq.LEDDisplay(id='svy1', value=sc1,
                                                     color='green'),
                                      ], className="one columns"),
                                  html.Div([
                                      html.H4("   C:"),
                                      ], className="one columns"),

                                  html.Div([
                                     daq.LEDDisplay(id='cos1', value=cc1,
                                                    color='black'),
                                     ], className="one columns"),

                            ], className="row"),
                            #---------------------------------------------------

                               ],style={'border': '1px solid white',
                                         'margin-left': '10px',
                                         'margin-right': '5px',
                                         'margin-top': '10px',
                                         'margin-bottom': '10px'})
                             ],style={'border': '1px solid white',
                                       'margin-left': '500px',
                                       'margin-right': '50px',
                                       'margin-top': '20px',
                                       'margin-bottom': '20px'}),
                            #End of checklist summary
                            #---------------------------------------------------

                           #---------------------------------------------------
                           html.Hr(),
                           #---------------------------------------------------
                           #---------------------------------------------------                          
                            html.Div([

                            html.Div([
                               html.H6(children='Select course_id:',
                                            style={'color':colors['txt3']}),
                                dcc.Dropdown(id='cidpicker',
                                         options=cidyn,
                                         value=cidyndft),
                            ], className="two columns",
                               style={'margin-left': '5px'}),

                            html.Div([
                               html.H6(children='Select a year:',
                                            style={'color':colors['txt3']}),
                                dcc.Dropdown(id='chklst_yr_picker',
                                         options=chklstyroptions,
                                         value=defaultcklstyr),
                            ], className="two columns",
                               style={'margin-left': '5px'}),
                            
                            html.Div([
                               html.H6(children='Reg-Select Yes/No:',
                                            style={'color':colors['txt3']}),
                                dcc.Dropdown(id='regynpicker',
                                         options=regyn,
                                         value=regyndft),
                            ], className="two columns",
                               style={'margin-left': '5px'}),

                            html.Div([
                               html.H6(children='Grade-Select Yes/No:',
                                            style={'color':colors['txt3']}),
                                dcc.Dropdown(id='graynpicker',
                                         options=grayn,
                                         value=grayndft),
                            ], className="two columns",
                               style={'margin-left': '5px'}),

                            html.Div([
                               html.H6(children='Svy-Select Yes/No:',
                                            style={'color':colors['txt3']}),
                                dcc.Dropdown(id='svyynpicker',
                                         options=svyyn,
                                         value=svyyndft),
                            ], className="two columns",
                               style={'margin-left': '5px'}),


                            html.Div([
                               html.H6(children='Cost-Select Yes/No:',
                                            style={'color':colors['txt3']}),
                                dcc.Dropdown(id='cmlynpicker',
                                         options=cmlyn,
                                         value=cmlyndft),
                            ], className="two columns",
                               style={'margin-left': '5px'}),



                            ], className="row"),


                            html.Div([
                                html.Div([
                                    html.Div([
                                        #html.Div(id="update_acl3_table")
                                        html.Div([
                                         dt.DataTable(
                                          id='chklst_table',
                                          columns=[{"name": i,
                                        "id": i} for i in chklstv1.columns],
                                          page_current=0,
                                          page_size=PAGE_SIZE,
                                          page_action='custom',
                                          #data=acl1.to_dict('records'),
                                          style_table={'margin-left': '200x'},
                                          style_header={
                                                'backgroundColor': 'white',
                                                'fontWeight': 'bold',
                                                'font_size': '23px',
                                                'border': '1px solid black'},
                                          style_cell={'textAlign': 'left',
                                                      'whiteSpace':'normal',
                                                      'font_size': '17px'},
                                          style_cell_conditional=[
                                                {'if': {'column_id': 'Region'},
                                                 'textAlign': 'left'}],
                                          style_data={
                                                   'border': '1px solid blue' },
                                          style_data_conditional=[
                                                {'if': {'row_index': 'odd'},
                                        'backgroundColor': 'rgb(248, 248, 248)'
                                          }],
                                          export_format='xlsx',
                                          export_headers='display')
                                        ])
                                        ],className="eleven columns")
                                    ],className="row"),
                                    html.Div([
                               			html.Div([
                               				html.Button('Save',
                                                     id='save_ckl', n_clicks=0),
                                               html.Div(id='con-button-ckl')
                               			], className="three columns"),

                                    html.Div([
                                    html.Div([
                                      html.Div(id='page_counter_ckl')
                                             ],style={'color':colors['txt3'],
                                              'textAlign' : 'center'}),
                                     ], className="three columns"),

                                       html.Div([
                                       html.Div([
                                         html.Div(id='page_shower_ckl')
                                                ],style={'color':colors['txt3'],
                                                 'textAlign' : 'right'}),
                                        ], className="three columns"),

                                      ], className="row"),
                                ],style={'border': '1px solid white',
                                        'margin-left': '10px',
                                        'margin-right': '10px',
                                        'margin-top': '10px',
                                        'margin-bottom': '30px'})
                            ],style={'border': '1px solid green',
                                    'margin-left': '50px',
                                    'margin-right': '50px'}),
                          ],className="row")
                       ],style={'border': '1px solid white',
                             'margin-left': '100px',
                             'margin-right': '10px',
                             'margin-top': '10px',
                             'margin-bottom': '30px'})
                  ],style={'border': '1px solid green',
                         'margin-left': '50px',
                          'margin-right': '50px'}),
            #-----------------------------------------------------
            # End of checklist
            #-----------------------------------------------------


            #-----------------------------------------------------
            # Section: All Courses
            #-----------------------------------------------------
            html.Div([
                html.H1(children='Course List',
                         style={'color':colors['txt3'],
                                 'margin-left': '10px',
                                 'margin-top': '10px'}),
                html.Div([
                    html.Div([
            #-----------------------------------------------------
            # Beginning of all courses-3columns
            #-----------------------------------------------------
                        html.Div([
                            html.H4(
                            children='Course-list without Filename Information',
                            style={'color':colors['txt3'],
                                    'margin-left': '10px',
                                    'margin-top': '10px'}),
                            html.Div([
                                html.Div([
                                    html.Div([
                                        #html.Div(id="update_acl3_table")
                                        html.Div([
                                         dt.DataTable(
                                          id='acl3_table',
                                          columns=[{"name": i,
                                               "id": i} for i in acl.columns],
                                          page_current=0,
                                          page_size=PAGE_SIZE,
                                          page_action='custom',
                                          #data=acl1.to_dict('records'),
                                          style_table={'margin-left': '200x'},
                                          style_header={
                                                'backgroundColor': 'white',
                                                'fontWeight': 'bold',
                                                'font_size': '23px',
                                                'border': '1px solid black'},
                                          style_cell={'textAlign': 'left',
                                                      'whiteSpace':'normal',
                                                      'font_size': '17px'},
                                          style_cell_conditional=[
                                                {'if': {'column_id': 'Region'},
                                                 'textAlign': 'left'}],
                                          style_data={
                                                   'border': '1px solid blue' },
                                          style_data_conditional=[
                                                {'if': {'row_index': 'odd'},
                                        'backgroundColor': 'rgb(248, 248, 248)'
                                          }],
                                          export_format='xlsx',
                                          export_headers='display')
                                        ])
                                        ],className="eleven columns")
                                    ],className="row"),
                                    html.Div([
                            			html.Div([
                            				html.Button('Save',
                                                  id='save_acl1', n_clicks=0),
                                            html.Div(id='container-button-acl1')
                            			], className="three columns"),

                                        html.Div([
                                        html.Div([
                                          html.Div(id='page_counter_acl3')
                                                 ],style={'color':colors['txt3'],
                                                  'textAlign' : 'right'}),
                                        ], className="three columns"),

                                        html.Div([
                                         html.Div([
                                         html.Div(id='page_shower_acl3')
                                                ],style={'color':colors['txt3'],
                                                 'textAlign' : 'right'}),
                                        ], className="three columns"),
                                      ], className="row"),

                                ],style={'border': '1px solid white',
                                        'margin-left': '10px',
                                        'margin-right': '10px',
                                        'margin-top': '10px',
                                        'margin-bottom': '30px'})
                            ],style={'border': '1px solid green',
                                    'margin-left': '50px',
                                    'margin-right': '50px'}),
            #-----------------------------------------------------
            # End of all courses-3columns
            #-----------------------------------------------------
            html.Hr(),
            #-----------------------------------------------------
            # Beginning of all courses-5columns
            #-----------------------------------------------------
                        html.Div([
                            html.H4(
                            children='Course-list with Filename Information',
                            style={'color':colors['txt3'],
                                    'margin-left': '10px',
                                    'margin-top': '10px'}),
                            html.Div([
                                html.Div([
                                    html.Div([
                                        #html.Div(id="update_acl3_table")
                                        html.Div([
                                         dt.DataTable(
                                          id='acl5_table',
                                          columns=[{"name": i,
                                               "id": i} for i in acl1.columns],
                                          page_current=0,
                                          page_size=PAGE_SIZE,
                                          page_action='custom',
                                          #data=acl1.to_dict('records'),
                                          style_table={'margin-left': '200x'},
                                          style_header={
                                                'backgroundColor': 'white',
                                                'fontWeight': 'bold',
                                                'font_size': '23px',
                                                'border': '1px solid black'},
                                          style_cell={'textAlign': 'left',
                                                      'whiteSpace':'normal',
                                                      'font_size': '17px'},
                                          style_cell_conditional=[
                                                {'if': {'column_id': 'Region'},
                                                 'textAlign': 'left'}],
                                          style_data={
                                                'border': '1px solid blue' },
                                          style_data_conditional=[
                                                {'if': {'row_index': 'odd'},
                                        'backgroundColor': 'rgb(248, 248, 248)'
                                          }],
                                          export_format='xlsx',
                                          export_headers='display')
                                        ])
                                        ],className="eleven columns")
                                    ],className="row"),

                                    html.Div([
                            			html.Div([
                            				html.Button('Save',
                                                  id='save_acl5', n_clicks=0),
                                            html.Div(id='container-button-acl5')
                            			], className="three columns"),
                                       html.Div([
                                       html.Div([
                                       html.Div(id='page_counter_acl5')
                                              ],style={'color':colors['txt3'],
                                               'textAlign' : 'center'}),
                                        ], className="three columns"),

                                       html.Div([
                                        html.Div([
                                         html.Div(id='page_shower_acl5')
                                                ],style={'color':colors['txt3'],
                                                 'textAlign' : 'right',
                                                 'margin-right': '140px'}),
                                        ], className="three columns"),
                                    ], className="row"),

                                ],style={'border': '1px solid white',
                                        'margin-left': '10px',
                                        'margin-right': '10px',
                                        'margin-top': '10px',
                                        'margin-bottom': '30px'})
                            ],style={'border': '1px solid green',
                                    'margin-left': '50px',
                                    'margin-right': '50px'}),
            #-----------------------------------------------------
            # End of all courses-5columns
            #-----------------------------------------------------
                    ],className="row")
                ],style={'border': '1px solid white',
                      'margin-left': '100px',
                      'margin-right': '10px',
                      'margin-top': '10px',
                      'margin-bottom': '30px'})
           ],style={'border': '1px solid green',
                  'margin-left': '50px',
                   'margin-right': '50px'}),
            #-----------------------------------------------------
            # End of all courses- Section
            #-----------------------------------------------------


            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),
            #-----------------------------------------------------


            #-----------------------------------------------------
            #Section:Grade Summary
            #-----------------------------------------------------
             html.Div([
              html.H1(children='Grade Summary',
                      style={'color':colors['txt3'],
                              'margin-left': '10px',
                              'margin-top': '10px'}),
              html.Div([
              html.Div([html.H4(children='Grade Barcharts:',
                               style={'color':colors['txt3'],
                              'margin-left': '10px',
                              'margin-top': '10px'}),
              html.Div([
              html.Div([
                html.Div([
                    #Grade Summary Barchart of selected course by course_id
                    html.H6(children='Select a Course_id:',
                                      style={'color':colors['txt3']}),
                    dcc.Dropdown(id='course_id_picker_ggra',
                             options=courseID_options,
                             value=default_course_id2),
                    html.Div(id='output-container-date-picker-range1'),
                    dcc.Graph(id='graph_gra')
                ], className="five columns"),

                html.Div([
                   dt.DataTable(
                       id='tableblkacl',
                       columns=[{"name": i, "id": i} for i in blank3.columns],
                       data=blank3.to_dict('records'),
                       style_header={'backgroundColor': 'white'},
                       style_cell={'backgroundColor': 'white',
                               'color': 'white','border': '0px solid white'})
                  ], className="one columns"),

                html.Div([
                    #Grade Summary Barchart of a course over a priod of time
                    html.H6(
                          children='Select Start and End Dates:',
                                      style={'color':colors['txt3']}),
                    dcc.DatePickerRange(
                        id='my-date-picker-range',
                        min_date_allowed=dtt(2020, 1, 1),
                        max_date_allowed=dtt(2100, 12, 31),
                        initial_visible_month=dtt(2020, 1, 1),
                        start_date=dtt(2020, 1, 1).date(),
                        end_date=dtt(int(yrc), 12, 31).date()),
                    html.Div(id='output-container-date-picker-range'),
                    dcc.Graph(id='graph_gra2')
                    ], className="five columns")
               ], className="row"),

               ],style={'border': '1px solid white',
                         'margin-left': '5px',
                         'margin-right': '5px',
                         'margin-top': '5px',
                         'margin-bottom': '5px'})
               ],style={'border': '1px solid black',
                         'margin-left': '10px',
                         'margin-right': '10px',
                         'margin-top': '10px',
                         'margin-bottom': '10px'}),

            html.Hr(),

            #Grade Table By a range of time: start_date to end_date
            html.Div([
            html.Div([html.H4(
                    children='Grade Summary of a Course over a Period of Time:',
                             style={'color':colors['txt3'],
                            'margin-left': '10px',
                            'margin-top': '10px'}),
            #------------------------------------------------
            html.Div([
            html.Div([
                html.Div([
                    dcc.DatePickerRange(
                        id='my-date-picker-range2',
                        min_date_allowed=dtt(2020, 1, 1),
                        max_date_allowed=dtt(2100, 12, 31),
                        initial_visible_month=dtt(2020, 1, 1),
                        start_date=dtt(2020, 1, 1).date(),
                        end_date=dtt(int(yrc), 12, 31).date()),
                    html.Div(id='output-container-date-picker-range2'),
                    html.H6(children='  ',style={'color':colors['txt3']}),
                    html.H6(children='  ',style={'color':colors['txt3']}),
                    #html.Div(id="update_gra_table2"),
                    ], className="row"),

                    html.Div([
                    html.Div([
                    html.Div([
                        dt.DataTable(id='tablegrade',
                            columns=[{"name": i, "id": i} for i in mf_col],
                            page_current=0,
                            page_size=PAGE_SIZE,
                            page_action='custom',
                            style_table={'margin-left': '200x'},
                            style_header={'backgroundColor': 'white',
                                            'fontWeight': 'bold',
                                            'font_size': '23px',
                                            'border': '1px solid black'},
                            style_cell={'textAlign': 'right',
                                        'whiteSpace':'normal',
                                        'font_size': '17px'},
                            style_cell_conditional=[
                                        {'if': {'column_id': 'Region'},
                                                'textAlign': 'left'}],
                            style_data={ 'border': '1px solid blue' },
                            style_data_conditional=[
                                    {'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(248, 248, 248)'}],
                            export_format='xlsx',
                            export_headers='display')
                            ])

                    ], className="eleven columns")
               ], className="row"),

               html.Div([
               html.Div([
               html.Div([
                 html.Div(id='page_counter_gra')
               ],style={'color':colors['txt3'],
                         'textAlign' : 'center'}),
               ], className="five columns"),
               html.Div([
                 html.Div([
                   html.Div(id='page_shower_gra')
                 ],style={'color':colors['txt3'],
                           'textAlign' : 'center'}),
                 ], className="five columns"),
                ], className="row"),

                html.Hr(),

                html.Div([
                html.Div([
                html.Div([
                    dt.DataTable(id='tablegradepf',
                        columns=[{"name": i, "id": i} for i in pfcol],
                        page_current=0,
                        page_size=PAGE_SIZE,
                        page_action='custom',
                        style_table={'margin-left': '200x'},
                        style_header={'backgroundColor': 'white',
                                        'fontWeight': 'bold',
                                        'font_size': '23px',
                                        'border': '1px solid black'},
                        style_cell={'textAlign': 'right',
                                    'whiteSpace':'normal',
                                    'font_size': '17px'},
                        style_cell_conditional=[
                                    {'if': {'column_id': 'Region'},
                                            'textAlign': 'left'}],
                        style_data={ 'border': '1px solid blue' },
                        style_data_conditional=[
                                {'if': {'row_index': 'odd'},
                                'backgroundColor': 'rgb(248, 248, 248)'}],
                        export_format='xlsx',
                        export_headers='display')
                        ])

                ], className="eleven columns")
           ], className="row"),

           html.Div([
             html.Div([
             html.Button('Save',
                       id='save_button_gra', n_clicks=0),
             html.Div(id='container-button-gratpf')
             ], className="three columns"),

             html.Div([
             html.Div([
               html.Div(id='page_counter_grapf')
             ],style={'color':colors['txt3'],
                       'textAlign' : 'center'}),
             ], className="three columns"),


             html.Div([
             html.Div([
               html.Div(id='page_shower_grapf')
             ],style={'color':colors['txt3'],
                       'textAlign' : 'center'}),
             ], className="three columns"),
            ], className="row"),


               ], className="row"),

               ],style={'border': '1px solid white',
                         'margin-top': '10px',
                         'margin-left': '100px',
                         'margin-bottom': '5px'})

                ],style={'border': '1px solid white',
                          'margin-left': '5px',
                          'margin-right': '5px',
                          'margin-top': '5px',
                          'margin-bottom': '5px'})

                ],style={'border': '1px solid black',
                          'margin-left': '10px',
                          'margin-right': '10px',
                          'margin-top': '10px',
                          'margin-bottom': '10px'}),
                #--------------------------------------------
                html.Hr(),
                #----------------------------------------------
                html.Div([
                html.Div([html.H4(
                        children='Summary of Academic Dishonesty:',
                                 style={'color':colors['txt3'],
                                'margin-left': '10px',
                                'margin-top': '10px'}),
                html.Div([
                 html.Div([
                  html.Div([
                   html.Div([
                    dt.DataTable(id='tablead',
                        columns=[{"name": i, "id": i} for i in grade_columns4],
                        page_current=0,
                        page_size=PAGE_SIZE,
                        page_action='custom',
                        style_table={'margin-left': '200x'},
                        style_header={'backgroundColor': 'white',
                                        'fontWeight': 'bold',
                                        'font_size': '23px',
                                        'border': '1px solid black'},
                        style_cell={'textAlign': 'right',
                                    'whiteSpace':'normal',
                                    'font_size': '17px'},
                        style_cell_conditional=[
                                    {'if': {'column_id': 'Region'},
                                            'textAlign': 'left'}],
                        style_data={ 'border': '1px solid blue' },
                        style_data_conditional=[
                                {'if': {'row_index': 'odd'},
                                'backgroundColor': 'rgb(248, 248, 248)'}],
                        export_format='xlsx',
                        export_headers='display')
                        ])

                ], className="eleven columns")
           ], className="row"),

           html.Div([
             html.Div([
             html.Button('Save',
                       id='save_button_ad', n_clicks=0),
             html.Div(id='container-button-ad')
             ], className="three columns"),

             html.Div([
              html.Div([
               html.Div(id='page_counter_ad')
             ],style={'color':colors['txt3'],
                       'textAlign' : 'center'}),
                ], className="three columns"),

             html.Div([
              html.Div([
               html.Div(id='page_shower_ad')
             ],style={'color':colors['txt3'],
                       'textAlign' : 'center'}),
                ], className="three columns"),
              ], className="row"),

               ], className="row"),

               ],style={'border': '1px solid white',
                         'margin-left': '5px',
                         'margin-right': '5px',
                         'margin-top': '5px',
                         'margin-bottom': '5px'}),
                ],style={'border': '1px solid black',
                          'margin-left': '10px',
                          'margin-right': '10px',
                          'margin-top': '10px',
                          'margin-bottom': '10px'}),
               #---------------------------------------------
               ],style={'border': '1px solid white',
                         'margin-left': '100px',
                         'margin-right': '10px',
                         'margin-top': '10px',
                         'margin-bottom': '30px'})
            ],style={'border': '1px solid black',
                      'margin-left': '50px',
                       'margin-right': '50px'}),
            # End of grade summary
            #-----------------------------------------------------


            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),
            #-----------------------------------------------------


            #-----------------------------------------------------
            #Section: Demographic Analysis
            #-----------------------------------------------------
            html.Div([
                html.H1(children='Demographic Analysis',
                                style={'color':colors['txt3'],
                                       'margin-left': '10px',
                                       'margin-top': '10px'}),
                #**********************************
                html.Div([
                  html.Div([
                   html.Div([
                   html.H4(children='BU versus Non-BU Trainees',
                                  style={'color':colors['txt3']}),
                   #-----------------------------------------------------
                   html.Hr(),                   
                   #-----------------------------------------------------
                   html.Div([
                     html.Div([
                        html.H6(children='Pick a course_abb:',
                                  style={'color':colors['txt3']}),
                        dcc.Dropdown(id='course_abb_picker',
                             options=buoption,
                             value=default_bu)
                         ], className="two columns"),

                      html.Div([
                        html.H6(children='Pick a date range:',
                                  style={'color':colors['txt3']}),
                    	dcc.DatePickerRange(
                        id='my-date-picker-range3',
                        min_date_allowed=dtt(2020, 1, 1),
                        max_date_allowed=dtt(2100, 12, 31),
                        initial_visible_month=dtt(2020, 1, 1),
                        start_date=dtt(2020, 1, 1).date(),
                        end_date=dtt(int(yrc), 12, 31).date()),
                        html.Div(id='output-container-date-picker-range3'),
                       ], className="four columns"),

                      html.Div([
                         html.H6(children='Pick a Course_id:',
                                  style={'color':colors['txt3']}),
                         dcc.Dropdown(id='course_cid_picker',
                             options=buoption_id,
                             value=default_bu_id)
                         ], className="five columns"),
                     ], className="row"),

                      #-----------------------------------------------------
                      html.Hr(),
                     #-----------------------------------------------------
                    html.Div([
                         html.Div([
                           html.Div([
                    		html.Div(id="update_bu_table1")
                            ], className="row"),

                            html.Div([
                             html.Div([
                                html.Div([
                                    html.Button('Save',
                                          id='save_bnb', n_clicks=0),
                                    html.Div(id='container-button-bnb')
                                ], className="three columns"),
                                html.Div([
                                html.Div([
                                html.Div(id="counter_budem"),
                                ], style={'color':colors['txt3'],
                                          'textAlign' : 'center'}),
                                ], className="three columns"),
                                ], className="row"),


                               ], className="row"),

                    		], className="six columns"),

                         html.Div([
                            html.Div([
                    		 html.Div(id="update_cid_table")
                            ], className="row"),

                            html.Div([
                                html.Div([
                                    html.Button('Save',
                                          id='save_bnb2', n_clicks=0),
                                    html.Div(id='container-button-bnb2')
                                ], className="two columns"),

                                html.Div([
                                    html.Div(id='counter_cid_table',
                                    style={'color':colors['txt3'],
                                           'alignment': 'left'}),
                                ], className="three columns"),


                               ], className="row"),

                    	 ], className="five columns")

                        ],className="row"),
                    ],style={'border': '1px solid white',
                              'margin-left': '10px',
                              'margin-right': '10px',
                              'margin-top': '10px',
                              'margin-bottom': '10px'})
                   ],style={'border': '1px solid blue',
                             'margin-left': '5px',
                             'margin-right': '5px',
                             'margin-top': '5px',
                             'margin-bottom': '5px'}),

                   #-----------------------------------------------------
                   html.Hr(),
                   #-----------------------------------------------------
                   html.Div([
                    html.Div([
                    html.H4(children='Trainees/Students by Various Categories',
                                      style={'color':colors['txt3']}),
                    #-----------------------------------------------------
                   html.Hr(),                   
                   #-----------------------------------------------------
                    html.Div([
                        html.Div([
                            html.H6(children=pie,
                                              style={'color':colors['txt3']}),
                            dcc.Dropdown(id='course_cid_picker_dept5',
                                         options=dept_ids,
                                         value=default_dept)
                            ],className="six columns"),


                       html.Div([

                        html.Div([
                        html.Div([  
                           html.H6(children= "Select Start and End Dates:",
                                              style={'color':colors['txt3']}),                         
                           dcc.DatePickerRange(
                               id='my-date-picker-rangedept',
                               min_date_allowed=dtt(2020, 1, 1),
                               max_date_allowed=dtt(2100, 12, 31),
                               initial_visible_month=dtt(2020, 1, 1),
                               start_date=dtt(2020, 1, 1).date(),
                               end_date=dtt(int(yrc), 12, 31).date()),
                            html.Div(id='output-container-date-picker-range5'),
                            ],className="four columns"),

                            html.Div([   
                            html.H6(children= "Course(s):",
                                              style={'color':colors['txt3']}),                                             
                            dcc.Dropdown(id='outputDemCrsPicker',
                                         options=demcrs,
                                         value = "All") 
                            ],className="two columns"),

                            ],className="row" ,style={'margin-left': '1px'}),

                           html.Div([  
                           html.Div([   
                            html.H6(children= "Select Course_id:",
                                              style={'color':colors['txt3']}),                                             
                            dcc.Dropdown(id='outputDemIdPicker',
                                         options=demid,
                                         value=default_demid) 
                            ],className="three columns"),

                           html.Div([      
                            html.H6(children= "Select Category:",
                                              style={'color':colors['txt3']}),                                             
                            dcc.Dropdown(id='outputDemCatPicker',
                                         options=By_options,
                                         value=default_By )
                            ],className="three columns"),

                          ],className="row",style={'margin-left': '350px'}), 
                       ],className="six columns"),

                      ],className="row"),
                #-----------------------------------------------------
                html.Hr(),
                #-----------------------------------------------------
                #**************************************
                html.Div([
                  #html.Div([
                    html.Div([
                        dcc.Graph(id='graph_dept')
                        ],className="six columns"),

                    html.Div([
                     html.Div([
                        dt.DataTable(
                            id='datatablewthpaging',
                    columns=[{"name": i, "id": i} for i in ['Categories', 'Count']],
                            page_current=0,
                            page_size=PAGE_SIZE20,
                            page_action='custom',
                            style_table={'margin-left': '200x'},
                            style_header={'backgroundColor': 'white',
                                  'fontWeight': 'bold',
                                  'font_size': '23px',
                                  'border': '1px solid black'},
                            style_cell={'textAlign': 'left',
                                            'whiteSpace':'normal',
                                            'font_size': '17px'},
                            style_cell_conditional=[
                                {'if': {'column_id': 'Region'},
                                 'textAlign': 'left'}],
                            style_data={ 'border': '1px solid blue' },
                            style_data_conditional=[
                                {'if': {'row_index': 'odd'},
                             'backgroundColor': 'rgb(248, 248, 248)'}],
                             export_format='xlsx',
                             export_headers='display')
                          ],className="row"),
                          html.Div([
                            html.Div([
                              html.Button('Save',
                                    id='save_button_dept', n_clicks=0),
                              html.Div(id='container-button-dept'),
                            ], className="two columns"),

                            html.Div([
                            html.Div([
                              html.Div(id='page_counter_dept'),
                            ],className="row",
                              style={'color':colors['txt3'],
                                      'textAlign' : 'center'}),
                              ], className="three columns"),

                          html.Div([
                          html.Div([
                            html.Div(id='page_shower_dept'),
                          ],className="row",
                            style={'color':colors['txt3'],
                                    'textAlign' : 'center'}),
                            ], className="three columns"),
                         ], className="row"),

                        ],className="five columns"),

              ],className="row"),



              ],style={'border': '1px solid white',
                        'margin-left': '10px',
                        'margin-right': '5px',
                        'margin-top': '10px',
                        'margin-bottom': '30px'})
              ],style={'border': '1px solid black',
                        'margin-left': '5px',
                        'margin-right': '5px',
                        'margin-top': '5px',
                        'margin-bottom': '5px'})

              ],style={'border': '1px solid white',
                        'margin-left': '100px',
                        'margin-right': '5px',
                        'margin-top': '10px',
                        'margin-bottom': '10px'})
            ],style={'border': '1px solid orange',
                      'margin-left': '50px',
                       'margin-right': '5px'}),
            #End of Demographic Analyis
            #-----------------------------------------------------


            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),
            #-----------------------------------------------------

            #-----------------------------------------------------
            #Section: Cost-Profit Analysis
            #-----------------------------------------------------
            html.Div([
                html.H1(children='Cost-Profit Analysis',
                                 style={'color':colors['txt3'],
                                        'margin-left': '10px',
                                        'margin-top': '10px'}),
                html.Div([

                html.Div([
                html.Div([
                html.Div([
                  html.Div([
                  html.Div([
                    html.H5(
                    # Start of Summary cost-profit analysis
                    children='Summary of Cost-Profit Analysis of a Course over'+
                              ' a Period of Time.',
                       style={'color':colors['txt3']}),
                    #-----------------------------
                    dcc.Dropdown(id='course_pc_picker',
                                  options=pc_id,
                                  value=default_pc),

                    dcc.DatePickerRange(
                                    id='my-date-picker-rangepc',
                                    min_date_allowed=dtt(2020, 1, 1),
                                    max_date_allowed=dtt(2100, 12, 31),
                                    initial_visible_month=dtt(2020, 1, 1),
                                    start_date=dtt(2020, 1, 1).date(),
                                    end_date=dtt(int(yrc), 12, 31).date()),
                    html.Div(id='output-container-date-picker-rangepc'),
                    html.Div(id="update_pc_table")
                    ],className="row"),

                    html.Div([
                        html.Div([
                            html.Button('Save',
                                  id='save_prof', n_clicks=0),
                            html.Div(id='container-button-prof')
                        ], className="three columns")
                       ], className="row"),

                   ], className="five columns"),
                    #-----------------------------
                 html.Div([
                   html.Div([
                    html.H5(children= var1 + var2,
                                          style={'color':colors['txt3']}),
                        #-----------------------------
                        dcc.Dropdown(id='course_pc_picker2',
                                  options=pc_options,
                                  value=default_pc),
                        html.Div(id="update_pc_table2")
                        ], className="row"),

                        html.Div([
                            html.Div([
                                html.Button('Save',
                                      id='save_prof2', n_clicks=0),
                                html.Div(id='container-button-prof2')
                            ], className="three columns")
                           ], className="row"),
                       ], className="six columns"),
                        #-----------------------------
               ], className="row")

               ],style={'border': '1px solid white',
                         'margin-left': '10px',
                         'margin-right': '10px',
                         'margin-top': '10px',
                         'margin-bottom': '60px'})
               ],style={'border': '1px solid black',
                         'margin-left': '5px',
                         'margin-right': '5px',
                         'margin-top': '5px',
                         'margin-bottom': '5px'}),

                # Start of Summary cost-profit analysis
               #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
               #-----------------------------------------------------
               html.Hr(),
               html.Hr(),
               #-----------------------------------------------------
               #Summarized Cost-Profit Analysis of Courses.
               #-----------------------------------------------------
               html.Div([
               html.Div([
               html.Div([
                 html.Div([
                   html.H5(
                     children='Summarized Cost-Profit Analysis of Courses.',
                        style={'color':colors['txt3']}),
                   dcc.DatePickerRange(
                                   id='date_picker_pcs',
                                   min_date_allowed=dtt(2020, 1, 1),
                                   max_date_allowed=dtt(2100, 12, 31),
                                   initial_visible_month=dtt(2020, 1, 1),
                                   start_date=dtt(2020, 1, 1).date(),
                                   end_date=dtt(int(yrc), 12, 31).date()),
                   html.Div(id='date_container_pcs'),
                   #html.Div(id="update_pc_table")
                   html.Div([
                    dt.DataTable(
                        id='pcs_table',
                        columns=[{"name": i, "id": i} for i in pc_col],
                        page_current=0,
                        page_size=PAGE_SIZE,
                        page_action='custom',
                        #data=prof5.to_dict('records'),
                        style_table={'margin-left': '200x'},
                        style_header={'backgroundColor': 'white',
                                       'fontWeight': 'bold',
                                        'font_size': '23px',
                                        'border': '1px solid black'},
                        style_cell={'textAlign': 'right',
                                    'whiteSpace':'normal',
                                    'font_size': '17px'},
                        style_cell_conditional=[
                                    {'if': {'column_id': 'Region'},
                                    'textAlign': 'left'}],
                        style_data={ 'border': '1px solid blue' },
                        style_data_conditional=[
                                    {'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(248, 248, 248)'}],
                        export_format='xlsx',
                        export_headers='display')
                        ],style={'margin-left': '300px'}),
                  ], className="eleven columns"),
              ], className="row"),
              html.Div([
                html.Div([
                  html.Button('Save',
                        id='save_button_pcs', n_clicks=0),
                  html.Div(id='container-button-pcs')
                ], className="three columns"),

                html.Div([
                 html.Div(id='page_counter_pcs')
                ], className="three columns",
                style={'color':colors['txt3'],
                        'textAlign' : 'center'}),

                html.Div([
                  html.Div(id='page_shower_pcs')
                  ],className="three columns",
                  style={'color':colors['txt3'],
                          'textAlign' : 'center'}),
                ], className="row",
                    style={'margin-left': '300px'}),


              ],style={'border': '1px solid white',
                        'margin-left': '10px',
                        'margin-right': '10px',
                        'margin-top': '10px',
                        'margin-bottom': '30px'})
              ],style={'border': '1px solid black',
                        'margin-left': '5px',
                        'margin-right': '5px',
                        'margin-top': '5px',
                        'margin-bottom': '5px'}),
                #-----------------------------------------------------
                #End of Summarized Cost-Profit Analysis of Courses.
               #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
               #-----------------------------------------------------
               html.Hr(),
               html.Hr(),
               #-----------------------------------------------------
               #-----------------------------------------------------
               #Registrant-Income Report
               #-----------------------------------------------------
                html.Div([
                html.Div([
                html.Div([
                  html.Div([
                    html.H5(
                      children='Registrants-Income Report.',
                         style={'color':colors['txt3']}),
                    dcc.DatePickerRange(
                                    id='date_picker_regin',
                                    min_date_allowed=dtt(2020, 1, 1),
                                    max_date_allowed=dtt(2100, 12, 31),
                                    initial_visible_month=dtt(2020, 1, 1),
                                    start_date=dtt(2020, 1, 1).date(),
                                    end_date=dtt(int(yrc), 12, 31).date()),
                    html.Div(id='date_container_regin'),
                    #html.Div(id="update_pc_table")
                    html.Div([
                     dt.DataTable(
                         id='regin_table',
                         columns=[{"name": i, "id": i} for i in colregin],
                         page_current=0,
                         page_size=PAGE_SIZE,
                         page_action='custom',
                         #data=prof5.to_dict('records'),
                         style_table={'margin-left': '200x'},
                         style_header={'backgroundColor': 'white',
                                        'fontWeight': 'bold',
                                         'font_size': '23px',
                                         'border': '1px solid black'},
                         style_cell={'textAlign': 'right',
                                     'whiteSpace':'normal',
                                     'font_size': '17px'},
                         style_cell_conditional=[
                                     {'if': {'column_id': 'Region'},
                                     'textAlign': 'left'}],
                         style_data={ 'border': '1px solid blue' },
                         style_data_conditional=[
                                     {'if': {'row_index': 'odd'},
                                     'backgroundColor': 'rgb(248, 248, 248)'}],
                         export_format='xlsx',
                         export_headers='display')
                         ],style={'margin-left': '300px'}),
                   ], className="eleven columns"),
               ], className="row"),
               html.Div([
                 html.Div([
                   html.Button('Save',
                         id='save_button_regin', n_clicks=0),
                   html.Div(id='container-button-regin')
                 ], className="three columns"),

                 html.Div([
                   html.Div(id='page_counter_regin')
                 ],className="three columns",
                   style={'color':colors['txt3'],
                           'textAlign' : 'center'}),

               html.Div([
                 html.Div(id='page_shower_regin')
               ],className="three columns",
                 style={'color':colors['txt3'],
                         'textAlign' : 'center'}),

               ], className="row",
                   style={'margin-left': '300px'}),


               ],style={'border': '1px solid white',
                         'margin-left': '10px',
                         'margin-right': '10px',
                         'margin-top': '10px',
                         'margin-bottom': '30px'})
               ],style={'border': '1px solid black',
                         'margin-left': '5px',
                         'margin-right': '5px',
                         'margin-top': '5px',
                         'margin-bottom': '5px'}),
               #-----------------------------------------------------
               #End of Registrant-Income Report
              #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
             ],style={'border': '1px solid white',
                       'margin-left': '100px',
                       'margin-right': '10px',
                       'margin-top': '10px',
                       'margin-bottom': '10px'})
            ],style={'border': '1px solid navy',
                      'margin-left': '50px',
                       'margin-right': '50px'}),
            # End of cost-profit analysis
            #-----------------------------------------------------


            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),
            #-----------------------------------------------------


            #-----------------------------------------------------
            #Section: Trainees' Opinion of Training (Survey)
            #-----------------------------------------------------
    	    html.Div([
                html.H1(children="Trainees' Opinion of Training",
                        style={'color':colors['txt3'],
                               'margin-left': '50px',
                               'margin-top': '10px'}),
            # R1
             html.Div([
                html.Div([
                  html.H5(children=npsat,
                     style={'color':colors['txt3'],
                            'margin-left': '100px'}),
                  ], className="row"),
                   html.Div([
                   html.Div([


                    html.Div([

                    html.Div([
                    html.Div([
                    html.Div([
                              html.H6(children="Select a Course_abb:",
                                style={'color':colors['txt3']}),
                              dcc.Dropdown(id='course_ab_statnps',
                                  options=npsab_options,
                                  value= 'None'),
                             ], className="four columns"),

                    html.Div([
                        html.H6(children="Select a Course_id:",
                                style={'color':colors['txt3']}),
                        dcc.Dropdown(id='course_id_statnps',
                             options=npsid_options,
                             value= 'None'),
                    ], className="four columns"),
                    ], className="row"),

                    html.Div([
                    html.Div([
                        html.H6(children="Select a Question:",
                                style={'color':colors['txt3']}),
                        dcc.Dropdown(id='course_qn_statnps',
                             options=npsqn_options,
                             value= 'None'),
                    ], className="four columns"),


                    html.Div([
                    html.H6(children="Select a Date Range:",
                            style={'color':colors['txt3']}),
                    dcc.DatePickerRange(
                                    id='date_picker_nps',
                                    min_date_allowed=dtt(2020, 1, 1),
                                    max_date_allowed=dtt(2100, 12, 31),
                                    initial_visible_month=dtt(2020, 1, 1),
                                    start_date=dtt(2020, 1, 1).date(),
                                    end_date=dtt(int(yrc), 12, 31).date()),
                    html.Div(id='date_container_nps'),
                    ], className="four columns"),
                   ], className="row"),

                    html.Div([
                       #html.Div([
                          dt.DataTable(id='sur_statabnps',
                             columns=[{"name": i, "id": i} for i in keysc],
                             style_table={'margin-left': '200x'},
                             style_header={'backgroundColor': 'white',
                                             'fontWeight': 'bold',
                                             'font_size': '23px',
                                             'border': '1px solid black'},
                             style_cell={'textAlign': 'center',
                                               'whiteSpace':'normal',
                                               'font_size': '17px'},
                             style_cell_conditional=[
                                             {'if': {'column_id': 'Region'},
                                               'textAlign': 'left'}],
                             style_data={ 'border': '1px solid blue' },
                             style_data_conditional=[
                                         {'if': {'row_index': 'odd'},
                                     'backgroundColor': 'rgb(248, 248, 248)'}],
                             export_format='xlsx',
                             export_headers='display'),
                             #html.A('Download Demography in CSV Fromat',
                                            #id='my-link2')
                         ], className="row"),

                         html.Div([
                             html.Div([
                                 html.Button('Save',
                                       id='save_nps', n_clicks=0),
                                 html.Div(id='container-button-nps')
                             ], className="three columns")
                            ], className="row"),

                      ], className="eight columns"),

                     html.Div([
                      dcc.Graph(id='nps_gauge')
                     ], className="four columns"),

                     ], className="row"),

               ],style={'border': '1px solid white',
                              'margin-left': '50px',
                              'margin-right': '5px',
                              'margin-top': '30px',
                              'margin-bottom': '30px'}),
             ], className="row",
                style={'border': '1px solid black',
                            'margin-left': '5px',
                            'margin-right': '5px',
                            'margin-top': '5px',
                            'margin-bottom': '5px'}),
              ], className="row"),
            # End of R1

             html.Div([
             html.H5(children='Graphical Depiction of TOOT per Course_id.',
                     style={'color':colors['txt3']}),
             ], className="row",
                style={'border': '1px solid white',
                         'margin-left': '100px'}),

               html.Div([
                html.Div([
                  html.Div([

            	    html.Div([
                	html.H6(children='1. Contribution To Learning',
                            style={'color':colors['txt3']}),
                	html.H6(children='2. Skill and Responsiveness',
                            style={'color':colors['txt3']}),
                	], className="four columns"),
            	    html.Div([
                	html.H6(children='3. Course Content',
                        style={'color':colors['txt3']}),
                	html.H6(children='7. Satisfaction Registration',
                        style={'color':colors['txt3']}),
                	], className="four columns"),
            	    html.Div([
                	html.H6(children='8. Overall Course Satisfaction',
                        style={'color':colors['txt3']}),
                	html.H6(children='9. Likelihood to Recommend the Course',
                        style={'color':colors['txt3']}),
                	], className="four columns"),
            	 ], className="row"),

                html.Hr(),
                html.Div([
                  html.Div([
                    html.Div([
                    html.H6(children='Pick a course_id',
                        style={'color':colors['txt3']}),
                       ], className="row"),
            	    html.Div([
                        dcc.Dropdown(id='cid_picker_id',
                             options=cisvy,
                             value=default_cisvy),
                        ], className="now"),
                        ], className="four columns"),
                        ], className="rows"),
                html.Hr(),

                html.Div([
                    html.Div([
                   dt.DataTable(
                       id='table1',
                       columns=[{"name": i, "id": i} for i in blank3.columns],
                       data=blank3.to_dict('records'),
                           style_header={'backgroundColor': 'white'},
                           style_cell={'backgroundColor': 'white',
                               'color': 'white','border': '0px solid white'},
                       )], className="two columns"),
            	    html.Div([
                        dcc.Graph(id='survey_graph')
                        ], className="ten columns"),

                    ], className="row")

               ],style={'border': '1px solid white',
                         'margin-left': '150px',
                         'margin-right': '10px',
                         'margin-top': '10px',
                         'margin-bottom': '30px'})
              ],style={'border': '1px solid black',
                        'margin-left': '5px',
                        'margin-right': '5px',
                        'margin-top': '5px',
                        'margin-bottom': '5px'}),
             # ****** Course range

            ],style={'border': '1px solid peru',
                          'margin-left': '50px',
                           'margin-right': '50px'}),

            # End of Trainees' Opinion of Training
            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),
            #-----------------------------------------------------
            #-----------------------------------------------------
            # Section: Additional Reports
            html.Div([
              html.H1(children= "Additional Reports",
                                      style={'color':colors['txt3'],
                                             'margin-left': '10px',
                                             'margin-top': '10px'}),
              html.Div([
                html.Div([
                html.Div([
                  # Headings row
                  html.Div([
                        html.Div([
                            html.H4(children= "Demographic Reports "+var3,
                                              style={'color':colors['txt3']}),
                            ], className="ten columns"),
                        ], className="row"),
                   # End of Headings Row
                  html.Hr(),
                 # Subheading row
                  html.Div([
                        html.Div([
                            html.H6(children= "Select a Course_acronym:",
                                              style={'color':colors['txt3']}),
                            ], className="two columns"),
                        html.Div([
                             html.H6(children= "Select a Course_id:",
                                               style={'color':colors['txt3']}),
                        ], className="two columns"),
                        html.Div([
                        html.H6(children= "Select Start and End Dates:",
                                style={'color':colors['txt3']}),
                        ], className="four columns"),
                        html.Div([
                            html.H6(children= "Select a By-Option:",
                                              style={'color':colors['txt3']}),
                                ], className="two columns")
                   ], className="row"),
                  # End of subheading Row

                  # selection row
                  html.Div([
                        html.Div([
                            dcc.Dropdown(id='course_id_picker_r1',
                                 options=cAbb_options,
                                 value=default_cAbb),
                        ], className="two columns"),
                        html.Div([
                            dcc.Dropdown(id='course_id_picker_r2',
                                 options=cIDr_options,
                                 value=default_cIDr),
                        ], className="two columns"),
                        html.Div([
                            dcc.DatePickerRange(
                                    id='my-date-picker-ranger1',
                                    min_date_allowed=dtt(2020, 1, 1),
                                    max_date_allowed=dtt(2100, 12, 31),
                                    initial_visible_month=dtt(2020, 1, 1),
                                    start_date=dtt(2020, 1, 1).date(),
                                    end_date=dtt(int(yrc), 12, 31).date()),
                            html.Div(id='output-container-date-picker-ranger1'),
                        ], className="four columns"),
                        html.Div([
                            dcc.Dropdown(id='course_id_picker_r3',
                                 options=By_options,
                                 value=default_By),
                        ], className="two columns"),
                    ], className="row"),
                   # End of selection Row
                html.Hr(),

                # Data row
                html.Div([
                    html.Div([
                         dt.DataTable(id='dem_rep',
                            columns=[{"name": i, "id": i} for i in cdc2],
                            page_current=0,
                            page_size=PAGE_SIZE,
                            page_action='custom',
                            #data=tmp.to_dict('records'),
                            style_table={'margin-left': '200x'},
                            style_header={'backgroundColor': 'white',
                                            'fontWeight': 'bold',
                                            'font_size': '23px',
                                            'border': '1px solid black'},
                            style_cell={'textAlign': 'left',
                                              'whiteSpace':'normal',
                                              'font_size': '17px'},
                            style_cell_conditional=[
                                            {'if': {'column_id': 'Region'},
                                              'textAlign': 'left'}],
                            style_data={ 'border': '1px solid blue' },
                            style_data_conditional=[
                                        {'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(248, 248, 248)'}],
                                          export_format='xlsx',
                                          export_headers='display'),
                                   #html.A('Download Demography in CSV Fromat',
                                           #id='my-link2')
                            ], className="eleven columns"),
                            html.Div([
                               html.Div([
                    			html.Div([
                    				html.H6(children= "Select a Filename:",
                                          style={'color':colors['txt3']})
                    			], className="three columns"),
                    		   ], className="row"),

                    			html.Div([
                    				dcc.Dropdown(id = 'file_name_dem',
                    	  				options = [
                    	  	                {'label': 'Demography',
                                            'value': 'Demography'},
                                            {'label': 'Demg',
                                            'value': 'Demg'}],
                    	  				value = 'Demg')
                    			], className="three columns"),
                    			html.Div([
                    				html.Button('Save',
                                          id='save_button_dem', n_clicks=0),
                                    html.Div(id='container-button-dem')
                    			], className="three columns")
                            ], className="row")
                   ], className="row"),
                   html.Div([
                     html.Div(id='page_shower_dem')
                   ],style={'color':colors['txt3'],
                             'textAlign' : 'right',
                             'margin-right': '140px'}),
                   # End of Data Row
              ],style={'border': '1px solid white',
                        'margin-left': '120px',
                        'margin-right': '10px',
                        'margin-top': '10px',
                        'margin-bottom': '30px'})
               ],style={'border': '1px solid white',
                         'margin-left': '5px',
                         'margin-right': '5px',
                         'margin-top': '5px',
                         'margin-bottom': '5px'})
             ],style={'border': '1px solid black',
                       'margin-left': '10px',
                       'margin-right': '10px',
                       'margin-top': '10px',
                       'margin-bottom': '10px'}),
            # End of of Demographic Reports
            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),

            #-----------------------------------------------------
            #-----------------------------------------------------
            # Survey Report
            html.Div([
              html.H4(children= "Survey Reports",
                                      style={'color':colors['txt3'],
                                             'margin-left': '120px',
                                             'margin-top': '10px'}),
              html.Div([
                html.Hr(),
               # Subheading row
                html.Div([
                      html.Div([
                          html.H6(children= "Pick a Course_acronym:",
                                            style={'color':colors['txt3']}),
                          ], className="two columns"),
                      html.Div([
                           html.H6(children= "Pick a Course_id:",
                                             style={'color':colors['txt3']}),
                      ], className="two columns"),
                      html.Div([
                        html.H6(children= "Pick Start and End Dates:",
                                            style={'color':colors['txt3']}),
                      ], className="four columns"),
                      html.Div([
                          html.H6(children= "Pick a Question # (1-9):",
                                            style={'color':colors['txt3']}),
                              ], className="two columns")
                    ], className="row"),
                # End of subheading Row
                # selection row
                html.Div([
                      html.Div([
                          dcc.Dropdown(id='cab_picker_svy',
                               options=absvy,
                               value=default_absvy),
                      ], className="two columns"),
                      html.Div([
                          dcc.Dropdown(id='cid_picker_svy',
                               options=cisvy,
                               value=default_cisvy),
                      ], className="two columns"),
                      html.Div([
                          dcc.DatePickerRange(
                                  id='date-picker_svy',
                                  min_date_allowed=dtt(2020, 1, 1),
                                  max_date_allowed=dtt(2100, 12, 31),
                                  initial_visible_month=dtt(2020, 1, 1),
                                  start_date=dtt(2020, 1, 1).date(),
                                  end_date=dtt(int(yrc), 12, 31).date()),
                          html.Div(id='date_container_svy'),
                      ], className="four columns"),
                      html.Div([
                          dcc.Dropdown(id='questn_picker_svy',
                               options=qn_options,
                               value='None'),
                      ], className="two columns"),
                  ], className="row"),
                 # End of selection Row
              html.Hr(),
              # Data row
              html.Div([
                  html.Div([
                       dt.DataTable(id='svy_table',
                          columns=[{"name": i, "id": i} for i in qnc],
                          page_current=0,
                          page_size=PAGE_SIZE,
                          page_action='custom',
                          style_table={'margin-left': '200x',
                                       'overflowY': 'scroll'},
                          style_header={'backgroundColor': 'white',
                                          'fontWeight': 'bold',
                                          'font_size': '23px',
                                          'border': '1px solid black'},
                          style_cell={'textAlign': 'left',
                                            'whiteSpace':'normal',
                                            'font_size': '17px'},
                          style_cell_conditional=[
                                          {'if': {'column_id': 'Region'},
                                            'textAlign': 'left'}],
                          style_data={ 'border': '1px solid blue' },
                          style_data_conditional=[
                                      {'if': {'row_index': 'odd'},
                                  'backgroundColor': 'rgb(248, 248, 248)'}],
                                        export_format='xlsx',
                                        export_headers='display'),
                                 #html.A('Download Demography in CSV Fromat',
                                         #id='my-link2')
                          ], className="eleven columns"),
                          html.Div([
                  			html.Div([
                  				html.H6(children= "Select a Filename:",
                                        style={'color':colors['txt3']})
                  			], className="three columns"),
                  		   ], className="row"),
                          html.Div([
                  			html.Div([
                  				dcc.Dropdown(id = 'file_name',
                  	  				options = [
                  	  						{'label': 'TOOT', 'value': 'TOOT'},
                  	  						{'label': 'SOOT', 'value': 'SOOT'}],
                  	  				value = 'TOOT')
                  			], className="three columns"),
                  			html.Div([
                  				html.Button('Save',
                                      id='save_button_svy', n_clicks=0),
                                html.Div(id='container-button-svy')
                  			], className="three columns")
                  		   ], className="row")
                 ], className="row"),
                 html.Div([
                   html.Div(id='page_shower')
                 ],style={'color':colors['txt3'],
                           'textAlign' : 'right',
                           'margin-right': '140px'}),

              ],style={'border': '1px solid white',
                        'margin-left': '120px',
                        'margin-right': '10px',
                        'margin-top': '10px',
                        'margin-bottom': '10px'})

               ],style={'border': '1px solid black',
                         'margin-left': '5px',
                         'margin-right': '5px',
                         'margin-top': '5px',
                         'margin-bottom': '5px'}),
              # End of of Survey Report Section

              #-----------------------------------------------------
              html.Hr(),
              html.Hr(),
              #-----------------------------------------------------
              #-----------------------------------------------------
              # How did you hear about us?
              html.Div([
                html.H4(children= "How Did You Hear About Us?",
                                        style={'color':colors['txt3'],
                                               'margin-left': '120px',
                                               'margin-top': '10px'}),
                html.Div([
                  html.Hr(),
                 # Subheading row
                  html.Div([
                        html.Div([
                            html.H6(children= "Pick a Course_acronym:",
                                              style={'color':colors['txt3']}),
                            ], className="two columns"),
                        html.Div([
                             html.H6(children= "Pick a Course_id:",
                                               style={'color':colors['txt3']}),
                        ], className="two columns"),
                        html.Div([
                          html.H6(children= "Pick Start and End Dates:",
                                              style={'color':colors['txt3']}),
                        ], className="six columns"),
                      ], className="row"),
                  # End of subheading Row
                  # selection row
                  html.Div([
                        html.Div([
                            dcc.Dropdown(id='cab_picker_hdh',
                                 options=abhdh,
                                 value=default_abhdh),
                        ], className="two columns"),
                        html.Div([
                            dcc.Dropdown(id='cid_picker_hdh',
                                 options=cihdh,
                                 value=default_cihdh),
                        ], className="two columns"),
                        html.Div([
                            dcc.DatePickerRange(
                                    id='date-picker_hdh',
                                    min_date_allowed=dtt(2020, 1, 1),
                                    max_date_allowed=dtt(2100, 12, 31),
                                    initial_visible_month=dtt(2020, 1, 1),
                                    start_date=dtt(2020, 1, 1).date(),
                                    end_date=dtt(int(yrc), 12, 31).date()),
                            html.Div(id='date_container_hdh'),
                        ], className="six columns"),
                    ], className="row"),
                   # End of selection Row
                html.Hr(),
                # Data row
                html.Div([
                    html.Div([
                         dt.DataTable(id='hdh_table',
                            columns=[{"name": i, "id": i} for i in colhdh2],
                            page_current=0,
                            page_size=PAGE_SIZE,
                            page_action='custom',
                            style_table={'margin-left': '200x',
                                         'overflowY': 'scroll'},
                            style_header={'backgroundColor': 'white',
                                            'fontWeight': 'bold',
                                            'font_size': '23px',
                                            'border': '1px solid black'},
                            style_cell={'textAlign': 'left',
                                              'whiteSpace':'normal',
                                              'font_size': '17px'},
                            style_cell_conditional=[
                                            {'if': {'column_id': 'Region'},
                                              'textAlign': 'left'}],
                            style_data={ 'border': '1px solid blue' },
                            style_data_conditional=[
                                        {'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(248, 248, 248)'}],
                                          export_format='xlsx',
                                          export_headers='display'),
                                   #html.A('Download Demography in CSV Fromat',
                                           #id='my-link2')
                            ], className="eleven columns"),
                            html.Div([
                    			html.Div([
                    				html.H6(children= "Select a Filename:",
                                          style={'color':colors['txt3']})
                    			], className="three columns"),
                    		   ], className="row"),
                            html.Div([
                    			html.Div([
                    				dcc.Dropdown(id = 'file_nhdh',
                    	  				options = [
                    	  						{'label': 'HDHAU',
                                                'value': 'HDHAU'},
                    	  						{'label': 'Hear',
                                                'value': 'Hear'},
                                                {'label': 'Aboutus',
                                                'value': 'Aboutus'}
                                                ],
                    	  				value = 'Aboutus')
                    			], className="three columns"),
                    			html.Div([
                    				html.Button('Save',
                                        id='save_button_hdh', n_clicks=0),
                                  html.Div(id='container-button-hdh')
                    			], className="three columns")
                    		   ], className="row")
                   ], className="row"),
                   html.Div([
                     html.Div(id='page_shower_hdh')
                   ],style={'color':colors['txt3'],
                             'textAlign' : 'right',
                             'margin-right': '140px'}),

                ],style={'border': '1px solid white',
                          'margin-left': '120px',
                          'margin-right': '10px',
                          'margin-top': '10px',
                          'margin-bottom': '10px'}),

                 ],style={'border': '1px solid black',
                           'margin-left': '5px',
                           'margin-right': '5px',
                           'margin-top': '5px',
                           'margin-bottom': '5px'}),
                # End of of how did you hearabout us


            ],style={'border': '1px solid cyan',
                      'margin-left': '50px',
                       'margin-right': '50px'}),

            # End of Reports Section
            #-----------------------------------------------------


            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),
            #-----------------------------------------------------


            #-----------------------------------------------------
            #Section: Search Trainees
            #-----------------------------------------------------
            html.Div([
                html.H1(children='Search Trainees By Lastname.',
                                 style={'color':colors['txt3'],
                                        'margin-left': '10px',
                                        'margin-top': '10px'}),
                html.Hr(),

                html.Hr(),
                html.Div([

                html.Div([
                html.Div([
                   html.Div([
                    html.H6(
                        children="Select a Lastname:",
                        style={'color':colors['txt3']}),
                   dcc.Dropdown(id = 'lnamerg_dwn',
   		              options = lname_dwn, value = None),
                        ],style={'margin-left': '300px'}),
                  ], className="five columns"),
              ], className="row"),

              html.Hr(),

              html.Div([
                  html.Div([
                      #html.Div(id="update_acl3_table")
                      html.Div([
                       dt.DataTable(
                        id='lnamer_table',
                        columns=[{"name": i,
                             "id": i} for i in regcol],
                        #data=acl1.to_dict('records'),
                        style_table={'margin-left': '200x'},
                        style_header={
                              'backgroundColor': 'white',
                              'fontWeight': 'bold',
                              'font_size': '23px',
                              'border': '1px solid black'},
                        style_cell={'textAlign': 'left',
                                    'whiteSpace':'normal',
                                    'font_size': '17px'},
                        style_cell_conditional=[
                              {'if': {'column_id': 'Region'},
                               'textAlign': 'left'}],
                        style_data={
                                 'border': '1px solid blue' },
                        style_data_conditional=[
                              {'if': {'row_index': 'odd'},
                      'backgroundColor': 'rgb(248, 248, 248)'
                        }],
                        export_format='xlsx',
                        export_headers='display')
                      ])
                      ],className="eleven columns")
                  ],className="row"),

                  html.Hr(),

                  html.Div([
                      html.Div([
                          html.Div([
                           dt.DataTable(
                            id='lnameg_table',
                            columns=[{"name": i,
                                 "id": i} for i in gracol],
                            #data=acl1.to_dict('records'),
                            style_table={'margin-left': '200x'},
                            style_header={
                                  'backgroundColor': 'white',
                                  'fontWeight': 'bold',
                                  'font_size': '23px',
                                  'border': '1px solid black'},
                            style_cell={'textAlign': 'left',
                                        'whiteSpace':'normal',
                                        'font_size': '17px'},
                            style_cell_conditional=[
                                  {'if': {'column_id': 'Region'},
                                   'textAlign': 'left'}],
                            style_data={
                                     'border': '1px solid blue' },
                            style_data_conditional=[
                                  {'if': {'row_index': 'odd'},
                          'backgroundColor': 'rgb(248, 248, 248)'
                            }],
                            export_format='xlsx',
                            export_headers='display')
                          ])
                          ],className="eleven columns")
                      ],className="row"),


             ],style={'border': '1px solid white',
                       'margin-left': '100px',
                       'margin-right': '10px',
                       'margin-top': '10px',
                       'margin-bottom': '100px'})
            ],style={'border': '1px solid navy',
                      'margin-left': '50px',
                       'margin-right': '50px'}),
            # End of Search section
            #-----------------------------------------------------

            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),
            #-----------------------------------------------------



            #-----------------------------------------------------
            #Section: DB Tables
            #-----------------------------------------------------
            html.Div([
                html.H1(children='Download Database Tables:',
                                 style={'color':colors['txt3'],
                                        'margin-left': '10px',
                                        'margin-top': '10px'}),
                html.Hr(),

                html.Div([

                  html.Div([
                  html.H6(children=table_list[0],
                          style={'color':colors['txt3']}),
                  html.H6(children=table_list[1],
                          style={'color':colors['txt3']}),
                  html.H6(children=table_list[2],
                          style={'color':colors['txt3']}),
                  ], className="four columns"),

                  html.Div([
                  html.H6(children=table_list[3],
                      style={'color':colors['txt3']}),
                  html.H6(children=table_list[4],
                      style={'color':colors['txt3']}),
                  ], className="four columns"),

                  html.Div([
                  html.H6(children=table_list[5],
                          style={'color':colors['txt3']}),
                  html.H6(children=table_list[6],
                      style={'color':colors['txt3']}),
                  ], className="four columns"),
               ], className="row",style={'margin-left': '300px'}),

                html.Hr(),
                html.Div([
                html.Div([
                html.Div([
                   html.Div([
                   html.H6(
                       children="Select a Table_name from the "+
                                str(len(table_list))+ " tables in DB:",
                       style={'color':colors['txt3']}),
                   dcc.Dropdown(id = 'dbt_dwn',
   		              options = dbdwn, value = 'frac_setting'),
                    html.Div(id="db_tables")
                        ],style={'margin-left': '300px'}),
                  ], className="five columns"),
              ], className="row"),

             html.Div([
                 html.Div([
                     html.Button('Save',
                           id='savetabs', n_clicks=0),
                     html.Div(id='container-button-dbt')
                 ], className="row")
                ],style={'color':colors['txt3'],
                 'textAlign' : 'right',
                 'margin-right': '1000px'}),

                html.Hr(),
                 html.Div([
                   html.Div(id='status_indicator')
                          ],className="row", style={'color':colors['txt3'],
                           'textAlign' : 'right',
                           'margin-right': '600px'}),


             ],style={'border': '1px solid white',
                       'margin-left': '100px',
                       'margin-right': '10px',
                       'margin-top': '10px',
                       'margin-bottom': '100px'})
            ],style={'border': '1px solid navy',
                      'margin-left': '50px',
                       'margin-right': '50px'}),
            # End of DB Tables section
            #-----------------------------------------------------



            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),
            #-----------------------------------------------------


            #-----------------------------------------------------
            #Section: Error Messages
            #-----------------------------------------------------
            html.Div([
                html.H1(children='Warning/Error Messages',
                                 style={'color':colors['txt3'],
                                        'margin-left': '10px',
                                        'margin-top': '10px'}),
                html.Hr(),
                html.H3(children='Possible Causes of Errors:',
                                 style={'color':colors['txt3'],
                                        'margin-left': '200px',
                                        'margin-top': '10px'}),
                html.Div([
                html.Div([
                html.H5(children='1: Columns or content Mismatches',
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                html.H5(children='2: Python Version Problem',
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                html.H5(children='3: Incorrectly changing part of the code',
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                ], className="five columns"),

                html.Div([
                html.H5(children='4: Incorrect path setting(s)',
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                html.H5(children='5: Incorrect Input Dataset Names',
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                html.H5(children='6: Missing Database',
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                ], className="six columns"),
                ], className="row"),


                html.H3(children='Possible Causes of Warnings:',
                                 style={'color':colors['txt3'],
                                        'margin-left': '200px',
                                        'margin-top': '10px'}),
                html.Div([
                html.Div([
                html.H5(children='1: Empty InputDatasets folder',
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                html.H5(children='2: Attempt to write empty dataframes',
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                html.H5(children='3: Empty Database (with no tables)',
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                ], className="five columns"),

                html.Div([
                html.H5(children='4: DB Backup issue due to no update',
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                html.H5(children="5: 'No **** List' File is a warning message",
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                html.H5(
                   children="6: 'No *** was inserted to DB' is a warning message",
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                ], className="six columns"),
                ], className="row"),

                html.Hr(),

                html.H5(children='NB: ' + nbmsg,
                                 style={'color':colors['txt3'],
                                        'margin-left': '300px'}),
                html.Hr(),


                html.Div([
                html.Div([
                html.Div([

                   html.Div([
                    dt.DataTable(
                        id='err_table',
                        columns=[{"name": i, "id": i} for i in dfer.columns],
                        data=dfer.to_dict('records'),
                        style_table={'margin-left': '200x'},
                        style_header={'backgroundColor': 'white',
                                       'fontWeight': 'bold',
                                        'font_size': '23px',
                                        'border': '1px solid black'},
                        style_cell={'textAlign': 'left',
                                    'whiteSpace':'normal',
                                    'font_size': '17px'},
                        style_cell_conditional=[
                                    {'if': {'column_id': 'Region'},
                                    'textAlign': 'left'}],
                        style_data={ 'border': '1px solid blue' },
                        style_data_conditional=[
                                    {'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(248, 248, 248)'}],
                        export_format='xlsx',
                        export_headers='display')
                        ],style={'margin-left': '300px'}),
                  ], className="eleven columns"),
              ], className="row"),

             ],style={'border': '1px solid white',
                       'margin-left': '100px',
                       'margin-right': '10px',
                       'margin-top': '10px',
                       'margin-bottom': '10px'})
            ],style={'border': '1px solid navy',
                      'margin-left': '50px',
                       'margin-right': '50px'}),
            # End of error-message section
            #-----------------------------------------------------



            #-----------------------------------------------------
            html.Hr(),
            html.Hr(),
            #-----------------------------------------------------


            #-----------------------------------------------------
            html.H1(children=cr,style={'color':colors['txt3'],
                                       'textAlign' : 'center'})
     ])
app.layout = serve_layout
#******************************************************************************
#@startof@appcallback
#******************************************************************************
#******************************************************************************
# 9. @app.callbacks to add interactive functionalities to the app
#******************************************************************************
#*************************************
# 9.0 Checklist
#*************************************
#*************************************
def update_output_chklst(pc, ps, cp, yr, rp,gp, sp, cmp,df):
    if df.shape[0]==0 or isinstance(df, bool)==True:
        return None, None, 0, False
    else:
        df1, df2 = df[list(df.columns)], df[list(df.columns)]
        df1,df2 = df1[df1['year'] == yr],df2[df2['year'] == yr]
        if cp != None and rp == None and gp == None and sp == None and cmp == None:
            df1 = df1[df1['course_id'] == cp]
            df2 = df2[df2['course_id'] == cp]
            df1['index'] = range(1, len(df1) + 1)
            tp = 'Total Pages: '+ str(ceil(df1.shape[0]/PAGE_SIZEacl))
            return df2, df1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp, True
        elif rp != None and cp == None and gp == None and sp == None and cmp == None:
            df1 = df1[df1['Registrants'] == rp]
            df2 = df2[df2['Registrants'] == rp]
            df1['index'] = range(1, len(df1) + 1)
            tp = 'Total Pages: '+ str(ceil(df1.shape[0]/PAGE_SIZEacl))
            return df2, df1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp, True
        elif gp != None and cp == None and rp == None and sp == None and cmp == None:
            df1 = df1[df1['Grades'] == gp]
            df2 = df2[df2['Grades'] == gp]
            df1['index'] = range(1, len(df1) + 1)
            tp = 'Total Pages: '+ str(ceil(df1.shape[0]/PAGE_SIZEacl))
            return df2, df1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp, True
        elif sp != None and cp == None and gp == None and rp == None and cmp == None:
            df1 = df1[df1['Surveys'] == sp]
            df2 = df2[df2['Surveys'] == sp]
            df1['index'] = range(1, len(df1) + 1)
            tp = 'Total Pages: '+ str(ceil(df1.shape[0]/PAGE_SIZEacl))
            return df2, df1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp, True
        elif cmp != None and cp == None and gp == None and sp == None and rp == None:
            df1 = df1[df1['Costs'] == cmp]
            df2 = df2[df2['Costs'] == cmp]
            df1['index'] = range(1, len(df1) + 1)
            tp = 'Total Pages: '+ str(ceil(df1.shape[0]/PAGE_SIZEacl))
            return df2, df1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp, True
        elif cmp == 'Yes' and gp == 'Yes' and sp == 'Yes' and rp == 'Yes':            
            df1 = df1[(df1['Registrants'] == 'Yes') & (df1['Grades'] == 'Yes') &\
                      (df1['Surveys'] == 'Yes') & (df1['Costs'] == 'Yes')]
            df2 = df2[(df2['Registrants'] == 'Yes') & (df2['Grades'] == 'Yes') &\
                      (df2['Surveys'] == 'Yes') & (df2['Costs'] == 'Yes')]            
            df1['index'] = range(1, len(df1) + 1)
            tp = 'Total Pages: '+ str(ceil(df1.shape[0]/PAGE_SIZEacl))
            return df2, df1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp, True
        elif cmp == 'NotAvail' and gp == 'NotAvail' and sp == 'NotAvail' and rp == 'NotAvail':            
            df1 = df1[(df1['Registrants'] == 'NotAvail') & (df1['Grades'] == 'NotAvail') &\
                      (df1['Surveys'] == 'NotAvail') & (df1['Costs'] == 'NotAvail')]
            df2 = df2[(df2['Registrants'] == 'NotAvail') & (df2['Grades'] == 'NotAvail') &\
                      (df2['Surveys'] == 'NotAvail') & (df2['Costs'] == 'NotAvail')]            
            df1['index'] = range(1, len(df1) + 1)
            tp = 'Total Pages: '+ str(ceil(df1.shape[0]/PAGE_SIZEacl))
            return df2, df1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp, True
        else:
            df1['index'] = range(1, len(df1) + 1)
            tp = 'Total Pages: '+ str(ceil(df1.shape[0]/PAGE_SIZEacl))
            return df2, df1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp, True             
        
#Checklist table
@app.callback([
    dash.dependencies.Output('con-button-ckl', 'children'),
    dash.dependencies.Output('chklst_table', 'data'),
    dash.dependencies.Output('page_counter_ckl', 'children'),
    dash.dependencies.Output('page_shower_ckl', 'children')],
    [dash.dependencies.Input('chklst_table', "page_current"),
     dash.dependencies.Input('chklst_table', "page_size"),
     dash.dependencies.Input('cidpicker', 'value'),
     dash.dependencies.Input('chklst_yr_picker', 'value'),
     dash.dependencies.Input('regynpicker', 'value'),
     dash.dependencies.Input('graynpicker', 'value'),
     dash.dependencies.Input('svyynpicker', 'value'),
     dash.dependencies.Input('cmlynpicker', 'value'),
     dash.dependencies.Input('save_ckl', 'n_clicks')])
def update_output_cklstmn(pc, ps, cp, yr, rp, gp, sp, cmp, n_clicks):
    df, data, tp1, flag1 = update_output_chklst(pc,ps,cp,yr,rp,gp,sp,cmp,chklstv1)
    nc = "Number of Courses: "+str(df.shape[0])
    if n_clicks == 0:
        return None, data, nc, tp1
    else:
        if flag1 == True:
            try:
                fn = 'checklist' + ('_').join([yrc,mhc,dyc])
                files =  glob.glob(path_3+'*.xlsx')
                if (path_3 + fn + '.xlsx') in files:
                    os.remove(path_3 + fn + '.xlsx')
                save_fmt_report(df, path_3, fn, flags[7])
            except:
                print("[Error]:", sys.exc_info()[0])
            else:
                print(f"{fn} was saved successfuly")
            finally:
                n_clicks = 0
        return None, data, nc, tp1
#*************************************
# 9.1 All Courses List
#*************************************
def update_output_acl(pc, ps, df):
    if df.shape[0]==0 or isinstance(df, bool)==True:
        return None, None, 0, False
    else:
        df1, df2 = df[list(df.columns)], df[list(df.columns)]
        df1['index'] = range(1, len(df1) + 1)
        tp = 'Total Pages: '+ str(ceil(df1.shape[0]/PAGE_SIZEacl))
        return df2, df1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp, True
#acl3 from acl vs acl
@app.callback([
    dash.dependencies.Output('container-button-acl1', 'children'),
    dash.dependencies.Output('acl3_table', 'data'),
    dash.dependencies.Output('page_counter_acl3', 'children'),
    dash.dependencies.Output('page_shower_acl3', 'children')],
    [dash.dependencies.Input('acl3_table', "page_current"),
     dash.dependencies.Input('acl3_table', "page_size"),
     dash.dependencies.Input('save_acl1', 'n_clicks')])
def update_output_acl3(pc, ps, n_clicks):
    df, data, tp, flag2 = update_output_acl(pc, ps, acl)
    nc2 = "Number of Courses: "+str(df.shape[0])
    if n_clicks == 0:
        return None, data, nc2,tp
    else:
        try:
            fn = 'All_Courses_3columns' + ('_').join([yrc,mhc,dyc])
            files =  glob.glob(path_3+'*.xlsx')
            if (path_3 + fn + '.xlsx') in files:
                os.remove(path_3 + fn + '.xlsx')            
            if flag2 == True:
                save_fmt_report(df, path_3, fn, flags[0])
        except:
            print("[Error]:", sys.exc_info()[0])
        else:
            print(f"{fn} was successfully saved!")
        finally:
            n_clicks = 0
        return None, data, nc2, tp

#*************************************
#acl5 from acl vs acl1
#*************************************
@app.callback([
    dash.dependencies.Output('container-button-acl5', 'children'),
    dash.dependencies.Output('acl5_table', 'data'),
    dash.dependencies.Output('page_counter_acl5', 'children'),
    dash.dependencies.Output('page_shower_acl5', 'children')],
    [dash.dependencies.Input('acl5_table', "page_current"),
     dash.dependencies.Input('acl5_table', "page_size"),
     dash.dependencies.Input('save_acl5', 'n_clicks')])
def update_output_acl5(pc, ps, n_clicks):
    df, data, tp, flag3 = update_output_acl(pc, ps, acl1)
    nc3 = "Number of Courses: "+str(df.shape[0])
    if n_clicks == 0:
        return None, data, nc3, tp
    else:
        try:
            fn = 'All_Courses_5columns' + ('_').join([yrc,mhc,dyc])
            files =  glob.glob(path_3+'*.xlsx')
            if (path_3 + fn + '.xlsx') in files:
                os.remove(path_3 + fn + '.xlsx')        
            if flag3 == True:
                save_fmt_report(df, path_3, fn, flags[1])
        except:
            print("[Error]:", sys.exc_info()[0])
        else:
            print(f"{fn} was saved successfully!")
        finally:
            n_clicks = 0
        return None, data, nc3, tp
#******************************************************************************
#*************************************
# 9.2 Grade graph and Tables app.callbacks
#*************************************
# Function for grade charts
#-------------------------------------
def gen_bar(gradebar, title):
    colors =["yellow","orange","red","green"]

    def colr(df):
        df['colr']= df['Grades'].apply(lambda x: 0 if x=='NaN'\
                                  else( 1 if x=='H'\
                                  else(2 if x=='Failed' else 3)))
        df=df.sort_values(by=['colr'])
        return df

    gradebar = colr(gradebar)
    def crfl(df):
        clrs=[]
        for cr in df['colr'].tolist():
            clrs.append(colors[cr])
        return clrs
    #---------------------------------
    # Initialize figure with subplots
    fig = make_subplots(rows=1, cols=1)
    #---------------------------------
    # Add locations bar chart-1
    lab = title
    fig.add_trace(go.Bar(name=lab,
                         x=gradebar['Grades'],
                         y=gradebar['Number of Trainees'],
                         text=gradebar['Number of Trainees'],
                         marker=dict(color=crfl(gradebar)),
                         showlegend=False),
                  row=1, col=1)
    #-------------------------------------
    # Update xaxis properties
    fig.update_xaxes(title_text=lab, row=1, col=1)
    fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

    # Set theme, margin, and annotation in layout
    fig.update_layout(template="plotly_dark",
                    width=850,
                    height=600,
                    margin=dict(r=30, t=30, b=30, l=30),
                    bargap = 0,
                    uniformtext_minsize=8,
                    uniformtext_mode='hide')
    return fig

#******************************************************************************
# Grade barchart @app.callback and update
@app.callback([
  dash.dependencies.Output('output-container-date-picker-range1', 'children'),
  dash.dependencies.Output('graph_gra', 'figure')],
  [dash.dependencies.Input('course_id_picker_ggra', 'value')])
#-------------------------------------
def update_bargrades(selected_course_id):
    string_prefix = 'Selected Course ID: '
    f_gra = gra[gra['course_id'] == selected_course_id]
    f_gra['Final Grade'] = f_gra['Final Grade'].fillna('NaN')
    string_prefix = string_prefix + selected_course_id
    gradep= f_gra['Final Grade'][f_gra['Final Grade']=='Passed']
    gradef= f_gra['Final Grade'][f_gra['Final Grade']=='Failed']
    gradena = f_gra['Final Grade'][f_gra['Final Grade']=='NaN']
    gradeh = f_gra['Final Grade'][f_gra['Final Grade']=='H']
    gradeplot = {'Grades': ['Passed','Failed','H','NaN'],
                 'Number of Trainees':[len(gradep),len(gradef),len(gradeh),
                                       len(gradena)]}
    gradebar = pd.DataFrame(gradeplot)
    title = "Grades of the course with course_id: "+ selected_course_id
    return string_prefix, gen_bar(gradebar, title)
#******************************************************************************
#*************************************
# Grade barchart of a range of courses selected by start_date and end_date
@app.callback([
    dash.dependencies.Output('output-container-date-picker-range', 'children'),
    dash.dependencies.Output('graph_gra2', 'figure')],
    [dash.dependencies.Input('my-date-picker-range', 'start_date'),
     dash.dependencies.Input('my-date-picker-range', 'end_date')])

def update_output_gra(start_date, end_date):
    string_prefix = 'Selected Dates: '
    start_date = dtt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    start_date_string = start_date.strftime('%B %d, %Y')
    string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '

    end_date = dtt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    end_date_string = end_date.strftime('%B %d, %Y')
    string_prefix = string_prefix + 'End Date: ' + end_date_string

    drange = [(start_date + timedelta(days=x)).strftime("%d/%m/%Y")
               for x in range((end_date-start_date).days + 1)]

    f_gra = gra[gra['startDate'].isin(drange)]
    f_gra['Final Grade'] = f_gra['Final Grade'].fillna('NaN')
    gradep= f_gra['Final Grade'][f_gra['Final Grade']=='Passed']
    gradef= f_gra['Final Grade'][f_gra['Final Grade']=='Failed']
    gradeh = f_gra['Final Grade'][f_gra['Final Grade']=='H']
    gradena = f_gra['Final Grade'][f_gra['Final Grade']=='NaN']
    gradeplot = {'Grades': ['Passed','Failed','H','NaN'],
                 'Number of Trainees':[len(gradep),len(gradef),len(gradeh),
                                       len(gradena)]}
    gradebar = pd.DataFrame(gradeplot)
    tl1 = start_date_string +" and "+end_date_string
    title = "Grades of courses offered between: "+tl1
    return string_prefix, gen_bar(gradebar,title)
#-----------------------------------------------------------------------------
# Average of passed and failed trainees
def get_pgavg(gra, acl):
    gra1 = gra[gracol]
    gra1['Final Grade'] = gra1['Final Grade'].fillna('NaN')
    gra1= gra1.drop(gra1[gra1["Final Exam"].isin(
        ['Passed','Failed','None','NaN', 'H', None])].index)
    gra1= gra1.dropna(subset=['Final Exam'])
    #gra1['Final Exam'] = gra1['Final Exam'].astype('str')
    #gra1= gra1[(gra1['Final Exam'].str.isnumeric())==True]
    #gra1= gra1[gra1['Final Exam']!='H']
    #gra1['Final Exam'] = gra1['Final Exam'].astype(float)
    gra1["Final Exam"]=pd.to_numeric(gra1["Final Exam"])
    gra1 = gra1[['course_abb', 'Final Exam', 'Final Grade']]
    poavg = gra1[gra1['Final Grade']=='Passed']
    poavg = np.mean(poavg['Final Exam'].tolist())
    foavg = gra1[gra1['Final Grade']=='Failed']
    foavg = np.mean(foavg['Final Exam'].tolist())
    oavg = {'course_name':['Overall'],'Avg_of_passed Trainees':[round(poavg,2)],
           'Avg_of_failed Trainees':[round(foavg,2)]}
    #print("oavg:",oavg)
    pfoavg = pd.DataFrame(oavg)

    gra1 = gra1.groupby(['course_abb','Final Grade']).mean().reset_index()
    cond71 = [(gra1['Final Grade'] == 'Passed')]
    cond72 = [(gra1['Final Grade'] == 'Failed')]
    values71 = [gra1['Final Exam']]
    values72 = [gra1['Final Exam']]
    gra1['Avg_of_passed Trainees'] = np.select(cond71, values71)
    gra1['Avg_of_failed Trainees'] = np.select(cond72, values72)
    gra1 = gra1[['course_abb','Avg_of_passed Trainees',
                 'Avg_of_failed Trainees']]
    gra1 = gra1.groupby(['course_abb']).sum().reset_index()

    aclm = acl[acl.columns[:2]]
    aclm.columns = ['course_name', 'course_abb']

    merged = aclm.merge(gra1, on ='course_abb',how='inner')
    merged = merged[['course_name','Avg_of_passed Trainees',
                     'Avg_of_failed Trainees']]
    mergedf = pd.concat([merged, pfoavg])
    mergedf = mergedf.round()
    return mergedf
#******************************************************************************
#*************************************
# Grade Table of a range of courses selected by start_date and end_date
#*************************************
# Function for generating a grade table for all courses in range of time
def filter_gradetab(start_date, end_date, pc, ps):
    spx, fnn = '',''
    start_date = dtt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    start_date_string = start_date.strftime('%B %d, %Y')
    spx = spx + start_date_string + ' | '
    fnn = fnn + start_date.strftime("%Y")+'_'+\
        start_date.strftime("%B")+'_'+ start_date.strftime("%d")

    end_date = dtt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    end_date_string = end_date.strftime('%B %d, %Y')
    spx = spx + end_date_string
    fnn = fnn + '_to_'+end_date.strftime("%Y")+'_'+\
        end_date.strftime("%B")+'_'+ end_date.strftime("%d")

    drange = [(start_date + timedelta(days=x)).strftime("%d/%m/%Y")
          for x in range((end_date-start_date).days + 1)]

    regtgc = ['course_id','Registration Status','course_abb','startDate']
    gratgc= ['course_id', 'course_abb', 'startDate','Final Grade']
    acltgc= ['course_name', 'acronym']
    regtgd, gratgd, acltgd = reg[regtgc], gra[gratgc], acl[acltgc]

    #pass and fail
    gradepf = gra[gra['startDate'].isin(drange)]
    gradepf = gradepf[gracol]
    #print("gradepf", gradepf)
    pfavg = get_pgavg(gradepf, acl)
    #print("pfavg2", pfavg)

    regtgd1 = regtgd[regtgd['Registration Status']=='Registered']
    regtgd1 = regtgd1[['course_id','course_abb','startDate']]
    regtgd1['countr'] = 1
    tmpg1 = ['course_id','course_abb','startDate']
    regtgd1 = regtgd1.groupby(tmpg1).sum().reset_index()

    gratgd1 = gratgd[(gratgd['Final Grade']=='Passed') |\
     (gratgd['Final Grade']=='Failed')]
    gratgd1['countg']=1
    tmpg2 = ['course_id','course_abb','startDate','Final Grade']
    gratgd1 = gratgd1.groupby(tmpg2).sum().reset_index()

    cond1 = [(gratgd1['Final Grade'] == 'Passed')]
    cond2 = [(gratgd1['Final Grade'] == 'Failed')]
    values1 = [gratgd1['countg']]
    values2 = [gratgd1['countg']]
    gratgd1['Passed'] = np.select(cond1, values1)
    gratgd1['Failed'] = np.select(cond2, values2)
    merged = regtgd1.merge(gratgd1, on=['course_id','course_abb','startDate'],
                           how='inner')
    merged = merged[['course_id','course_abb','startDate','countr', 'countg',
                     'Passed','Failed']]
    merged.columns = ['course_id','course_abb','startDate','Enrolled', 'Submitted',
                   'Passed','Failed']

    merged = merged[merged['startDate'].isin(drange)]
    merged1 = merged.groupby(['course_abb']).sum().reset_index()
    merged1['Enrolled'] = merged1['Enrolled']/2
    aclm = acl[acl.columns[:2]]
    aclm.columns = ['course_name', 'course_abb']
    merged2 = aclm.merge(merged1, on ='course_abb',how='inner')

    merged2['Passing rate of submitted']=\
                                   merged2['Passed']/merged2['Submitted']*100
    merged2['Passing rate of enrolled']=\
                                    merged2['Passed']/merged2['Enrolled']*100
    merged2['Submission rate']=merged2['Submitted']/merged2['Enrolled']*100
    merged2 = merged2.round()


    totdict2 ={'course_name':['Total'],'Enrolled':[merged2['Enrolled'].sum()],
              'Submitted':[merged2['Submitted'].sum()],
              'Passed':[merged2['Passed'].sum()],
              'Failed':[merged2['Failed'].sum()],'Passing rate of submitted':\
               [merged2['Passed'].sum()/merged2['Submitted'].sum()*100],
              'Passing rate of enrolled':[merged2['Passed'].sum()/\
                   merged2['Enrolled'].sum()*100],
              'Submission rate':[merged2['Submitted'].sum()/\
                                 merged2['Enrolled'].sum()*100]}

    mergednew = pd.concat([merged2, pd.DataFrame(totdict2)])
    mergednew = mergednew.round()

    mf1, mf2 = mergednew[mf_col], mergednew[mf_col]
    mf1['index'] = range(1, len(mf1) + 1)
    tp = 'Total Pages: ' + str(ceil(mf1.shape[0]/PAGE_SIZE))
    return mf2, spx,mf1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,fnn,pfavg

#******************************************************************************
@app.callback([
    dash.dependencies.Output('container-button-gratpf', 'children'),
    dash.dependencies.Output('output-container-date-picker-range2', 'children'),
    dash.dependencies.Output('tablegrade', 'data'),
    dash.dependencies.Output('tablegradepf', 'data'),
    dash.dependencies.Output('page_counter_gra', 'children'),
    dash.dependencies.Output('page_shower_gra', 'children'),
    dash.dependencies.Output('page_counter_grapf', 'children'),
    dash.dependencies.Output('page_shower_grapf', 'children')],
    [dash.dependencies.Input('my-date-picker-range2', 'start_date'),
     dash.dependencies.Input('my-date-picker-range2', 'end_date'),
     dash.dependencies.Input('tablegrade', "page_current"),
     dash.dependencies.Input('tablegrade', "page_size"),
     dash.dependencies.Input('tablegradepf', "page_current"),
     dash.dependencies.Input('tablegradepf', "page_size"),
     dash.dependencies.Input('save_button_gra','n_clicks')])

def update_output_gra(start_date, end_date, pc, ps, pc1, ps1, n_clicks):
    df,strpx,data,tp,fnn,pfavg = filter_gradetab(start_date, end_date, pc, ps)
    pfavg2 = pfavg[['course_name','Avg_of_passed Trainees',
                    'Avg_of_failed Trainees']]
    pfavg['index'] = range(1, len(pfavg) + 1)
    data1 = pfavg.iloc[pc1*ps1:(pc1+ 1)*ps1].to_dict('records')
    nc4 = "Number of Courses: "+str(df.shape[0])
    nc41 = "Number of Courses: "+str(pfavg2.shape[0])
    if n_clicks == 0:
        return None, strpx, data, data1, nc4,tp,nc41,tp
    else:
        if n_clicks != 0:
            try:
                fnold = 'GradeSummary212'
                files =  glob.glob(path_3+'*.xlsx')
                if (path_3 + fnold + '.xlsx') in files:
                    os.remove(path_3 + fnold + '.xlsx')                
                save_fmt_report(df, path_3, fnold, flags[2])
                fn = path_3+'GradeSmry_'+fnn+'.xlsx'
                if fn in files:
                    os.remove(fn) 
                fnold = path_3+fnold+'.xlsx'
                os.rename(r''+fnold, r''+fn)                

                fnold11 = 'PassedFailed212'                
                if path_3 + fnold11 + '.xlsx' in files:
                    os.remove(path_3 + fnold11 + '.xlsx')                
                save_fmt_report(pfavg2, path_3, fnold11, 'pf')
                fn11 = path_3+'PassedFailedPercent_'+fnn+'.xlsx'
                if fn11 in files:
                    os.remove(fn11) 
                fnold11 = path_3+fnold11+'.xlsx'
                os.rename(r''+fnold11, r''+fn11)
            except:
                print("[Error]:", sys.exc_info()[0])
            else:
                print(f"{fn} {fn11} were saved successfully!")
            finally:
                n_clicks = 0
            return None, strpx, data,data1, nc4,tp,nc41,tp

#******************************************************************************
@app.callback([
    dash.dependencies.Output('container-button-ad', 'children'),
    dash.dependencies.Output('tablead', 'data'),
    dash.dependencies.Output('page_counter_ad', 'children'),
    dash.dependencies.Output('page_shower_ad', 'children')],
    [dash.dependencies.Input('tablead', "page_current"),
     dash.dependencies.Input('tablead', "page_size"),
     dash.dependencies.Input('save_button_ad','n_clicks')])

def update_output_ad(pc, ps, n_clicks):
    graad = gra[grade_columns3]
    graad['year']=graad['course_id'].str.split('_')
    graad['year']=graad['year'].apply(lambda x:x[1])      
    grah = graad[graad['Final Exam']=='H']      
    ad1, ad2 = grah[grade_columns4], grah[grade_columns4]
    print("yearad1", ad1) 
    print("yearad2", ad2)  
    ad1['index'] = range(1, len(ad1) + 1)
    tp = 'Total Pages: ' + str(ceil(ad1.shape[0]/PAGE_SIZE))
    nc5 = "Number of Courses: "+str(ad2.shape[0])
    if n_clicks == 0:
        return None, ad1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),nc5,tp
    else:
        try:
            fname = "grades_academicDishonesty"
            files =  glob.glob(path_3+'*.xlsx')
            if (path_3 + fname + '.xlsx') in files:
                os.remove(path_3 + fname + '.xlsx')
            save_fmt_report(ad2, path_3, fname, 'ad')
        except:
            print("[Error]:", sys.exc_info()[0])
        else:
            print(f"{fname} was saved successfully!")
        finally:
            n_clicks =0
        return None, ad1.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),nc5,tp

#******************************************************************************
#*************************************
# 9.3 Demographic Analysis Tables
#*************************************
#*************************************
# BU vs Non-BU by course_abb and date range.
@app.callback([
    dash.dependencies.Output('output-container-date-picker-range3', 'children'),
    dash.dependencies.Output('update_bu_table1', 'children'),
    dash.dependencies.Output('container-button-bnb', 'children'),
    dash.dependencies.Output('counter_budem', 'children')],
    [dash.dependencies.Input('course_abb_picker', 'value'),
     dash.dependencies.Input('my-date-picker-range3', 'start_date'),
     dash.dependencies.Input('my-date-picker-range3', 'end_date'),
     dash.dependencies.Input('save_bnb','n_clicks')])
#-------------------------------------
def update_BUvsNonBU(abb, start_date, end_date, n_clicks):
    string_prefix, fnn = 'Selected Dates: ', ''
    start_date = dtt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    start_date_string = start_date.strftime('%B %d, %Y')
    string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    fnn = fnn + start_date.strftime("%Y")+start_date.strftime("%B")[:3]+\
          start_date.strftime("%d")

    end_date = dtt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    end_date_string = end_date.strftime('%B %d, %Y')
    fned = end_date.strftime('%Y_%m_%d')
    string_prefix = string_prefix + 'End Date: ' + end_date_string
    fnn = fnn+'_to_'+end_date.strftime("%Y")+end_date.strftime("%B")[:3]+\
    end_date.strftime("%d")

    drange = [(start_date + timedelta(days=x)).strftime("%d/%m/%Y")
              for x in range((end_date-start_date).days + 1)]

    bnb = bnb1[bnb1['course_abb'] == abb]
    bnbu = bnb[bnb['startDate'].isin(drange)]
    bnbu  = bnbu[['object', 'count']]
    bnbu.columns = ['Institution', 'Count']
    bnbu = bnbu.groupby(['Institution']).sum().reset_index()
    nc6 = "Number of Institutions: "+str(bnbu.shape[0])
    if n_clicks != 0:
        try:
            fname1 = 'BUNonBU_xxx'
            files =  glob.glob(path_3+'*.xlsx')
            if (path_3 + fname1 + '.xlsx') in files:
                os.remove(path_3 + fname1 + '.xlsx')        
            save_additional(bnbu, path_3, fname1, 'bunbuabb')
            fname = 'BUNonBU_'+abb+'_'+fnn
            if path_3 + fname+'.xlsx' in files:
                os.remove(path_3 + fname+'.xlsx') 
            os.rename(r''+path_3+fname1+'.xlsx', r''+path_3+fname+'.xlsx')
        except:
            print("[Error]:", sys.exc_info()[0])
        else:
            print(f"{fname} was saved successfully!")
        finally:
            n_clicks = 0
    return None,  html.Div([
                            dt.DataTable(
                               id='table4',
                               columns=[{"name": i,
                                            "id": i} for i in bnbu.columns],
                                data=bnbu.to_dict('records'),
                                style_table={'margin-left': '200x'},
                                style_header={'backgroundColor': 'white',
                                              'fontWeight': 'bold',
                                              'font_size': '23px',
                                              'border': '1px solid black'},
                                style_cell={'textAlign': 'center',
                                                        'whiteSpace':'normal',
                                                        'font_size': '17px'},
                                style_cell_conditional=[
                                            {'if': {'column_id': 'Region'},
                                             'textAlign': 'left'}],
                                style_data={ 'border': '1px solid blue' },
                                style_data_conditional=[
                                    {'if': {'row_index': 'odd'},
                                    'backgroundColor': 'rgb(248, 248, 248)'}],
                                export_format='xlsx',
                                export_headers='display')
                         		 ]), None, nc6

#******************************************************************************
#*************************************
# BU vs Non-BU by course_id
@app.callback([
    dash.dependencies.Output('container-button-bnb2', 'children'),
    dash.dependencies.Output('update_cid_table', 'children'),
    dash.dependencies.Output('counter_cid_table', 'children')],
    [dash.dependencies.Input('course_cid_picker', 'value'),
     dash.dependencies.Input('save_bnb2','n_clicks')])
#-------------------------------------
def update_BUvsNonBU(cid,n_clicks):
    bnb = bnb1[bnb1['course_id'] == cid]
    bnbu  = bnb[['object', 'count']]
    bnbu.columns = ['Institution', 'Count']
    #print('bnbu',bnbu)
    nc7 = "Number of Institutions: "+str(bnbu.shape[0])
    if cid == 'None':
        return None, None,nc7
    else:
        if n_clicks!=0:
            try:
                fname = 'BUNonBU_'+cid
                files =  glob.glob(path_3+'*.xlsx')
                if path_3 + fname + '.xlsx' in files:
                    os.remove(path_3 + fname + '.xlsx')        
                save_additional(bnbu, path_3, fname, 'bunbucid')                
            except:
                print("[Error]:", sys.exc_info()[0])
            else:
                print(f"{fname} was saved successfully!")
            finally:
                n_clicks = 0 
        return None, html.Div([
                    dt.DataTable(
                        id='table5',
                        columns=[{"name": i, "id": i} for i in bnbu.columns],
                        data=bnbu.to_dict('records'),
                        style_table={'margin-left': '200x'},
                        style_header={'backgroundColor': 'white',
                                          'fontWeight': 'bold',
                                          'font_size': '23px',
                                           'border': '1px solid black'},
                        style_cell={'textAlign': 'center',
                                                    'whiteSpace':'normal',
                                                    'font_size': '17px'},
                        style_cell_conditional=[
                                       {'if': {'column_id': 'Region'},
                                        'textAlign': 'left'}],
                        style_data={ 'border': '1px solid blue' },
                        style_data_conditional=[
                                {'if': {'row_index': 'odd'},
                                'backgroundColor': 'rgb(248, 248, 248)'}],
                        export_format='xlsx',
                        export_headers='display')
                     ]),nc7
#******************************************************************************
#*************************************
# Trainees/Students by Departments
@app.callback(
  dash.dependencies.Output('graph_dept', 'figure'),
  [dash.dependencies.Input('course_cid_picker_dept5', 'value')])
#-------------------------------------
def update_piechart(val):
    deptc = ['course_id', 'Department:','Fee Type','course_abb','startDate']
    budepts = reg[deptc]
    #budepts = budepts[budepts['Fee Type'].isin(dpts)]
    budepts['count']=1
    byDept= budepts[budepts['course_id'] == val]
    byDept = byDept[['Department:', 'count']]
    gdept = byDept.groupby(['Department:']).sum().reset_index()
    gdept.columns = ['Department', 'Count']
    fig = go.Figure(data=[go.Pie(labels = gdept['Department'],
                             values = gdept['Count'])])
    fig.update_layout(template="plotly_dark",
                    width=1100,
                    height=1000,
                    margin=dict(r=30, t=30, b=30, l=30),
                    bargap = 0,
                    uniformtext_minsize=8,
                    uniformtext_mode='hide')
    return fig

#******************************************************************************
# A function that filters the demographic data by dept to create a table.
def filter_demos(pc, ps, start_date, end_date, crs, cid, by):
    spx, fnn = '',''
    start_date = dtt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    start_date_string = start_date.strftime('%B %d, %Y')
    spx = spx + start_date_string + ' | '
    fnn = fnn + start_date.strftime("%Y")[2:]+start_date.strftime("%B")[:3]\
          + start_date.strftime("%d")

    end_date = dtt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    end_date_string = end_date.strftime('%B %d, %Y')
    spx = spx + end_date_string
    fnn=fnn+'_to_'+end_date.strftime("%Y")[2:]+end_date.strftime("%B")[:3]\
          + end_date.strftime("%d")

    drange = [(start_date + timedelta(days=x)).strftime("%d/%m/%Y")
              for x in range((end_date-start_date).days + 1)]

    budepts = dem[['course_id', 'course_abb','object', 'by','count','startDate']]   
    res = budepts[budepts['startDate'].isin(drange)]
    #print("res@time:", res)
    print(f"crs:{crs}, cid: {cid}, by: {by}")
    def output(res, pc, ps, fnn):
        res.columns = ["Categories", "Count"] 
        res.sort_values(by='Count', ascending=False, inplace=True)
        df2 = res[["Categories", "Count"]]
        res['index'] = range(1, len(res) + 1)
        tp = 'Total Pages: '+ str(ceil(res.shape[0]/PAGE_SIZE20))
        print("PAGE_SIZE20:", PAGE_SIZE20)
        return df2, spx, res.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,fnn

    if by != None and cid != None and (crs == "All" or crs != "All"):        
        res = res[res['course_id'] == cid]
        res = res[res['by'] == by]
        res = res[['object', 'count']]
        return output(res, pc, ps, fnn)
    elif by != None and cid == None and crs == "All":
        res = res[['object', 'by','count']]        
        res = res[res['by'] == by]
        res = res[['object', 'count']]
        return output(res, pc, ps, fnn)    
    elif by != None and cid == None and crs != "All":
        res = res[res['course_abb'] == crs]       
        res = res[res['by'] == by]
        res = res[['object', 'count']]
        return output(res, pc, ps, fnn)  
    elif by == None and cid == None and crs != "All":
        res = res[res['course_abb'] == crs]         
        res = res[['object', 'count']]
        return output(res, pc, ps, fnn)      
    elif by == None and cid != None and (crs == "All" or crs != "All"): 
        res = res[res['course_id'] == cid]       
        res = res[['object', 'count']]
        return output(res, pc, ps, fnn)         
    else:        
        res = res[['object', 'count']]
        return output(res, pc, ps, fnn)    
    
#******************************************************************************
#html.Div(id="update_table_dept")
@app.callback([
  dash.dependencies.Output('container-button-dept', 'children'),
  dash.dependencies.Output('output-container-date-picker-range5', 'children'),
  dash.dependencies.Output('datatablewthpaging', 'data'),
  dash.dependencies.Output('page_counter_dept', 'children'),
  dash.dependencies.Output('page_shower_dept', 'children')],
  [dash.dependencies.Input('datatablewthpaging', 'page_current'),
   dash.dependencies.Input('datatablewthpaging', 'page_size'),
   dash.dependencies.Input('my-date-picker-rangedept', 'start_date'),
   dash.dependencies.Input('my-date-picker-rangedept', 'end_date'),
   dash.dependencies.Input('outputDemCrsPicker', 'value'),
   dash.dependencies.Input('outputDemIdPicker', 'value'),
   dash.dependencies.Input('outputDemCatPicker', 'value'),
   dash.dependencies.Input('save_button_dept', 'n_clicks')])
   #-------------------------------------
def update_demos(pc, ps, start_date, end_date, crs, cid, by,n_clicks):
    df,strpx, data, tp, fnn = filter_demos(pc, ps, start_date, 
                                          end_date, crs, cid, by)
    nc8 = "Number of Categories: "+str(df.shape[0])
    #print("data:",data)
    if n_clicks == 0:
        return None, strpx, data, nc8,tp
    else:
        try:
            if by != None:
                nameme = by
            elif crs != "All" and by == None:
                nameme = crs+"_categries"
            else:                
                nameme = "all_categries"               

            fnold = 'BU202002xx'           
            files =  glob.glob(path_3+'*.xlsx')
            if (path_3 + fnold + '.xlsx') in files:
                os.remove(path_3 + fnold + '.xlsx')
            save_fmt_report(df, path_3, fnold, flags[3])
            fn = path_3 + nameme+"_"+fnn+'.xlsx'
            if fn in files:
                os.remove(fn) 
            fnold = path_3 + fnold + '.xlsx'
            os.rename(r''+fnold, r''+fn)
        except:
            print("[Error]:", sys.exc_info()[0])
        else:
            print(f"{fn} was saved successfully!")
        finally:
            n_clicks = 0
        return None, strpx, data, nc8, tp
#******************************************************************************
#******************************************************************************
# 9.4 Profit Analysis
#*************************************
#*************************************
@app.callback([
    dash.dependencies.Output('container-button-prof', 'children'),
    dash.dependencies.Output('output-container-date-picker-rangepc','children'),
    dash.dependencies.Output('update_pc_table', 'children')],
    [dash.dependencies.Input('course_pc_picker', 'value'),
     dash.dependencies.Input('my-date-picker-rangepc', 'start_date'),
     dash.dependencies.Input('my-date-picker-rangepc', 'end_date'),
     dash.dependencies.Input('save_prof','n_clicks')])
#-------------------------------------
def update_profitcourse(crs_abb,start_date, end_date, n_clicks):
    string_prefix, fnn = 'Selected Dates: ', ''
    start_date = dtt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    start_date_string = start_date.strftime('%B %d, %Y')
    string_prefix = string_prefix + 'Start Date: ' + start_date_string + ' | '
    fnn = fnn + start_date.strftime("%Y")+start_date.strftime("%B")[:3]+\
          start_date.strftime("%d")
    end_date = dtt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    end_date_string = end_date.strftime('%B %d, %Y')
    fned = start_date.strftime('%Y_%m_%d')
    string_prefix = string_prefix + 'End Date: ' + end_date_string
    fnn = fnn+'_to_'+end_date.strftime("%Y")+end_date.strftime("%B")[:3]+\
        end_date.strftime("%d")

    drange = [(start_date + timedelta(days=x)).strftime("%d/%m/%Y")
          for x in range((end_date-start_date).days + 1)]
    #print("profit",drange)
    #prof = pft[pft.columns]

    if (crs_abb == 'None') or ('xxx' in prof['course_id'].tolist()==True):
        return None, string_prefix, None
    else:
        prof0 = prof[prof['startDate'].isin(drange)]
        cprof= prof0[prof0['course_abb'] == crs_abb]
        clprof = ['course_id',  'Type', 'Amount']
        if cprof.shape[0] == 0:
            return None, string_prefix, None
        else:
            prof1 = cprof[clprof]
            prof2 = prof1[prof1['Type'].isin(type_col)]
            prof3 = prof2.groupby(['Type']).sum().reset_index()
            tmplst = prof3['Type'].tolist()
            keys = [sort_dict2[tmplst[i]] for i in range(len(tmplst))]
            prof3['key']=keys
            prof3.sort_values('key', inplace=True)
            prof4 = prof3[['Type', 'Amount']]
            pfttmp = prof4['Amount'][prof4['Type']=='Profit'].tolist()[0]
            ti = prof4['Amount'][prof4['Type']=='Total Income'].tolist()[0]
            pt = {'Type':['profit%'],'Amount':[round(pfttmp*100/(ti),2)]}
            prof5 = pd.concat([prof4,pd.DataFrame(pt)], ignore_index=True)
            prof5 = prof5.round(2)

            if n_clicks != 0:
                try:
                    fname1 = 'profit_xxx'
                    files =  glob.glob(path_3+'*.xlsx')
                    if (path_3 + fname1 + '.xlsx') in files:
                        os.remove(path_3 + fname1 + '.xlsx')        
                    save_additional(prof5, path_3, fname1, 'profabb')  
                    fname = 'profit_'+fnn
                    if path_3 + fname+'.xlsx' in files:
                         os.remove(path_3 + fname+'.xlsx') 
                    os.rename(r''+path_3+fname1+'.xlsx', r''+path_3+fname+'.xlsx')              
                except:
                    print("[Error]:", sys.exc_info()[0])
                else:
                    print(f"{fname} was saved successfully!")
                finally:
                    n_clicks = 0 
            return None, string_prefix,  html.Div([dt.DataTable(
                            		id='table3',
                        columns=[{"name": i, "id": i} for i in prof5.columns],
                            		data=prof5.to_dict('records'),
                            		style_table={'margin-left': '200x'},
                            		style_header={'backgroundColor': 'white',
                                          'fontWeight': 'bold',
                                          'font_size': '23px',
                                          'border': '1px solid black'},
                            		style_cell={'textAlign': 'right',
                                                    'whiteSpace':'normal',
                                                    'font_size': '17px'},
                            		style_cell_conditional=[
                                        {'if': {'column_id': 'Region'},
                                         'textAlign': 'left'}],
                            		style_data={ 'border': '1px solid blue' },
                            		style_data_conditional=[
                                    	{'if': {'row_index': 'odd'},
                                     'backgroundColor': 'rgb(248, 248, 248)'}],
                                    export_format='xlsx',
                                    export_headers='display')
                     		      ])
#******************************************************************************
#*************************************
# Profit Analysis by course_id
@app.callback([
    dash.dependencies.Output('container-button-prof2', 'children'),
    dash.dependencies.Output('update_pc_table2', 'children')],
    [dash.dependencies.Input('course_pc_picker2', 'value'),
    dash.dependencies.Input('save_prof2','n_clicks')])
#-------------------------------------
def update_profitcurrent(selected_course_id, n_clicks):
    byprof= prof[prof['course_id'] == selected_course_id]
    lg1 = ('xxx' in byprof['course_id'].tolist()==True)
    prof2 = byprof[profc]
    prof2 =prof2.round(2)
    if selected_course_id == 'None' or prof2.shape[0]==0 or lg1:
        return None, None
    else:
        tmpx1 = prof2['Type'].tolist()
        keysx1 = [sort_dict[tmpx1[i]] for i in range(len(tmpx1))]
        prof2['key']=keysx1
        prof2.sort_values('key', inplace=True)
        prof2 = prof2[profc]
        if n_clicks != 0:
            try:
                fname = 'profit_'+selected_course_id
                files =  glob.glob(path_3+'*.xlsx')
                if (path_3 + fname + '.xlsx') in files:
                        os.remove(path_3 + fname + '.xlsx')        
                save_additional(prof2, path_3, fname, 'profcid')              
            except:
                print("[Error]:", sys.exc_info()[0])
            else:
                print(f"{fname} was saved successfully!")
            finally:
                n_clicks = 0       
        return None, html.Div([dt.DataTable(
                    id='table5',
                    columns=[{"name": i, "id": i} for i in prof2.columns],
                    data=prof2.to_dict('records'),
                    style_table={'margin-left': '200x'},
                    style_header={'backgroundColor': 'white',
                                          'fontWeight': 'bold',
                                          'font_size': '23px',
                                           'border': '1px solid black'},
                    style_cell={'textAlign': 'right',
                                                    'whiteSpace':'normal',
                                                    'font_size': '17px'},
                    style_cell_conditional=[
                                       {'if': {'column_id': 'Region'},
                                        'textAlign': 'left'}],
                    style_data={ 'border': '1px solid blue' },
                    style_data_conditional=[
                            {'if': {'row_index': 'odd'},
                            'backgroundColor': 'rgb(248, 248, 248)'}],
                    export_format='xlsx',
                    export_headers='display')
                ])

#******************************************************************************
#*************************************
# Summarized cost-profit analysis of courses offered in a range of time
#-------------------------------------
#******************************************************************************
# A function that filters a profit_summary sql table by date-range
def filter_profitsmry(start_date, end_date, pc, ps, pfs):
    #time filter here
    spx, fnn = '',''
    start_date = dtt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    start_date_string = start_date.strftime('%B %d, %Y')
    spx = spx + start_date_string + ' | '
    fnn = fnn + start_date.strftime("%Y")+start_date.strftime("%B")+\
          start_date.strftime("%d")

    end_date = dtt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    end_date_string = end_date.strftime('%B %d, %Y')
    spx = spx + end_date_string
    fnn = fnn +'_to_'+end_date.strftime("%Y")+end_date.strftime("%B")+\
          end_date.strftime("%d")

    drange = [(start_date + timedelta(days=x)).strftime("%d/%m/%Y")
              for x in range((end_date-start_date).days + 1)]
    fcol = ['course_abb', 'startDate','total_income',
                'total_cost','profit', 'profit%']
    profsmry = pfs[fcol]
    profsmry1 = profsmry[profsmry['startDate'].isin(drange)]

    pscl = ['course_abb', 'total_income', 'total_cost', 'profit', 'profit%']
    profsmry2 = profsmry1[list(profsmry1.columns)]
    psgpd = profsmry2.groupby(['course_abb']).sum().reset_index()
    psgpd['profit%'] = psgpd['profit']/psgpd['total_income']*100


    aclm = acl[acl.columns]
    aclm.columns = ['course_name', 'course_abb', 'cost_model']
    aclm = aclm[['course_name', 'course_abb']]
    psmry2 = aclm.merge(psgpd, on ='course_abb',how='inner')

    pscl = ['course_name', 'total_income', 'total_cost', 'profit', 'profit%']
    psmry2 = psmry2[pscl]

    profsmrydict ={'course_name':['Total'],'total_income':\
                   [psmry2['total_income'].sum()],
              'total_cost':[psmry2['total_cost'].sum()],
              'profit':[psmry2['profit'].sum()],
              'profit%':[psmry2['profit'].sum()/psmry2['total_income'].sum()*100]}

    psmry2new = pd.concat([psmry2, pd.DataFrame(profsmrydict)])
    psmry2new = psmry2new.round(2)
    psmry3 = psmry2new[pscl]

    psmry2new['index'] = range(1, len(psmry2new) + 1)
    tp = 'Total Pages: '+ str(ceil(psmry2new.shape[0]/PAGE_SIZE))
    return psmry3,spx,psmry2new.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,fnn
#******************************************************************************
@app.callback([
  dash.dependencies.Output('container-button-pcs', 'children'),
  dash.dependencies.Output('date_container_pcs', 'children'),
  dash.dependencies.Output('pcs_table', 'data'),
  dash.dependencies.Output('page_counter_pcs', 'children'),
  dash.dependencies.Output('page_shower_pcs', 'children')],
  [dash.dependencies.Input('date_picker_pcs', 'start_date'),
   dash.dependencies.Input('date_picker_pcs', 'end_date'),
   dash.dependencies.Input('pcs_table', "page_current"),
   dash.dependencies.Input('pcs_table', "page_size"),
   dash.dependencies.Input('save_button_pcs','n_clicks')])
   #-------------------------------------
def update_pcstable(start_date, end_date, pc, ps, n_clicks):
    pfs = profsmry
    df,strpx, data, tp, fnn = filter_profitsmry(start_date, end_date,pc,ps,pfs)
    nc9 = "Number of Courses: "+str(df.shape[0])
    if n_clicks == 0:
        return None, strpx, data, nc9,tp
    else:
        try:
            fnold = "Profit202002xx"            
            files =  glob.glob(path_3+'*.xlsx')
            if (path_3 + fnold + '.xlsx') in files:
                os.remove(path_3 + fnold + '.xlsx')
            save_fmt_report(df, path_3, fnold, flags[4])
            fn = path_3 + 'ProfitCostSummary_'+fnn+'.xlsx'
            if fn in files:
                os.remove(fn) 
            fnold = path_3 + fnold + '.xlsx'
            os.rename(r''+fnold, r''+fn)
        except:
            print("[Error]:", sys.exc_info()[0])
        else:
            print(f"{fn} was saved successfully!")
        finally:
            n_clicks = 0
        return None, strpx, data, nc9, tp
#******************************************************************************
#*************************************
# Registrant-Income Report
#-------------------------------------
#******************************************************************************
# A function that filters a profit_summary sql table by date-range
def filter_regin(start_date, end_date, pc, ps):
    #time filter here
    spx, fnn = '',''
    start_date = dtt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    start_date_string = start_date.strftime('%B %d, %Y')
    spx = spx + start_date_string + ' | '
    fnn = fnn + start_date.strftime("%Y")+start_date.strftime("%B")+\
          start_date.strftime("%d")

    end_date = dtt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    end_date_string = end_date.strftime('%B %d, %Y')
    spx = spx + end_date_string
    fnn = fnn +'_to_'+end_date.strftime("%Y")+end_date.strftime("%B")+\
          end_date.strftime("%d")

    drange = [(start_date + timedelta(days=x)).strftime("%d/%m/%Y")
              for x in range((end_date-start_date).days + 1)]
    tmp = regincome[regincome['startDate'].isin(drange)]
    tmp1, tmp2  = tmp[colregin],tmp[colregin]
    tmp2['index'] = range(1, len(tmp2) + 1)
    tp = 'Total Pages: '+ str(ceil(tmp2.shape[0]/PAGE_SIZE))
    return tmp1,spx,tmp2.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,fnn 
#******************************************************************************
@app.callback([
  dash.dependencies.Output('container-button-regin', 'children'),
  dash.dependencies.Output('date_container_regin', 'children'),
  dash.dependencies.Output('regin_table', 'data'),
  dash.dependencies.Output('page_counter_regin', 'children'),
  dash.dependencies.Output('page_shower_regin', 'children')],
  [dash.dependencies.Input('date_picker_regin', 'start_date'),
   dash.dependencies.Input('date_picker_regin', 'end_date'),
   dash.dependencies.Input('regin_table', "page_current"),
   dash.dependencies.Input('regin_table', "page_size"),
   dash.dependencies.Input('save_button_regin','n_clicks')])
   #-------------------------------------
def update_pcstable(start_date, end_date, pc, ps, n_clicks):
    df,strpx, data, tp, fnn = filter_regin(start_date, end_date, pc, ps)
    lsti = ['Grand Total','Subtotal']
    tmpdf = df[~df['Month/Year'].isin(lsti)]
    nc10 = "Number of Courses: "+str(tmpdf.shape[0])
    if n_clicks == 0:
        return None, strpx, data, nc10, tp
    else:
        try:
            fnold = "regin2021xxxx"           
            files =  glob.glob(path_3+'*.xlsx')
            if path_3 + fnold + '.xlsx' in files:
                os.remove(path_3 + fnold + '.xlsx')                
            save_fmt_report(df, path_3, fnold, flags[4])
            fn = path_3 + 'RegistrantIncomeSummary_'+fnn+'.xlsx'            
            if fn in files:
                os.remove(fn)  
            fnold = path_3 + fnold + '.xlsx'
            os.rename(r''+fnold, r''+fn)
        except:
            print("[Error]:", sys.exc_info()[0])
        else:
            print(f"{fn} was saved successfully!")
        finally:
            n_clicks = 0
        return None, strpx, data, nc10, tp   
#******************************************************************************
#**************************************
# 9.5 Surveys app.callbacks
#*************************************#
# Functions for filtering the Survey df to generate statistics
  # and Net Promoter Score (NPS)
def gen_nps(tmp):
    tmp['prod'] = tmp['count']*tmp['scores']
    tmp9 = tmp[tmp['qnum'].isin([9])]
    tmp9a = tmp[['opinion','count']]
    tmp9a['opinion']=tmp9a['opinion'].astype(str)

    tmp16 = tmp9a[tmp9a['opinion'].isin(['1','2','3','4','5','6',
                '1.0','2.0','3.0','4.0','5.0','6.0'])]
    tmp16['count'] = pd.to_numeric(tmp16['count'])
    tmp16['opinion']= pd.to_numeric(tmp16['opinion'])
    tmp16['prod'] = tmp16['count']*tmp16['opinion']

    tmp78 = tmp9a[tmp9a['opinion'].isin(['7','8','7.0','8.0'])]
    tmp78['count'] = pd.to_numeric(tmp78['count'])
    tmp78['opinion']= pd.to_numeric(tmp78['opinion'])
    tmp78['prod'] = tmp78['count']*tmp78['opinion']

    tmp910 = tmp9a[tmp9a['opinion'].isin(['9','10','9.0','10.0'])]
    tmp910['count'] = pd.to_numeric(tmp910['count'])
    tmp910['opinion']= pd.to_numeric(tmp910['opinion'])
    tmp910['prod'] = tmp910['count']*tmp910['opinion']

    tmpall = pd.concat([tmp16, tmp78, tmp910])
    print(tmpall)

    #NPS = (((#9 + #10)/# of Total Ratings) -
    #       ((#6+#5+#4+#3+#2+#1)/# of Total Ratings))) x 100%
    nps1 = (tmp910['count'].sum()-tmp16['count'].sum())
    nps = nps1/tmpall['count'].sum()*100
    return round(nps,2)

def computestat(tmp, cntc):
    try:
        tmp['count'] = pd.to_numeric(tmp['count'])
        tmp['scores'] = pd.to_numeric(tmp['scores'])
        tmp['prod'] = tmp['count']*tmp['scores']
        tmp['qnum']=tmp['qnum'].astype(str)
        tmpencoded = tmp[tmp['qnum'].isin(['1','2','3','7','8',
        '1.0','2.0','3.0','7.0','8.0'])]
        stat1 = tmpencoded['scores'].tolist()
        cnt1 = tmpencoded['count'].tolist()
        stat = []
        for i in range(len(cnt1)):
            for j in range(cnt1[i]):
                stat.append(stat1[i])
        stats = []
        count = len(stat)
        stats.append(round(np.mean(stat),2))
        stats.append(round(np.std(stat),2))
        stats.append(np.min(stat))
        stats.append(np.percentile(stat, 25))
        stats.append(np.percentile(stat, 50))
        stats.append(np.percentile(stat, 75))
        stats.append(np.max(stat))
        stattics = {'Count':[cntc],'Mean':[stats[0]],'STD':[stats[1]],
                    'MIN':[stats[2]],'25%':[stats[3]],'50%':stats[4],
                    '75%':[stats[5]], 'MAX':[stats[6]]}
        dfst = pd.DataFrame(stattics)
    except:
        print("Input dataframe to this section is empty!")
        if tmp.empty == False:
            tmp['count'] = pd.to_numeric(tmp['count'])
            tmpp = tmp[list(tmp.columns)]
            tmpcnt = tmpp[tmpp['questions']==\
                              'Your Likelihood to Recommend this course?']
            cnt = tmpcnt['count'].sum()
        else:
            cnt = 0
        errorz = {'Count':[cnt],'Mean':[0],'STD':[0],'MIN':[0],
            '25%':[0],'50%':[0],'75%':[0],
            'MAX':[0]}
        dfst0 = pd.DataFrame(errorz)
        return dfst0
    else:
        return dfst
#******************************************************************************
def count_resp(df):
    tmpt = df[list(df.columns)]
    tmpt['count'] = pd.to_numeric(tmpt['count'])
    tmpcnt = tmpt[tmpt['questions']==\
                      'Your Likelihood to Recommend this course?']
    return tmpcnt['count'].sum()
#******************************************************************************
# Function for gauge graph
def gen_gauge(nps, tit):
    #nps = df['NPS'].tolist()[0]
    fig = go.Figure(go.Indicator(
            mode = "gauge+number+delta",
            value = nps,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': tit+" \nNet Promoter Score (NPS)",
                                               'font': {'size': 24}},
            delta = {'reference': 0, 'increasing': {'color': "green"}},
            gauge = {
                    'axis': {'range': [0, 100], 'tickwidth': 1,
                    'tickcolor': "darkblue"},
                    'bar': {'color': "darkblue"},
                    'bgcolor': "white",
                    'borderwidth': 2,
                    'bordercolor': "gray",
                    'steps': [
                        {'range': [0, 20], 'color': 'red'},
                        {'range': [21, 40], 'color': 'peru'},
                        {'range': [41, 60], 'color': 'orange'},
                        {'range': [61, 80], 'color': 'YellowGreen'},
                        {'range': [81, 100], 'color': 'DarkGreen'}],
                    'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 81}}))

    fig.update_layout(paper_bgcolor = "lavender",
                      font = {'color': "darkblue", 'family': "Arial"})
    return fig
#******************************************************************************
#*************************************
# Callback for stat and nps table
@app.callback([
  dash.dependencies.Output('container-button-nps', 'children'),
  dash.dependencies.Output('date_container_nps', 'children'),
  dash.dependencies.Output('sur_statabnps', 'data'),
  dash.dependencies.Output('nps_gauge', 'figure')],
  [dash.dependencies.Input('date_picker_nps', 'start_date'),
   dash.dependencies.Input('date_picker_nps', 'end_date'),
   dash.dependencies.Input('course_ab_statnps', "value"),
   dash.dependencies.Input('course_id_statnps', 'value'),
   dash.dependencies.Input('course_qn_statnps', 'value'),
   dash.dependencies.Input('save_nps', 'n_clicks')])

def calc_svyr(start_date, end_date, ca, ci, qn, n_clicks):
    spx, fnn = '', ''
    start_date = dtt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    start_date_string = start_date.strftime('%B %d, %Y')
    spx = spx + start_date_string + ' | '
    fnn = fnn + start_date.strftime("%Y")+start_date.strftime("%B")[:3]+\
          start_date.strftime("%d")

    end_date = dtt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    end_date_string = end_date.strftime('%B %d, %Y')
    spx = spx + end_date_string
    fnn = fnn+'_to_'+end_date.strftime("%Y")+end_date.strftime("%B")[:3]+\
    end_date.strftime("%d")

    drange = [(start_date + timedelta(days=x)).strftime("%d/%m/%Y")
              for x in range((end_date-start_date).days + 1)]

    qn = npslst[qn]
    tmp = svyq[list(svyq.columns)]
    
    if ca != None and (ci == None or ci != None):
        tmp = tmp[tmp['startDate'].isin(drange)]
        tmp = tmp[tmp['course_abb']==ca]
        cntc = count_resp(tmp)
        nps = gen_nps(tmp)
        gph = gen_gauge(nps, ca)
        tmp = tmp[tmp['qnum']==qn]
        dfst = computestat(tmp, cntc)

        if n_clicks != 0:
            try:
                fname1 = 'npstat_xxx'
                files =  glob.glob(path_3+'*.xlsx')
                if (path_3 + fname1) in files:
                        os.remove(path_3 + fname1)        
                save_additional(dfst, path_3, fname1, 'npstat')
                fname = 'survey_stat_'+ca+'_'+'Q'+str(qn)+'_'+fnn
                if path_3 + fname+'.xlsx' in files:
                    os.remove(path_3 + fname+'.xlsx') 
                os.rename(r''+path_3+fname1+'.xlsx', r''+path_3+fname+'.xlsx')             
            except:
                print("[Error]:", sys.exc_info()[0])
            else:
                print(f"{fname} was saved successfully!")
            finally:
                n_clicks = 0  
        return None, spx, dfst.to_dict('records'),gph

    elif ca == None and ci != None:
        tmp = tmp[tmp['course_id']==ci]
        cntc = count_resp(tmp)
        nps = gen_nps(tmp)
        gph = gen_gauge(nps, ci)
        tmp = tmp[tmp['qnum']==qn]
        dfst = computestat(tmp, cntc)

        if n_clicks != 0:
            try:
                fname = 'survey_stat_'+ci+'_'+'Q'+str(qn)
                files =  glob.glob(path_3+'*.xlsx')
                if (path_3 + fname+'.xlsx') in files:
                        os.remove(path_3 + fname+'.xlsx')        
                save_additional(dfst, path_3, fname, 'npstat')
                fname = 'survey_stat_'+ca+'_'+'Q'+str(qn)+'_'+fnn
                if path_3 + fname+'.xlsx' in files:
                    os.remove(path_3 + fname+'.xlsx') 
                os.rename(r''+path_3+fname1+'.xlsx', r''+path_3+fname+'.xlsx')             
            except:
                print("[Error]:", sys.exc_info()[0])
            else:
                print(f"{fname} was saved successfully!")
            finally:
                n_clicks = 0 
        return None, spx, dfst.to_dict('records'), gph

    else:
        tit = 'Date Ranges'
        tmp = tmp[tmp['startDate'].isin(drange)]
        cntc = count_resp(tmp)
        nps = gen_nps(tmp)
        gph = gen_gauge(nps, tit)
        tmp = tmp[tmp['qnum']==qn]
        dfst = computestat(tmp, cntc)

        if n_clicks != 0:
            try:
                fname1 = 'npstat_xxx'
                files =  glob.glob(path_3+'*.xlsx')
                if (path_3 + fname1+'.xlsx') in files:
                        os.remove(path_3 + fname1+'.xlsx')        
                save_additional(dfst, path_3, fname1, 'npstat')
                fname = 'survey_stat_dateRange'+'Q'+str(qn)+'_'+fnn
                if path_3 + fname+'.xlsx' in files:
                    os.remove(path_3 + fname+'.xlsx') 
                os.rename(r''+path_3+fname1+'.xlsx', r''+path_3+fname+'.xlsx')             
            except:
                print("[Error]:", sys.exc_info()[0])
            else:
                print(f"{fname} was saved successfully!")
            finally:
                n_clicks = 0 
        return None, spx, dfst.to_dict('records'), gph

#*******************************************************************************
# Grouped Subplots of Barcgarts
def update_barsubplots(df):
    dsq11 = df[df['questions'].isin(c1_new)]
    dsq22 = df[df['questions'].isin(c2_new)]
    dsq33 = df[df['questions'].isin(c3_new)]
    dsq77 = df[df['questions'].isin(c7_new)]
    dsq88 = df[df['questions'].isin(c8_new)]
    dsq99 = df[df['questions'].isin(c9_new)]

    dcol = ['questions','opinion','count']
    dsq11, dsq22 = dsq11[dcol], dsq22[dcol]
    dsq33, dsq77 = dsq33[dcol], dsq77[dcol]
    dsq88, dsq99 = dsq88[dcol], dsq99[dcol]

    def subq(df, col):
        return df[df['questions'].isin([col])]

    q11,q12 = subq(dsq11,c1_new[0]),subq(dsq11,c1_new[1])
    q13,q14 = subq(dsq11,c1_new[2]),subq(dsq11,c1_new[3])

    q21,q22 = subq(dsq22,c2_new[0]),subq(dsq22,c2_new[1])
    q23,q24 = subq(dsq22,c2_new[2]),subq(dsq22,c2_new[3])

    q31,q32 = subq(dsq33,c3_new[0]),subq(dsq33,c3_new[1])
    q33,q34 = subq(dsq33,c3_new[2]),subq(dsq33,c3_new[3])
    q35 = subq(dsq33,c3_new[4])

    q71,q72 = subq(dsq77,c7_new[0]), subq(dsq77,c7_new[1])

    q81,q91 = subq(dsq88,c8_new[0]), subq(dsq99,c9_new[0])


    colors =["crimson","purple","cyan","blue","green"]
    colors2 =["crimson","purple","brown","cyan","blue",
              "navy","yellow","YellowGreen","green","DarkGreen"]

    def colr(df):
        df['colr']= df['opinion'].apply(lambda x: 0 if x=='Limited'\
                                  else(1 if x=='Fair'\
                                       else(2 if x=='Satisfactory'\
                                            else(3 if x=='Very good' else 4))))
        df=df.sort_values(by=['colr'])
        return df

    def colr1(df):
        df['colr']= df['opinion'].apply(lambda x: 0 if x=='Strongly disgree'\
                                  else(1 if x=='Disagree'\
                                       else(2 if x=='Neutral'\
                                            else(3 if x=='Agree' else 4))))
        df=df.sort_values(by=['colr'])
        return df

    def colr2(df):
        df['colr']= df['opinion'].apply(lambda x: 0 if x=='Very Dissatisfied'\
                                  else(1 if x=='Dissatisfied'\
                                       else(2 if x=='Neutral'\
                                            else(3 if x=='Satisfied' else 4))))
        df=df.sort_values(by=['colr'])
        return df

    def crfl(df):
        clrs=[]
        for cr in df['colr'].tolist():
            clrs.append(colors[cr])
        return clrs

    def crfl2(df):
        df['opinion'] = pd.to_numeric(df['opinion'])
        clrs=[]
        for cr in df['opinion'].tolist():
            indx = int(cr)-1
            clrs.append(colors2[indx])
        return clrs

    q11,q12,q13,q14=colr(q11),colr(q12),colr(q13),colr(q14)
    q21,q22,q23,q24=colr1(q21),colr1(q22),colr1(q23),colr1(q24)
    q31,q32,q33,q34,q35=colr1(q31),colr1(q32),colr1(q33),colr1(q34),colr1(q35)
    q71,q72,q81=colr2(q71),colr2(q72),colr2(q81)
    q91=q91.sort_values(by=['opinion'])

    #---------------------------------
    # Initialize figure with subplots
    fig = make_subplots(rows=9, cols=2)
    #---------------------------------
    # Add locations bar chart-1
    fig.add_trace(go.Bar(name=c1_new[0],
                         x=q11['opinion'],
                         y=q11['count'],
                         text=q11['count'],
                         marker=dict(color=crfl(q11)),
                         showlegend=False),
                  row=1, col=1)

    # Add locations bar chart-2
    fig.add_trace(go.Bar(name=c1_new[1],
                         x=q12['opinion'],
                         y=q12['count'],
                         text=q12['count'],
                         marker=dict(color=crfl(q12)),
                         showlegend=False),
                  row=1, col=2)

    # Add locations bar chart-3
    fig.add_trace(go.Bar(name=c1_new[2],
                         x=q13['opinion'],
                         y=q13['count'],
                         text=q13['count'],
                         marker=dict(color=crfl(q13)),
                         showlegend=False),
                  row=2, col=1)

    # Add locations bar chart-4
    fig.add_trace(go.Bar(name=c1_new[3],
                         x=q14['opinion'],
                         y=q14['count'],
                         text=q14['count'],
                         marker=dict(color=crfl(q14)),
                         showlegend=False),
                   row=2, col=2)
    #------------------------------
    # Add locations bar chart-5
    fig.add_trace(go.Bar(name=c2_new[0],
                         x=q21['opinion'],
                         y=q21['count'],
                         text=q21['count'],
                         marker=dict(color=crfl(q21)),
                         showlegend=False),
                   row=3, col=1)

    # Add locations bar chart-6
    fig.add_trace(go.Bar(name=c2_new[1],
                         x=q22['opinion'],
                         y=q22['count'],
                         text=q22['count'],
                         marker=dict(color=crfl(q22)),
                         showlegend=False),
                   row=3, col=2)

    # Add locations bar chart-7
    fig.add_trace(go.Bar(name=c2_new[2],
                         x=q23['opinion'],
                         y=q23['count'],
                         text=q23['count'],
                         marker=dict(color=crfl(q23)),
                         showlegend=False),
                   row=4, col=1)

    # Add locations bar chart-8
    fig.add_trace(go.Bar(name=c2_new[3],
                         x=q24['opinion'],
                         y=q24['count'],
                         text=q24['count'],
                         marker=dict(color=crfl(q24)),
                         showlegend=False),
                   row=4, col=2)
    #-------------------------------------
    # Add locations bar chart-9
    fig.add_trace(go.Bar(name=c3_new[0],
                         x=q31['opinion'],
                         y=q31['count'],
                         text=q31['count'],
                         marker=dict(color=crfl(q31)),
                         showlegend=False),
                   row=5, col=1)

    # Add locations bar chart-10
    fig.add_trace(go.Bar(name=c3_new[1],
                         x=q32['opinion'],
                         y=q32['count'],
                         text=q32['count'],
                         marker=dict(color=crfl(q32)),
                         showlegend=False),
                   row=5, col=2)

    # Add locations bar chart-11
    fig.add_trace(go.Bar(name=c3_new[2],
                         x=q33['opinion'],
                         y=q33['count'],
                         text=q33['count'],
                         marker=dict(color=crfl(q33)),
                         showlegend=False),
                   row=6, col=1)

    # Add locations bar chart-12
    fig.add_trace(go.Bar(name=c3_new[3],
                         x=q34['opinion'],
                         y=q34['count'],
                         text=q34['count'],
                         marker=dict(color=crfl(q34)),
                         showlegend=False),
                   row=6, col=2)
    # Add locations bar chart-13
    fig.add_trace(go.Bar(name=c3_new[4],
                         x=q35['opinion'],
                         y=q35['count'],
                         text=q35['count'],
                         marker=dict(color=crfl(q35)),
                         showlegend=False),
                   row=7, col=1)
    #-------------------------------------
    # Add locations bar chart-14
    fig.add_trace(go.Bar(name=c7_new[0],
                         x=q71['opinion'],
                         y=q71['count'],
                         text=q71['count'],
                         marker=dict(color=crfl(q71)),
                         showlegend=False),
                   row=7, col=2)

    # Add locations bar chart-15
    fig.add_trace(go.Bar(name=c7_new[1],
                         x=q72['opinion'],
                         y=q72['count'],
                         text=q72['count'],
                         marker=dict(color=crfl(q72)),
                         showlegend=False),
                   row=8, col=1)

    # Add locations bar chart-16
    fig.add_trace(go.Bar(name=c8_new[0],
                         x=q81['opinion'],
                         y=q81['count'],
                         text=q81['count'],
                         marker=dict(color=crfl(q81)),
                         showlegend=False),
                   row=8, col=2)
    # Add locations bar chart-17
    fig.add_trace(go.Bar(name=c9_new[0],
                         x=q91['opinion'],
                         y=q91['count'],
                         text=q91['count'],
                         marker=dict(color=crfl2(q91)),
                         showlegend=False),
                   row=9, col=1)
    #-------------------------------------
    # Update xaxis properties
    fig.update_xaxes(title_text=c_new[0], row=1, col=1)
    fig.update_xaxes(title_text=c_new[1], row=1, col=2)
    fig.update_xaxes(title_text=c_new[2], row=2, col=1)
    fig.update_xaxes(title_text=c_new[3], row=2, col=2)

    fig.update_xaxes(title_text=c_new[4], row=3, col=1)
    fig.update_xaxes(title_text=c_new[5], row=3, col=2)
    fig.update_xaxes(title_text=c_new[6], row=4, col=1)
    fig.update_xaxes(title_text=c_new[7], row=4, col=2)

    fig.update_xaxes(title_text=c_new[8], row=5, col=1)
    fig.update_xaxes(title_text=c_new[9], row=5, col=2)
    fig.update_xaxes(title_text=c_new[10], row=6, col=1)
    fig.update_xaxes(title_text=c_new[11], row=6, col=2)
    fig.update_xaxes(title_text=c_new[12], row=7, col=1)

    fig.update_xaxes(title_text=c_new[13], row=7, col=2)
    fig.update_xaxes(title_text=c_new[14], row=8, col=1)
    fig.update_xaxes(title_text=c_new[15], row=8, col=2)
    fig.update_xaxes(title_text=c_new[16], row=9, col=1)
    #fig.update_xaxes(title_text=c_new[17], row=9, col=2)

    fig.update_traces(texttemplate='%{text:.2s}', textposition='inside')

    # Set theme, margin, and annotation in layout
    fig.update_layout(template="plotly_dark",
                    width=1800,
                    height=2400,
                    margin=dict(r=150, t=70, b=40, l=150),
                    bargap = 0,
                    uniformtext_minsize=8,
                    uniformtext_mode='hide')
    return fig
#*******************************************************************************
# Callback for stat-nps table and graph
@app.callback(dash.dependencies.Output('survey_graph', 'figure'),
              [dash.dependencies.Input('cid_picker_id', 'value')])
#-------------------------------------
def update_bargraph(selected_course_id):
    dfsvy = svyg[svyg['course_id'] == selected_course_id]
    return update_barsubplots(dfsvy)
#*******************************************************************************
#******************************************************************************
# 9.6 Additional Reports
#*************************************
# Demography Report
#-------------------------------------
# Dem Reports filtering function
def filter_courseabb(dem):
    cdc23 = ['course_id', 'course_abb', 'startDate', 'course_type', 'object', 'by']
    dfdemcat1 = dem[cdc23]
    dfdemcat1.sort_values(by =['course_abb','object','by'],inplace = True)
    dfdemcat1 =dfdemcat1.drop_duplicates(subset=['course_abb','object','by'],
                                          keep='first')

    dfdemcat2 = dem[['course_abb','object', 'by', 'count']]
    dfdemcat2 = dfdemcat2.groupby(['course_abb','object','by']\
                                 ).sum().reset_index()
    dfdemcat = dfdemcat1.merge(dfdemcat2, on =['course_abb','object','by'],
                               how='inner')
    return dfdemcat

def filter_demr(pc, ps, start_date, end_date, ca, ci, by):
    spx, fnn = '', ''
    start_date = dtt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    start_date_string = start_date.strftime('%B %d, %Y')
    spx = spx + start_date_string + ' | '
    fnn = fnn + start_date.strftime("%Y")+start_date.strftime("%B")[:3]+\
          start_date.strftime("%d")

    end_date = dtt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    end_date_string = end_date.strftime('%B %d, %Y')
    spx = spx + end_date_string
    fnn = fnn+'_to_'+end_date.strftime("%Y")+end_date.strftime("%B")[:3]+\
    end_date.strftime("%d")

    drange = [(start_date + timedelta(days=x)).strftime("%d/%m/%Y")
              for x in range((end_date-start_date).days + 1)]
    nl = []
    tmp = dem[list(dem.columns)]
    #tmp['index'] = range(1, len(tmp) + 1)
    #tmp = tmp[tmp['startDate'].isin(drange)]
    #print(tmp)

    def output2(tmp, pc, ps, nl):
        tmp['index'] = range(1, len(tmp) + 1)
        tp = 'Total Pages: '+ str(ceil(tmp.shape[0]/PAGE_SIZE))
        return tmp,spx,tmp.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,nl


    if ca != None and ci == None and by == None:
        nl.append(ca); nl.append(fnn)
        tmp = tmp[tmp['course_abb']==ca]
        tmp = filter_courseabb(tmp)
        tmp = tmp[tmp['startDate'].isin(drange)]       
        return output2(tmp, pc, ps, nl)
    elif ca != None and ci == None and by != None:
        nl.append(ca); nl.append('By'+re.sub(':', '', by));nl.append(fnn)
        tmp = filter_courseabb(tmp)
        tmp = tmp[tmp['startDate'].isin(drange)]
        tmp = tmp[tmp['course_abb']==ca]
        tmp = tmp[tmp['by']==by]
        return output2(tmp, pc, ps, nl)
    elif ca == None and ci != None and by != None:
        nl.append(ci); nl.append('By'+re.sub(':', '', by))
        tmp = tmp[tmp['course_id']==ci]
        tmp = tmp[tmp['by']==by]
        return output2(tmp, pc, ps, nl)
    elif ca == None and ci != None and by == None:
        nl.append(ci)
        tmp = tmp[tmp['course_id']==ci]
        return output2(tmp, pc, ps, nl)
    elif ca == None and ci == None and by != None:
        nl.append('By'+re.sub(':', '', by))        
        tmp = tmp[tmp['by']==by]
        return output2(tmp, pc, ps, nl)
    else:
        tmp = tmp[tmp['startDate'].isin(drange)]
        tmp1 = tmp
        return output2(tmp, pc, ps, nl)

#******************************************************************************
#********************
@app.callback([
  dash.dependencies.Output('container-button-dem', 'children'),
  dash.dependencies.Output('output-container-date-picker-ranger1', 'children'),
  dash.dependencies.Output('dem_rep', 'data'),
  dash.dependencies.Output('page_shower_dem', 'children')],
  [dash.dependencies.Input('dem_rep', 'page_current'),
   dash.dependencies.Input('dem_rep', 'page_size'),
   dash.dependencies.Input('my-date-picker-ranger1', 'start_date'),
   dash.dependencies.Input('my-date-picker-ranger1', 'end_date'),
   dash.dependencies.Input('course_id_picker_r1', 'value'),
   dash.dependencies.Input('course_id_picker_r2', 'value'),
   dash.dependencies.Input('course_id_picker_r3', 'value'),
   dash.dependencies.Input('file_name_dem','value'),
   dash.dependencies.Input('save_button_dem','n_clicks')])
   #-------------------------------------
def update_demrtable(pc, ps, start_date, end_date, ca, ci, by, fn, n_clicks):
    df, strpx, data, tp, nl = filter_demr(pc,ps,start_date,end_date,ca,ci,by)
    nl = [re.sub(' ', '', n) for n in nl]
    name1, fn =('_').join(nl),(('_').join([fn,yrc,mhc,dyc]))
    if n_clicks == 0:
        return None, strpx, data, tp
    else:
        try:
            fnold = "Demography202002xx"           
            files =  glob.glob(path_3+'*.xlsx')
            if (path_3 + fnold + '.xlsx') in files:
                os.remove(path_3 + fnold + '.xlsx')
            save_fmt_report(df, path_3, fnold, flags[4])
            fn = path_3 + fn+'_'+name1+'.xlsx'
            if fn in files:
                os.remove(fn) 
            fnold = path_3 + fnold + '.xlsx'
            os.rename(r''+fnold, r''+fn)
        except:
            print("[Error]:", sys.exc_info()[0])
        else:
            print(f"{fn} was saved successfully!")
        finally:
            n_clicks = 0
        return None, strpx, data, tp
#*************************************
# Survey
#-------------------------------------
# A function for filtering the Survey Report
def filter_svyrep(svyq):
    ccc = ['course_id', 'course_abb', 'startDate', 'course_type',
            'questions', 'qnum', 'opinion', 'scores']
    vdf1 = svyq[ccc]
    tmpccc = ['course_abb','questions', 'qnum', 'opinion', 'scores']
    vdf1.sort_values(by = tmpccc, inplace = True)
    vdf1 = vdf1.drop_duplicates(subset=tmpccc, keep='first')

    vdf2 = svyq[['course_abb','questions', 'qnum', 'opinion', 'scores',
                                                              'count']]
    vdf2 = vdf2.groupby(tmpccc).sum().reset_index()
    vdf = vdf1.merge(vdf2, on =tmpccc,how='inner')
    return vdf

def filter_svyr(start_date, end_date, pc, ps, ca, ci, qn):
    spx, fnn = '', ''
    start_date = dtt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    start_date_string = start_date.strftime('%B %d, %Y')
    spx = spx + start_date_string + ' | '
    fnn = fnn + start_date.strftime("%Y")+start_date.strftime("%B")[:3]+\
          start_date.strftime("%d")

    end_date = dtt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    end_date_string = end_date.strftime('%B %d, %Y')
    spx = spx + end_date_string
    fnn = fnn+'_to_'+end_date.strftime("%Y")+end_date.strftime("%B")[:3]+\
    end_date.strftime("%d")

    drange = [(start_date + timedelta(days=x)).strftime("%d/%m/%Y")
              for x in range((end_date-start_date).days + 1)]
    nl = []
    tmp = svyq[qnc1]
    val_bool = tmp['startDate'].isin(drange).tolist()
    #print("cols:",svyq.columns)

    if ca != None and ci == None and qn == None and (True in val_bool):
        nl.append(ca);nl.append(fnn)
        tmp = filter_svyrep(tmp)
        tmp = tmp[tmp['startDate'].isin(drange)]
        tmp = tmp[tmp['course_abb']==ca]
        tmp['index'] = range(1, len(tmp) + 1)
        tp = 'Total Pages: '+ str(ceil(tmp.shape[0]/PAGE_SIZE))
        return tmp,spx,tmp.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,nl
    elif ca != None and ci == None and qn != None and (True in val_bool):
        nl.append(ca);nl.append('Q'+str(qn));nl.append(fnn)
        tmp = filter_svyrep(tmp)
        tmp = tmp[tmp['startDate'].isin(drange)]
        tmp = tmp[tmp['course_abb']==ca]
        tmp = tmp[tmp['qnum']==qn]
        tmp['index'] = range(1, len(tmp) + 1)
        tp = 'Total Pages: '+ str(ceil(tmp.shape[0]/PAGE_SIZE))
        return tmp,spx,tmp.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,nl

    elif ca == None and ci != None and qn != None:
        nl.append(ci);nl.append('Q'+str(qn))
        tmp = tmp[tmp['course_id']==ci]
        tmp = tmp[tmp['qnum']==qn]
        tmp['index'] = range(1, len(tmp) + 1)
        tp = 'Total Pages: '+ str(ceil(tmp.shape[0]/PAGE_SIZE))
        return tmp, spx, tmp.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,nl
    elif ca == None and ci != None and qn == None:
        nl.append(ci)
        tmp = tmp[tmp['course_id']==ci]
        tmp['index'] = range(1, len(tmp) + 1)
        tp = 'Total Pages: '+ str(ceil(tmp.shape[0]/PAGE_SIZE))
        return tmp, spx, tmp.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,nl
    elif ca == None and ci == None and qn != None:
        nl.append('Q'+str(qn))        
        tmp = tmp[tmp['qnum']==qn]
        tmp['index'] = range(1, len(tmp) + 1)
        tp = 'Total Pages: '+ str(ceil(tmp.shape[0]/PAGE_SIZE))
        return tmp, spx, tmp.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,nl
    else:
        nl.append(fnn)
        tmp = filter_svyrep(tmp)
        tmp = tmp[tmp['startDate'].isin(drange)]
        tmp['index'] = range(1, len(tmp) + 1)
        tp = 'Total Pages: '+ str(ceil(tmp.shape[0]/PAGE_SIZE))
        return tmp,spx,tmp.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,nl

@app.callback([
  dash.dependencies.Output('container-button-svy', 'children'),
  dash.dependencies.Output('date_container_svy', 'children'),
  dash.dependencies.Output('svy_table', 'data'),
  dash.dependencies.Output('page_shower', 'children')],
  [dash.dependencies.Input('date-picker_svy', 'start_date'),
   dash.dependencies.Input('date-picker_svy', 'end_date'),
   dash.dependencies.Input('svy_table', "page_current"),
   dash.dependencies.Input('svy_table', "page_size"),
   dash.dependencies.Input('cab_picker_svy', 'value'),
   dash.dependencies.Input('cid_picker_svy', 'value'),
   dash.dependencies.Input('questn_picker_svy', 'value'),
   dash.dependencies.Input('file_name','value'),
   dash.dependencies.Input('save_button_svy','n_clicks')])
   #-------------------------------------
def update_svyrtable(start_date, end_date, pc, ps, ca, ci, qn,fn,n_clicks):
    qn = qnlst[qn]
    df,strpx, data, tp, nl = filter_svyr(start_date, end_date, pc,ps,ca,ci,qn)
    name1, fn =('_').join(nl),(('_').join([fn,yrc,mhc,dyc]))
    if n_clicks == 0:
        return None, strpx, data, tp
    else:
        try:
            fnold = 'survey202002xx'        
            files =  glob.glob(path_3+'*.xlsx')
            if (path_3 + fnold + '.xlsx') in files:
                os.remove(path_3 + fnold + '.xlsx')
            save_fmt_report(df, path_3, fnold, flags[4])
            fn = path_3 + fn + '_' + name1 + '.xlsx'
            if fn in files:
                os.remove(fn) 
            fnold = path_3 + fnold + '.xlsx'
            os.rename(r''+fnold, r''+fn)
        except:
            print("[Error]:", sys.exc_info()[0])
        else:
            print(f"{fn} was saved successfully!")
        finally:
            n_clicks = 0
        return None, strpx, data, tp

#*************************************
# Hod did you hear about us
#-------------------------------------
# A function for filtering how did you hear data
def filter_hdh(start_date, end_date, pc, ps, ca, ci):
    spx, fnn = '', ''
    start_date = dtt.strptime(re.split('T| ', start_date)[0], '%Y-%m-%d')
    start_date_string = start_date.strftime('%B %d, %Y')
    spx = spx + start_date_string + ' | '
    fnn = fnn + start_date.strftime("%Y")+start_date.strftime("%B")[:3]+\
          start_date.strftime("%d")

    end_date = dtt.strptime(re.split('T| ', end_date)[0], '%Y-%m-%d')
    end_date_string = end_date.strftime('%B %d, %Y')
    spx = spx + end_date_string
    fnn = fnn+'_to_'+end_date.strftime("%Y")+end_date.strftime("%B")[:3]+\
    end_date.strftime("%d")

    drange = [(start_date + timedelta(days=x)).strftime("%d/%m/%Y")
              for x in range((end_date-start_date).days + 1)]
    nl = []
    tmp = hdhhearg[list(hdhhearg.columns)]

    def get_col(df):
        df = df[['Courses', 'startDate',
       'How did you hear about this course?', 'count']]
        df.columns = colhdh2
        return df
    #print("cols:",svyq.columns)
    if ca != None and ci == None:
        nl.append(ca);nl.append(fnn)
        tmp = tmp[tmp['course_abb']==ca]
        tmp = get_col(tmp)
        tmp1 = tmp[colhdh2]
        tmp['index'] = range(1, len(tmp) + 1)
        tp = 'Total Pages: '+ str(ceil(tmp.shape[0]/PAGE_SIZE))
        return tmp1, spx,tmp.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,nl

    elif ca == None and ci != None:
        nl.append(ci);nl.append(fnn)
        tmp = tmp[tmp['course_id']==ci]
        tmp = get_col(tmp)
        tmp1 = tmp[colhdh2]
        tmp['index'] = range(1, len(tmp) + 1)
        tp = 'Total Pages: '+ str(ceil(tmp.shape[0]/PAGE_SIZE))
        return tmp1, spx, tmp.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,nl
    else:
        nl.append(fnn)
        tmp = tmp[tmp['startDate'].isin(drange)]
        tmp = get_col(tmp)
        tmp1 = tmp[colhdh2]
        tmp['index'] = range(1, len(tmp) + 1)
        tp = 'Total Pages: '+ str(ceil(tmp.shape[0]/PAGE_SIZE))
        return tmp1,spx,tmp.iloc[pc*ps:(pc+ 1)*ps].to_dict('records'),tp,nl
@app.callback([
  dash.dependencies.Output('container-button-hdh', 'children'),
  dash.dependencies.Output('date_container_hdh', 'children'),
  dash.dependencies.Output('hdh_table', 'data'),
  dash.dependencies.Output('page_shower_hdh', 'children')],
  [dash.dependencies.Input('date-picker_hdh', 'start_date'),
   dash.dependencies.Input('date-picker_hdh', 'end_date'),
   dash.dependencies.Input('hdh_table', "page_current"),
   dash.dependencies.Input('hdh_table', "page_size"),
   dash.dependencies.Input('cab_picker_hdh', 'value'),
   dash.dependencies.Input('cid_picker_hdh', 'value'),
   dash.dependencies.Input('file_nhdh','value'),
   dash.dependencies.Input('save_button_hdh','n_clicks')])
   #-------------------------------------
def update_svyrtable(start_date, end_date, pc, ps, ca, ci, fn,n_clicks):
    df,strpx, data, tp, nl = filter_hdh(start_date, end_date, pc,ps,ca,ci)
    name1, fn =('_').join(nl),(('_').join([fn,yrc,mhc,dyc]))
    if n_clicks == 0:
        return None, strpx, data, tp
    else:
        try:
            fnold = 'hearatus0011xx'       
            files =  glob.glob(path_3+'*.xlsx')
            if (path_3 + fnold + '.xlsx') in files:
                os.remove(path_3 + fnold + '.xlsx')
            save_fmt_report(df, path_3, fnold, flags[4])
            fn=path_3+fn+'_'+name1+'.xlsx'
            if fn in files:
                os.remove(fn) 
            fnold = path_3 + fnold + '.xlsx'
            os.rename(r''+fnold, r''+fn)
        except:
            print("[Error]:", sys.exc_info()[0])
        else:
            print(f"{fn} was saved successfully!")
        finally:
            n_clicks = 0
        return None, strpx, data, tp
#******************************************************************************
#******************************************************************************
# 10. Search Trainees By Lastname
#******************************************************************************
#******************************************************************************
@app.callback([
  dash.dependencies.Output('lnamer_table', 'data'),
  dash.dependencies.Output('lnameg_table', 'data')],
  [dash.dependencies.Input('lnamerg_dwn','value')])
   #-------------------------------------
def update_svyrtable(selected_lname):
    regt = reg[reg['Last Name:']==selected_lname]
    grat = gra[gra['Last Name']==selected_lname]
    regt, grat = regt[regcol], grat[gracol]
    return regt.to_dict('records'), grat.to_dict('records')
#******************************************************************************
#******************************************************************************
# 11. Database Tables
#******************************************************************************
#******************************************************************************
# Filter Tables
@app.callback([
  dash.dependencies.Output('container-button-dbt', 'children'),
  dash.dependencies.Output('status_indicator', 'children')],
  [dash.dependencies.Input('dbt_dwn','value'),
   dash.dependencies.Input('savetabs', 'n_clicks')])
   #-------------------------------------
def update_dbtables(value, n_clicks):
    dtbs = ['course_list', 'registrants', 'demography', 'cost_model',
             'grade_report', 'surveys', 'frac_setting', 'profit_by_id',
             'profit_by_abb']
    #acl, reg, dem, cml, gra, prof, profsmry, svy, fset
    if value == dtbs[0] and n_clicks != 0:
        print("path_7", path_7)
        files =  glob.glob(path_7+'*.xlsx')
        print(files)
        if (path_7 + dtbs[0] + '.xlsx') in files:
            os.remove(path_7 + dtbs[0] + '.xlsx')  
        save_dbtables(acl, path_7, dtbs[0], dtbs[0])
        n_clicks=0
        return None, 'Table ' + dtbs[0] +' has been saved to Reports folder!'
    elif value == dtbs[1] and n_clicks != 0:
        files =  glob.glob(path_7+'*.xlsx')
        if (path_7 + dtbs[1] + '.xlsx') in files:
            os.remove(path_7 + dtbs[1] + '.xlsx')  
        save_dbtables(reg, path_7, dtbs[1], dtbs[1])
        n_clicks=0
        return None, 'Table ' + dtbs[1] +' has been saved to Reports folder!'
    elif value == dtbs[2] and n_clicks != 0:
        files =  glob.glob(path_7+'*.xlsx')
        if (path_7 + dtbs[2] + '.xlsx') in files:
            os.remove(path_7 + dtbs[2] + '.xlsx')  
        save_dbtables(dem, path_7, dtbs[2], dtbs[2])
        n_clicks=0
        return None, 'Table ' + dtbs[2] +' has been saved to Reports folder!'
    elif value == dtbs[3] and n_clicks != 0:
        files =  glob.glob(path_7+'*.xlsx')
        if (path_7 + dtbs[3] + '.xlsx') in files:
            os.remove(path_7 + dtbs[3] + '.xlsx')  
        save_dbtables(cml, path_7, dtbs[3], dtbs[3])
        n_clicks=0
        return None, 'Table ' + dtbs[3] +' has been saved to Reports folder!'
    elif value == dtbs[4] and n_clicks != 0:
        files =  glob.glob(path_7+'*.xlsx')
        if (path_7 + dtbs[4] + '.xlsx') in files:
            os.remove(path_7 + dtbs[4] + '.xlsx')  
        save_dbtables(gra, path_7, dtbs[4], dtbs[4])
        n_clicks=0
        return None, 'Table ' + dtbs[4] +' has been saved to Reports folder!'
    elif value == dtbs[5] and n_clicks != 0:
        files =  glob.glob(path_7+'*.xlsx')
        if (path_7 + dtbs[5] + '.xlsx') in files:
            os.remove(path_7 + dtbs[5] + '.xlsx')  
        save_dbtables(svy, path_7, dtbs[5], dtbs[5])
        n_clicks=0
        return None, 'Table ' + dtbs[5] +' has been saved to Reports folder!'
    elif value == dtbs[6] and n_clicks != 0:
        files =  glob.glob(path_7+'*.xlsx')
        if (path_7 + dtbs[6] + '.xlsx') in files:
            os.remove(path_7 + dtbs[6] + '.xlsx')  
        save_dbtables(fset, path_7, dtbs[6], dtbs[6])
        n_clicks=0
        return None, 'Table ' + dtbs[6] +' has been saved to Reports folder!'
    #elif value == dtbs[7] and n_clicks != 0:
        #save_dbtables(pft, path_7, dtbs[7], dtbs[7])
        #n_clicks=0
        #return None, 'Table ' + dtbs[7] +' has been saved to Reports folder!'
    #elif value == dtbs[8] and n_clicks != 0:
        #save_dbtables(pfs, path_7, dtbs[8], dtbs[8])
        #n_clicks=0
        #return None, 'Table ' + dtbs[8] +' has been saved to Reports folder!'
    else:
        return None, None
#******************************************************************************
# 12. Update Data from external sources and DB.
#******************************************************************************
#******************************************************************************
# Dash updating function
#******************************************************************************
# Dash updating function
def update_dash():
    print('Updating .................................................')
    gen_warning()
    global filenames, ids, dfall, dfreg, dfgra, dfcos, dfsur, dfset, dfcklst
    global allf, demog, rev, regf, ccid1, ccid2, graf, ccid3, cosf, setf
    global profit, profsumry, proff, dfsur1, ccid4, sur1f, table_list
    global acl, reg, dem, cml, gra, prof, profsmry, svy
    global yrc, mhc, dyc, cr, bnb1, blank_colns, blank2, blank3, acl1
    global dsq1, dsq2, dsq3, dsq7, dsq8, dsq9, svyg,svyq, cyc,rc1,gc1,sc1,cc1
    global acl1, reg1, dem1, cml1, gra1, svy1, fset1, setf, errors, pft1, pfs1
    global flagacl,flagreg,flagdem,flaggra,flagcml,flagsvy,flagset
    global er1, er2, er3, er4, er5, er6, er7
    global facl, freg, fdem, fcml, fgra, fsvy, fset, pft, pfs

    filenames, ids, dfall, dfreg, dfgra, dfcos, dfsur, dfset,dfcklst = read_dsets(path_1)
    call_writer()
    remove_inputfiles()
    dfall, allf = handle_acl(dfall)
    demog, rev1, regf, ccid1 = gen_demography(dfreg)
    dfgra, ccid2, graf = gen_grades(dfgra,ids)
    dfcos, ccid3, cosf = gen_costModels(dfcos)
    dfset, setf = proc_dfset(dfset)
    #profit, profsumry, proff = analyze_costprofit(rev, dfcos, dfset)
    dfsur1, ccid4, sur1f = gen_toot(dfsur)
    dfreg,demog,dfcos,dfgra,dfsur1 = \
    add_abb_date(dfreg,demog,dfcos,dfgra,dfsur1, ids)

    acl1 = querydb(dbpath, acl_col_db, querycol['acl'], tbls['acl'])
    reg1 = querydb(dbpath, reg_col_db, querycol['reg'], tbls['reg'])
    dem1 = querydb(dbpath, dem_col_db, querycol['dem'], tbls['dem'])
    gra1 = querydb(dbpath, gra_col_db, querycol['gra'], tbls['gra'])
    cml1 = querydb(dbpath, cml_col_db, querycol['cml'], tbls['cml'])
    svy1 = querydb(dbpath, svy_col_db, querycol['svy'], tbls['svy'])
    fset1 = querydb(dbpath, dest_cols, querycol['set'], tbls['set'])
    #pft1 = querydb(dbpath, querycol['pft'], tbls['pft'])
    #pfs1 = querydb(dbpath, querycol['pfs'], tbls['pfs'])    

    er1, rpc1 = tosqlite(dbpath, dfall, acl1, allf, tbls['acl'],
            tabmsg['acl'], 'acl', 'append', 'acronym', acl_col_db)
    er2, rpc2 = tosqlite(dbpath, dfreg, reg1, regf, tbls['reg'],
            tabmsg['reg'],'reg', 'append', 'course_id', reg_col_db)
    er3, rpc3 = tosqlite(dbpath, demog, dem1, regf, tbls['dem'],
            tabmsg['dem'], 'dem', 'append', 'course_id', dem_col_db)    
    er4, rpc4 = tosqlite(dbpath, dfgra, gra1, graf, tbls['gra'],
            tabmsg['gra'], 'gra', 'append', 'course_id', gra_col_db)    
    er5, rpc5 = tosqlite(dbpath, dfcos, cml1, cosf, tbls['cml'],
            tabmsg['cml'], 'cml', 'append', 'course_id', cml_col_db)
    er6, rpc6 = tosqlite(dbpath, dfsur1, svy1, sur1f, tbls['svy'],
            tabmsg['svy'], 'svy', 'append', 'course_id', svy_col_db)
    er7, rpc7 = tosqlite(dbpath, dfset, fset1, setf, tbls['set'],
            tabmsg['set'], 'set', 'replace', 'course_id', dest_cols)
    errors.append(er1+er2+er3+er4+er5+er6+er7)

    table_list, msg = check_tables(dbpath)
    backupDb(path_4, dbpath)

    acl = sqliteTopd(dbpath, querycol['acl'], 'course_list', dupcols['acl'],
                            acl_col_db)
    reg = sqliteTopd(dbpath, querycol['reg'], 'registrants', dupcols['reg'],
                            reg_col_db)
    dem = sqliteTopd(dbpath, querycol['dem'], 'demography', dupcols['dem'],
                            dem_col_db)
    cml = sqliteTopd(dbpath, querycol['cml'], 'cost_model', dupcols['cml'],
                            cml_col_db)
    gra = sqliteTopd(dbpath, querycol['gra'], 'grade_report', dupcols['gra'],
                            gra_col_db)
    svy = sqliteTopd(dbpath, querycol['svy'], 'surveys', dupcols['svy'],
                            svy_col_db)
    fset = sqliteTopd(dbpath, querycol['set'], 'frac_setting', dupcols['set'],
                            dest_cols) 
    
    #prof = pd.DataFrame(tmpprof)
    prof = gen_profit(reg, cml, fset, mrkt)
    #profsmry = pd.DataFrame(tmpsmry)
    profsmry = gen_profsmry(prof) 
    
    yrc, mhc, dyc, cr = get_date()
    bnb1, blank_colns, blank2, blank3, acl1 = dash_sets1(dem, acl)
    dsq1, dsq2, dsq3, dsq7, dsq8, dsq9, svyg,svyq, cyc = dash_sets2(svy,reg)
    rc1,gc1,sc1,cc1 = gen_cnt(reg, gra, svy,cml)

    global courseID_options, buoption, buoption_id, cAbb_options
    global cIDr_options, By_options, pc_options, cisvy, absvy, cns
    global pc_id, chklstv1, hdhhearg, abhdh, cihdh, demcrs, demid
    #global qn_options, pc_id, npsab_options, npsid_options

    courseID_options = get_options(reg,'course_id')
    buoption =  get_options(bnb1, 'course_abb')
    buoption_id  = get_options(bnb1, 'course_id')
    cAbb_options = get_options(dem, 'course_abb')
    cAbb_options.append({'label':str(None),'value':None})
    cIDr_options = get_options(dem, 'course_id')
    dept_ids, top5_ids= cIDr_options,cIDr_options
    dept_ids.append([{'label':'None','value':'None'}])
    top5_ids.append([{'label':'None','value':'None'}])
    cIDr_options.append({'label':str(None),'value':None})
    By_options = get_options(dem, 'by')
    By_options.append({'label':str(None),'value':None})
    pc_options = get_options(prof, 'course_id')
    pc_options.append([{'label':'None','value':'None'}])

    demcrs = get_options(dem, 'course_abb') 
    demcrs.append({'label':'All','value': "All"})  

    demid = get_options(dem, 'course_id')
    demid.append({'label':str(None),'value':None}) 

    cisvy = get_options(svyg,'course_id')
    cisvy.append({'label':str(None),'value':None})
    absvy = get_options(svyg,'course_abb')
    absvy.append({'label':str(None),'value':None})

    hdhhearg = get_hdh(reg, acl)
    abhdh = get_options(hdhhearg,'course_abb')
    abhdh.append({'label':str(None),'value':None})
    cihdh = get_options(hdhhearg,'course_id')
    cihdh.append({'label':str(None),'value':None})

    cns = [(svyq['questions'].isin(c1_new)),(svyq['questions'].isin(c2_new)),
       (svyq['questions'].isin(c3_new)),(svyq['questions'].isin(c4_new)),
       (svyq['questions'].isin(c5_new)),(svyq['questions'].isin(c6_new)),
       (svyq['questions'].isin(c7_new)),(svyq['questions'].isin(c8_new)),
       (svyq['questions'].isin(c9_new))]
    svyq['qnum'] = np.select(cns, vls)
    chklstv1 = get_chklst(reg,gra,cml,svy,dfcklst)
    if isinstance(reg, bool) == False and isinstance(acl, bool) == False:
        regincome = gen_regenr(reg,acl)
    else:
        regincome = False

    #qn_options = get_options(svyq, 'qnum')
    #qn_options.append({'label':str(None),'value':None})

    pc_id = get_options(prof, 'course_abb')
    #print('pc_id', pc_id)
    npsab_options = get_options(svyq, 'course_abb')
    npsab_options.append({'label':str(None),'value':None})
    npsid_options = get_options(svyq, 'course_id')
    npsid_options.append({'label':str(None),'value':None})
    app.layout = serve_layout

    #npsqn_options = get_options(svyq, 'qnum')
    #npsqn_options.append({'label':str(None),'value':None})
    return errors

#*****************************************************************************
# Dash updating f@app.callback([
#******************************************************************************
@app.callback([
    dash.dependencies.Output('container-button-basic', 'children'),
    dash.dependencies.Output('update_status', 'children')],
    [dash.dependencies.Input('submit-val', 'n_clicks')])
def update_output(n_clicks):
    if n_clicks >0:
        errors = update_dash()        
        msgdu = pd.DataFrame({"Input, Insert & Query Status": errors})
        print(msgdu)
        dtdate.append(dtt.now().strftime("%Y-%B-%d %H:%M:%S"))
        n_clicks = 0
        return None, html.Div([dt.DataTable(
                    id='iiq_status',
                    columns=[{"name": i, "id": i} for i in dfer.columns],
                    data=dfer.to_dict('records'),
                    style_table={'margin-left': '200x'},
                    style_header={'backgroundColor': 'white',
                                          'fontWeight': 'bold',
                                          'font_size': '23px',
                                           'border': '1px solid black'},
                    style_cell={'textAlign': 'right',
                                                    'whiteSpace':'normal',
                                                    'font_size': '17px'},
                    style_cell_conditional=[
                                       {'if': {'column_id': 'Region'},
                                        'textAlign': 'left'}],
                    style_data={ 'border': '1px solid blue' },
                    style_data_conditional=[
                            {'if': {'row_index': 'odd'},
                            'backgroundColor': 'rgb(248, 248, 248)'}],
                    export_format='xlsx',
                    export_headers='display')
                    ])
    else:
        print("Dashboard last updated on", dtdate[-1])
        return None, None

#*****************************************************************************
# Replace Pertinent Tables in DB
#******************************************************************************
@app.callback([
    dash.dependencies.Output('container-button-basic2', 'children'),
    dash.dependencies.Output('replace_status', 'children'),
    dash.dependencies.Output('error_status', 'children')],
    [dash.dependencies.Input('submit-val2', 'n_clicks')])
def replace_trables(n_clicks):
    if n_clicks > 0:
        from replace import replace_tables
        errorsr, reptabs = replace_tables(rpath, apath, dbpath)
        if len(reptabs) == 0:
            reptabs.append('None')
        msgtr = pd.DataFrame({'Tables Whose Records were Updated':reptabs})
        infoerr = pd.DataFrame({'Additional Information':errorsr})
        print(msgtr)
        n_clicks = 0
        return None, html.Div([dt.DataTable(
                    id='rep_status',
                    columns=[{"name": i, "id": i} for i in msgtr.columns],
                    data=msgtr.to_dict('records'),
                    style_table={'margin-left': '200x'},
                    style_header={'backgroundColor': 'white',
                                          'fontWeight': 'bold',
                                          'font_size': '23px',
                                           'border': '1px solid black'},
                    style_cell={'textAlign': 'right',
                                                    'whiteSpace':'normal',
                                                    'font_size': '17px'},
                    style_cell_conditional=[
                                       {'if': {'column_id': 'Region'},
                                        'textAlign': 'left'}],
                    style_data={ 'border': '1px solid blue' },
                    style_data_conditional=[
                            {'if': {'row_index': 'odd'},
                            'backgroundColor': 'rgb(248, 248, 248)'}],
                    export_format='xlsx',
                    export_headers='display')
                ]), html.Div([dt.DataTable(
                    id='err_status',
                    columns=[{"name": i, "id": i} for i in infoerr.columns],
                    data=infoerr.to_dict('records'),
                    style_table={'margin-left': '200x'},
                    style_header={'backgroundColor': 'white',
                                          'fontWeight': 'bold',
                                          'font_size': '23px',
                                           'border': '1px solid black'},
                    style_cell={'textAlign': 'right',
                                                    'whiteSpace':'normal',
                                                    'font_size': '17px'},
                    style_cell_conditional=[
                                       {'if': {'column_id': 'Region'},
                                        'textAlign': 'left'}],
                    style_data={ 'border': '1px solid blue' },
                    style_data_conditional=[
                            {'if': {'row_index': 'odd'},
                            'backgroundColor': 'rgb(248, 248, 248)'}],
                    export_format='xlsx',
                    export_headers='display')
                ])
    else:
        print("Dashboard last updated on", dtdate[-1])
        return None, None, None
#******************************************************************************
#@endofapp
#******************************************************************************
#******************************************************************************
# 12. Run the app by adding the server clause
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


