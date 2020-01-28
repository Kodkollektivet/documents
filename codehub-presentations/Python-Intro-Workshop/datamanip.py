import pandas as pd

df =  pd.read_csv("Names.cvs",header=None,index_col=0,names=["Kommunkod","Namn"])
df2 = pd.read_csv("Pop.cvs",header=None,index_col=0,names=["Kommunkod","Year","TotPop"])
df3 = pd.read_csv("Res.cvs",header=None,index_col=0,names=["Kommunkod","Year","Result"])

total = df.join(df2,how="left").join(df3,on="Kommunkod",how="inner",rsuffix="_drop")

total[["TotPop","Result"]].to_csv("Kommundata.csv")
