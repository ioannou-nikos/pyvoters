#Read the data
df = read.csv("METRHSH.txt",header=TRUE,sep=";",quote="",encoding="UTF-8")

#install the package reshape
install.packages('reshape')

#load reshape
library(reshape)

#Create a dataframe from dimos ipopsifios and arithmos
df_dimos = df[,c("X.U.FEFF.DIMOS","METRHSH","ARITHMOS")]

#Use cast to move dhmoi into columns
cast(df_dimos,X.U.FEFF.DIMOS ~ METRHSH)
