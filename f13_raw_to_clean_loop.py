import streamlit  as st
import pandas as pd
from   f12_raw_to_clean  import raw_to_clean

# C = raw_to_clean_loop(cols, d_0)
@st.cache_data(show_spinner="Processing raw tables...")
def raw_to_clean_loop(cols, d_0):
    d_1 = []
    d_2 = []
    for tb in range(4,cols.shape[1]):
        d0 = d_0[tb-4]
        d1, d2 = raw_to_clean(cols, tb, d0)            
        d_1.append(d1)       # column-consistent and filtered
        d_2.append(d2)       # resampled to an even 1h time grid
    
    # merge tables in one starting from the tail of header row in cols
    C = d_2[-1].copy()
    if len(d_2)>1:
        for i in range(len(d_2)-1,0,-1):
            C.update(d_2[i-1])
            C = pd.concat([C, d_2[i-1].loc[~d_2[i-1].index.isin(C.index)]])

    # Add water year column
    m = C.index.month > 9
    C.insert( 0, 'WatYr', C.index.year+1*m.astype(int) )

    
    return C

#))))))))))
# import matplotlib.pyplot as plt
# from   matplotlib.widgets import CheckButtons
# c = 6
# fig, ax = plt.subplots()

# hobo_0h, = ax.plot( d_0[1].iloc[:,0], d_0[1].iloc[:,11], color='black', marker='.', label='hobo_0' )
# csci_0h, = ax.plot( d_0[0].iloc[:,0], d_0[0].iloc[:,18], color='red'  , marker='.', label='csci_0' )

# hobo_1h, = ax.plot( d_1[1].index, d_1[1].iloc[:,c], color='black', marker='o', markersize=5, markerfacecolor='none', markeredgewidth=1,label='hobo_1' )
# csci_1h, = ax.plot( d_1[0].index, d_1[0].iloc[:,c], color='red'  , marker='o', markersize=5, markerfacecolor='none', markeredgewidth=1,label='csci_1' )

# hobo_2h, = ax.plot( d_2[1].index, d_2[1].iloc[:,c], color='black', marker='*', label='hobo_2' )
# csci_2h, = ax.plot( d_2[0].index, d_2[0].iloc[:,c], color='red'  , marker='*', label='csci_2' )
# combo_h, = ax.plot(      C.index,      C.iloc[:,c], color='blue' , marker='.', label='combo' )


# plt.title( C.columns[c] )
# ax.legend()
# rax = plt.axes([0, 0.4, 0.15, 0.20], frameon=False)

# check = CheckButtons(rax, labels=['hobo_0', 'csci_0', 'hobo_1', 'csci_1', 'hobo_2', 'csci_2', 'combo'], actives=[True, True, True, True, True, True, True])

# # Function to handle the visibility toggle
# def toggle_visibility(label):
#     lines[label].set_visible(not lines[label].get_visible())
#     plt.draw()

# # Connect the check buttons to the toggle function
# check.on_clicked(toggle_visibility)

# # Store the lines in a dictionary for easy access
# lines = {'hobo_0': hobo_0h,
#           'csci_0': csci_0h,
#           'hobo_1': hobo_1h,
#           'csci_1': csci_1h,
#           'hobo_2': hobo_2h,
#           'csci_2': csci_2h,
#           'combo':  combo_h}

# plt.close('all')
# del c, fig, ax, hobo_0h, csci_0h, hobo_1h, csci_1h, hobo_2h, csci_2h, combo_h, rax, lines
