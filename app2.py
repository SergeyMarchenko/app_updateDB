# z:
# cd Z:\FLNRO\Russell Creek\Data\DB\code_2_db\c02_app
# streamlit run app2.py

import streamlit         as st
# import os
# os.chdir('Z:\FLNRO\Russell Creek\Data\DB\code_2_db\c02_app')
import pandas as pd
import numpy  as np
from datetime               import datetime
from f01_get_config         import get_config
from f10_upload_db          import upload_db
from f11_get_db_loop        import get_db_loop
from f13_raw_to_clean_loop  import raw_to_clean_loop
from f14_make_plot_clean    import make_plot_clean
from f15_sites_tables_cols  import sites_tables_cols

st.title('raw_ -> clean_')
st.header('Process raw_* tables with data collected at one site using different installations and merge them to a single clean_* table.', divider="green")


#____Read text files with login details and prepare to connect to the MySQL database,

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
#____Choose the site____
#__________________________________________
if st.checkbox('use a template', value = True, help = 'if checked, a template is downloaded and user chooses a site from suggested list'):
    sites, cols_S1, cols_S2, cols_S4, cols_S6 = sites_tables_cols()
    
    # select template from the column mapping file
    site = st.selectbox( "Choose site", sites, index = None )
    # site = 'S1'
    
    if not site:
      st.warning('To proceed choose the site first!')
      st.stop()
      
    if   site == 'S1':
                        cols = cols_S1
    elif site == 'S2':
                        cols = cols_S2
    elif site == 'S4':
                        cols = cols_S4
    elif site == 'S6':
                        cols = cols_S6
    
tables_raw = ''
for tb in range(4,cols.shape[1]):
    tables_raw = tables_raw + cols.columns[tb] + ', '
tables_raw = tables_raw[0:-2]
db_path_updated = cols.columns[0] + '_' + datetime.now().strftime("%Y%m%d")

with st.expander('Show how tables ' + tables_raw + ' are converted to a "clean_*" table' ):
    st.write("Table used for routing columns from raw tables to clean")
    st.dataframe(cols)

    
# Confirm names of tables to be downloaded and used for merging

# buttons for downloading raw_ tables and generating clean_ tables
r11, r12 = st.columns([0.3, 0.7])
r21, r22 = st.columns([0.3, 0.7])
b_get_db_loop  = r11.button("Download raw_* tables" , help = "Download raw_* tables listed as headers of columns 4... in the table above")
b_raw_to_clean = r21.button("Generate clean_* table", help = "Process raw_* tables to have consistent column structure, no unfeasible values, even 1h time step, water year column and merge in one clean_* table")


if 'd_0' not in st.session_state:
    st.session_state.d_0       = {}
    
if site not in st.session_state.d_0:
    st.session_state.d_0[site] = []

if b_get_db_loop:
    st.session_state.d_0[site] = get_db_loop(cols, url)
    # d_0                      = get_db_loop(cols, url)
    
if st.session_state.d_0[site] == []:
    st.warning('To proceed download raw_ tables for site "' + site + '" first')
    st.stop()
else:
    r12.success("tables " + tables_raw + " are downloaded")
    d_0 = st.session_state.d_0[site]



if 'c'   not in st.session_state:
    st.session_state.c         = {}
    
if site not in st.session_state.c:
    st.session_state.c[site]   = []
        
if b_raw_to_clean:
    st.session_state.c[site] = raw_to_clean_loop(cols, d_0)
    # c                        = raw_to_clean_loop(cols, d_0)

if isinstance(st.session_state.c[site], list) or st.session_state.c[site].empty:
    st.warning('To proceed generate clean_ table for site "' + site + '" first')
    st.stop()
else:
    r22.success("clean_ table: " + db_path_updated + " is generated")
    c = st.session_state.c[site]

"---"
# plotting
v = st.selectbox( "Choose a variable to plot", cols.iloc[1:,0], index = None )

if st.button("Plot", help = "Plot data from raw tables and clean table"):
    if not v:
      st.warning('To proceed choose the variable to plot first!')
      st.stop()
      
    fig = make_plot_clean(cols, v, c, d_0)
    st.plotly_chart(fig, use_container_width=True)
    
"---"    
    
# Export table to database
db_path_updated = st.text_input('Name for the clean DataBase table:', db_path_updated)
# db_path_updated = cols.columns[0] + '_today'
if st.button('Upload DataBase table', key = "p_upd"):
    m = upload_db(c, url, db_path_updated)
    m1 = ''
    for tb in range(4,cols.shape[1]):
        m1 = m1 + cols.columns[tb] + ', '
    mm = st.text_area(' ', m + '\n' + 'For that tables: "' + m1[0:-2] + ' were used.' )

    if np.random.randint(0, 100)>50:
        st.balloons()
    else:
        st.snow()
    st.cache_data.clear()

st.stop()






#))))))))))
# import time
# t0 = time.time()
# dt = time.time() - t0
# st.write(dt)
# del t0, dt