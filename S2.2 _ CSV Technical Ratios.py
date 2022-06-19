#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd


# In[ ]:


#file = pd.read_csv('-Alphabet.csv')


# In[ ]:


_input = input()
date_input = _input + '-Alphabet.csv'
file = pd.read_csv(date_input)


# In[ ]:


file = file.drop(file.columns[0], axis=1)
file


# In[ ]:


start_date = file.iloc[0][0]
#print(start_date)
end_date = file.iloc[-1][0]
#print(end_date)

#s = pd.date_range(start_date, end_date, freq='D').to_series()
#s_0 = s.dt.dayofweek
#s_1 = pd.Series(s_0).array
#s_2 = s_0.to_frame()
#print(s_2)
#s_2[0]


file['Date'] = pd.to_datetime(file['Date'])
file_0 = file['Date'].dt.day_name()
file_1 = file.merge(file_0.rename('Weekday'), left_index=True, right_index=True)
#file['Date'].dt.day_name()


# In[ ]:


file_1


# In[ ]:


end_week = file_1.loc[file_1['Weekday'] == 'Friday']


# In[ ]:


col_one_list = end_week['Date'].tolist()


# In[ ]:


#file_1['Adj.Avg'] = file_1.apply(lambda _: '', axis=1)

#Adj Close

#file_1['Std.Dev'] = file_1.apply(lambda _: '', axis=1)
#file_1['CV'] = file_1.apply(lambda _: '', axis=1)

#High Low Volatility

#file_1['H-L_Std.Dev'] = file_1.apply(lambda _: '', axis=1)
#file_1['H-L_CV'] = file_1.apply(lambda _: '', axis=1)
#file_1['H-L_Diff'] = file_1.apply(lambda _: '', axis=1)

#Open Close Volatility

#file_1['O-C_Std.Dev'] = file_1.apply(lambda _: '', axis=1)
#file_1['O-C_CV'] = file_1.apply(lambda _: '', axis=1)
#file_1['O-C_Diff'] = file_1.apply(lambda _: '', axis=1)

#Normalization

#file_1['Norm'] = file_1.apply(lambda _: '', axis=1)


# In[ ]:


file_2 = file_1.set_index('Date')
    
length = len(col_one_list)
for i in range(length):
    print(file_2.at[col_one_list[i], 'Adj Close'])
    print(file_2.index.get_loc(col_one_list[i]))

    if file_2.index.get_loc(col_one_list[i]) >=5:
        print("Enough data to calculate past week's Adj.Avg")
        
##################           
        
        
        
        
        
        
        AdjClose = file_2.at[col_one_list[i], 'Adj Close']
        print(AdjClose)
        Index = file_2.index.get_loc(col_one_list[i])
        print(Index)

        index1 = int(Index)-1
        index2 = int(Index)-2
        index3 = int(Index)-3
        index4 = int(Index)-4
        index_ls = list(file_2.index)
        print(index_ls[index1])

        #ADJ CLOSE VALUES N-4
        V0 = file_2.at[index_ls[index1], 'Adj Close']
        V1 = file_2.at[index_ls[index2], 'Adj Close']
        V2 = file_2.at[index_ls[index3], 'Adj Close']
        V3 = file_2.at[index_ls[index4], 'Adj Close']

        A1 = (AdjClose + V0 + V1 + V2 + V3) / 5
        N_days = 1/(5-1)
        A2 = N_days * ((AdjClose - A1)**2 + (V0 - A1)**2 + (V1 - A1)**2 + (V2 - A1)**2 + (V3 - A1)**2)
        A3 = (A2 / A1) * 100

        #LOW HIGH VALUES N-4
        High = file_2.at[col_one_list[i], 'High']
        V5 = file_2.at[index_ls[index1], 'High']
        V6 = file_2.at[index_ls[index2], 'High']
        V7 = file_2.at[index_ls[index3], 'High']
        V8 = file_2.at[index_ls[index4], 'High']

        Low = file_2.at[col_one_list[i], 'Low']
        V9 = file_2.at[index_ls[index1], 'Low']
        V10 = file_2.at[index_ls[index2], 'Low']
        V11 = file_2.at[index_ls[index3], 'Low']
        V12 = file_2.at[index_ls[index4], 'Low']

        A4 = N_days * ((max(High, V5, V6, V7, V8) - min(Low, V9, V10, V11, V12))**2)
        A5 = (A4 / A1) * 100
        A6 = (A1 - min(Low, V9, V10, V11, V12))/(max(High, V5, V6, V7, V8) - min(Low, V9, V10, V11, V12))

        #OPEN CLOSE VALUES N-4
        Open = file_2.at[col_one_list[i], 'Open']
        V13 = file_2.at[index_ls[index1], 'Open']
        V14 = file_2.at[index_ls[index2], 'Open']
        V15 = file_2.at[index_ls[index3], 'Open']
        V16 = file_2.at[index_ls[index4], 'Open']

        Close = file_2.at[col_one_list[i], 'Close']
        V17 = file_2.at[index_ls[index1], 'Close']
        V18 = file_2.at[index_ls[index2], 'Close']
        V19 = file_2.at[index_ls[index3], 'Close']
        V20 = file_2.at[index_ls[index4], 'Close']

        A7 = N_days * ((max(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20) - min(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20))**2)
        A8 = (A7 / A1) * 100
        A9 = (A1 - min(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20))/(max(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20) - min(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20))

        A10 = (A1 - min(AdjClose, V0, V1, V2, V3))/(max(AdjClose, V0, V1, V2, V3) - min(AdjClose, V0, V1, V2, V3))


        file_2.at[col_one_list[i], 'Adj.Avg'] = A1
        file_2.at[col_one_list[i], 'Std.Dev'] = A2
        file_2.at[col_one_list[i], 'CV'] = A3
        file_2.at[col_one_list[i], 'H-L-Std.Dev'] = A4
        file_2.at[col_one_list[i], 'H-L-CV'] = A5
        file_2.at[col_one_list[i], 'H-L-Diff.'] = A6
        file_2.at[col_one_list[i], 'O-C-Std.Dev'] = A7
        file_2.at[col_one_list[i], 'O-C-CV'] = A8
        file_2.at[col_one_list[i], 'O-C-Diff.'] = A9
        file_2.at[col_one_list[i], 'Norm.'] = A10
        
        
        
        
        
        
        
##################        
        
    else:
        print("Not enough data to calculate past week's Adj.Avg")
        

        
file_2 = file_2.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume', 'Weekday'])


# In[ ]:


file_2['Adj.Avg'].replace('', np.nan, inplace=True)
file_2 = file_2.dropna(subset=['Adj.Avg'])
file_2.to_csv(_input + "-Ratio-TF.csv")


# In[ ]:




