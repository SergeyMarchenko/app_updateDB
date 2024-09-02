import sys
# import os
# import mpld3
# import re
# os.chdir('Z:\FLNRO\Russell Creek\Data\DB\code_2_db\c02_app')
import pandas            as pd
import numpy             as np
import streamlit         as st
from f01_get_config     import get_config
from f02_get_tables     import get_tables
from f03_get_db         import get_db
from f04_get_file       import get_file_prelim, get_file_defined
from f05_make_plot_t    import make_plot_t
from f06_col_routes     import col_routes
from f07_merge_dbfl     import merge_dbfl
from f08_make_plot_raw  import make_plot_raw
from f09_col_stats      import col_stats
from f10_upload_db      import upload_db
# from streamlit_modal     import Modal
from collections        import defaultdict
from datetime           import datetime


# z:
# cd Z:\FLNRO\Russell Creek\Data\DB\code_2_db\c02_app
# streamlit run app.py

    
st.write("""
# Update an online DataBase table using data from an AWS file
# """)

#__________________________________________
#____Read csv file with login details and generate a connection with MySQL database____
#__________________________________________

st.write('1. Path to config.csv file with credentials to access the DataBase:')
path_config = st.file_uploader(' ')
#
# path_config = 'Z:/FLNRO/Russell Creek/Data/DB/code_2_db/config.csv'
#
if not path_config:
  st.warning('To proceed upload the file "config.csv" first!')
  st.stop()

url = get_config(path_config)
del path_config

"---"
#__________________________________________
#____Load data from the online database____
#__________________________________________
st.write('2. Define the DataBase table to update')
new_old = st.radio(
    '2.1. New or existing table:',
    ['Existing table', 'New table'], help = 'Choose whether data in the text file is used to update an existing table in the DataBase or start a new one.',
    captions = ['',''])

if new_old == "Existing table":
    table_names = get_tables(url)
    db_path = st.selectbox( "2.2. Choose DataBase table to update (reload required if recently updated)", table_names, index = None )
    #
    # db_path = 'raw_RussellMain_hobo'
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
    

"---"


#__________________________________________
#____load data from the text file downloaded from the logger____
#__________________________________________

st.write("3. Text file to be used for updating/initiating of a DataBase table (from e.g. AWS data logger)")

# fl_path = 'Z:\FLNRO\Russell Creek\Data\DB\data_1_legacy\legacy_non_upd\S1_CSci.txt'
# delim = ';'
# rskip = '1'
# tcol  = '1,2,3,4,5,6'
# dcol  = '7'
# hrow  = '0'
# urow  = '1'
# drow  = '3'
    
r1, r2 = st.columns([0.8, 0.2])
with r1:
    fl_path = st.file_uploader("Path to file:")
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
    dcol  = st.text_input('Data col(s):'  , value = '1', key='fl_dcol' , help='Number of first column with data, all columns to the right are read too. If multiple numbers separated by "," are given, only the specific columns are read.')
with r3:
    hrow  = st.text_input('Header row:'   , value = '1', key='fl_hrow' , help='Number of the row with column headers.')
with r4:
    urow  = st.text_input('Units row:'    , value = '2', key='fl_urow' , help='Number of the row with column units. Leave empty if now such row exists.')
with r5:
    drow  = st.text_input('Data row(s):'  , value = '4', key='fl_drow' , help='Number of first row with data, all rows below are read too.')



    
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
    

#__________________________________________
#____table to map columns in file to columns in database
#__________________________________________
"---"

st.write("3. Route columns in the AWS file to columns in the database table")

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
"---"


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



upload = st.button('Initiate/Update DataBase table', key = "p_upd")
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
    
"---"

sys.exit()






    







    
  




