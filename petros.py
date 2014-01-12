# -*- coding: utf-8 -*-
"""
Created on Tue Jan 07 23:41:17 2014

@author: LENOVO
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#specify the location of the file
loc = "petros_new.xls"
names = ['maios2012','iounios2012','euro2009','per2010','dim2010']
frames = {
          names[0]:pd.read_excel(loc,names[0],header=1,skiprows=0,index_col=0,parse_cols="B:C,D:O",na_values=['NA']),
          names[1]:pd.read_excel(loc,names[1],header=1,skiprows=0,index_col=0,parse_cols="B:C,D:O",na_values=['NA']),
          names[2]:pd.read_excel(loc,names[2],header=1,skiprows=0,index_col=0,parse_cols="B:C,D:O",na_values=['NA']),
          names[3]:pd.read_excel(loc,names[3],header=1,skiprows=0,index_col=0,parse_cols="B:C,D:O",na_values=['NA']),
          names[4]:pd.read_excel(loc,names[4],header=1,skiprows=0,index_col=0,parse_cols="B:C,D:O",na_values=['NA'])}
print frames[names[3]]
#Read data for maios 2012
