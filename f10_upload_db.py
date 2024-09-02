import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy import text

# m = upload_db(c, url, db_path_updated)
@st.cache_data(show_spinner="Uploading table to the SQL database...")
def upload_db(c, url, db_path_updated):
    c_out = c
    c_out.insert(0, 't', c_out.index)
    c_out.reset_index(drop=True, inplace=True)
    engine = create_engine(url)
    c.to_sql(name=db_path_updated, con=engine, if_exists = 'replace', index = False)
    with engine.connect() as con:
        con.execute(text('alter table ' + db_path_updated + ' add primary key (t)'))

    
    m = 'The table: "' + db_path_updated + '"' + 'is uploaded to the DataBase.'
    
    return m
