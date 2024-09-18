import pandas    as pd

# sites, tables_S1, cols_S1, tables_S2, cols_S2 = sites_tables_cols()
def sites_tables_cols():
    sites     = ['S1', 'S2', 'S4', 'S6']
    
    tables_S1 = ['clean_Steph1'  ,'aggregation_method'  , 'min', 'max', 'raw_Steph1_CSci'  ,'raw_Steph1_hobo']
    cols_S1 = pd.DataFrame([
    ['DateTime'         ,''           ,   0 ,   0         ,'DateTime'            ,'DateTime'              ],
    ['Air_Temp'	    	,'mean'       , -40 ,  40         ,'AirTemp_Avg_Deg_C'   ,'Temp_degC'             ],
    ['RH'			    ,'mean'       ,   0 , 100         ,'RH_Avg_percent'		 ,'RH_percent'            ],
    ['BP'			    ,'mean'       , 500 ,1500         ,'AirPressur_Avg_hPa'  ,''                      ],
    ['Wind_Speed'	    ,'mean'       ,   0 , 100         ,'WindSpd_Avg_m/s'	 ,'wind_speed_m_s^-1'     ],
    ['Wind_Dir'         ,'mean_deg'   ,   0 , 360         ,'WindDir_D1_WVT_m/s'	 ,'wind_direction_deg'    ],
    ['Pk_Wind_Speed'    ,'max'        ,   0 , 100         ,'WindSpd_Max_m/s'	 ,'gust_speed_m_s^-1'     ],
    ['PP_Tipper'        ,'sum'        ,   0 , 300         ,'Rain_mm_Tot_mm'		 ,'Rain_(liquid)_water_layer_thickness_mm'],
    ['PC_Tipper'		,'sum'        ,   0 ,float('inf') ,''					 ,''                      ],
    ['PC_Raw_Pipe'		,'mean'       ,   0 ,2500         ,''					 ,''                      ],
    ['Snow_Depth'		,'mean'       ,-500 , 500         ,'DT_m'				 ,'Snow_depth_cm'         ],
    ['SWE'				,'mean'       ,   0 ,1000         ,''                    ,''                      ],
    ['Solar_Rad'		,'mean'       , -10 ,1500         ,'SolarRad_Avg_W/m2'   ,'solar_radiation_w_m^-2'],
    ['Batt'             ,'mean'       ,   0 ,  20         ,'BattV_Avg_Volts'	 ,'Batt_V'                ]
     ])
    
    
    tables_S2 = ['clean_Steph2'  ,'aggregation_method'  , 'min', 'max', 'raw_Steph2_CSci']
    cols_S2 = pd.DataFrame([
    ['DateTime'         ,''           ,   0 ,   0         ,'DateTime'           ],
    ['Air_Temp'	    	,'mean'       , -40 ,  40         ,'AirTemp_Avg_Deg_C'  ],
    ['RH'			    ,'mean'       ,   0 , 100         ,'RH_Avg_percent'		],
    ['BP'			    ,'mean'       , 500 ,1500         ,''                   ],
    ['Wind_Speed'	    ,'mean'       ,   0 , 100         ,'WindSpd_Avg_m/s'	],
    ['Wind_Dir'         ,'mean_deg'   ,   0 , 360         ,'WindDir_D1_WVT_m/s'	],
    ['Pk_Wind_Speed'    ,'max'        ,   0 , 100         ,'WindSpd_Max_m/s'	],
    ['PP_Tipper'        ,'sum'        ,   0 , 300         ,'Rain_Tot_mm'		],
    ['PC_Tipper'		,'sum'        ,   0 ,float('inf') ,''					],
    ['PC_Raw_Pipe'		,'mean'       ,   0 ,2500         ,'PrecipLvl_Avg_M'	],
    ['Snow_Depth'		,'mean'       ,-500 , 500         ,'TCDT_M'				],
    ['SWE'				,'mean'       ,   0 ,1000         ,''                   ],
    ['Solar_Rad'		,'mean'       , -10 ,1500         ,'SolarRad_Avg_W/m2'  ],
    ['Batt'             ,'mean'       ,   0 ,  20         ,'BattV_Avg_Volts'	]
      ])
    
    
    tables_S4 = ['clean_Steph4'  ,'aggregation_method'  , 'min', 'max', 'raw_Steph4_CSci', 	'raw_Steph4_hobo']
    cols_S4 = pd.DataFrame([
    ['DateTime'         ,''           ,   0 ,   0         ,'DateTime'          ,'DateTime'                ],
    ['Air_Temp'	    	,'mean'       , -40 ,  40         ,'AirTemp_Avg_Deg_C' ,'temp_degC'               ],
    ['RH'			    ,'mean'       ,   0 , 100         ,'RH_Avg_percent'	   ,'rh_percent'              ],
    ['BP'			    ,'mean'       , 500 ,1500         ,''                  ,''                        ],
    ['Wind_Speed'	    ,'mean'       ,   0 , 100         ,'WindSpd_m/s'	   ,'wind_speed_m_s^-1'       ],
    ['Wind_Dir'         ,'mean_deg'   ,   0 , 360         ,'WindDir_degrees'   ,'Wind_Direction_deg'	  ],
    ['Pk_Wind_Speed'    ,'max'        ,   0 , 100         ,'WindSpd_Max_m/s'   ,'gust_speed_m_s^-1'	      ],
    ['PP_Tipper'        ,'sum'        ,   0 , 300         ,'Rain_Tot_mm'	   ,'Rain_(liquid)_water_layer_thickness_mm'	],
    ['PC_Tipper'		,'sum'        ,   0 ,float('inf') ,''				   ,''	                      ],
    ['PC_Raw_Pipe'		,'mean'       ,   0 ,2500         ,''	               ,''                        ],
    ['Snow_Depth'		,'mean'       ,-500 , 500         ,'TCDT_m'			   ,'Snow_depth_cm'	          ],
    ['SWE'				,'mean'       ,   0 ,1000         ,''                  ,''                        ],
    ['Solar_Rad'		,'mean'       , -10 ,1500         ,'SolarRad_Avg_W/m2' ,'Solar_Radiation_W_m^-2'  ],
    ['Batt'             ,'mean'       ,   0 ,  20         ,'BattV_Avg_Volts'   ,'Batt_V'	              ]
      ])
    
    
    tables_S6 = ['clean_Steph6'  ,'aggregation_method'  , 'min', 'max', 'raw_Steph6_CSci', 	'raw_Steph6_hobo']
    cols_S6 = pd.DataFrame([
    ['DateTime'         ,''           ,   0 ,   0         ,'DateTime'          ,'t'                      ],
    ['Air_Temp'	    	,'mean'       , -40 ,  40         ,'AirTemp_Avg_Deg_C' ,'temp_degC'              ],
    ['RH'			    ,'mean'       ,   0 , 100         ,'RH_Avg_percent'    ,'RH_percent'             ],
    ['BP'			    ,'mean'       , 500 ,1500         ,''                  ,''                       ],
    ['Wind_Speed'	    ,'mean'       ,   0 , 100         ,'WindSpd_Avg_m/s'   ,'wind_speed_m_s^-1'      ],
    ['Wind_Dir'         ,'mean_deg'   ,   0 , 360         ,'WindDir_D1_WVT_m/s','wind_direction_deg'     ],
    ['Pk_Wind_Speed'    ,'max'        ,   0 , 100         ,'WindSpd_Max_m/s'   ,'gust_speed_m_s^-1'      ],
    ['PP_Tipper'        ,'sum'        ,   0 , 300         ,'Rain_Tot_mm'       ,'Rain_(liquid)_water_layer_thickness_mm' ],
    ['PC_Tipper'		,'sum'        ,   0 ,float('inf') ,''                  ,''                       ],
    ['PC_Raw_Pipe'		,'mean'       ,   0 ,2500         ,'PrecipLvl_Avg_M'   ,'Precip_pressure_mm'     ],
    ['Snow_Depth'		,'mean'       ,-500 , 500         ,'TCDT_M'            ,'snow_depth_cm'          ],
    ['SWE'				,'mean'       ,   0 ,1000         ,''                  ,''                       ],
    ['Solar_Rad'		,'mean'       , -10 ,1500         ,'SolarRad_Avg_W/m2' ,'solar_radiation_w_m^-2' ],
    ['Batt'             ,'mean'       ,   0 ,  20         ,'BattV_Avg_Volts'   ,'Batt_V'                 ]
      ])
    
    cols_S1.columns = tables_S1
    cols_S2.columns = tables_S2
    cols_S4.columns = tables_S4
    cols_S6.columns = tables_S6
        
    return sites, cols_S1, cols_S2, cols_S4, cols_S6