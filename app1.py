import sys
# import os
# import mpld3
# import re
# os.chdir('Z:\FLNRO\Russell Creek\Data\DB\code_2_db\c02_app')
import pandas               as pd
import numpy                as np
from   sqlalchemy           import create_engine, text
import streamlit            as st
import plotly.graph_objects as go
from f01_get_config         import get_config
from f02_get_tables         import get_tables
from f03_get_db             import get_db
from f04_get_file           import get_file_prelim, get_file_defined
from f05_make_plot_t        import make_plot_t
from f06_col_routes         import col_routes
from f07_merge_dbfl         import merge_dbfl
from f08_make_plot_raw      import make_plot_raw
from f09_col_stats          import col_stats
from f10_upload_db          import upload_db
from f12_raw_to_clean       import raw_to_clean
from f14_make_plot_clean    import make_plot_clean
from f15_sites_tables_cols  import sites_tables_cols
# from streamlit_modal     import Modal
from collections            import defaultdict
from datetime               import datetime, timedelta


# z:
# cd Z:\FLNRO\Russell Creek\Data\DB\code_2_db\c02_app
# streamlit run app1.py

    
st.header('Update or initiate an online DataBase table')
st.header('using data from an AWS file', divider='green')


#__________________________________________
#____Read csv file with login details and generate a connection with MySQL database____
#__________________________________________

st.subheader('1. DataBase access')
path_config = st.file_uploader('Path to config.csv file with credentials to access the DataBase:')
#
# path_config = 'Z:/FLNRO/Russell Creek/Data/DB/code_2_db/config.csv'
#
if not path_config:
  st.warning('To proceed upload the file "config.csv" first!')
  st.stop()

url = get_config(path_config)
del path_config

st.header('', divider='green')
#__________________________________________
#____Load data from the online database____
#__________________________________________
st.subheader('2. Choose DataBase table to update')
new_old = st.radio(
    '2.1. New or existing table:',
    ['Existing table', 'New table'], help = 'Choose whether data in the text file is used to update an existing table in the DataBase or start a new one.',
    captions = ['',''])

if new_old == "Existing table":
    table_names = get_tables(url)
    db_path = st.selectbox( "2.2. Choose DataBase table to update (reload required if recently updated)", table_names, index = None )
    #
    # db_path = 'raw_Steph1_CSci'
    #
    if not db_path:
      st.warning('To proceed choose table to update first!')
      st.stop()
    del table_names

    db_d, db_h, db_coltyp = get_db(url, db_path)
    
    r1, r2 = st.columns(2)
    with r1:
        b1 = st.button("Show the current DataBase table")
    with r2:
        cb1 = st.checkbox('First 10 and last 2 rows', value = True, help = "Uncheck the box to show the entire table.", key = 'cb1')
    # with st.expander("Show the top and bottom of the current DataBase table"):        

    if b1 and cb1:
        tmp = pd.concat([db_d.head(10), pd.DataFrame(np.nan, index=[0], columns=db_d.columns), db_d.tail(2)], ignore_index=False)
        st.dataframe(tmp, hide_index = False)
        del tmp
    elif b1:
        st.dataframe(db_d)
else:
    db_path = "raw"
    # st.text_input('Name for the new database table:', "raw_")
    

st.header('', divider='green')


#__________________________________________
#____load data from the text file downloaded from the logger____
#__________________________________________

st.subheader("3. Choose text file")

# fl_path = 'Z:/FLNRO/Russell Creek/Data/1 Steph 1/2024/2024_04_18/Steph1_Hourly1_2023-11-30T09-52.dat'
# delim = ','
# rskip = '1'
# tcol  = '0'
# dcol  = '2'
# hrow  = '0'
# urow  = '1'
# drow  = '3'
    
r1, r2 = st.columns([0.8, 0.2])
with r1:
    fl_path = st.file_uploader("Path to the file to be used for updating/initiating a DataBase table (from e.g. AWS data logger):")
with r2:
    delim   = st.text_input('Column delimiter:' , value = ',', max_chars=1, key='fl_delim', help='Symbol separating columns')
    rskip   = st.text_input('N of rows to skip:', value = '1', key='fl_rskip' , help='Number of rows to skip. Number of columns should should be the same as in all rows')

if not fl_path:
  st.warning('To proceed choose text file!')
  st.stop()

fl_d0 = get_file_prelim(fl_path, delim, rskip)

with st.expander("Show the preliminary read AWS file"):
# if st.button("Show the preliminary read AWS file"):
    st.dataframe(fl_d0.head(10), hide_index = False)


st.write("Settings for the text file reader, column and row numbers are given with reference to the preliminary read file:")

r1, r2, r3, r4, r5 = st.columns(5)
with r1:
    tcol  = st.text_input('Time col(s):'  , value = '0', key='fl_tcol' , help='Number of column(s) with time stamps. Multiple numbers are to be separated by ","')
with r2:
    dcol  = st.text_input('Data col(s):'  , value = '2', key='fl_dcol' , help='Number of first column with data, all columns to the right are read too. If multiple numbers separated by "," are given, only the specific columns are read.')
with r3:
    hrow  = st.text_input('Header row:'   , value = '0', key='fl_hrow' , help='Number of the row with column headers.')
with r4:
    urow  = st.text_input('Units row:'    , value = '1', key='fl_urow' , help='Number of the row with column units. Leave empty if now such row exists.')
with r5:
    drow  = st.text_input('Data row(s):'  , value = '3', key='fl_drow' , help='Number of first row with data, all rows below are read too.')



    
fl_d, fl_h, fl_coltyp = get_file_defined(fl_d0, tcol, dcol, hrow, urow, drow)

del fl_d0


r1, r2 = st.columns(2)
with r1:
    b2 = st.button("Show the AWS file")
with r2:
    cb2 = st.checkbox('First 10 and last 2 rows', value = True, help = "Uncheck the box to show the entire file.", key = 'cb2')

if b2 and cb2:
    tmp = pd.concat([fl_d.head(10), fl_d.tail(2)], ignore_index=False)
    st.dataframe(tmp , hide_index = False)
    del tmp
elif b2:
    st.dataframe(fl_d, hide_index = False)
    
    

if new_old == "New table":
    db_h      = fl_h
    db_coltyp = fl_coltyp
    db_d      = fl_d.head(0)
    
st.header('', divider='green')
#__________________________________________
#____table to map columns in file to columns in database
#__________________________________________

st.subheader("3. Route AWS file columns to DataBase table columns")

if st.button("Show time lines for existing DataBase table and AWS file"):
    fig_t = make_plot_t(db_d.index.tolist(), fl_d.index.tolist())
    st.plotly_chart(fig_t, use_container_width=True)

col_dict = {key: '' for key in fl_h}
_, col_dict = col_routes(db_d, fl_d, db_h, fl_h)    #for each column in the data file find the best matching column in the database


col = [2.5, 3.5, 0.8, 0.8, 0.8, 0.8, 0.8, 1.2]

r1, r2, r3  = st.columns([col[0], col[1], sum(col[2:])])
with r1:
   st.text("AWS file")

with r2:
   st.text("Database")
   
with r3:
    h = """
    Statistics for data in DataBase and AWS file for overlapping times:
        fraction of elements that are exactly the same, %
        coefficient of correlation
        fraction of NAN values in DataBase, %
        fraction of NAN values in AWS file, %
    Checkbox - click to overwrite non-NaN values in the DataBase
    by values from for the overlapping time period
        """
    st.text("Common time stats and control", help = h)

if new_old == "Existing table":
    db_h_o = ['add NEW COLUMN to db', 'SKIP the column'] + db_h
else:
    db_h_o = [                        'SKIP the column'] + db_h

ow_flag = [False] * len(col_dict)
count = 0
for key in col_dict:
    r1, r2, r3, r4, r5, r6, r7, r8 = st.columns(col)
    with r1:
        st.write(key)

    with r2:
        if col_dict[key] == '':
            ind = None
        else:
            ind = db_h_o.index(col_dict[key])
        col_dict[key] = st.selectbox(" "   , db_h_o, key = "o_"+key, index = ind, label_visibility="collapsed" )
        del ind
        
    if col_dict[key] != 'add NEW COLUMN to db' and col_dict[key] != 'SKIP the column' and any(fl_d.index.isin(db_d.index)):
        _, Ne, cc_d, cc_h, nana, nanb = col_stats(db_d, fl_d, col_dict, key)
        with r3:
            st.text(Ne)
        with r4:
            st.text(cc_d)
        with r5:
            st.text(nana)
        with r6:
            st.text(nanb)
    
    with r7:
        ow_flag[count] = st.checkbox(' ', False, key = "ow_flag_"+key, label_visibility = 'collapsed')
        
    with r8:
        p = st.button( 'plot', key = "p_"+key, disabled = col_dict[key] == None )
        
    count = count + 1

#_______________________
# group col_dict keys with same values in rows of a list
repcol = defaultdict(list)
for key, value in col_dict.items():
    if value != 'add NEW COLUMN to db' and value != 'SKIP the column':
        repcol[value].append(key)
repcol = [keys for keys in repcol.values() if len(keys) > 1]

# warning message in case two columns from file are routed to the same column in database
if len(repcol)>0:
    st.warning('Following columns in the AWS file have the same destination:')
    for row in repcol:
        st.write(row)
    st.warning('choose a different destination for one of the columns above to continue!')
    st.stop()

# merge the existing DataBase table and data in the text file    
c, col_dict_out = merge_dbfl(db_d, fl_d, col_dict, ow_flag)

# plot to visualize data in the: existing DataBase table, text file, merged dataframe
for key in col_dict.keys():
    if st.session_state["p_" + key]:
        fig = make_plot_raw(db_d, fl_d, c, col_dict, col_dict_out, key)
        st.plotly_chart(fig, use_container_width=True)
        
# modal = Modal(
#     "Plot",
#     key="figure_window",
#     padding   =    2,    # Optional, default value -  20
#     max_width = 1500     # Optional, default value - 744
# )
# open_modal = st.button("plot", key = "p_1")
# if open_modal:
#     modal.open()


# if modal.is_open():
#     with modal.container():
#        fig = make_plot(db_t, db_d, fl_t, fl_d, c, col_dict, "BattV_Avg_Volts")
#        st.plotly_chart(fig, use_container_width=True)


# convert columns with TimeStamps back to DateTime strings if they are not meant to be skipped
if 'time' in fl_coltyp:
    ind_fl = [i for i, x in enumerate(fl_coltyp) if x == 'time']
    for i in ind_fl:
        if fl_h[i] in col_dict_out.keys():
            c[col_dict_out[fl_h[i]]] = pd.to_datetime( c[col_dict_out[fl_h[i]]] )

elif 'datetime64[ns]' in db_coltyp:
    ind_db = [i for i, x in enumerate(db_coltyp) if x == 'datetime64[ns]']
    for i in ind_db:
        c[db_h[i]] = pd.to_datetime( c[db_h[i]], unit = 'ns' )

st.header('', divider='green')


#_______________________
st.subheader('4. Update/initiate raw_ table')

r1, r2 = st.columns(2)
with r1:
    b3 = st.button("Show the new/updated DataBase table")
with r2:
    cb3 = st.checkbox('First 10 and last 2 rows', value = True, help = "Uncheck the box to show the entire table.", key = 'cb3')

if b3 and cb3:
    tmp = pd.concat([c.head(10), c.tail(2)], ignore_index=False)
    st.dataframe(tmp , hide_index = False)
    del tmp
elif b3:
    st.dataframe(c)


now = datetime.now()
now = now.strftime("%Y%m%d")

db_path_updated = st.text_input('Name for the new/updated DataBase table:', db_path + '_upd_' + now)


upload = st.button('Initiate/Update DataBase table', key = 'p_upd')
if upload:
    m3 = upload_db(c, url, db_path_updated)
    m1 = 'DataBase table "' + db_path + '" updated '
    m2 = 'using data from file "' + fl_path.name + '"'
    mm = st.text_area(' ', m1 + '\n' + m2 + '\n' + m3)
    
    if np.random.randint(0, 100)>50:
        st.balloons()
    else:
        st.snow()
    st.cache_data.clear()
    
st.header('', divider='green')


#_______________________
st.subheader('5. Update clean_ table')
st.markdown(':red[Stop! Have you forgotten Hourly2?]')
st.write('If the logger generates more than one data table simultaneously, the clean_ table is to be updated only after when the raw_ table has been updated using all files from the data logger.')

# if not 'mm' in locals():
#     st.warning('To proceed update the raw_ table first!')
#     st.stop()
    
sites, cols_S1, cols_S2, cols_S4, cols_S6 = sites_tables_cols()
if   '1' in db_path:
    ind = 0
elif '2' in db_path:
    ind = 1
elif '4' in db_path:
    ind = 2
elif '6' in db_path:
    ind = 3
    
clean_site = st.selectbox( "Choose site profile for generating the clean_ table ", sites, index = ind )
if   clean_site == 'S1':
        cols = cols_S1
elif clean_site == 'S2':
        cols = cols_S2
elif clean_site == 'S4':
        cols = cols_S4
elif clean_site == 'S6':
        cols = cols_S6

if 'd_2' not in st.session_state:
    st.session_state.d_0 = []
    st.session_state.d_2 = []
    st.session_state.D   = []
r1, r2, r3 = st.columns([0.4, 0.3, 0.3])
with r1:
    b41 = st.button('Generate data in clean_ format', key = 'p_gen_clean', help = "Using data from the raw_ table and AWS file a table in clean_ format will be generated for the times covered by the AWS file and 15 days preceding that.")
with r2:
    b42  = st.button("Show the clean_ table")
with r3:
    b43 = st.checkbox('First 10 and last 2 rows', value = True, help = 'Uncheck the box to show the entire table.', key = 'cb4')

if b41:
    t_max_f = fl_d.index[0] - timedelta(days = 15)
    d_0 = c[c.index > t_max_f].reset_index()
    st.session_state.d_0 = d_0
    _, d_2 = raw_to_clean(cols, 4, d_0)
    m = d_2.index.month > 9   # Add water year column
    d_2.insert( 0, 'WatYr', d_2.index.year+1*m.astype(int) )
    st.session_state.d_2 = d_2
    
    engine = create_engine(url)
    with engine.connect() as connection:
        t_max_c = connection.execute(text(f"SELECT MAX(t) FROM {cols.columns[0]}"))
    st.session_state.D = d_2[d_2.index>t_max_c.scalar()]
    
   

if b42:
    if len( st.session_state.d_2 ) == 0:
        st.warning('To proceed generate clean_ table first!')
        st.stop()
    d_2 = st.session_state.d_2
    if b43:
        st.dataframe(pd.concat([d_2.head(10), d_2.tail(2)], ignore_index=False) , hide_index = False)
    else:
        st.dataframe(d_2)
st.title('')

# plotting
if 'С' not in st.session_state:
    st.session_state.С = []
r1, r2, r3 = st.columns([0.4, 0.3, 0.3])
with r1:
    b51 = st.button('Load UNupdated clean_ table', key = 'p_load_clean', help = 'Download the current clean_ table from the DataBase for plotting.')
with r2:
    b52 = st.selectbox( 'Choose variable to plot', cols.iloc[1:,0], index = None )
    # b52 = "Air_Temp"
with r3:
    b53 = st.button('Plot', help = 'Plot data from raw and clean tables')


if b51:            # download existing clean_ table and update it using data from the raw_ table
    engine = create_engine(url)
    with engine.connect() as connection:
        st.session_state.С = pd.read_sql(f"SELECT * FROM {cols.columns[0]}", connection)
    st.session_state.С.set_index('t', inplace=True)
    # st.session_state.D = st.session_state.C.copy()
    # st.session_state.D.update(d_2)
    # st.session_state.D = pd.concat([st.session_state.D, d_2.loc[~d_2.index.isin(st.session_state.D.index)]])

if b53:
    if not b52 or len(st.session_state.С) == 0:
      st.warning('To proceed load UNupdated clean_ table and choose the variable to plot!')
      st.stop()
      
    v = b52
    d_0 = st.session_state.d_0
    С = st.session_state.С
    fig = make_plot_clean(cols, v, С, [d_0])
    s = go.Scattergl(x=st.session_state.D.index,
                     y=st.session_state.D[v],
                     name=cols.columns[0] + ' (data for update): ' + v,
                     mode='markers')
    s.marker.color = 'rgb(214,39,40)'
    s.marker.size = 1
    s.marker.line.color = 'rgb(214,39,40)'
    s.marker.line.width = 1
    fig.add_trace(s)
    
    # fig.write_html('plot.html')
    st.plotly_chart(fig, use_container_width=True)



b6 = st.button('Update clean_ table', key = 'p_upd_clean', help = "Append new data from raw_ table to the clean_ table.")
st.session_state.D
if b6:
    engine = create_engine(url)
    st.session_state.D.to_sql(name=cols.columns[0], con=engine, if_exists = 'append', index = False)
    
st.stop()

    



    




# c_out = c
# c_out.insert(0, 't', c_out.index)
# c_out.reset_index(drop=True, inplace=True)

# with engine.connect() as con:
#     con.execute(text('alter table ' + db_path_updated + ' add primary key (t)'))
    
sys.exit()






    







    
  




