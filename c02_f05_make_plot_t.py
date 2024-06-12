# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 16:12:17 2024

@author: marchenks
"""

import plotly.graph_objects as go
import streamlit            as st

# fig_t = make_plot_t(db_t, fl_t)
@st.cache_data(show_spinner="Drawing figure...")
def make_plot_t(db_t, fl_t):
    # db_t = db_d.index.tolist()
    # fl_t = fl_d.index.tolist()
            
    t_aws     = go.Scatter(x=[fl_t[0], fl_t[-1]], y=[1, 1], name='AWS file'      , mode='lines+markers')
    t_aws.marker     = dict(color = 'rgba(204,  0,   0, 1)', size = 4, line = dict(color = 'rgba(204,  0,   0, 1)', width = 1))
    t_aws.line       = dict(color = 'rgba(204,  0,   0, 1)', width = 2 )

    fig_t = go.Figure(data=t_aws)
    
    if db_t:
        t_dbt = go.Scatter(x=[db_t[0], db_t[-1]], y=[2, 2], name='DataBase table', mode='lines+markers')
        t_dbt.marker = dict(color = 'rgba( 11, 83, 148, 1)', size = 4, line = dict(color = 'rgba( 11, 83, 148, 1)', width = 1))
        t_dbt.line   = dict(color = 'rgba( 11, 83, 148, 1)', width = 2 )
        fig_t.add_trace(t_dbt)
    
        
    
    fig_t.update_layout(yaxis = dict(ticks = ""))
    fig_t.update_layout(xaxis_title='time',
                        yaxis_range=[0,3],
                        autosize=False, width=1100, height=250 )

    # fig_t.write_html('plot.html')

    return fig_t

    