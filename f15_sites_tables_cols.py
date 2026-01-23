import pandas    as pd

# D  = sites_tables_cols()
def sites_tables_cols():
    
    
    tables_S1 = ['clean_steph1'  ,'aggregation_method'  , 'raw_Steph1_CSci'  ,'raw_Steph1_hobo']
    cols_S1 = [
    ['DateTime'         ,''           ,'DateTime'            ,'DateTime'                                ],
    ['Air_Temp'	    	,'mean'       ,'AirTemp_Avg_Deg_C'   ,'Temp_degC'                               ],
    ['RH'			    ,'mean'       ,'RH_Avg_percent'		 ,'RH_percent'                              ],
    ['BP'			    ,'mean'       ,'AirPressur_Avg_hPa'  ,''                                        ],
    ['Wind_Speed'	    ,'mean'       ,'WindSpd_Avg_m/s'	 ,'wind_speed_m_s^-1'                       ],
    ['Wind_Dir'         ,'mean_deg'   ,'WindDir_D1_WVT_m/s'	 ,'wind_direction_deg'                      ],
    ['Pk_Wind_Speed'    ,'max'        ,'WindSpd_Max_m/s'	 ,'gust_speed_m_s^-1'                       ],
    ['PP_Tipper'        ,'sum'        ,'Rain_mm_Tot_mm'		 ,'Rain_(liquid)_water_layer_thickness_mm'  ],
    ['PC_Tipper'		,'sum'        ,''					 ,''                                        ],
    ['PC_Raw_Pipe'		,'mean'       ,''					 ,''                                        ],
    ['Snow_Depth'		,'mean'       ,'TCDT_m'				 ,'Snow_depth_cm'                           ],
    ['SWE'				,'mean'       ,''                    ,''                                        ],
    ['Solar_Rad'		,'mean'       ,'SolarRad_Avg_W/m2'   ,'solar_radiation_w_m^-2'                  ],
    ['Batt'             ,'mean'       ,'BattV_Avg_Volts'	 ,'Batt_V'                                  ],
    ['Pk_Wind_Dir'      ,''           ,''	                 ,''                                        ],
    ['PP_Pipe'          ,''           ,''	                 ,''                                        ],
    ['SWU'              ,''           ,''	                 ,''                                        ],
    ['SWL'              ,''           ,''	                 ,''                                        ],
    ['LWU'              ,''           ,''	                 ,''                                        ],
    ['LWL'              ,''           ,''	                 ,''                                        ],
    ['Lysimeter'        ,''           ,''	                 ,'Lysimeter_water_layer_thickness_mm'      ],
    ['Soil_Moisture'    ,''           ,''	                 ,''                                        ],
    ['Soil_Temperature' ,''           ,''	                 ,''                                        ]
    ]
    # raw_Steph1_CSci
    # 'BattV_Min_Volts', 'BattV_Max_Volts', 'BattV_Avg_Volts',
    # 'AirTemp_Avg_Deg_C', 'AirTemp_Min_Deg_C', 'AirTemp_Max_Deg_C', 'RH_Avg_percent', 'AirPressur_Avg_hPa',
    # 'WindSpdInst_m/s', 'WindSpd_Avg_m/s', 'WindSpd_Min_m/s', 'WindSpd_Max_m/s', 'WindSpd_TMx', 'WindSpd_S_WVT_m/s', 'WindDir_D1_WVT_m/s', 'WindDir_SD1_WVT_m/s',
    # 'SolarRad_Avg_W/m2', 'Rain_mm_Tot_mm', 'Rain_Counts_Tot',
    # 'DT_m', 'DT_Avg_m', 'DT_Min_m', 'DT_Max_m', 'Q', 'Q_Avg', 'Q_Min', 'Q_Max', 'TCDT_m', 'TCDT_Avg_m', 'TCDT_Min_m', 'TCDT_Max_m'
    # 
    # raw_Steph1_hobo
    # 'Batt_V',
    # 'Temp_degC', 'RH_percent',
    # 'wind_speed_m_s^-1', 'gust_speed_m_s^-1', 'wind_direction_deg',
    # 'Snow_depth_cm',
    # 'solar_radiation_w_m^-2',
    # 'Rain_(liquid)_counts', 'Rain_(liquid)_conversion_coeff_mm_tip^-1', 'Rain_(liquid)_water_layer_thickness_mm',
    # 'Lysimeter_counts', 'Lysimeter_conversion_coeff_mm_tip^-1', 'Lysimeter_water_layer_thickness_mm'

    tables_S2 = ['clean_steph2'  ,'aggregation_method', 'raw_Steph2_CSci']
    cols_S2 = [
    ['DateTime'         ,''           ,'DateTime'           ],
    ['Air_Temp'	    	,'mean'       ,'AirTemp_Avg_Deg_C'  ],
    ['RH'			    ,'mean'       ,'RH_Avg_percent'		],
    ['BP'			    ,'mean'       ,''                   ],
    ['Wind_Speed'	    ,'mean'       ,'WindSpd_Avg_m/s'	],
    ['Wind_Dir'         ,'mean_deg'   ,'WindDir_D1_WVT_m/s'	],
    ['Pk_Wind_Speed'    ,'max'        ,'WindSpd_Max_m/s'	],
    ['PP_Tipper'        ,'sum'        ,'Rain_Tot_mm'		],
    ['PC_Tipper'		,'sum'        ,''					],
    ['PC_Raw_Pipe'		,'mean'       ,'PrecipLvl_Avg_M'	],
    ['Snow_Depth'		,'mean'       ,'DTbest'				],
    ['SWE'				,'mean'       ,''                   ],
    ['Solar_Rad'		,'mean'       ,'SolarRad_Avg_W/m2'  ],
    ['Batt'             ,'mean'       ,'BattV_Avg_Volts'	],
    ['Pk_Wind_Dir'      ,''           ,''	                ],
    ['PP_Pipe'          ,''           ,''	                ],
    ['SWU'              ,''           ,''	                ],
    ['SWL'              ,''           ,''	                ],
    ['LWU'              ,''           ,''	                ],
    ['LWL'              ,''           ,''	                ],
    ['Lysimeter'        ,''           ,'Lys_Tot_mm'         ],
    ['Soil_Moisture'    ,''           ,''	                ],
    ['Soil_Temperature' ,''           ,''	                ]
    ]
    # raw_Steph2_CSci
    # 'BattV_Avg_Volts',
    # 'AirTemp_Avg_Deg_C', 'AirTemp_Min_Deg_C', 'AirTemp_Max_Deg_C', 'RH_Avg_percent',
    # 'WindSpdInst_m/s', 'WindSpd_Avg_m/s', 'WindSpd_Min_m/s', 'WindSpd_Max_m/s', 'WindSpd_S_WVT_m/s', 'WindDir_D1_WVT_m/s', 'WindDir_SD_Deg', 'WindSpd_TMx_m/s',
    # 'SolarRad_Avg_W/m2', 'Rain_Tot_mm', 'Rain_Counts_Tot',
    # 'DTbest', 'Qbest', 'TCDT_M',
    # 'PrecipLvl_M', 'PrecipLvl_Avg_M', 'PrecipLvl_Min_M', 'PrecipLvl_Max_M', 'PrecipTemp_Deg_C', 'PrecipTemp_Avg_Deg_C', 'PrecipTemp_Min_Deg_C', 'PrecipTemp_Max_Deg_C',
    # 'Lys_Counts_Tot', 'Lys_Tot_mm',


    tables_S3 = ['clean_steph3'  ,'aggregation_method', 'raw_Steph3_CSci']
    cols_S3 = [
    ['DateTime'         ,''           ,'DateTime'           ],
    ['Air_Temp'	    	,'mean'       ,'Air_Temp'           ],
    ['RH'			    ,'mean'       ,'RH'		            ],
    ['BP'			    ,'mean'       ,''                   ],
    ['Wind_Speed'	    ,'mean'       ,'Wind_Speed'	        ],
    ['Wind_Dir'         ,'mean_deg'   ,'Wind_Dir'	        ],
    ['Pk_Wind_Speed'    ,'max'        ,'Gust_Speed'	        ],
    ['PP_Tipper'        ,'sum'        ,'Rain'		        ],
    ['PC_Tipper'		,'sum'        ,''					],
    ['PC_Raw_Pipe'		,'mean'       ,''	                ],
    ['Snow_Depth'		,'mean'       ,'Snow_Depth'			],
    ['SWE'				,'mean'       ,''                   ],
    ['Solar_Rad'		,'mean'       ,'Solar_Rad'          ],
    ['Batt'             ,'mean'       ,'BattV_Min'	        ],
    ['Pk_Wind_Dir'      ,''           ,''	                ],
    ['PP_Pipe'          ,''           ,''	                ],
    ['SWU'              ,''           ,''	                ],
    ['SWL'              ,''           ,''	                ],
    ['LWU'              ,''           ,''	                ],
    ['LWL'              ,''           ,''	                ],
    ['Lysimeter'        ,''           ,'Lysimeter'	        ],
    ['Soil_Moisture'    ,''           ,''	                ],
    ['Soil_Temperature' ,''           ,''	                ]
    ]
    # raw_Steph3_CSci
    # 'Lysimeter', 'Rain', 'Solar_Rad', 'Snow_Depth', 'Current', 'Air_Temp', 'RH', 'Wind_Speed', 'Gust_Speed', 'Wind_Dir', 'Backup_Batt', 'BattV_Min', 'WindDir_SD'


    tables_S4 = ['clean_steph4'  ,'aggregation_method', 'raw_Steph4_CSci', 	'raw_Steph4_hobo']
    cols_S4 = [
    ['DateTime'         ,''           ,'DateTime'          ,'DateTime'                                 ],
    ['Air_Temp'	    	,'mean'       ,'AirTemp_Avg_Deg_C' ,'temp_degC'                                ],
    ['RH'			    ,'mean'       ,'RH_Avg_percent'	   ,'rh_percent'                               ],
    ['BP'			    ,'mean'       ,''                  ,''                                         ],
    ['Wind_Speed'	    ,'mean'       ,'WindSpd_m/s'	   ,'wind_speed_m_s^-1'                        ],
    ['Wind_Dir'         ,'mean_deg'   ,'WindDir_degrees'   ,'Wind_Direction_deg'	                   ],
    ['Pk_Wind_Speed'    ,'max'        ,'WindSpd_Max_m/s'   ,'gust_speed_m_s^-1'	                       ],
    ['PP_Tipper'        ,'sum'        ,'Rain_Tot_mm'	   ,'Rain_(liquid)_water_layer_thickness_mm'   ],
    ['PC_Tipper'		,'sum'        ,''				   ,''	                                       ],
    ['PC_Raw_Pipe'		,'mean'       ,''	               ,''                                         ],
    ['Snow_Depth'		,'mean'       ,'TCDT_m'			   ,'Snow_depth_cm'	                           ],
    ['SWE'				,'mean'       ,''                  ,''                                         ],
    ['Solar_Rad'		,'mean'       ,'SolarRad_Avg_W/m2' ,'Solar_Radiation_W_m^-2'                   ],
    ['Batt'             ,'mean'       ,'BattV_Avg_Volts'   ,'Batt_V'	                               ],
    ['Pk_Wind_Dir'      ,''           ,''	               ,''                                         ],
    ['PP_Pipe'          ,''           ,''	               ,''                                         ],
    ['SWU'              ,''           ,''	               ,''                                         ],
    ['SWL'              ,''           ,''	               ,''                                         ],
    ['LWU'              ,''           ,''	               ,''                                         ],
    ['LWL'              ,''           ,''	               ,''                                         ],
    ['Lysimeter'        ,''           ,''	               ,''                                         ],
    ['Soil_Moisture'    ,''           ,''	               ,''                                         ],
    ['Soil_Temperature' ,''           ,''	               ,'SoilTemp_degC'                            ]
    ]
    # raw_Steph4_CSci
    # 'BattV_Avg_Volts',
    # 'AirTemp_Avg_Deg_C', 'RH_Avg_percent',
    # 'WindSpd_Max_m/s', 'WindSpd_TMx_m/s', 'WindSpd_m/s', 'WindDir_degrees', 'WindDir_SD_m/s',
    # 'SolarRad_Avg_W/m2', 'Rain_Tot_mm', 'Rain_Counts_Tot',
    # 'DTbest', 'Qbest', 'TCDT_m',

    # raw_Steph4_hobo
    # 'Batt_V',
    # 'rh_percent', 'temp_degC',
    # 'gust_speed_m_s^-1', 'wind_speed_m_s^-1', 'Wind_Direction_deg',
    # 'Rain_(liquid)_counts', 'Rain_(liquid)_conversion_coeff_mm_tip^-1', 'Rain_(liquid)_water_layer_thickness_mm', 'Rain_(liquid)_water_volume_mL',
    # 'Solar_Radiation_W_m^-2', 'Snow_depth_cm', 'SoilTempBattery_V', 'SoilTemp_degC'


    tables_S5 = ['clean_steph5'  ,'aggregation_method', 'raw_Steph5_CSci']
    cols_S5 = [
    ['DateTime'         ,''           ,'DateTime'           ],
    ['Air_Temp'	    	,'mean'       ,'AirT_Avg_degC'      ],
    ['RH'			    ,'mean'       ,'AirH_Avg_percent'   ],
    ['BP'			    ,'mean'       ,''                   ],
    ['Wind_Speed'	    ,'mean'       ,'WindSpd_m/s'	    ],
    ['Wind_Dir'         ,'mean_deg'   ,'WindDir_deg'	    ],
    ['Pk_Wind_Speed'    ,'max'        ,'WindSpd_Max_m/s'    ],
    ['PP_Tipper'        ,'sum'        ,'Rain_Tot_mm_we'     ],
    ['PC_Tipper'		,'sum'        ,''					],
    ['PC_Raw_Pipe'		,'mean'       ,''	                ],
    ['Snow_Depth'		,'mean'       ,'SR50_DTcomp_Avg_m'  ],
    ['SWE'				,'mean'       ,''                   ],
    ['Solar_Rad'		,'mean'       ,'SW_Avg_W/m2'        ],
    ['Batt'             ,'mean'       ,'BattV_Min_Volts'	],
    ['Pk_Wind_Dir'      ,''           ,''	                ],
    ['PP_Pipe'          ,''           ,''	                ],
    ['SWU'              ,''           ,''	                ],
    ['SWL'              ,''           ,''	                ],
    ['LWU'              ,''           ,''	                ],
    ['LWL'              ,''           ,''	                ],
    ['Lysimeter'        ,''           ,''	                ],
    ['Soil_Moisture'    ,''           ,''	                ],
    ['Soil_Temperature' ,''           ,''	                ]
    ]
    # raw_Steph5_CSci
    # 'BattV_Min_Volts', 'AirT_Avg_degC', 'AirH_Avg_percent',
    # 'SR50_DTcomp_Avg_m', 'SR50_T_Avg_degC',
    # 'Rain_Tot_mm_we', 'SW_Avg_W/m2',
    # 'WindSpd_Max_m/s', 'WindSpd_m/s', 'WindDir_deg', 'WindDir_SD_m/s'


    tables_S6 = ['clean_steph6'  ,'aggregation_method', 'raw_Steph6_CSci', 	'raw_Steph6_hobo']
    cols_S6 = [
    ['DateTime'         ,''           ,'DateTime'          ,'DateTime'                               ],
    ['Air_Temp'	    	,'mean'       ,'AirTemp_Avg_Deg_C' ,'temp_degC'                              ],
    ['RH'			    ,'mean'       ,'RH_Avg_percent'    ,'RH_percent'                             ],
    ['BP'			    ,'mean'       ,'BP_Avg_kpa'        ,''                                       ],
    ['Wind_Speed'	    ,'mean'       ,'WindSpd_Avg_m/s'   ,'wind_speed_m_s^-1'                      ],
    ['Wind_Dir'         ,'mean_deg'   ,'WindDir_D1_WVT_m/s','wind_direction_deg'                     ],
    ['Pk_Wind_Speed'    ,'max'        ,'WindSpd_Max_m/s'   ,'gust_speed_m_s^-1'                      ],
    ['PP_Tipper'        ,'sum'        ,'Rain_Tot_mm'       ,'Rain_(liquid)_water_layer_thickness_mm' ],
    ['PC_Tipper'		,'sum'        ,''                  ,''                                       ],
    ['PC_Raw_Pipe'		,'mean'       ,'PrecipLvl_Avg_M'   ,'Precip_pressure_mm'                     ],
    ['Snow_Depth'		,'mean'       ,'TCDT_M'            ,'snow_depth_cm'                          ],
    ['SWE'				,'mean'       ,''                  ,''                                       ],
    ['Solar_Rad'		,'mean'       ,'SolarRad_Avg_W/m2' ,'solar_radiation_w_m^-2'                 ],
    ['Batt'             ,'mean'       ,'BattV_Avg_Volts'   ,'Batt_V'                                 ],
    ['Pk_Wind_Dir'      ,''           ,''	               ,''                                       ],
    ['PP_Pipe'          ,''           ,''	               ,'Precip_(liquid_and_solid)_water_layer_thickness_mm' ],
    ['SWU'              ,''           ,''	               ,''                                       ],
    ['SWL'              ,''           ,''	               ,''                                       ],
    ['LWU'              ,''           ,''	               ,''                                       ],
    ['LWL'              ,''           ,''	               ,''                                       ],
    ['Lysimeter'        ,''           ,'Lys_Tot_mm'        ,'Lysimeter_water_layer_thickness_mm'     ],
    ['Soil_Moisture'    ,''           ,''	               ,''                                       ],
    ['Soil_Temperature' ,''           ,''	               ,'Soil_Temp_1_degC'                       ]
    ]
    # raw_Steph6_CSci
    # 'BattV_Avg_Volts', 'BattV_Min_Volts', 'AirTemp_Avg_Deg_C', 'AirTemp_Min_Deg_C', 'AirTemp_Max_Deg_C', 'RH_Avg_percent',
    # 'WindSpdInst_m/s', 'WindSpd_Avg_m/s', 'WindSpd_Min_m/s', 'WindSpd_Max_m/s', 'WindSpd_S_WVT_m/s', 'WindDir_D1_WVT_m/s', 'WindSpd_TMx_m/s', 'WindDir_SD_m/s',
    # 'SolarRad_Avg_W/m2', 'Rain_Tot_mm', 'Rain_Counts_Tot', 'Lys_Counts_Tot', 'Lys_Tot_mm',
    # 'DTbest', 'Qbest', 'TCDT_M',
    # 'PrecipLvl_M', 'PrecipLvl_Avg_M', 'PrecipLvl_Min_M', 'PrecipLvl_Max_M', 'PrecipTemp_Deg_C', 'PrecipTemp_Avg_Deg_C', 'PrecipTemp_Min_Deg_C', 'PrecipTemp_Max_Deg_C',
    # 'BP_Avg_kpa', 

    # raw_Steph6_hobo
    # 'Batt_V', 'temp_degC', 'RH_percent',
    # 'wind_speed_m_s^-1', 'gust_speed_m_s^-1', 'wind_direction_deg',
    # 'snow_depth_cm', 'solar_radiation_w_m^-2',
    # 'Rain_(liquid)_counts', 'Rain_(liquid)_conversion_coeff_mm_tip^-1', 'Rain_(liquid)_water_layer_thickness_mm',
    # 'Precip_(liquid_and_solid)_counts', 'Precip_(liquid_and_solid)_conversion_coeff_mm_tip^-1', 'Precip_(liquid_and_solid)_water_layer_thickness_mm', 'Precip_pressure_mm',
    # 'Lysimeter_counts', 'Lysimeter_conversion_coeff_mm_tip^-1', 'Lysimeter_water_layer_thickness_mm',
    # 'Soil_Temp_1_degC', 'Soil_Temp_2_degC', 'Soil_Temp_3_degC'


    tables_S7 = ['clean_steph7'  ,'aggregation_method', 'raw_Steph7_CSci', 	'raw_Steph7_hobo']
    cols_S7 = [
    ['DateTime'         ,''           ,'DateTime'          ,'DateTime'                               ],
    ['Air_Temp'	    	,'mean'       ,'AirTemp_Avg_Deg_C' ,'Air_Temp_degC'                          ],
    ['RH'			    ,'mean'       ,'RH_Avg_percent'    ,'airRH_percent'                          ],
    ['BP'			    ,'mean'       ,''                  ,''                                       ],
    ['Wind_Speed'	    ,'mean'       ,'WindSpd_m/s'       ,'Wind_Speed_m_s^-1'                      ],
    ['Wind_Dir'         ,'mean_deg'   ,'WindDir_degrees'   ,'Wind_Direction_degrees'                 ],
    ['Pk_Wind_Speed'    ,'max'        ,'WindSpd_Max_m/s'   ,'Wind_Gust_Speed_m_s^-1'                 ],
    ['PP_Tipper'        ,'sum'        ,'Rain_Tot_mm'       ,'Rain_(liquid)_water_layer_thickness_mm' ],
    ['PC_Tipper'		,'sum'        ,''                  ,''                                       ],
    ['PC_Raw_Pipe'		,'mean'       ,''                  ,''                                       ],
    ['Snow_Depth'		,'mean'       ,'TCDT_M'            ,'Snow_depth_cm'                          ],
    ['SWE'				,'mean'       ,''                  ,''                                       ],
    ['Solar_Rad'		,'mean'       ,'SolarRad_Avg_W/m2' ,'Solar_Radiation_W_m^-2'                 ],
    ['Batt'             ,'mean'       ,'BattV_Avg_Volts'   ,'Battery_V'                              ],
    ['Pk_Wind_Dir'      ,''           ,''	               ,''                                       ],
    ['PP_Pipe'          ,''           ,''	               ,'Precipitation_(liquid+solid)_water_layer_thickness_mm' ],
    ['SWU'              ,''           ,''	               ,''                                       ],
    ['SWL'              ,''           ,''	               ,''                                       ],
    ['LWU'              ,''           ,''	               ,''                                       ],
    ['LWL'              ,''           ,''	               ,''                                       ],
    ['Lysimeter'        ,''           ,''	               ,''                                       ],
    ['Soil_Moisture'    ,''           ,''	               ,''                                       ],
    ['Soil_Temperature' ,''           ,''	               ,''                                       ]
    ]
    # raw_Steph7_CSci
    # 'BattV_Avg_Volts', 'AirTemp_Avg_Deg_C', 'RH_Avg_percent',
    # 'WindSpd_Max_m/s', 'WindSpd_TMx_m/s', 'WindSpd_m/s', 'WindDir_degrees', 'WindDir_SD_m/s',
    # 'SolarRad_Avg_W/m2', 'Rain_Tot_mm', 'Rain_Counts_Tot', 'DTbest', 'Qbest', 'TCDT_M'

    # raw_Steph7_hobo
    # 'Battery_V', 'Air_Temp_degC', 'airRH_percent',
    # 'Current_mA',
    # 'Wind_Gust_Speed_m_s^-1', 'Wind_Speed_m_s^-1', 'Wind_Direction_degrees',
    # 'Solar_Radiation_W_m^-2',
    # 'Precipitation_(liquid+solid)_counts', 'Precipitation_(liquid+solid)_conversion_coeff_for_mm_tip^-1', 'Precipitation_(liquid+solid)_water_layer_thickness_mm',
    # 'Rain_(liquid)_counts', 'Rain_(liquid)_conversion_coeff_for_mm_tip^-1', 'Rain_(liquid)_water_layer_thickness_mm',
    # 'Judd_snow_depth_readings', 'Snow_depth_cm'

    
    tables_S8 = ['clean_steph8'  ,'aggregation_method', 'raw_Steph8_CSci', 	'raw_Steph8_hobo']
    cols_S8 = [
    ['DateTime'         ,''           ,'DateTime'          ,'DateTime'                                  ],
    ['Air_Temp'	    	,'mean'       ,'AirTemp_Avg_Deg_C' ,'Air_Temperature_degC'                      ],
    ['RH'			    ,'mean'       ,'RH_Avg_percent'    ,'Air_relative_humidity_percent'             ],
    ['BP'			    ,'mean'       ,''                  ,''                                          ],
    ['Wind_Speed'	    ,'mean'       ,'WindSpd_m/s'       ,'Wind_Speed_m_sec^-1'                       ],
    ['Wind_Dir'         ,'mean_deg'   ,'WindDir_degrees'   ,'Wind_Direction_deg'                        ],
    ['Pk_Wind_Speed'    ,'max'        ,'WindSpd_Max_m/s'   ,'Wind_Gust_Speed_m_s^-1'                    ],
    ['PP_Tipper'        ,'sum'        ,'Rain_Tot_mm'       ,'Rain_(liquid)_water_layer_thickness_mm'    ],
    ['PC_Tipper'		,'sum'        ,''                  ,''                                          ],
    ['PC_Raw_Pipe'		,'mean'       ,''                  ,''                                          ],
    ['Snow_Depth'		,'mean'       ,'TCDT_m'            ,'Distance_to_snow_cm'                       ],
    ['SWE'				,'mean'       ,''                  ,''                                          ],
    ['Solar_Rad'		,'mean'       ,'SolarRad_Avg_W/m2' ,'solar_radiation_w_m^-2'                    ],
    ['Batt'             ,'mean'       ,'BattV_Avg_Volts'   ,'Batt_V'                                    ],
    ['Pk_Wind_Dir'      ,''           ,''	               ,''                                          ],
    ['PP_Pipe'          ,''           ,''	               ,''                                          ],
    ['SWU'              ,''           ,''	               ,''                                          ],
    ['SWL'              ,''           ,''	               ,''                                          ],
    ['LWU'              ,''           ,''	               ,''                                          ],
    ['LWL'              ,''           ,''	               ,''                                          ],
    ['Lysimeter'        ,''           ,'Lys_Tot_mm'	       ,'Lysimeter_tipper_water_layer_thickness_mm' ],
    ['Soil_Moisture'    ,''           ,''	               ,''                                          ],
    ['Soil_Temperature' ,''           ,''	               ,''                                          ]
    ]
# 	raw_Steph8_CSci
#   'BattV_Avg_Volts', 'AirTemp_Avg_Deg_C', 'RH_Avg_percent',
#   'WindSpd_Max_m/s', 'WindSpd_TMx_m/s', 'WindSpd_m/s', 'WindDir_degrees', 'WindDir_SD_m/s',
#   'SolarRad_Avg_W/m2',
#   'Rain_Tot_mm', 'Rain_Counts_Tot',
#   'Lys_Tot_mm', 'Lys_Counts_Tot',
#   'DTbest', 'Qbest', 'TCDT_m'

#   raw_Steph8_hobo
#   'Batt_V', 'Air_Temperature_degC', 'Air_relative_humidity_percent',
#   'solar_radiation_w_m^-2',
#   'Wind_Speed_m_sec^-1', 'Wind_Gust_Speed_m_s^-1', 'Wind_Direction_deg',
#   'Distance_to_snow_cm',
#   'Lysimeter_tipper_counts', 'Lysimeter_tipper_conversion_coeff_mm_tip^-1', 'Lysimeter_tipper_water_layer_thickness_mm', 'Lysimeter_tipper_water_volume_mL',
#   'Rain_(liquid)_tipper_counts', 'Rain_(liquid)_conversion_coeff_mm_tip^-1', 'Rain_(liquid)_water_layer_thickness_mm'
	

    tables_S9 = ['clean_upperrussell'  ,'aggregation_method', 'raw_UpperRussell_CSci']
    cols_S9 = [
    ['DateTime'         ,''           ,'DateTime'      ],
    ['Air_Temp'	    	,'mean'       ,'Air_Temp'      ],
    ['RH'			    ,'mean'       ,'RH'            ],
    ['BP'			    ,'mean'       ,'airP_Avg'      ],
    ['Wind_Speed'	    ,'mean'       ,'Wind_speed'	   ],
    ['Wind_Dir'         ,'mean_deg'   ,'Wind_Dir'	   ],
    ['Pk_Wind_Speed'    ,'max'        ,'Pk_Wind_Speed' ],
    ['PP_Tipper'        ,'sum'        ,'PP_Tipper'     ],
    ['PC_Tipper'		,'sum'        ,''			   ],
    ['PC_Raw_Pipe'		,'mean'       ,'PC_Raw_Pipe'   ],
    ['Snow_Depth'		,'mean'       ,'Snow_Depth'    ],
    ['SWE'				,'mean'       ,''              ],
    ['Solar_Rad'		,'mean'       ,'Solar_Rad'     ],
    ['Batt'             ,'mean'       ,'Batt'	       ],
    ['River_Thick'      ,'mean'       ,'River_Thick'   ],
    ['Pk_Wind_Dir'      ,''           ,''	           ],
    ['PP_Pipe'          ,''           ,''	           ],
    ['SWU'              ,''           ,''	           ],
    ['SWL'              ,''           ,''	           ],
    ['LWU'              ,''           ,''	           ],
    ['LWL'              ,''           ,''	           ],
    ['Lysimeter'        ,''           ,''	           ],
    ['Soil_Moisture'    ,''           ,''	           ],
    ['Soil_Temperature' ,''           ,''	           ]
    ]
    # raw_UpperRussell_CSci
    # 'Batt', 'Air_Temp', 'RH', 'airP_Avg',
    # 'Wind_speed', 'Wind_Dir', 'Pk_Wind_Speed',
    # 'PP_Tipper_cnt', 'PP_Tipper', 'PC_Raw_Pipe',
    # 'Snow_Depth', 'Solar_Rad', 'River_Thick', 'River_Thick_SD'
    
    
    tables_S10 = ['clean_russellmain' ,'aggregation_method', 'raw_RussellMain_hobo']
    cols_S10 = [
    ['DateTime'         ,''           ,'DateTime'                               ],
    ['Air_Temp'	    	,'mean'       ,'AirTemp_degC'                           ],
    ['RH'			    ,'mean'       ,'RH_percent'                             ],
    ['BP'			    ,'mean'       ,''                                       ],
    ['Wind_Speed'	    ,'mean'       ,''	                                    ],
    ['Wind_Dir'         ,'mean_deg'   ,''	                                    ],
    ['Pk_Wind_Speed'    ,'max'        ,'gust_speed_m_s^-1'                      ],
    ['PP_Tipper'        ,'sum'        ,'Rain_(liquid)_water_layer_thickness_mm' ],
    ['PC_Tipper'		,'sum'        ,''			                            ],
    ['PC_Raw_Pipe'		,'mean'       ,''                                       ],
    ['Snow_Depth'		,'mean'       ,''                                       ],
    ['SWE'				,'mean'       ,''                                       ],
    ['Solar_Rad'		,'mean'       ,''                                       ],
    ['Batt'             ,'mean'       ,'Batt_V'                                 ],
    ['Pk_Wind_Dir'      ,''           ,''	                                    ],
    ['PP_Pipe'          ,''           ,''	                                    ],
    ['SWU'              ,''           ,''	                                    ],
    ['SWL'              ,''           ,''	                                    ],
    ['LWU'              ,''           ,''	                                    ],
    ['LWL'              ,''           ,''	                                    ],
    ['Lysimeter'        ,''           ,''	                                    ],
    ['Soil_Moisture'    ,''           ,''	                                    ],
    ['Soil_Temperature' ,''           ,''	                                    ]
    ]
    # raw_RussellMain_hobo
    # 'Batt_V', 'AirTemp_degC', 'RH_percent', 'gust_speed_m_s^-1',
    # 'Rain_(liquid)_tipper_counts', 'Rain_(liquid)_conversion_coeff_mm_tip^-1', 'Rain_(liquid)_water_layer_thickness_mm'


    # ref = [
    # 'DateTime'     ,
    # 'Air_Temp'     ,      # air temperature, degC
    # 'RH'			 ,      # air relative humidity, percent
    # 'BP'			 ,      # air pressure, units
    # 'Wind_Speed'	 ,      # wind speed, units
    # 'Wind_Dir'     ,      # wind direction, degrees
    # 'Pk_Wind_Speed',      # max wind speed, units
    # 'PP_Tipper'    ,      # liquid precipitation during a time step derived from a tipping bucket, mm of we
    # 'PC_Tipper'	 ,      # 
    # 'PC_Raw_Pipe'	 ,      # cumulative total precipitation derived from pressure sensor in a precipitation pipe, m of we
    # 'Snow_Depth'	 ,      # snow depth, cm
    # 'SWE'			 ,      # 
    # 'Solar_Rad'	 ,      # SW radiation, W m^-2
    # 'Batt'         ,      # Battery voltage, V
    # 'Pk_Wind_Dir'  ,      # 
    # 'PP_Pipe'      ,      # total precipitation during a time step derived from a tipping bucket fed by overflow from a precipitation pipe, mm of we
    # 'SWU'          ,      # 
    # 'SWL'          ,      # 
    # 'LWU'          ,      # 
    # 'LWL'          ,      # 
    # 'Lysimeter'    ,      # 
    # 'Soil_Moisture',      # 
    # 'Soil_Temperature' ]  # 
    
    # def find_deviations(A, **lists):
    #     bad = []
    #     for name, L in lists.items():
    #         firsts = [sub[0] for sub in L]
    #         if firsts != A:
    #             bad.append(name)
    #     return bad
    
    # deviations = find_deviations(ref, c1 = cols_S1, c2 = cols_S2, c3 = cols_S3, c4 = cols_S4, c5 = cols_S5, c6 = cols_S6)
    # del ref, deviations
            
    D = {
        'S1' : pd.DataFrame(cols_S1 , columns=tables_S1 ),
        'S2' : pd.DataFrame(cols_S2 , columns=tables_S2 ),
        'S3' : pd.DataFrame(cols_S3 , columns=tables_S3 ),
        'S4' : pd.DataFrame(cols_S4 , columns=tables_S4 ),
        'S5' : pd.DataFrame(cols_S5 , columns=tables_S5 ),
        'S6' : pd.DataFrame(cols_S6 , columns=tables_S6 ),
        'S7' : pd.DataFrame(cols_S7 , columns=tables_S7 ),
        'S8' : pd.DataFrame(cols_S8 , columns=tables_S8 ),
        'S9' : pd.DataFrame(cols_S9 , columns=tables_S9 ),
        'S10': pd.DataFrame(cols_S10, columns=tables_S10)
         }
    
    for site in D.keys():
        D[site] = D[site].set_index(D[site].columns[0])
            
    return D