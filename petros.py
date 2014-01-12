# -*- coding: utf-8 -*-
"""
Created on Tue Jan 07 23:41:17 2014

@author: LENOVO
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Sophisticated use of read_excel for future use
#pd.read_excel(loc,names[0],header=0,skiprows=0,
#                                 index_col=0,parse_cols="B:C,D:O",na_values=['NA'])

#specify the location of the file
loc = "data.xls"
#Specify the sheet names
names = ['data']

col_names = ['ENOTHTA','EKL_PER','DIMOS','EKLOGI','FASI','METRHSH','ARITHMOS','IS_TOTAL']

#Read the data into the data frame
df = pd.read_excel(loc,'data',header=0,skiprows=0,index_col=None,parse_cols='A:H',na_values=['NA'])


print df
