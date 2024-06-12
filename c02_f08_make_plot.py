# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 11:28:28 2024

@author: marchenks
"""

import pandas               as pd
import plotly.graph_objects as go
import streamlit            as st

# fig = make_plot(db_t, db_d, fl_t, fl_d, c, col_dict, key)
@st.cache_data(show_spinner="Drawing figure...")
def make_plot(db_d, fl_d, c, col_dict, col_dict_out, key):
    # key = "AirTemp_Avg_Deg_C"
    b = fl_d[             key ].squeeze() # AWS data file
    if  col_dict[key] == "SKIP the column":
            
        s2 = go.Scatter(x=b.index, y=b, name='AWS file'         , mode='markers')
        s2.marker = dict(color = 'rgba(204,  0,   0, 0)', size = 4, line = dict(color = 'rgba(204,  0,  0, 1)', width = 1))
        
        fig = go.Figure(data=[s2])
        t = "Note: data from the AWS file shown below will NOT be included in the updated DataBase table."
        
        
    elif col_dict[key] == "add NEW COLUMN to db":
        m =    c[col_dict_out[key]]                                    # updated database table
        
        s2 = go.Scatter(x=b.index, y=b, name='AWS file'         , mode='markers')
        s3 = go.Scatter(x=m.index, y=m, name='updated database' , mode='markers')

        s2.marker = dict(color = 'rgba(204,  0,   0, 0)', size = 4, line = dict(color = 'rgba(204,  0,  0, 1)', width = 1))
        s3.marker = dict(color = 'rgba(  0,  0,   0, 0)', size = 7, line = dict(color = 'rgba(  0,  0,  0, 1)', width = 1))

        fig = go.Figure(data=[s2, s3])
        t = "Note: data from the AWS file shown below will be added to a new column in the updated DataBase table."
                
        
    else:
        a = db_d[col_dict[key]].squeeze() # initial database table
        m =    c[col_dict[key]]                                    # updated database table
        
        if a.size == 0:
            t = "Note: data from the AWS file shown below will be added to a new DataBase table."

        elif any(a.index.isin( b.index)):    # DataBase table overlaps in time with AWS file
            ind1a = abs( a.index - b.index[0             ] )    # difference in time between TimeStamps in initial database table and first row in AWS data file
            ind2a = abs( a.index - b.index[len(b.index)-1] )    #                                                                     last
            ind1a = ind1a.argmin() - 240                        
            ind2a = ind2a.argmin() + 240
            ind1a = max([ind1a, 0           ])
            ind2a = min([ind2a, len(a.index)])
        
            ind1c = abs( m.index - b.index[0             ] )
            ind2c = abs( m.index - b.index[len(b.index)-1] )
            ind1c = ind1c.argmin() - 240
            ind2c = ind2c.argmin() + 240
            ind1c = max([ind1c, 0           ])
            ind2c = min([ind2c, len(m.index)])
            
            a = a.iloc[ind1a:ind2a]
            m = m.iloc[ind1c:ind2c]
            
            t = "Note: showing data only for the time period covered by the AWS data file -+ ca10 days"
            
        elif a.index[-1] < b.index[0]:   # DataBase table entirely before AWS file
            a_ind = a.index >= (a.index[-1] - pd.DateOffset(days=30))       # rows in initial Database covering last 30 days of data
            a = a[a_ind]
            
            m_ind = m.index >= a.index[0]                                   #   ...   updated ...
            m = m[m_ind]
                        
            t = "Note: showing data only for the time period covered by the AWS data file and ca 30 last days of the initial DataBase"
            
        elif b.index[-1] < a.index[0]:   # DataBase table entirely after  AWS file
            a_ind = a.index >= (a.index[0] + pd.DateOffset(days=30))
            a = a[a_ind]
            
            m_ind = m.index >= a.index[0]
            m = m[m_ind]
                        
            t = "Note: showing data only for the time period covered by the AWS data file and ca 30 first days of the initial DataBase"
        
        if a.size > 0:
            s1 = go.Scatter(x=a.index, y=a, name='initial DataBase' , mode='markers')
        s2     = go.Scatter(x=b.index, y=b, name='AWS file'         , mode='markers')
        s3     = go.Scatter(x=m.index, y=m, name='updated DataBase' , mode='markers')
        
        if a.size > 0:
            s1.marker = dict(color = 'rgba( 61, 133, 198, 0)', size = 2, line = dict(color = 'rgba( 61, 133, 198, 1)', width = 1))        
        s2.marker     = dict(color = 'rgba(204,   0,   0, 0)', size = 4, line = dict(color = 'rgba(204,   0,   0, 1)', width = 1))
        s3.marker     = dict(color = 'rgba(  0,   0,   0, 0)', size = 7, line = dict(color = 'rgba(  0,   0,   0, 1)', width = 1))
        
        if a.size > 0:
            fig = go.Figure(data=[s1, s2, s3])
        else:
            fig = go.Figure(data=[s2, s3])
        
                
    fig.update_layout( title=t, xaxis_title='time', yaxis_title=key, autosize=False, width=1100, height=500 )
    # fig.write_html('plot.html')

    return fig