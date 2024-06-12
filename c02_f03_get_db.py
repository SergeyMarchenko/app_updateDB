# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:35:54 2024

@author: marchenks
"""
import numpy as np
import pandas     as pd
import streamlit  as st
from   sqlalchemy import create_engine


# db_d = get_db(url, db_path)
# db_d, db_h, db_coltyp = get_db(url, db_path)
@st.cache_data(ttl = 120, show_spinner="Fetching table from SQL DataBase...")
def get_db(url, db_path):
    engine = create_engine(url)
    with engine.connect() as connection:
        db_d = pd.read_sql(f"SELECT * FROM {db_path}", connection)
    # return db_d
    
    db_t = db_d.iloc[:, 0]
    db_t.name = 't'
    db_d = db_d.iloc[:,1:]
    
    db_d = pd.concat([db_t, db_d], axis=1).set_index('t').squeeze()
        
    
    # Replace "%" in column names with "percent"
    for c in db_d.columns:
        if "%" in c:
            new = c.replace("%", "percent")
            db_d.rename(columns={c: new}, inplace=True)


    db_h = db_d.columns.astype(str).tolist()

    db_coltyp = db_d.dtypes.astype(str).tolist()
    
    ind = []
    for c in range(0,db_d.shape[1]):        # convert finite values in the columns with times to unix time stamps
        if db_coltyp[c] == 'datetime64[ns]':
            # ind = pd.notna(db_d.iloc[:,c]).tolist()
            # db_d.iloc[ind,c] = db_d.iloc[ind,c].apply(lambda x: x.timestamp())
            
            ind  = pd.notna(db_d.iloc[:,c]).tolist()
            tmp  = pd.Series([np.nan] * db_d.shape[0])
            name = db_d.columns[c]
                        
            tmp.iloc[ind] = ( db_d.iloc[ind,c].astype(np.int64) ).astype(np.float64)
            tmp.index = db_d.index
                        
            db_d = db_d.drop(db_d.columns[c], axis=1)
            
            db_d.insert(c, name, tmp)
            
    return db_d, db_h, db_coltyp