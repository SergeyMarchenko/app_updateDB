import plotly.graph_objects as go
import streamlit            as st

# fig = make_plot_clean(c_db_p      =      c_db[sites[0]],
                      # d0_p        =        d0[sites[0]],
                      # c_p         =         c[sites[0]],
                      # cols_p      =         D[sites[0]],
                      # raw_tb_dl_p = raw_tb_dl[sites[0]],
                      # DTnew_p     =     DTnew[sites[0]],
                      # mask_p      =      mask[sites[0]],
                      # v_p         =         v,
                      # rb_p        =        rb )
@st.cache_data(show_spinner="Drawing figure...")
def make_plot_clean(**kwargs):
    # c_db_p      =      c_db[sites[0]]
    # d0_p        =        d0[sites[0]]
    # c_p         =         c[sites[0]]
    # cols_p      =         D[sites[0]]
    # raw_tb_dl_p = raw_tb_dl[sites[0]]
    # DTnew_p     =     DTnew[sites[0]]
    # mask_p      =      mask[sites[0]]
    # v_p         =         v
    # rb_p        =        rb
    
    c_db_p      = kwargs.get('c_db_p'     )
    d0_p        = kwargs.get('d0_p'       )
    c_p         = kwargs.get('c_p'        )
    cols_p      = kwargs.get('cols_p'     )
    raw_tb_dl_p = kwargs.get('raw_tb_dl_p')
    DTnew_p     = kwargs.get('DTnew_p'    )
    mask_p      = kwargs.get('mask_p'     )
    v_p         = kwargs.get('v_p'        )
    rb_p        = kwargs.get('rb_p'       )
       
    if rb_p == 'update existing':
        mask_p = mask_p[v_p]            # leave only the relevant column
        mask_p = mask_p[mask_p]         # leave only the relevant rows
        mask_p = c_p.loc[mask_p.index, mask_p.name]
    
    # r = cols_p[cols_p.index == v_p].index[0]
        
    colors = [
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
    
    
    # raw_ tables with True in check boxes
    i = 0
    for key_table, value in raw_tb_dl_p.items():
        # key_table = 'raw_Steph1_CSci'
        # key_table = 'raw_Steph1_hobo'
        # value = raw_tb_dl_p[key_table]
        if value:
            s = go.Scattergl(x       = d0_p[key_table].index,
                             y       = d0_p[key_table][cols_p.loc[v_p,key_table]],
                             name    = key_table + ': ' + v_p,
                             mode    = 'markers',
                             visible = 'legendonly')
            s.marker.color      = colors[i]
            s.marker.size       = 2
            s.marker.line.color = colors[i]
            s.marker.line.width = 1
            fig.add_trace(s)
        i = i + 1
        
        
    # existing DB clean_ table
    s = go.Scattergl(x    = c_db_p.index,
                     y    = c_db_p[v_p],
                     name = 'existing ' + cols_p.index.name,
                     mode = 'markers')
    s.marker.color      = 'rgb(0,0,0)'
    s.marker.symbol     = 'circle-open'
    s.marker.size       = 5
    s.marker.line.color = 'rgb(0,0,0)'
    s.marker.line.width = 1
    fig.add_trace(s)
    
    
    # new clean_ table        
    if rb_p == 'create new':
        s = go.Scattergl(x    = c_p.index,
                         y    = c_p[v_p],
                         name = 'new ' + cols_p.index.name,
                         mode = 'markers')
        s.marker.color      = colors[i]
        s.marker.symbol     = 'circle-open'
        s.marker.size       = 5
        s.marker.line.color = colors[i]
        s.marker.line.width = 1
        fig.add_trace(s)


    # rows in fresh clean_ that do not exist or have different values in the existing clean_
    if rb_p == 'update existing':
        s = go.Scattergl(x    = DTnew_p,
                         y    = c_p.loc[c_p.index.isin(DTnew_p), v_p],
                         name = 'new values',
                         mode = 'markers')
        s.marker.color      = colors[i]
        s.marker.symbol     = 'circle-open'
        s.marker.size       = 5
        s.marker.line.color = colors[i]
        s.marker.line.width = 1
        fig.add_trace(s)
        i = i + 1
        
        s = go.Scattergl(x    = mask_p.index,
                         y    = mask_p,
                         name = 'updated values',
                         mode = 'markers')
        s.marker.color      = colors[i]
        s.marker.symbol     = 'circle-open'
        s.marker.size       = 5
        s.marker.line.color = colors[i]
        s.marker.line.width = 1
        fig.add_trace(s)


    fig.update_layout( xaxis_title = 'time', yaxis_title = v_p, autosize=False, width=1000, height=500 )
    
    # from pathlib import Path
    # file_path = Path('Z:/FLNRO/Russell Creek/Data/DB/code_2_db/c02_app/plot.html')
    # if file_path.exists():
    #     file_path.unlink()
    #     print(f'{file_path} deleted.')
    # else:
    #     print('File not found.')
    # fig.write_html('plot.html')
    
    return fig




# import plotly.graph_objects as go
# import streamlit            as st

# # fig = make_plot_clean(cols, v, c, d_0)
# @st.cache_data(show_spinner="Drawing figure...")
# def make_plot_clean(cols, v, c, d_0):


#     r = cols[cols.iloc[:,0] == v].index[0]
    
#     col = [
#     'rgb(31,119,180)',
#     'rgb(255,127,14)',
#     'rgb(44,160,44)',
#     'rgb(214,39,40)',
#     'rgb(148,103,189)',
#     'rgb(140,86,75)',
#     'rgb(227,119,194)',
#     'rgb(127,127,127)',
#     'rgb(188,189,34)',
#     'rgb(23,190,207)'
#     ]
    
#     fig = go.Figure()
#     s = go.Scattergl(x=c.index,
#                      y=c[v],
#                      name=cols.columns[0] + ': ' + cols.iloc[r,0],
#                      mode='markers')
#     s.marker.color = 'rgb(0,0,0)'
#     s.marker.symbol = 'circle-open'
#     s.marker.size = 5
#     s.marker.line.color = 'rgb(0,0,0)'
#     s.marker.line.width = 1
#     fig.add_trace(s)
#     for i in range(len(d_0)):
#         s = go.Scattergl(x=d_0[i].iloc[:,0], y=d_0[i][cols.iloc[r,i+4]], name=cols.columns[i+4] + ': ' + cols.iloc[r,i+4] , mode='markers')
#         s.marker.color = col[i]
#         s.marker.size = 2
#         s.marker.line.color = col[i]
#         s.marker.line.width = 1
#         fig.add_trace(s)
        
#     fig.update_layout( xaxis_title='time', autosize=False, width=1000, height=500 )
#     # fig.write_html('plot.html')
    
#     return fig