# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 13:20:13 2024

@author: marchenks
"""

import pandas    as pd
import numpy     as np
import streamlit as st

# c, col_dict_out = merge_dbfl(db_d, fl_d, col_dict)
@st.cache_data(show_spinner="Merging file and database...")
def merge_dbfl(db_d, fl_d, col_dict, ow_flag):
    col_dict_out = col_dict
        
    db_d1 = db_d
    fl_d1 = fl_d
    
    # if any of the columns in the AWS data table are to be skipped:
    if 'SKIP the column'      in col_dict_out.values():
        skip     = [key            for key, value in col_dict_out.items() if value == 'SKIP the column']  # find the keys in the "col_dict_out" dictionary that correspond to values 'SKIP the column',
        col_dict_out = {key: value for key, value in col_dict_out.items() if value != 'SKIP the column'}  # delete the items from the "col_dict_out" dictionary.
        fl_d1    = fl_d1.drop( columns = skip )                                                           # delete the corresponding columns in the local copy of the AWS file data table

    # if any of the columns in the AWS data table are to go to new columns in the database:
    if 'add NEW COLUMN to db' in col_dict_out.values():
        new      = [key        for key, value in col_dict_out.items() if value == 'add NEW COLUMN to db']   # find the keys ("new") in the "col_dict_out" dictionary that correspond to values 'add NEW COLUMN to db',
        existing = [elem       for elem       in new                  if elem  in db_d1.columns]            # in "new" find the items ("existing") that already exist as column names in the database table,
        # display warning message
        if len(existing) > 0:          # to avoid overwriting data in valuable database columns generate "nc" - names of new columns in the database table: add suffix "_new" to all items in "new" that also appear in "existing"
            nc   = [elem + "_new" if elem in existing else elem for elem in new]
        else:
            nc   = new
        db_d1[nc] = np.nan             # add new columns to the database table and name them as in "nc"
        for key, nc in zip(new, nc):   # redefine values for "new" keys in the "col_dict_out" so that data from columns in AWS file know where to go in the database table.
            if key in col_dict_out:
                col_dict_out[key] = nc

    fl_d1 = fl_d1.rename(columns = col_dict_out)       # rename columns in the file using their database counterparts
    
    # ow_flag = [False, True, False, False, True, True, True]
    # fl_d1.iloc[3:5,:] = -88888
    
    for i in range(0,fl_d1.shape[1]):
        tmp = fl_d1.iloc[:,i]
        db_d1.update(tmp, overwrite = ow_flag[i])             # replace nan elements in db by finite values in file

    ind = fl_d1.index.difference(db_d1.index)      # ind - indexes in the AWS file table that do not appear in the indexes of the database table
    db_d1 = pd.concat([db_d1, fl_d1.loc[ind,:]])   # for "ind" rows in database table write data from corresponding columns in the AWS file table
    db_d1 = db_d1.sort_index()
    
    return db_d1, col_dict_out