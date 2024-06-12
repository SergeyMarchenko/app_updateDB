# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:28:07 2024

@author: marchenks
"""

import streamlit as st
import numpy     as np
import pandas as pd
import Levenshtein

# N, Ne, cc_d, cc_h, nana, nanb = col_stats(db_d, fl_d, col_dict, key)
@st.cache_data(show_spinner="Calculating statistics for time-overlapping data in AWS file and database table...")
def col_stats(db_d, fl_d, col_dict, key):
    # key = "DTbest"
    
    # a  = pd.concat([db_t, db_d[col_dict[key]]], axis=1).set_index('t').squeeze()
    # b  = pd.concat([fl_t, fl_d[         key] ], axis=1).set_index('t').squeeze()
        
    a = db_d.loc[db_d.index.isin(fl_d.index), col_dict[key]] # elements of database that are also a part of file
    b = fl_d.loc[fl_d.index.isin(db_d.index),          key ] #    ...      file            ...              database
    
    a = pd.to_numeric(a)
    b = pd.to_numeric(b)
    ind = np.where(np.isfinite(a) & np.isfinite(b))[0] # indexes into the common time file and database values where both are finite
    
    # number of elements with the same time stamp
    N = len(a)
    
    # fraction of elements that are exactly the same
    a_tmp = a.iloc[ind]
    b_tmp = b.iloc[ind]
    if len(a_tmp)>0:
        Ne = a_tmp.isin(b_tmp).sum() / len(a_tmp) * 100
    else:
        Ne = 0.00
    
    # coefficient of correlation
    if ind.size == 0:
        cc_d = 0
    else:
        cc_d = np.corrcoef(a.iloc[ind], b.iloc[ind], rowvar=False)[0, 1]
    
    # metric of how close two column headers are to each other
    cc_h = 1 - Levenshtein.distance(a.name,b.name) / max(len(a.name), len(b.name))
    
    # fraction of nan values
    nana = sum(np.isnan(a))/len(a)*100
    nanb = sum(np.isnan(b))/len(b)*100
    
    Ne   = round(Ne  ,0)
    cc_d = round(cc_d,2)
    cc_h = round(cc_h,2)
    nana = round(nana,2)
    nanb = round(nanb,2)
    
    
    N    = str(N)
    Ne   = str(Ne)
    Ne   = Ne[0:-2]
    cc_d = str(cc_d)
    if cc_d == '1.0':
        cc_d = cc_d[0:-2]
    
    # cc_d = f"{cc_d:.2f}"
    
    nana = f"{nana:.1f}"
    nanb = f"{nanb:.1f}"
    
    nana = nana[0:-2]
    nanb = nanb[0:-2]
    return N, Ne, cc_d, cc_h, nana, nanb