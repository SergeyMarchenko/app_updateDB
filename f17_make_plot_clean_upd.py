# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:25:13 2024

@author: marchenks
"""

import plotly.graph_objects as go
import streamlit            as st

# fig = make_plot_clean_upd(cols, v, c, d_0, D)
@st.cache_data(show_spinner="Drawing figure...")
def make_plot_clean_upd(cols, v, C, d_0, D):


    r = cols[cols.iloc[:,0] == v].index[0]
        
    fig = go.Figure()
    s = go.Scattergl(x=C.index, y=C[v],
                     name = "UNupdated table " + cols.columns[0] + ': ' + cols.iloc[r,0],
                     mode='markers')
    s.marker.color = 'rgb(0,0,0)'
    s.marker.symbol = 'circle-open'
    s.marker.size = 5
    s.marker.line.color = 'rgb(0,0,0)'
    s.marker.line.width = 1
    fig.add_trace(s)
    
    s = go.Scattergl(x=d_0.iloc[:,0], y=d_0[cols.iloc[r,4]],
                     name = cols.columns[4] + ': ' + cols.iloc[r,4] , mode='markers')
    s.marker.color = 'rgb(31,119,180)'
    s.marker.size = 2
    s.marker.line.color = 'rgb(31,119,180)'
    s.marker.line.width = 1
    fig.add_trace(s)
        
    s = go.Scattergl(x=D.index,
                     y=D[v],
                     name = "data to be added to the clean_ table " + cols.columns[0] + ' (data for update): ' + v,
                     mode='markers')
    s.marker.color = 'rgb(214,39,40)'
    s.marker.size = 1
    s.marker.line.color = 'rgb(214,39,40)'
    s.marker.line.width = 1
    fig.add_trace(s)
        
    fig.update_layout( xaxis_title='time', autosize=False, width=1000, height=500,
                      legend=dict(orientation="h",  # Horizontal legend
                                  yanchor="top",    # Anchor the legend at the top
                                  y=-0.2,           # Position the legend below the plot
                                  xanchor="left", # Center the legend
                                  x=0.1             # Horizontally center the legend
                                  ))
    # fig.write_html('plot.html')
    
    return fig