import streamlit     as st
import pandas        as pd
import numpy         as np
from   f16_mean_deg  import mean_deg

# d1, d2 = raw_to_clean(D[outer_key], F[outer_key][inner_key], inner_key, d0[outer_key][inner_key])
@st.cache_data(show_spinner="Processing raw table...")
def raw_to_clean(cols, info, key_table, d0_p):
    # cols      = D[outer_key]
    # info      = F[outer_key][inner_key]
    # key_table = inner_key
    # d0_p      = d0[outer_key][inner_key]
    
    # make a new table with consistent column structure and apply basic filtering of data
    d1 = pd.DataFrame(np.nan, index=d0_p.index, columns=cols.index[1:])
    for col in cols.index[1:]:
        # col = cols.index[1]
        if cols.loc[col,key_table] != '':
            d1[col] = d0_p[cols.loc[col,key_table]]
            # below = d1[col]<info[col]['min']
            # above = d1[col]>info[col]['max']
            # d1.loc[below,col]=np.nan
            # d1.loc[above,col]=np.nan
            if info[col]['events']:
                for event in info[col]['events'].keys():
                    # print(event)
                    i1 = info[col]['events'][event].loc['from_DateTime'].iloc[0]
                    i2 = info[col]['events'][event].loc['till_DateTime'].iloc[0]
                    i3 = info[col]['events'][event].loc['koefficient'  ].iloc[0]
                    i4 = info[col]['events'][event].loc['offset'       ].iloc[0]
                    if  i1 == 'first':
                        i1 = d1.index[ 0]
                    if  i2 == 'last':
                        i2 = d1.index[-1]
                    d1.loc[i1:i2,col] = d1.loc[i1:i2,col] * i3 + i4
                    
            below = d1[col]<info[col]['min']
            above = d1[col]>info[col]['max']
            d1.loc[below,col]=np.nan
            d1.loc[above,col]=np.nan

    # if not all increments in time are equal to 1h, resample table to an even 1h time step
    dt = d1.index.to_series().diff()
    dt1h = dt[1:] == pd.Timedelta(hours=1)
    if not dt1h.all():
        aggr = dict(zip(cols.index, cols.iloc[:,0]))
        aggr = {k: v for k, v in aggr.items() if v}
        for key_var, value in aggr.items():
            if value == 'mean_deg':
                aggr[key_var] = mean_deg
        d2 = d1.resample('1h', label='right', closed='right').agg(aggr)
        
        # Add missing columns with NaNs
        missing_cols = [col for col in d1.columns if col not in d2.columns]
        for col in missing_cols:
            d2[col] = np.nan
    else:
        d2 = d1.copy()
        
     
    return d1, d2

