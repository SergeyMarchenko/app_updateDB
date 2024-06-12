# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 15:39:05 2024

@author: marchenks
"""
import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy import text

# message = upload_db(c, url, db_path_updated, fl_path, db_path)
@st.cache_data(show_spinner="Uploading table to the SQL database...")
def upload_db(c, url, db_path_updated, fl_path, db_path):
    c_out = c
    c_out.insert(0, 't', c_out.index)
    c_out.reset_index(drop=True, inplace=True)
    engine = create_engine(url)
    c.to_sql(name=db_path_updated, con=engine, if_exists = 'replace', index = False)
    with engine.connect() as con:
        con.execute(text('alter table ' + db_path_updated + ' add primary key (t)'))

    m1 = 'DataBase table "' + db_path + '" updated '
    m2 = 'using data from file "' + fl_path.name + '"'
    m3 = 'the updated table is named: "' + db_path_updated + '"'
    message = m1 + '\n' + m2 + '\n' + m3

    return message
