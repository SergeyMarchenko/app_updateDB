# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 17:44:31 2024

@author: marchenks
"""

import streamlit as st
import numpy     as np
import pandas as pd
import Levenshtein

# ccmaxind, col_dict = col_routes(db_d, fl_d, db_h, fl_h)
@st.cache_data(show_spinner="Routing columns in file to columns in database table...")
def col_routes(db_d, fl_d, db_h, fl_h):
    fl_ind_com = np.where(fl_d.index.isin(db_d.index))[0]  # indexes into elements of times in file     that are also a part of times in DataBase
    db_ind_com = np.where(db_d.index.isin(fl_d.index))[0]  #             ...                   DataBase     ...                          file

    # fl_c = 0
    # db_c = 0
    cc_d = np.full((db_d.shape[1], fl_d.shape[1]), np.nan) # nan matrix for correlation coefficients    between common-timestamped finite values in file and database
    cc_h = np.full((db_d.shape[1], fl_d.shape[1]), np.nan) #                Levenshtein distancebetween   ...   names        of          columns         ...
    for     fl_c in range(0,fl_d.shape[1]):
        for db_c in range(0,db_d.shape[1]):
            print(fl_c)
            print(db_c)
            fl_col = fl_d.iloc[fl_ind_com,fl_c].reset_index(drop=True)  # file     values for common time stamps
            db_col = db_d.iloc[db_ind_com,db_c].reset_index(drop=True)  # database           ...
            fl_col = pd.to_numeric(fl_col)
            db_col = pd.to_numeric(db_col)
            ind    = np.where(np.isfinite(fl_col) & np.isfinite(db_col))[0] # indexes into the common time file and database values where both are finite
            if ind.size == 0:
                cc_d[db_c,fl_c] = 0
            else:
                cc_d[db_c,fl_c] = np.corrcoef(fl_col[ind],
                                              db_col[ind], rowvar=False)[0, 1]
            cc_h[db_c,fl_c] = 1 - Levenshtein.distance(fl_h[fl_c], db_h[db_c]) / max(len(fl_h[fl_c]), len(db_h[db_c]))
            
    cc = cc_d + cc_h
    ccmaxind = np.nanargmax(cc, axis=0)
    ccmaxind = [int(x) for x in ccmaxind]
    
    db_h_tmp = [db_h[i] for i in ccmaxind]
    col_dict = dict(zip(fl_h, db_h_tmp))

    return ccmaxind, col_dict