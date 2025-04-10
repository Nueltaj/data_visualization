"""Understanding pandaa"""
import pandas as pd
import numpy as np

df = pd.read_csv("understanding_panda/Carbon_(CO2)_Emissions_by_Country.csv")
#to output the first 5 rows
print(df.head())
#to describe a dataset
print(df.describe())
#to know the frequency of a value in a specified column
#print(df["Country"].value_counts())
#to remove a row where data is not correctly displayed
df.dropna()#it only displays a data frame with no Nan
#to create a data frame with no Nan
df.dropna(inplace=True)
#or
df2=df.dropna()
#to create a new column
df["Megatons of Co2"]=df["Kilotons of Co2"]*100
print(df.head())
#to know if a file contains nan
df["Kilotons of Co2"].isna()#displays True if na exist,False if it doesn't
#creating a new column that contains Nan and a value
mask =df["Kilotons of Co2"].isna()
#if x i true, assigns a value in x to the new column,else asigns the y value to
#the new column
df["text value"]=np.where(mask,df["Kilotons of Co2"],np.nan)

#filling up the text value column with a value
#df["text value"]=df["text value"].bfill()
df["text value"] = df["text value"].fillna("Unknown")
print(df.head)