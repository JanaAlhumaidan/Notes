#Laibrary: 
import pandas as pd
import matplotlib.pyplot as plt #if needed

#2 main Data types: 
#Series:
x = pd.Series(["x", "y", "z"])
# dataFarme (2D)
x = pd.DataFrame({"column name1": seriesName, "column name2": seriesName})

#importing Data
x = pd.read_csv(r"filePath")

# Exporting a dataframe
x.to_csv("y", index=False) # y = the name of the new file

#Describing data  ---- with () for functions    without () for Attributes
x.dtype #prints the dtype of each column
x["column name"].dtype #prints the dtype of the chosen column
x.columns #shows you the column's names
x.index 
x.describe() #prints out the count, mean, std, min of the int columns
x.info() #prints some info about the column's data
x.mean()
x.sum()
x["column name"].sum() #if I want a specific column
len(x) #no. of rows

#Viewing and Selecting
x.head() #prints the first 5 rows 
x.head(y) # y = number >> if I want a specific no. of rows
x.tail() #last 4 rows
x.iloc[3] # .iloc refers to position
x.loc[3] # .loc refers to index
x.columnName #prints the data in this column >> will not work if the column name have a space
x["column name"] #prints the data in this column
x[x["column name"] == "object"] #prints the rows that has the chosen object in the chosen column
x[x["column name"] > 100000] #prints the rows that goes with the rule in the chosen column
pd.crosstab(x["column name1"], x["column name2"])

#changing the dtype
x['column name'] = x['column name'].astype(str)
x["column name"] = x["column name"].str.replace('[\$\,\.]', '') #replacing a char in a column
x["column name"] = x["column name"].str.replace('[\$\,\.]', '').astype(int) #replacing & changing the dtype

#Graphs
x.plot()
x.hist()
x.plot().bar()
x.plot().bar(stacked=True)
x["column name"].plot() # if I want a specific column

#Manipulating data
x["column name"] = x["column name"].str.lower() #lower case