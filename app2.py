# z:   
# cd Z:\FLNRO\Russell Creek\Data\DB\code_2_db\c02_app
# streamlit run app2.py


# import os
# os.chdir('Z:\FLNRO\Russell Creek\Data\DB\code_2_db\c02_app')
import streamlit         as st
import pandas as pd
import numpy  as np
from sqlalchemy            import create_engine, inspect, text, types
from f01_get_config        import get_config
from f03_get_db            import get_db
from f13_raw_to_clean_loop import raw_to_clean_loop
from f14_make_plot_clean   import make_plot_clean
from f15_sites_tables_cols import sites_tables_cols
from f17_filter_raw_info   import filter_raw_info


st.title('raw_ -> clean_')
st.header('Convert tables from raw_ to clean_ format.', divider='green')

#__________________________________________
#____Read text files with login details and prepare to connect to the MySQL database,
#__________________________________________
st.write('1. Access DataBase')
path_config = st.file_uploader('Path to config.csv file with credentials to access the DataBase:', key = 'app2_fileUpl')
# path_config = 'Z:/FLNRO/Russell Creek/Data/DB/code_2_db/config.csv'
if not path_config:
    st.warning('To proceed upload the file "config.csv" first!')
    st.stop()

url = get_config(path_config)
del path_config


"---"

#__________________________________________
#____Choose the site____
#__________________________________________
st.write('2. Set up raw_ -> clean_ processing')

D = sites_tables_cols()
F = filter_raw_info()

if st.button('Start over' , help = 'starts a new session by cleaning the cache memory'):
    st.cache_data.clear()
    st.session_state.clear()
    st.session_state['site_select'] = None
    if 'd_0' in st.session_state:
        del st.session_state.d_0
    st.warning('App cache is clear and all created variables deleted.')


# select template from the column mapping table
st.write('2.1. Choose site:')
help_txt_sites = '''
          For each site listed a template guiding the raw_ -> clean_ format
          convertsion exists and will be applied.
          If the 'All sites' option is highlighted
          all sites will be processed even some of them are not highlighted.
          In that case user has reduced options for customizing the process.
          Choosing one site allows user to see the table guiding the
          raw_ -> clean_ format convertsion, customize processing and
          visualize individual parameters.'
          '''
sites = st.pills('', ('All sites',) + tuple(D.keys()), selection_mode='multi', default=None, key='site_select',
              help = help_txt_sites,
              label_visibility = 'visible', width='content')
if not sites:
  st.warning('To proceed choose the site first!')
  st.stop()
  
sites = tuple(sites)
# sites = ('S1',)
# sites = ('All sites',)
if 'All sites' in sites:
    sites = tuple(D.keys())
else:
    sites = tuple(sorted(sites, key=lambda x: int(x[1:])))

D = {k: v for k, v in D.items() if k in sites}
F = {k: v for k, v in F.items() if k in sites}

if len(D)==1:
    with st.expander('Show how existing raw_ tables are converted to clean_ format' ):
        st.dataframe(next(iter(D.values())), key = 'app2_datFr_columnRouting')
    # with st.expander('Show allowed min and max values for variables in clean_ table' ):
        # st.dataframe(appropriate variable, key = 'app2_datFr_minmax')
    with st.expander('Show events in the filtering routine' ):
        i = 0
        for raw_table in F[sites[0]].keys():
            print(raw_table)
            for var_name in F[sites[0]][raw_table].keys():
                print(var_name)
                if F[sites[0]][raw_table][var_name]:
                    if F[sites[0]][raw_table][var_name]['events']:
                        for ev in F[sites[0]][raw_table][var_name]['events'].keys():
                            st.write('Table: ' + raw_table + ', variable: ' + var_name)
                            st.dataframe(F[sites[0]][raw_table][var_name]['events'][ev], key = 'app2_datFr_events'+str(i))
                            i = i+1
        


# Confirm names of tables to be downloaded and used for merging
st.write('2.2. Select raw_ tables to be downloaded and converted to clean_ format:')
raw_tb_dl = {site: {k2: False for k2 in raw_table} for site, raw_table in F.items()}

if len(D) == 1:
    for key in raw_tb_dl[sites[0]]:
        raw_tb_dl[sites[0]][key] = st.checkbox(key, value=raw_tb_dl[sites[0]][key], help='Checking the box includes corresponding tables in processing loop. Tables are listed as headers of columns 5... in the table above', key = 'app2_chBox_includeRawTable'+key)
# key = list(raw_tb_dl[sites[0]].keys())
# raw_tb_dl[sites[0]][key[0]] = True
# raw_tb_dl[sites[0]][key[1]] = True

# all_latest = 'all'
# all_latest = 'only latest'

if len(D) > 1:
    all_latest = st.radio('', ['all', 'only latest'],
                          captions = ['all raw_ tables for all sites will be converted to clean_ format', 'only the latest raw_ tables for all sites will be converted to clean_ format'],
                          horizontal = True, label_visibility = 'collapsed', index = 0, key = 'app2_radio_allLatest')
    if all_latest == 'all':
        for outer_key, inner_dict in raw_tb_dl.items():
            for inner_key in inner_dict:
                inner_dict[inner_key] = True
        del outer_key, inner_dict, inner_key
        
    if all_latest == 'only latest':
        for outer_key, inner_dict in raw_tb_dl.items():
            first = True
            for inner_key in inner_dict:
                if first:
                    inner_dict[inner_key] = True
                    first = False
                else:
                    inner_dict[inner_key] = False
        del outer_key, inner_dict, first, inner_key



# ! Implement smth to ensure that names of columns in column routing file make sense: exist in the tables, are not doubled in source or destination 



st.write('2.3. Download chosen raw_ tables and convert them to clean_ format')
r11, r12 = st.columns([0.3, 0.7])
help_txt ='''
          Hitting the button will initiate download of existing clean_ and raw_ tables for the chosen sites.\n
          raw_ tables will be converted to clean_ format, this involves:\n
          consistent column structure, no unfeasible values, even 1h time step, water year column.\n
          If multiple tables with raw_ data collected at one site but using different installations are selected,\n
          generated clean_ tables are merged in one. For overlapping time steps merging implies preference of\n
          data from new installations (in f15_sites_tables_cols.py names appear to the left) over\n
          data from phased out stations (in f15_sites_tables_cols.py names appear to the right).
          '''
b_raw_to_clean = r11.button('raw_ -> clean_' , help = help_txt)  # button for downloading raw_ tables and generating clean_ tables

if 'c_db' not in st.session_state:
    st.session_state.c_db  = {}

if 'd0'   not in st.session_state:
    st.session_state.d0    = {}

if 'c'    not in st.session_state:
    st.session_state.c     = {}

# routines upon clicking the raw_ -> clean_ button
if b_raw_to_clean:
    d0, c = raw_to_clean_loop(D, F, raw_tb_dl, url)
    
    c_db = {}
    for site_key in c.keys():
        # site_key = 'S1'
        c_db[site_key]  = {}
        insp = inspect(create_engine(url))
        if D[site_key].index.name in insp.get_table_names():
            c_db[site_key], _, _ = get_db(url, D[site_key].index.name)
            c_db[site_key] = c_db[site_key].replace({None: np.nan})
        else:
            c_db[site_key] = pd.DataFrame( columns = c[site_key].columns,
                                            index   = pd.DatetimeIndex([]) )

    st.session_state.c_db = c_db
    st.session_state.d0   = d0
    st.session_state.c    = c
    

if st.session_state.d0 == {}:
    st.warning('To proceed download raw_ tables and convert them to clean_ format first')
    st.stop()
else:
    r12.success('Selected raw_ tables are downloaded and converted to clean_ format. Existing clean_ tables are downloaded.')
    c_db = st.session_state.c_db
    d0   = st.session_state.d0
    c    = st.session_state.c

st.write('2.4. Create a new clean_ table or update existing?')
# clean_ tables from DB: for exist -> download, if not -> create fake dummies
# if all( (len(df) == 1) and df.isna().all().all() for df in c_db.values() ):
    # rb = st.radio('', ['create new'                   ], captions = ['generated table will be uploaded to DB'   ,                                                     ], horizontal = True, label_visibility = 'collapsed', index = 0, key = 'app2_radio_new')
# else:
rb = st.radio('', ['create new', 'update existing'], captions = ['generated table replaces the existing one', 'generated table is used to update the existing one'], horizontal = True, label_visibility = 'collapsed', index = 1, key = 'app2_radio_newExisting')
    
# rb = 'create new'
# rb = 'update existing'
if len(D) == 1:
    cb1 = st.checkbox('First and last 10 rows', value = True, help = 'Uncheck the box to show the entire table.', key = 'app2_chBox_clean_firstlast10')
    with st.expander('Show the generated clean_ table'):
        if rb == 'update existing':
            st.write('Showing the entire table in clean_ format including rows possibly overlapping with the existing ' + D[sites[0]].columns[0] + ' DB table.')
        if cb1:
            st.dataframe(pd.concat([c[sites[0]].head(10), c[sites[0]].tail(10)]), hide_index = False, key = 'app2_datFr_showClean_firstLast10')
        else:
            st.dataframe(           c[sites[0]]                                 , hide_index = False, key = 'app2_datFr_showClean_all')

DTnew  = {}
DTdiff = {}
mask   = {}
for site_key in c.keys():
    # site_key = 'S1'
    timestamps: list[pd.Timestamp] = []
    DTnew[site_key]  = timestamps
    DTdiff[site_key] = timestamps
    mask[site_key]   = pd.DataFrame(columns=c[site_key].columns, index=pd.DatetimeIndex([]))
    del timestamps
    if rb == 'update existing':
        DTnew[site_key] = c[site_key].index.difference(  c_db[site_key].index).tolist() # new DateTimes in fresh clean_ table that are not found in the existing clean_ table
        DTcom           = c[site_key].index.intersection(c_db[site_key].index).tolist() # common DateTimes
        # Compare only rows where index is common and return DateTimes where any pair of values is different by more than 0.1%
        if DTcom != []:
            mask[site_key] = np.isclose(c_db[site_key].loc[DTcom],
                                            c[site_key].loc[DTcom],
                                          rtol=1e-3, equal_nan=True) == False
            DTdiff[site_key] = [d for d, flag in zip(DTcom, mask[site_key].any(axis=1)) if flag]
            mask[site_key] = pd.DataFrame(mask[site_key], index=DTcom, columns=c[site_key].columns)
            mask[site_key] = mask[site_key].loc[mask[site_key].index.isin(DTdiff[site_key])]
            
if   rb == 'update existing':
    with st.expander('Show data to be used for updating the existing clean_ table(s).'):
        for site_key in c.keys():
            st.write(site_key)
            tmp1 = c[site_key].loc[c[site_key].index.isin( DTnew[site_key] )]
            tmp2 = c[site_key].loc[c[site_key].index.isin(DTdiff[site_key] )]
            pd.set_option("styler.render.max_elements", 2000000 )
            tmp2 = tmp2.style.apply(lambda s: ['background-color: orange' if mask[site_key].loc[s.name, c] else '' for c in s.index], axis=1)
            with st.expander(str(tmp1.shape[0]) + ' rows in the newly generated clean_ table are NOT in the existing clean_ table. They will be appended:'):
                st.dataframe(tmp1, hide_index = False, key = 'app2_datFr_showNew_'+site_key)
            with st.expander(str(tmp2.data.shape[0]) + ' rows exist BOTH in newly generated and existing clean_ tables, but have different values in some columns. These rows in the new clean_ table will be used to update the existing clean_ table:'):
                if st.checkbox('Highlight differing cells', value = False, help = 'This may slow down the app if number of rows is large.', key = 'app2_cb_highlightdiff_'+site_key):
                    st.dataframe(tmp2, hide_index = False, key = 'app2_datFr_showDiff_'+site_key)
                else:
                    st.dataframe(tmp2.data, hide_index = False, key = 'app2_datFr_showDiff_styled_'+site_key)
            del tmp1, tmp2



"---"
#__________________________________________
#____ plotting
#__________________________________________
if len(c) == 1:
    st.write('3. Plotting. Choose a variable to plot:')
    L = [col for col in c[sites[0]].columns if not c[sites[0]][col].replace('', np.nan).isna().all()]
    L.remove('WatYr')
    # v = L[0]
    v = st.selectbox( '', L, index = None, label_visibility = 'collapsed', key = 'app2_selBox_plotVar' )
    if st.button('Plot', help = 'Plot data from raw tables and clean table', key = 'app2_butt_figClean' ):
        if not v:
          st.warning('To proceed choose the variable to plot first!')
        else:
            fig = make_plot_clean(c_db_p      =      c_db[sites[0]],
                                  d0_p        =        d0[sites[0]],
                                  c_p         =         c[sites[0]],
                                  cols_p      =         D[sites[0]],
                                  raw_tb_dl_p = raw_tb_dl[sites[0]],
                                  DTnew_p     =     DTnew[sites[0]],
                                  mask_p      =      mask[sites[0]],
                                  v_p         =         v,
                                  rb_p        =        rb )
            st.plotly_chart(fig, use_container_width=True, key = 'app2_fig_figClean')


    
"---"
#__________________________________________
#____ Update existing DB table
#__________________________________________
st.write('4. Upload generated table(s)')

if   rb == 'create new':
    b_upl_help_text = 'Generated table '   + D[sites[0]].index.name + ' will be uploaded to DB. If DB already contains a table with the same name, it will be overwritten.'
elif rb == 'update existing':
    b_upl_help_text = 'Existing DB table ' + D[sites[0]].index.name + ' will be updated using the newly generated table based on DateTime values in rows: rows with new DateTime values are appended, rows with existing DateTime values and deviating column values will overwrite rows in DB table.'
    
if st.button('Upload clean_ !', help = b_upl_help_text, key = 'app2_butt_UpdateClean'):
    
    if  rb == 'create new':
        for site_key in c.keys():
            co = c[site_key].copy()
            co = co.reset_index()
            dtypes = {col: types.Float for col in co.columns if col != 'DateTime' or col != 'WatYr'}
            dtypes['DateTime'] = types.DateTime
            dtypes['WatYr'   ] = types.INTEGER
            engine = create_engine(url)
            co.to_sql(name=D[site_key].index.name, con=engine, if_exists = 'replace', index = False, dtype=dtypes)
            with engine.connect() as con:
                con.execute(text('alter table ' + D[site_key].index.name + ' add primary key (DateTime)'))
            
            st.success( 'The DataBase table: "' + D[site_key].index.name + '" was replaced using data from table ' + ", ".join([f'"{k}"' for k, v in raw_tb_dl[site_key].items() if v]) + ' in clean_ format' )

    
    if  rb == 'update existing':
        for site_key in c.keys():
            # site_key = 'S1'
            co = c[site_key].copy()
            # leave only rows that are either not found in the current DB table or differ in value from rows with the same time stamp
            co = co.loc[co.index.isin(set(DTnew[site_key]) | set(DTdiff[site_key]))]
            co = co.reset_index()
                        
            # create a temporary table
            engine = create_engine(url)
            co.to_sql('staging_table', engine, if_exists='replace', index=False)
            
            # build the sql query
            cols = co.columns.tolist()
            col_list = ", ".join(cols)
            update_list = ", ".join([f"{c} = new.{c}" for c in cols if c != "DateTime"])
            merge_sql = f"""
            INSERT INTO {D[site_key].index.name} ({col_list})
            SELECT {col_list}
            FROM staging_table AS new
            ON DUPLICATE KEY UPDATE
                {update_list};
            """
            
            # update the existing clean_ table using rows from the temporary clean_ table, then delete the latter
            with engine.begin() as conn:
                try:
                    conn.execute(text(merge_sql))
                except:
                    conn.execute(text('DROP TABLE IF EXISTS staging_table;'))
                    raise
                finally:
                    conn.execute(text('DROP TABLE IF EXISTS staging_table;'))
            
            del co, engine, cols, col_list, update_list, merge_sql
            
            st.success( 'The DataBase table: "' + D[site_key].index.name + '" was updated using data from table ' + ", ".join([f'"{k}"' for k, v in raw_tb_dl[site_key].items() if v]) )


    if np.random.randint(0, 100)>50:
        st.balloons()
    else:
        st.snow()
    st.cache_data.clear()
    st.session_state.clear()
    st.warning('App cache is clear and all created variables deleted.')
    
    
"---"
    
st.stop()

