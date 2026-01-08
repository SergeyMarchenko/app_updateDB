import streamlit  as st
import pandas as pd
import numpy  as np
from   f03_get_db            import get_db
from   f12_raw_to_clean      import raw_to_clean

# d0, c = raw_to_clean_loop(D, F, raw_tb_dl, url)
@st.cache_data(show_spinner="Converting raw_ tables to clean_ format ...")
def raw_to_clean_loop(D, F, raw_tb_dl, url):
    d0  = {}        # downloaded data
    # d1  = {}        # column-consistent and filtered
    d2  = {}        # resampled to an even 1h time grid
    c   = {}        # merged in one, if multiple raw_ tables are processed
    for outer_key, inner_dict in raw_tb_dl.items():
        # outer_key = 'S9'
        # inner_dict = raw_tb_dl[outer_key]
        d0[outer_key]  = {}
        # d1[outer_key]  = {}
        d2[outer_key]  = {}
        c[ outer_key]  = {}
        for inner_key in inner_dict.keys():
            # inner_key = 'raw_UpperRussell_CSci'
            if inner_dict[inner_key]:
                d0[outer_key][inner_key], _, _ = get_db(url, inner_key)
                # d0[outer_key][inner_key].reset_index(inplace=True)
                d0[outer_key][inner_key] = d0[outer_key][inner_key].where(d0[outer_key][inner_key].notna(), np.nan)
                for col in d0[outer_key][inner_key].select_dtypes(include=['object']).columns:
                    d0[outer_key][inner_key][col] = pd.to_numeric(d0[outer_key][inner_key][col], errors='coerce').astype('float64')
                # d1[outer_key][inner_key], d2[outer_key][inner_key] = raw_to_clean(D[outer_key], inner_key, d0[outer_key][inner_key])
                
                _, d2[outer_key][inner_key] = raw_to_clean(D[outer_key], F[outer_key][inner_key], inner_key, d0[outer_key][inner_key])
        
                # if more than one clean_ table were created, merge them in one.
                # for overlapping time steps:
                # data from raw_ tables with names appearing to the left  in the header row of the cols variable overwrites
                # data from raw_ tables with names appearing to the right in the header row of the cols variable
                c[outer_key] = d2[outer_key][inner_key].copy()
        
        if len(d2[outer_key])>1:
            inner_keys = list(d2[outer_key].keys())
            for inner_key in reversed(inner_keys[:-1]):
                tmp = d2[outer_key][inner_key]
                c[outer_key].update(tmp)
                # c[outer_key] = pd.concat([c[outer_key], d2[outer_key][inner_key].loc[~d2[outer_key][inner_key].index.isin(c[outer_key].index)]])
                missing_idx = tmp.index.difference(c[outer_key].index)
                if not missing_idx.empty:
                    c[outer_key] = pd.concat([c[outer_key], tmp.loc[missing_idx]])
        
        # Add water year column
        m = c[outer_key].index.month > 9
        c[outer_key].insert( 0, 'WatYr', c[outer_key].index.year+1*m.astype(int) )
        
        if len(D)>1:
            d0[outer_key]  = {}
        d2[outer_key]  = {}

    
    return d0, c
