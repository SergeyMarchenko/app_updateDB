import numpy     as np
import pandas    as pd
import streamlit as st

# fl_d0                 = get_file_prelim( fl_path, delim)
# fl_d, fl_h, fl_coltyp = get_file_defined(fl_d0, tcol, dcol, hrow, urow, drow)

# fl_path = 'Z:/FLNRO\Russell Creek\Data\DB\data_1_legacy\legacy_non_upd\S1_CSci.txt'                           # CSci compilation
# fl_path = 'Z:\FLNRO\Russell Creek\Data\DB\data_1_legacy\legacy_non_upd\S1_hobo.txt'                           # hobo compilation
# fl_path = 'Z:/FLNRO\Russell Creek/Data/2 Steph 2/2022/2022-09-12/CR200 Series_Hourly1_2022-09-14T08-11.dat'   # CSci data file
# fl_path = 'Z:/FLNRO/Russell Creek/Data/DB/data_0_raw/1 Steph 1/hobo\Steph_1_3.csv'                            # hobo data file
# delim = ';'
# rskip = '1'
# tcol  = '0'
# dcol  = '2'
# hrow  = '1'
# urow  = '2'
# drow  = '4'


@st.cache_data(show_spinner="Fetching file...")
def get_file_prelim(fl_path, delim, rskip):
    rskip = int(rskip)
    fl_d0      = pd.read_csv(fl_path , sep = delim, index_col=False, low_memory=False, skiprows = rskip)
                
    fl_d0.loc[-1] = fl_d0.columns.tolist()  # Add headers as a row at the end of the DataFrame
    fl_d0.index = fl_d0.index + 1           # Increment all index values by 1
    fl_d0 = fl_d0.sort_index()
    fl_d0.columns = range(len(fl_d0.columns))
    
    return fl_d0





@st.cache_data(show_spinner="Fetching file...")
def get_file_defined(fl_d0, tcol, toff, dcol, hrow, urow, drow):
               
    # Convert the string with numbers of column containing time stamp to a list of integers
    tcol = tcol.split(',')
    tcol = [int(i) for i in tcol]
    
    # Convert the string with numbers of column containing data       to a list of integers
    dcol = dcol.split(',')
    dcol = [int(i) for i in dcol]
    if len(dcol) == 1:
        dcol = list(range(dcol[0], fl_d0.shape[1]))
    
    # Convert the strings with numbers of rows for headers, units and data to a list of integers       
    hrow = int(hrow)
            
    if len(urow)>0:
        urow = int(urow)
    else:
        urow = np.nan
    drow = int(drow)
    
    
    fl_t = fl_d0.iloc[drow:, tcol]
    if fl_t.shape[1] == 6:
        fl_t = fl_t.astype(int)
        fl_t = fl_t.astype(str)
        fl_t = fl_t.iloc[:,0] + '-' + fl_t.iloc[:,1] + '-' + fl_t.iloc[:,2] + ' ' + fl_t.iloc[:,3] + ':' + fl_t.iloc[:,4] + ':' + fl_t.iloc[:,5]
        fl_t = pd.to_datetime(fl_t)
        fl_t = pd.DataFrame({ 'DateTime':fl_t})
    else:
        fl_t.columns = ['DateTime']
    
    
     
    fl_d = fl_d0.iloc[drow:,dcol]
    fl_d = pd.concat([fl_t, fl_d], axis=1).set_index('DateTime').squeeze()
    fl_d.index = pd.to_datetime( fl_d.index )
    fl_d = pd.DataFrame(fl_d)               # make sure that the variable is a DataFrame and associated methods can be applied to it


    fl_h = fl_d0.iloc[hrow,dcol].tolist()       # extract the rows with headers and units and merge them in one variable
    if np.isnan(urow):
        fl_u = ['' for _ in range(len(dcol))]
    else:
        fl_u = fl_d0.iloc[urow,dcol].tolist()
                                  
    for i in range(0,len(fl_h)):                
        fl_h[i] = fl_h[i].strip()
        fl_h[i] = fl_h[i].replace(" ", "_")
        if not pd.isna(fl_u[i]):
            fl_u[i] = fl_u[i].strip()
            fl_u[i] = fl_u[i].replace(" ", "_")
            fl_h[i] = fl_h[i] + '_' + fl_u[i]
    del i, fl_u
    fl_d = fl_d.rename(columns=dict(zip(fl_d.columns, fl_h)))
    
    
    
    fl_d = fl_d.replace('NAN', pd.NA, inplace = False)
    na_columns = fl_d.columns[fl_d.isna().all()]        # Drop columns containing only pd.NA values
    fl_d = fl_d.drop(columns=na_columns)
    fl_h = fl_d.columns.tolist()



    fl_coltyp = []
    for i in range(0,len(fl_h)):                #     ... convert strings in columns to numbers and, when strings are time stamps, to DateTime and then to number of seconds
        # if any(fl_d.iloc[:,i].str.contains(':', na=False)):
        if fl_d.iloc[:,i].astype(str).str.contains(':', na=False).any():
            fl_d.iloc[:,i] = pd.to_numeric( pd.to_datetime( fl_d.iloc[:,i] ) )
            fl_d.iloc[fl_d.iloc[:,i]<0,i] = np.nan
            fl_coltyp.append("time")
            # fl_d.iloc[:,12] = pd.to_datetime( fl_d.iloc[:,12] )
        else:
            fl_d.iloc[:,i] = pd.to_numeric(  fl_d.iloc[:,i] )
            fl_coltyp.append("float")
            
    fl_d = fl_d.astype("float")
    
    fl_d.index = fl_d.index + pd.DateOffset(hours=toff)


    return fl_d, fl_h, fl_coltyp