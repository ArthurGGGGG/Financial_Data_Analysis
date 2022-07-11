#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install keras

import pandas as pd
from heading import *
from sklearn.linear_model import LinearRegression


# In[ ]:


df = pd.read_csv("../Alphabet Inc (GOOG)/S5 _ CSV z.##/P2 _ Correlation.csv")
df.set_index('Unnamed: 0')
N = 6
df = df.iloc[: , :-N]

AdjClose_Cor = df.loc[df['Unnamed: 0'] == 'Adj Close']
AdjClose_Cor = AdjClose_Cor.reset_index()
AdjClose_Cor = AdjClose_Cor.T
AdjClose_Cor = AdjClose_Cor.iloc[2: , :]
AdjClose_Cor

# HIGHLY POSITIVELY CORRELATED
AdjClose_PC = AdjClose_Cor.loc[(AdjClose_Cor[0] >= 0.7) & (AdjClose_Cor[0] <= 1.0)]
print(AdjClose_PC)
AdjClose_PC_List = AdjClose_PC.index.values.tolist()
AdjClose_PC_List.append('Adj Close')
print(AdjClose_PC_List)

# HIGHLY NEGATIVELY CORRELATED
AdjClose_NC = AdjClose_Cor.loc[(AdjClose_Cor[0] >= -1.0) & (AdjClose_Cor[0] <= -0.7)]
print(AdjClose_NC)
AdjClose_NC_List = AdjClose_NC.index.values.tolist()
AdjClose_NC_List.append('Adj Close')
print(AdjClose_NC_List)

#AdjClose_PC = AdjClose_Cor[0].between(0.7, 1.0, inclusive=True)
#AdjClose_PC
#AdjClose_PC = AdjClose_PC.reset_index()
#AdjClose_PC.loc[AdjClose_PC[0] == 'True']
#AdjClose_NC = AdjClose_Cor[0].between(-1.0, -0.7, inclusive=True)

#AdjClose_Cor[~AdjClose_Cor['values'].between('2017-03-02', '2017-03-05', inclusive=False)]
#AdjClose_Cor = AdjClose_Cor[AdjClose_Cor["AdjClose"] > 0.7]
#df.loc[:, df.columns[(df.loc['Adj Close'] > 0.7)]]
#df_0 = (AdjClose_Cor['Adj Close'] >= -0.5) & (AdjClose_Cor['Adj Close'] < 0.5)

# TO DO!
df = pd.read_csv("../Alphabet Inc (GOOG)/S5 _ CSV z.##/P2 _ Correlation.csv")
#print(df)
PC_List_Ind = []
NC_List_Ind = []
#print(df)
length_PC = len(AdjClose_PC_List)
length_NC = len(AdjClose_NC_List)

for i in range(length_PC):
    AdjClose_PC_List_Ind = df.index[df['Unnamed: 0'] == AdjClose_PC_List[i]].tolist()
    #print(AdjClose_PC_List_Ind)
    PC_List_Ind.append(AdjClose_PC_List_Ind)

for i in range(length_NC):
    AdjClose_NC_List_Ind = df.index[df['Unnamed: 0'] == AdjClose_NC_List[i]].tolist()
    #print(AdjClose_PC_List_Ind)
    NC_List_Ind.append(AdjClose_NC_List_Ind)
    
#print('Index of Financial Ratio HIGHLY POSITIVELY CORRELATED to "Close" Price')
#print(PC_List_Ind)
#my_PC_str = ''.join(map(str, PC_List_Ind))
#print(my_PC_str)
#PC_List_Ind_0 = print(sum(PC_List_Ind, []))
#PC_List_Ind_0

#print('Index of Financial Ratio HIGHLY NEGATIVELY CORRELATED to "Close" Price')
#print(NC_List_Ind)
#my_NC_str = ''.join(map(str, NC_List_Ind))
#print(my_NC_str)
#NC_List_Ind_0 = print(sum(NC_List_Ind, []))
#NC_List_Ind_0

##

# ADD '1' AS INT TO ALL ELEMENTS IN LIST (SHIFT IN INDEX(n))
##
length = len(PC_List_Ind)
#print(length)
PC_List_Ind_0 = []

for i in range(length):
    index_int = str(PC_List_Ind[i])
    #print(index_int)
    index_int = index_int.replace("[", "")
    index_int = index_int.replace("]", "")
    index_int = int(index_int)
    index_int = index_int + 1
    PC_List_Ind_0.append(index_int)
    #int(index_int)

#print(PC_List_Ind_0)

length = len(NC_List_Ind)
#print(length)
NC_List_Ind_0 = []

for i in range(length):
    index_int = str(NC_List_Ind[i])
    #print(index_int)
    index_int = index_int.replace("[", "") ## CHANGE TO INT
    index_int = index_int.replace("]", "") ## CHANGE TO INT
    index_int = int(index_int) ## CHANGE TO INT
    index_int = index_int + 1 ## ADD '1' AS INT TO ALL ELEMENTS IN LIST (SHIFT RIGHT IN INDEX(n)) _ SEE "aima-data/R_DF_Analysis.csv"
    NC_List_Ind_0.append(index_int) ## APPEND TO NEW INT_LIST
    #int(index_int)

#print(NC_List_Ind_0)


# In[ ]:


df = pd.read_csv("../Alphabet Inc (GOOG)/Alphabet-DF-Analysis.csv", header = None)
#df = pd.read_csv("Alphabet-DF-Analysis.csv", header = None, index_col = None, usecols = None)
df.drop(columns=df.columns[0], axis=1, inplace=True)
df = df.iloc[1: , :]
df.to_csv("aima-data/R_DF_Analysis.csv", index = False, header = None)
#df[1] = df[1].str.replace('\d+', '')
df


# In[ ]:


# ONLY SELECT COLUMNS THAT ARE HIGHLY CORRELATED TO AdjClose
#THIS MEANS [ -1 < X < -0.7 ] && [ 0.7 < X < 1 ]
df_0 = df[PC_List_Ind_0]
df_0.to_csv("aima-data/R_DF_Analysis_PC.csv", index = False, header = None)
df_0.to_csv("../Alphabet Inc (GOOG)/S5 _ CSV z.##/R_DF_Analysis_PC.csv", index = False, header = None)
#df_0


# In[ ]:


df_0 = df[NC_List_Ind_0]
df_0.to_csv("aima-data/R_DF_Analysis_NC.csv", index = False, header = None)
df_0.to_csv("../Alphabet Inc (GOOG)/S5 _ CSV z.##/R_DF_Analysis_NC.csv", index = False, header = None)
#df_0


# In[ ]:


### TO DO ###

goog_PC = DataSet(name="R_DF_Analysis_PC", target='Adj Close', attr_names=AdjClose_PC_List)
#house = DataSet(name="HousingData", target='HousePrice', attr_names='HouseAge HouseSize HousePrice')

print(goog_PC.examples[0])
print(goog_PC.examples[:3])

train_data = []
train_label = []
test_data = []
test_label = []

train_data, train_label, test_data, test_label = seperate_train_and_test_data(goog_PC.examples, (length_PC/1.3))

#

futureSample_data =[]
futureSample_label = []
futureSample_data= test_data[-2:]
futureSample_label= test_label[-2:]

test_data =test_data[:-2]
test_label =test_label[:-2]

lr = LinearRegression()

lr.fit(train_data,train_label)

train_accuracy= lr.score(train_data, train_label)
print (train_accuracy)

# TEST ACCURACY
test_accuracy= lr.score(test_data, test_label)
print (test_accuracy)

for x in futureSample_data:
    print(x,lr.predict([x]))


# In[ ]:


### SAVE OUTPUTS FOR TEST ACC >= 0.999 __ LOOP OVER

n = 0
ls = []

while n != 20:
    ##
    goog_PC = DataSet(name="R_DF_Analysis_PC", target='Adj Close', attr_names=AdjClose_PC_List)
    #
    train_data = []
    train_label = []
    test_data = []
    test_label = []
    #
    train_data, train_label, test_data, test_label = seperate_train_and_test_data(goog_PC.examples, (length_PC/1.3))
    #
    futureSample_data =[]
    futureSample_label = []
    futureSample_data= test_data[-2:]
    futureSample_label= test_label[-2:]
    #
    test_data =test_data[:-2]
    test_label =test_label[:-2]
    #
    lr = LinearRegression()
    lr.fit(train_data,train_label)
    #
    train_accuracy= lr.score(train_data, train_label)
    test_accuracy= lr.score(test_data, test_label)
    #
    #for x in futureSample_data:
        #print(x,lr.predict([x]))
    ##
    if test_accuracy >= 0.9995:
        print("T_" + str(n))
        print(test_accuracy)
        #for x in futureSample_data:
            #print(x,lr.predict([x]))
        print(lr.predict([x]))
        ls.append(int(lr.predict([x])))
        #print(ls)
        # SAVE [print(x,lr.predict([x]))]
        n = n + 1

print(ls)


# In[ ]:


# PLOT LR_00 RESULTS
# USE MACHINE LEARNING, ITERATIONS OVER TRAINING && TESTING


# In[ ]:


import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# INITIAL DATAFRAME
df = pd.read_csv("../Alphabet Inc (GOOG)/Alphabet-DF-Analysis.csv", header = 0)
df = df[['Financial Ratio', 'Adj Close']]
#print(df)

# APPEND NEW PREDICTED VALUES (LATER USED TO VERIFY CHANGES IN BEHAVIOUR OF BEST-FIT LINE(S)) /DIRECTION
last_date_index = int(len(ls)+1)
last_date_str = str(df.iloc[last_date_index, df.columns.get_loc("Financial Ratio")])

for i in range(len(ls)):
    df2 = pd.DataFrame({'Financial Ratio': [last_date_str], 'Adj Close' : [ls[i]]})
    #print(df2)
    df = pd.concat([df, df2], ignore_index = True, axis = 0)   
#print(df)

# Calculate equation of linear best fit line python.

#print(df.dtypes)
df['Financial Ratio']= pd.to_datetime(df['Financial Ratio'])
df = df.astype({"Adj Close": int}, errors='raise') 
#print(df.dtypes)
# Method:1 USING df.plot.scatter()
df.plot.scatter(x = 'Financial Ratio', y = 'Adj Close')
# (...)


# In[ ]:


# Method:2 USING 'matplotlib'
import matplotlib.pyplot as plt
#plt.scatter(df.x, df.y) # ISSUE 
# https://pythonguides.com/matplotlib-best-fit-line/
# (...)


# In[ ]:




