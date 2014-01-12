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

#print df.index #Print the index of the dataframe

#print df.columns #Print the column names

#print df.values #Print the values

#print df.describe() #Show basic descriptive statistics

#print df.sort_index(axis=1, ascending=False) #Sort by axis

#print df['ENOTHTA'] #Select a single column
#print df[0:10] #Slice the rows
#print df.loc[0:10,['ENOTHTA','DIMOS']]
#print df.iloc[0:2,[1,3]]
sample = df.iloc[0:,[0,4,5,6]]
print sample.describe()
