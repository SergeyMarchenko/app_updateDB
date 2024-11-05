# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:28:28 2024

@author: marchenks
"""

import pandas               as pd
import plotly.graph_objects as go
import streamlit            as st

# fig = make_plot_raw(db_d, fl_d, c, col_dict, key)
@st.cache_data(show_spinner="Drawing figure...")
def make_plot_raw(db_d, fl_d, c, col_dict, col_dict_out, key):
    # key = "AirTemp_Avg_Deg_C"
    b = fl_d[             key ].squeeze() # AWS data file
    if  col_dict[key] == "SKIP the column":
            
        s2 = go.Scattergl(x=b.index, y=b, name='AWS file'         , mode='markers')
        s2.marker = dict(color = 'rgba(204,  0,   0, 0)', size = 4, line = dict(color = 'rgba(204,  0,  0, 1)', width = 1))
        
        fig = go.Figure(data=[s2])
        t = "Note: data from the AWS file shown below will NOT be included in the updated DataBase table."
        
        
    elif col_dict[key] == "add NEW COLUMN to db":
        m =    c[col_dict_out[key]]                                    # updated database table
        
        s2 = go.Scattergl(x=b.index, y=b, name='AWS file'         , mode='markers')
        s3 = go.Scattergl(x=m.index, y=m, name='updated database' , mode='markers')

        s2.marker = dict(color = 'rgba(204,  0,   0, 0)', size = 4, line = dict(color = 'rgba(204,  0,  0, 1)', width = 1))
        s3.marker = dict(color = 'rgba(  0,  0,   0, 0)', size = 7, line = dict(color = 'rgba(  0,  0,  0, 1)', width = 1))

        fig = go.Figure(data=[s2, s3])
        t = "Note: data from the AWS file shown below will be added to a new column in the updated DataBase table."
                
        
    else:
        a = db_d[col_dict[key]].squeeze() # initial database table
        m =    c[col_dict[key]]           # updated database table
        
        if a.size == 0:
            t = "Note: data from the AWS file shown below will be added to a new DataBase table."

        elif any(a.index.isin( b.index)):                       # DataBase table overlaps in time with AWS file
            a = a[a.index >= b.index.min() - pd.DateOffset(days=10)]
            a = a[a.index <= b.index.max() + pd.DateOffset(days=10)]
            m = m[m.index >= b.index.min() - pd.DateOffset(days=10)]
            m = m[m.index <= b.index.max() + pd.DateOffset(days=10)]
            t = "Note: showing data only for the time period covered by the AWS data file -+ ca10 days"
            
        elif a.index[-1] < b.index[0]:   # DataBase table entirely before AWS file
            a = a[a.index >= (a.index[-1] - pd.DateOffset(days=30))]        # rows in initial Database covering last 30 days of data
            m = m[m.index >= a.index[0]]                                    #   ...   updated ...
            t = "Note: showing data only for the time period covered by the AWS data file and ca 30 last days of the initial DataBase"
            
        elif b.index[-1] < a.index[0]:   # DataBase table entirely after  AWS file
            a = a[a.index >= (a.index[0] + pd.DateOffset(days=30))]
            m = m[m.index >= a.index[0]]
            t = "Note: showing data only for the time period covered by the AWS data file and ca 30 first days of the initial DataBase"
        
        if a.size > 0:
            s1 = go.Scattergl(x=a.index, y=a, name='initial DataBase' , mode='markers')
        s2     = go.Scattergl(x=b.index, y=b, name='AWS file'         , mode='markers')
        s3     = go.Scattergl(x=m.index, y=m, name='updated DataBase' , mode='markers')
        new = m.index.difference(a.index)
        s4     = go.Scattergl(x=new, y=m[new], name='new values in DataBase', mode='markers')
        
        if a.size > 0:
            s1.marker = dict(color = 'rgba( 61, 133, 198, 0)', size = 2, line = dict(color = 'rgba( 61, 133, 198, 1)', width = 1))        
        s2.marker     = dict(color = 'rgba(204,   0,   0, 0)', size = 4, line = dict(color = 'rgba(204,   0,   0, 1)', width = 1))
        s3.marker     = dict(color = 'rgba(  0,   0,   0, 0)', size = 7, line = dict(color = 'rgba(  0,   0,   0, 1)', width = 1))
        s4.marker     = dict(color = 'rgba(248, 113,  13, 0)', size = 7, line = dict(color = 'rgba(248, 113,  13, 1)', width = 1))
        
        
        if a.size > 0:
            fig = go.Figure(data=[s1, s2, s3, s4])
        else:
            fig = go.Figure(data=[s2, s3])
        
                
    fig.update_layout( title=t, xaxis_title='time', yaxis_title=key, autosize=False, width=1100, height=500 )
    # fig.write_html('plot.html')

    return fig