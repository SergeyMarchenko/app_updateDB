import plotly.graph_objects as go
import streamlit            as st

# fig = make_plot_clean(cols, v, c, d_0)
@st.cache_data(show_spinner="Drawing figure...")
def make_plot_clean(cols, v, c, d_0):


    r = cols[cols.iloc[:,0] == v].index[0]
    
    col = [
    'rgb(31,119,180)',
    'rgb(255,127,14)',
    'rgb(44,160,44)',
    'rgb(214,39,40)',
    'rgb(148,103,189)',
    'rgb(140,86,75)',
    'rgb(227,119,194)',
    'rgb(127,127,127)',
    'rgb(188,189,34)',
    'rgb(23,190,207)'
    ]
    
    fig = go.Figure()
    s = go.Scattergl(x=c.index,
                     y=c[v],
                     name=cols.columns[0] + ': ' + cols.iloc[r,0],
                     mode='markers')
    s.marker.color = 'rgb(0,0,0)'
    s.marker.symbol = 'circle-open'
    s.marker.size = 5
    s.marker.line.color = 'rgb(0,0,0)'
    s.marker.line.width = 1
    fig.add_trace(s)
    for i in range(len(d_0)):
        s = go.Scattergl(x=d_0[i].iloc[:,0], y=d_0[i][cols.iloc[r,i+4]], name=cols.columns[i+4] + ': ' + cols.iloc[r,i+4] , mode='markers')
        s.marker.color = col[i]
        s.marker.size = 2
        s.marker.line.color = col[i]
        s.marker.line.width = 1
        fig.add_trace(s)
        
    fig.update_layout( xaxis_title='time', autosize=False, width=1000, height=500 )
    # fig.write_html('plot.html')
    
    return fig