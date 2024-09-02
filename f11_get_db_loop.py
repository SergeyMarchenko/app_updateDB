# import streamlit  as st
from f03_get_db      import get_db

# d_0 = get_db_loop(cols, url)
# @st.cache_data(show_spinner="Downloading raw tables...")
def get_db_loop(cols, url):
    d_0 = []
    
    for tb in range(4,cols.shape[1]):
        d0, _, _ = get_db(url, cols.columns[tb])   
        d0.reset_index(inplace=True)
        d_0.append(d0)                             # downloaded data
                            
        # Ensure that names of columns in column routing file make sense: exist in the tables, are not doubled in source or destination 
    return d_0