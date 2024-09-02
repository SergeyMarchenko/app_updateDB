import streamlit     as st
import pandas        as pd
import numpy         as np
from   f16_mean_deg  import mean_deg

# d1, d2 = raw_to_clean(cols, tb, d0)
@st.cache_data(show_spinner="Processing raw table...")
def raw_to_clean(cols, tb, d0):
    
    # make a new table with consistent column structure and apply basic filtering of data
    d1 = pd.DataFrame(np.nan, index=range(d0.shape[0]), columns=cols.iloc[:,0])
    d1['DateTime'] = pd.to_datetime(d1['DateTime'])
    for cl in range(0, cols.shape[0]):
        if not cols.iloc[cl,tb] == '':
            d1.iloc[:,cl] = d0[cols.iloc[cl,tb]]
            if cl>0:
                below = d1.iloc[:,cl]<cols.iloc[cl,2]
                above = d1.iloc[:,cl]>cols.iloc[cl,3]
                d1.iloc[below,cl]=np.nan
                d1.iloc[above,cl]=np.nan
    del cl, below, above
    d1 = d1.set_index('DateTime')
    
    
    # resample table to an even 1h time step
    dt = d1.index.to_series().diff()
    dt1h = dt[1:] == pd.Timedelta(hours=1)
    if not dt1h.all():
        aggr = dict(zip(cols.iloc[1:,0], cols.iloc[1:,1]))
        for key, value in aggr.items():
            if value == 'mean_deg':
                aggr[key] = mean_deg
        d2 = d1.resample('1h', label='right', closed='right').agg(aggr)
    else:
        d2 = d1.copy()
        
     
    return d1, d2

