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
loc = "petros_new.xls"
#Specify the sheet names
names = ['maios2012','iounios2012','euro2009','per2010','dim2010']

names_voul = ['enotita','dimos','egg','psifisan','eggira','akira','lefka',
                'nd','siriza','pasok','xa','kke','anel','dimar']
#create a dictionary of dataframes from the excel file
frames = {
          names[0]:pd.read_excel(loc,names[0],header=None,skiprows=1,
                                 index_col=None,parse_cols="A:N",na_values=['NA']),
          names[1]:pd.read_excel(loc,names[1],header=0,skiprows=0,
                                 index_col=0,parse_cols="A:N",na_values=['NA']),
          names[2]:pd.read_excel(loc,names[2],header=0,skiprows=0,
                                 index_col=0,parse_cols="A:N",na_values=['NA']),
          names[3]:pd.read_excel(loc,names[3],header=0,skiprows=0,
                                 index_col=0,parse_cols="A:AB",na_values=['NA']),
          names[4]:pd.read_excel(loc,names[4],header=0,skiprows=0,
                                 index_col=0,parse_cols="A:L",na_values=['NA'])}

#Fix column names
frames[names[0]].columns = names_voul
print frames[names[0]]

#Work with maios2012
m12 = frames[names[0]]
#Group by enotita
g_m12 = m12.groupby('enotita')
print g_m12.groups
