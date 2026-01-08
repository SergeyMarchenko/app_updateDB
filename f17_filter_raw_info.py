import pandas    as pd
from f15_sites_tables_cols import sites_tables_cols

# F = filter_raw_info()
def filter_raw_info():
    
# structure of the F dictionary:
# site -> raw table name -> variable name in clean_ format  -> variable name in raw_ format
# 														       unit
# 														       min
# 														       max
# 														       events                       -> 1 -> from_DateTime
# 																	                           2    till_DateTime
# 																	                                koefficient
# 																	                                offset
# 																	                                note

    D_p = sites_tables_cols()
    F = D_p.copy()
    for site in F.keys():
        # site = 'S1'
        # print(site)
        # D_p[site] = D_p[site].set_index(D_p[site].columns[0])
        F[site] = {}
        F[site] = {key: {} for key in D_p[site].columns[1:]}
        for raw_table in F[site].keys():
            # print(raw_table)
            F[site][raw_table] = {key: {} for key in D_p[site].index[1:]}
            for clean_var in F[site][raw_table].keys():
                # clean_var = 'Air_Temp'
                # print(clean_var)
                tmp = D_p[site].loc[clean_var, raw_table]
                if tmp != '':
                    F[site][raw_table][clean_var]['raw_ column'] = tmp
                    F[site][raw_table][clean_var]['events'] = []
                    
                    if  clean_var  == 'Air_Temp':
                        F[site][raw_table][clean_var]['unit'] = 'degC'
                        F[site][raw_table][clean_var]['min' ] =  -40
                        F[site][raw_table][clean_var]['max' ] =   40 
                    if  clean_var  == 'RH':
                        F[site][raw_table][clean_var]['unit'] = 'percent'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] =  100
                    if  clean_var  == 'BP':
                        F[site][raw_table][clean_var]['unit'] = 'units'
                        F[site][raw_table][clean_var]['min' ] =  500
                        F[site][raw_table][clean_var]['max' ] = 1500
                    if  clean_var == 'Wind_Speed':
                        F[site][raw_table][clean_var]['unit'] = 'km h^-1'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] =  100
                    if  clean_var == 'Wind_Dir':
                        F[site][raw_table][clean_var]['unit'] = 'degrees'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] =  360
                    if  clean_var == 'Pk_Wind_Speed':
                        F[site][raw_table][clean_var]['unit'] = 'km h^-1'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] =  100
                    if  clean_var == 'PP_Tipper':
                        F[site][raw_table][clean_var]['unit'] = 'mm of we'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] =  300
                    if  clean_var == 'PC_Tipper':
                        F[site][raw_table][clean_var]['unit'] = 'mm we'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] = float('inf')
                    if  clean_var == 'PC_Raw_Pipe':
                        F[site][raw_table][clean_var]['unit'] = 'mm of we'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] = 2500
                    if  clean_var == 'Snow_Depth':
                        F[site][raw_table][clean_var]['unit'] = 'cm'
                        F[site][raw_table][clean_var]['min' ] = -500
                        F[site][raw_table][clean_var]['max' ] =  500
                    if  clean_var == 'SWE':
                        F[site][raw_table][clean_var]['unit'] = 'mm we'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] = 1000
                    if  clean_var == 'Solar_Rad':
                        F[site][raw_table][clean_var]['unit'] = 'W m^-2'
                        F[site][raw_table][clean_var]['min' ] =  -10
                        F[site][raw_table][clean_var]['max' ] = 1500
                    if  clean_var == 'Batt':
                        F[site][raw_table][clean_var]['unit'] = 'Volts'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] =   20
                    if  clean_var == 'Pk_Wind_Dir':
                        F[site][raw_table][clean_var]['unit'] = 'degrees'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] =  360
                    if  clean_var == 'PP_Pipe':
                        F[site][raw_table][clean_var]['unit'] = 'mm of we'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] =  300
                    if  clean_var == 'SWU':
                        F[site][raw_table][clean_var]['unit'] = 'W m^-2'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] = 1500
                    if  clean_var == 'SWL':
                        F[site][raw_table][clean_var]['unit'] = 'W m^-2'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] = 1500
                    if  clean_var == 'LWU':
                        F[site][raw_table][clean_var]['unit'] = 'W m^-2'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] = 1500
                    if  clean_var == 'LWL':
                        F[site][raw_table][clean_var]['unit'] = 'W m^-2'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] = 1500
                    if  clean_var == 'Lysimeter':
                        F[site][raw_table][clean_var]['unit'] = 'mm we'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] = 1000
                    if  clean_var == 'Soil_Moisture':
                        F[site][raw_table][clean_var]['unit'] = 'percent'
                        F[site][raw_table][clean_var]['min' ] =    0
                        F[site][raw_table][clean_var]['max' ] =  100
                    if  clean_var == 'Soil_Temperature':
                        F[site][raw_table][clean_var]['unit'] = 'degC'
                        F[site][raw_table][clean_var]['min' ] =  -40
                        F[site][raw_table][clean_var]['max' ] =   40
                    if  clean_var == 'River_Thick':
                        F[site][raw_table][clean_var]['unit'] = 'm'
                        F[site][raw_table][clean_var]['min' ] =  0
                        F[site][raw_table][clean_var]['max' ] =  3

    F['S1']['raw_Steph1_hobo']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S1']['raw_Steph1_CSci']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S1']['raw_Steph1_hobo']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S1']['raw_Steph1_CSci']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S1']['raw_Steph1_hobo']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', '2013 9 12 13 0 0'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , -1     ],
                             ['offset'       ,  205   ],
                             ['note'         , 'conversion from [distance to snow] -> [depth of snow]'] ])}
    F['S1']['raw_Steph1_CSci']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , -100   ],
                             ['offset'       ,  360   ],
                             ['note'         , 'conversion from [distance to snow] in [m] to [depth of snow] in [cm]'] ])}
    
    F['S2']['raw_Steph2_CSci']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S2']['raw_Steph2_CSci']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S2']['raw_Steph2_CSci']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , -100   ],
                             ['offset'       ,  286   ],
                             ['note'         , 'conversion from [distance to snow] in [m] to [depth of snow] in [cm]'] ])}
    F['S2']['raw_Steph2_CSci']['PC_Raw_Pipe']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  ,  1000  ],
                             ['offset'       ,  0     ],
                             ['note'         , 'unit conversion from [m] to [mm]'] ])}
    
    F['S3']['raw_Steph3_CSci']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', '2024 10 1 0 0 0'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S3']['raw_Steph3_CSci']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', '2024 10 1 0 0 0'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S3']['raw_Steph3_CSci']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', '2021 7 1 0 0 0'],
                             ['till_DateTime', '2024 7 1 0 0 0' ],
                             ['koefficient'  , -1   ],
                             ['offset'       ,  240 ],
                             ['note'         , 'conversion from [distance to snow] in [m] to [depth of snow] in [cm]'] ]),
            2: pd.DataFrame([['from_DateTime', '2024 7 1 0 0 0'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , -100   ],
                             ['offset'       ,  270 ],
                             ['note'         , 'conversion from [distance to snow] in [m] to [depth of snow] in [cm]'] ])}
    
    F['S4']['raw_Steph4_hobo']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S4']['raw_Steph4_CSci']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S4']['raw_Steph4_hobo']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S4']['raw_Steph4_CSci']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S4']['raw_Steph4_hobo']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', '2021 7 1 0 0 0' ],
                             ['koefficient'  , -1     ],
                             ['offset'       ,  260   ],
                             ['note'         , 'conversion from [distance to snow] to [depth of snow]'] ]),
            2: pd.DataFrame([['from_DateTime', '2024 7 1 0 0 0'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  ,  1     ],
                             ['offset'       ,  10    ],
                             ['note'         , 'corection of the bare ground level'] ])}
    F['S4']['raw_Steph4_CSci']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', '2023 7 1 0 0 0' ],
                             ['koefficient'  , -100   ],
                             ['offset'       ,  330   ],
                             ['note'         , 'conversion from [distance to snow] in [m] to [depth of snow] in [cm]'] ]),
            2: pd.DataFrame([['from_DateTime', '2023 7 1 0 0 0'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , -100   ],
                             ['offset'       ,  325   ],
                             ['note'         , 'conversion from [distance to snow] in [m] to [depth of snow] in [cm]'] ])}
    
    F['S5']['raw_Steph5_CSci']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S5']['raw_Steph5_CSci']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S5']['raw_Steph5_CSci']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , -100   ],
                             ['offset'       ,  292   ],
                             ['note'         , 'conversion from [distance to snow] in [m] to [depth of snow] in [cm]'] ])}
    
    F['S6']['raw_Steph6_hobo']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S6']['raw_Steph6_CSci']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S6']['raw_Steph6_hobo']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S6']['raw_Steph6_CSci']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S6']['raw_Steph6_hobo']['PC_Raw_Pipe']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 0.001  ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [mm we to [m we]'] ])}
    F['S6']['raw_Steph6_hobo']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , -1     ],
                             ['offset'       , 263    ],
                             ['note'         , 'conversion from [distance to snow] to [depth of snow]'] ])}
    F['S6']['raw_Steph6_CSci']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , -100   ],
                             ['offset'       , 348    ],
                             ['note'         , 'conversion from [distance to snow] in [m] to [depth of snow] in [cm]'] ])}
    
    
    F['S7']['raw_Steph7_hobo']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S7']['raw_Steph7_CSci']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S7']['raw_Steph7_hobo']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S7']['raw_Steph7_CSci']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S7']['raw_Steph7_hobo']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', '2021 7 1 0 0 0' ],
                             ['koefficient'  , -1     ],
                             ['offset'       , 235    ],
                             ['note'         , 'conversion from [distance to snow] to [depth of snow]'] ])}
    F['S7']['raw_Steph7_CSci']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , -100   ],
                             ['offset'       , 304    ],
                             ['note'         , 'conversion from [distance to snow] in [m] to [depth of snow] in [cm]'] ])}
    
    F['S8']['raw_Steph8_hobo']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S8']['raw_Steph8_CSci']['Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S8']['raw_Steph8_hobo']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S8']['raw_Steph8_CSci']['Pk_Wind_Speed']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}
    F['S8']['raw_Steph8_hobo']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', '2012 10 1 0 0 0' ],
                             ['koefficient'  , -1     ],
                             ['offset'       , 235    ],
                             ['note'         , 'conversion from [distance to snow] to [depth of snow]'] ]),
            2: pd.DataFrame([['from_DateTime', '2012 10 1 0 0 0'],
                             ['till_DateTime', '2016 10 1 0 0 0'],
                             ['koefficient'  , -1     ],
                             ['offset'       , 220    ],
                             ['note'         , 'conversion from [distance to snow] to [depth of snow]'] ]),
            3: pd.DataFrame([['from_DateTime', '2016 10 1 0 0 0'],
                             ['till_DateTime', '2021 10 1 0 0 0'],
                             ['koefficient'  , -1     ],
                             ['offset'       , 236    ],
                             ['note'         , 'conversion from [distance to snow] to [depth of snow]'] ]),
            4: pd.DataFrame([['from_DateTime', '2021 10 1 0 0 0'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 1      ],
                             ['offset'       , 2      ],
                             ['note'         , 'corection of offset'] ])}
    F['S8']['raw_Steph8_CSci']['Snow_Depth']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', '2024 7 1 0 0 0' ],
                             ['koefficient'  , -100   ],
                             ['offset'       , 283    ],
                             ['note'         , 'conversion from [distance to snow] in [m] to [depth of snow] in [cm]'] ]),
            2: pd.DataFrame([['from_DateTime', '2024 7 1 0 0 0'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , -100   ],
                             ['offset'       , 290    ],
                             ['note'         , 'conversion from [distance to snow] in [m] to [depth of snow] in [cm]'] ])}
    
    F['S9']['raw_UpperRussell_CSci']['PC_Raw_Pipe']['events'] = {
            1: pd.DataFrame([['from_DateTime', '2021 11 1 0 0 0'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 1000   ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m] to [mm]'] ])}
    F['S9']['raw_UpperRussell_CSci']['River_Thick']['events'] = {
            1: pd.DataFrame([['from_DateTime', 'first'],
                             ['till_DateTime', 'last' ],
                             ['koefficient'  , 0.01   ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [cm] to [m]'] ])}
    
    F['S10']['raw_RussellMain_hobo']['PC_Raw_Pipe']['events'] = {
            1: pd.DataFrame([['from_DateTime', '2009 1 1 0 0 0'],
                             ['till_DateTime', '2012 1 1 0 0 0' ],
                             ['koefficient'  , 3.6    ],
                             ['offset'       , 0      ],
                             ['note'         , 'unit conversion from [m sec^-1] to [km h^-1]'] ])}


    for site in F.keys():
        # site = 'S1'
        # print(site)
        for table in F[site].keys():
            # table = 'raw_Steph1_CSci'
            # print(table)
            for var in F[site][table].keys():
                # var = 'Snow_Depth'
                # print(var)
                if F[site][table][var] != {}:
                    if len(F[site][table][var]['events'])>0:
                        for event in F[site][table][var]['events'].keys():
                            # event = 1
                            F[site][table][var]['events'][event] = F[site][table][var]['events'][event].set_index(0)
                            # print(event)
                            if  F[site][table][var]['events'][event].loc['from_DateTime'].iloc[0] != 'first':
                                F[site][table][var]['events'][event].loc['from_DateTime'] = pd.to_datetime(
                                F[site][table][var]['events'][event].loc['from_DateTime'], format="%Y %m %d %H %M %S" )
                            if  F[site][table][var]['events'][event].loc['till_DateTime'].iloc[0] != 'last':
                                F[site][table][var]['events'][event].loc['till_DateTime'] = pd.to_datetime(
                                F[site][table][var]['events'][event].loc['till_DateTime'], format="%Y %m %d %H %M %S" )

# S1
#     raw_Steph1_CSci
#     raw_Steph1_hobo
# S2
#     raw_Steph2_CSci
# S3
#     raw_Steph3_CSci
# S4
#     raw_Steph4_CSci
#     raw_Steph4_hobo
# S5
#     raw_Steph5_CSci
# S6
#     raw_Steph6_CSci
#     raw_Steph6_hobo
# S7
#     raw_Steph7_CSci
#     raw_Steph7_hobo
# S8
#     raw_Steph8_CSci
#     raw_Steph8_hobo
# S9
#     raw_UpperRussell_CSci
# S10
#     raw_RussellMain_hobo


# Wind_Speed
# Pk_Wind_Speed
# PC_Raw_Pipe
# Snow_Depth

# PP_Tipper
# PC_Tipper


# PP_Pipe
# Lysimeter



    return F