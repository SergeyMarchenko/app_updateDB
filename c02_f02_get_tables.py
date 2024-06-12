# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 16:29:14 2024

@author: marchenks
"""

import streamlit  as st
from   sqlalchemy import create_engine, inspect

# table_names = get_tables(url)
@st.cache_data(show_spinner="browsing available tables...")
def get_tables(url):
    
    engine = create_engine(url)
    inspection   = inspect(engine)
    table_names  = inspection.get_table_names("viuhydro_wx_data_v2")
    table_names = [x for x in table_names if x.startswith("raw")]

    return table_names