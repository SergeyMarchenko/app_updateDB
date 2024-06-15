import numpy     as np
import pandas    as pd
import streamlit as st

# fl_d, fl_h, fl_coltyp = get_file(fl_path)
@st.cache_data(show_spinner="Fetching file...")
def get_file_alt(*args):
    # fl_path = 'Z:\FLNRO\Russell Creek\Data\DB\code_2_db/DUMMY_FILE_REF.dat'
    # delim = ','
    # tcol = '0'
    # dcol = '1'
    # drow = '4'
    # hrow = '1'
    # urow = '2'
    if len(args) == 2:
        fl_path = args[0]
        delim   = args[1]
        fl_d0 = pd.read_csv(fl_path, sep = delim, index_col=False, low_memory=False)
                
        fl_d0.loc[-1] = fl_d0.columns.tolist()  # Add headers as a row at the end of the DataFrame
        fl_d0.index = fl_d0.index + 1           # Increment all index values by 1
        fl_d0 = fl_d0.sort_index()
        fl_d0.columns = range(len(fl_d0.columns))
        
        return fl_d0
    
    
    
    
    fl_d0 = args[0]
    tcol  = args[1]
    dcol  = args[2]
    hrow  = args[3]
    urow  = args[4]
    drow  = args[5]
               
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
    urow = int(urow)
    drow = int(drow)
    
    
    
    
        
    fl_t = fl_d0.iloc[drow:, tcol]
    fl_t.columns = ['t']
     
    fl_d = fl_d0.iloc[drow:,dcol]
    fl_d = pd.concat([fl_t, fl_d], axis=1).set_index('t').squeeze()
    fl_d.index = pd.to_datetime( fl_d.index )

    fl_h = fl_d0.iloc[hrow,dcol].tolist()       # extract the rows with headers and units and merge them in one variable
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
    
    
    
    
    # delete column with numbers of records
    colrem = fl_d.filter(like='RECORD').columns.tolist()
    if any(fl_d.columns == colrem[0]):
        fl_d = fl_d.drop(columns=colrem[0])
        
    fl_d = fl_d.replace('NAN', pd.NA, inplace = False)
    
    na_columns = fl_d.columns[fl_d.isna().all()]        # Drop columns containing only pd.NA values
    fl_d = fl_d.drop(columns=na_columns)
    fl_h = fl_d.columns.tolist()
    
    fl_coltyp = []
    for i in range(0,len(fl_h)):                #     ... convert strings in columns to numbers and, when strings are time stamps, to DateTime and then to number of seconds
        if any(fl_d.iloc[:,i].str.contains(':', na=False)):
            fl_d.iloc[:,i] = pd.to_numeric( pd.to_datetime( fl_d.iloc[:,i] ) )
            fl_d.iloc[fl_d.iloc[:,i]<0,i] = np.nan
            fl_coltyp.append("time")
            # fl_d.iloc[:,12] = pd.to_datetime( fl_d.iloc[:,12] )
        else:
            fl_d.iloc[:,i] = pd.to_numeric(  fl_d.iloc[:,i] )
            fl_coltyp.append("float")
            
    fl_d = fl_d.astype("float")


    return fl_d, fl_h, fl_coltyp