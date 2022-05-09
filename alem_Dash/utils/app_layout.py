def app_layout():
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
