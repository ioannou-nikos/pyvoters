# -*- coding: utf-8 -*-
"""
Ioannou Nikos

Try to make a generic plotting tool
"""

#Import the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.backends.backend_pdf import PdfPages

#MATPLOT PARAMETERS FOR DRAWING
matplotlib.rcParams['font.family'] = 'DejaVu Sans'
matplotlib.rcParams['axes.titlesize'] = 16.0
matplotlib.rcParams['xtick.labelsize'] = 10.0
my_colors = plt.cm.Set1(np.linspace(0,1,25)) #25 Color map

#GLOBAL READ ONLY VARIABLES
ACTIVE = 0
ELECTED = 1
ISTOTAL = None

def filereader():
    """Read the data file into a dataframe"""
    df = pd.read_csv("METRHSH_FULL.txt",sep=";",encoding="utf-8",header=0,
                     names=["ekl_per","dhmos","et","diamerisma","metrhsh",
                             "arithmos","elected","active","istotal"])
    return df
    
def create_pdf(df,mtitle,mlabels):
    fig = plt.figure(figsize=(20,20))
    ax = fig.add_subplot(111)
    ax.pie(df.arithmos,labels=mlabels,
           autopct='%1.2f%%',colors=my_colors)
    ax.axis('equal')    
    plt.title(mtitle)
    return fig

def generate_dhmo_active(df,dm,pp):
    print dm
    dfe = df[(df.active==ACTIVE) & (df.dhmos==dm)]
    dfeg = dfe.groupby('metrhsh',as_index=False)
    dfegs = dfeg.aggregate(np.sum)
    pg = create_pdf(dfegs,dm,dfegs.metrhsh)
    pp.savefig(pg)

def generate_dhmo_elected(df,dm,pp):
    print dm
    dfe = df[(df.elected==ELECTED) & (df.dhmos==dm)]
    dfeg = dfe.groupby('metrhsh',as_index=False)
    dfegs = dfeg.aggregate(np.sum)
    pg = create_pdf(dfegs,dm,dfegs.metrhsh)
    pp.savefig(pg)

def generate_ipopsifio_active(df,dm,pp):
    print dm
    dfe = df[(df.active==ACTIVE) & (df.metrhsh==dm)]
    dfeg = dfe.groupby('dhmos',as_index=False)
    dfegs = dfeg.aggregate(np.sum)
    pg = create_pdf(dfegs,dm,dfegs.dhmos)
    pp.savefig(pg)

def generate_ipopsifio_elected(df,dm,pp):
    print dm
    dfe = df[(df.elected==ELECTED) & (df.metrhsh==dm)]
    dfeg = dfe.groupby('dhmos',as_index=False)
    dfegs = dfeg.aggregate(np.sum)
    pg = create_pdf(dfegs,dm,dfegs.dhmos)
    pp.savefig(pg)

def generate_general_active(df,mtitle,pp,ekl_per):
	if ekl_per == 1:
		dfe = df[(df.active==ACTIVE)&(df.ekl_per==u"Α")]
	elif ekl_per == 2:
		dfe = df[(df.active==ACTIVE)&(df.ekl_per==u"Β")]
	else
		dfe = df[(df.ACTIVE==1)]
    dfeg = dfe.groupby('metrhsh',as_index=False)
    dfegs = dfeg.aggregate(np.sum)
    pg = create_pdf(dfegs,u"ΝΟΜΟΣ",dfegs.metrhsh)
    pp.savefig(p1)

def generate_general_elected(df,mtitle,pp,ekl_per):
	if ekl_per == 1:
		dfe = df[(df.elected==ELECTED)&(df.ekl_per==u"Α")]
	elif ekl_per == 2:
		dfe = df[(df.elected==ELECTED)&(df.ekl_per==u"Β")]
	else
		dfe = df[(df.elected==1)]
    dfeg = dfe.groupby('metrhsh',as_index=False)
    dfegs = dfeg.aggregate(np.sum)
    pg = create_pdf(dfegs,u"ΝΟΜΟΣ",dfegs.metrhsh)
    pp.savefig(p1)

def all_general_elected(df,p):
    generate_general_elected(df,u"ΝΟΜΟΣ",pp=p)
	generate_general_elected(df,u"Α ΠΕΡΙΦΕΡΕΙΑ",1,pp=p)
	generate_general_elected(df,u"Β ΠΕΡΙΦΕΡΕΙΑ",2,pp=p)
	
def all_general_active(df,p):
    generate_general_active(df,u"ΝΟΜΟΣ",pp=p)
	generate_general_active(df,u"Α ΠΕΡΙΦΕΡΕΙΑ",1,pp=p)
	generate_general_active(df,u"Β ΠΕΡΙΦΕΡΕΙΑ",2,pp=p)

if __name__ == '__main__':
    pp = PdfPages('presentation.pdf') 
	df = filereader()
	generate_general_elected(df,pp)
	#Generate Dhmoi
	dhmoi = df.groupby('dhmos',as_index=False)['arithmos'].sum()
	for index,row in dhmoi.iterrows():
		generate_dhmo_elected(df, row['dhmos'],pp)
	#Generate Ipopsifioi
	df_elected = df[(df.active==1)]
	ipopsifioi = df_elected.groupby('metrhsh',as_index=False)['arithmos'].sum()
	for index,row in ipopsifioi.iterrows():
		generate_ipopsifio(df, row['metrhsh'],pp)
	pp.close()
