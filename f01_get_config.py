# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:15:18 2024

@author: marchenks
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 11:35:54 2024

@author: marchenks
"""
import pandas as pd
import streamlit as st

# url = get_config(path_config)
@st.cache_data(show_spinner="Uploading config file...")
def get_config(path_config):
    config_data = pd.read_csv(path_config, header=None)
    config_data = dict(zip(config_data[0], config_data[1]))

    url = ('mysql+mysqlconnector://' + config_data['config_username']  + ':' +
                                       config_data['config_password']  + '@' +
                                       config_data['config_host']      + ':' +
                                       config_data['config_port']      + '/' +
                                       config_data['config_database'])
    return url