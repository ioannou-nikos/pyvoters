# -*- coding: utf-8 -*-
"""
Ioannou Nikos

This file is an attempt to use pandas and pyplot
in order to create presantation of the voting data.
"""
#%%
#Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages

#Unicode fonts
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
matplotlib.rcParams['axes.titlesize'] = 16.0
matplotlib.rcParams['xtick.labelsize'] = 10.0
#25 Color map
my_colors = plt.cm.Set1(np.linspace(0,1,25))

#Read the data file into a dataframe
df = pd.read_csv("METRHSH_FULL.txt",sep=";",encoding="utf-8",header=0,
                 names=["ekl_per","dhmos","et","diamerisma","metrhsh",
                         "arithmos","elected","active","istotal"])
    
def create_pdf(df,mtitle,mlabels):
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    ax.pie(df.arithmos,labels=mlabels,
           autopct='%1.2f%%',colors=my_colors)
    ax.axis('equal')
    
    plt.title(mtitle)
    return fig

def generate_dhmo(df,dm,pp):
    print dm
    df_elected = df[(df.active==1) & (df.dhmos==dm)]
    df_elected_grouped = df_elected.groupby('metrhsh',as_index=False)
    dfegs = df_elected_grouped.aggregate(np.sum)
    pg = create_pdf(dfegs,dm,dfegs.metrhsh)
    pp.savefig(pg)

def generate_ipopsifio(df,dm,pp):
    print dm
    df_elected = df[(df.active==1) & (df.metrhsh==dm)]
    df_elected_grouped = df_elected.groupby('dhmos',as_index=False)
    dfegs = df_elected_grouped.aggregate(np.sum)
    pg = create_pdf(dfegs,dm,dfegs.dhmos)
    pp.savefig(pg)

pp = PdfPages('ENERGOI.pdf') 
#ELECTED PRESENTATION
df_elected = df[(df.active==1)]
df_elected_grouped = df_elected.groupby('metrhsh',as_index=False)
dfegs = df_elected_grouped.aggregate(np.sum)
p1 = create_pdf(dfegs,u"ΝΟΜΟΣ",dfegs.metrhsh)
pp.savefig(p1)

df_elected = df[(df.active==1)&(df.ekl_per==u"Α")]
df_elected_grouped = df_elected.groupby('metrhsh',as_index=False)
dfegs = df_elected_grouped.aggregate(np.sum)
p2 = create_pdf(dfegs,u"Α ΠΕΡΙΦΕΡΕΙΑ",dfegs.metrhsh)
pp.savefig(p2)

df_elected = df[(df.active==1)&(df.ekl_per==u"Β")]
df_elected_grouped = df_elected.groupby('metrhsh',as_index=False)
dfegs = df_elected_grouped.aggregate(np.sum)
p3 = create_pdf(dfegs,u"Β ΠΕΡΙΦΕΡΕΙΑ",dfegs.metrhsh)
pp.savefig(p3)

#Generate Dhmoi
dhmoi = df.groupby('dhmos',as_index=False)['arithmos'].sum()
for index,row in dhmoi.iterrows():
    generate_dhmo(df, row['dhmos'],pp)

#Generate Ipopsifioi
df_elected = df[(df.active==1)]
ipopsifioi = df_elected.groupby('metrhsh',as_index=False)['arithmos'].sum()
for index,row in ipopsifioi.iterrows():
    generate_ipopsifio(df, row['metrhsh'],pp)

pp.close()

    