# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:55:50 2024

@author: marchenks
"""
import numpy     as np
import pandas    as pd
import streamlit as st

# fl_d, fl_h, fl_coltyp = get_file(fl_path)
@st.cache_data(show_spinner="Fetching file...")
def get_file(fl_path):
    fl_d = pd.read_csv(fl_path, skiprows = 1, sep = ',', low_memory=False)
    # return fl_d
    
    if any(fl_d.columns == 'RECORD'):           # delete column with numbers of records
        fl_d = fl_d.drop(columns='RECORD')
        
    fl_t = fl_d.iloc[:, 0]
    fl_t.name = 't'
    fl_d = fl_d.iloc[:,1:]
    fl_d = pd.concat([fl_t, fl_d], axis=1).set_index('t').squeeze()

    fl_h = fl_d.columns.tolist()    # extract the rows with headers and units and...
    fl_u = fl_d.iloc[0 ,:].tolist()
    fl_d = fl_d.iloc[2:,:]
    
    fl_d.index = pd.to_datetime( fl_d.index )
        
    for i in range(0,len(fl_h)):                #     ... merge them in one variable
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