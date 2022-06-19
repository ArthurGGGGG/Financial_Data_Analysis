#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import glob
import os


# In[ ]:


mydir = os.getcwd()

#Update listdir() to specify folder.
for file in os.listdir('Alphabet Inc (GOOG)'):
    if file.endswith(".xlsx"):
        print(os.path.join(file))


# In[ ]:


#file_list = glob.glob("Alphabet Inc (GOOG)/*.xlsx")
#sorted(file_list)


# In[ ]:


## SEE OTHER SOURCE CODE IN NOTES


# In[ ]:


result = []

#Update listdir() to specify folder.
for file in os.listdir('Alphabet Inc (GOOG)/'):
    if file.endswith(".xlsx"):
        result.append(os.path.join(file))
        #print(os.path.join(file))

sorted_list = sorted(result)
#sorted_list = sorted_list[:-1]


# In[ ]:


length = len(sorted_list)

for i in range(length):
    input_date = sorted_list[i]
    
    #Update url() to specify folder.
    url = 'Alphabet Inc (GOOG)/' + input_date
    file = pd.read_excel(url)
    
    s_0 = pd.read_excel(url, sheet_name=0)
    s_1 = pd.read_excel(url, sheet_name=1)
    s_2 = pd.read_excel(url, sheet_name=2)
    s_3 = pd.read_excel(url, sheet_name=3)
    s_4 = pd.read_excel(url, sheet_name=4)
    s_5 = pd.read_excel(url, sheet_name=5)
    s_6 = pd.read_excel(url, sheet_name=6)
    s_7 = pd.read_excel(url, sheet_name=7)

    colname = s_0.columns[0]
    #print(colname)
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        print('CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions')
        BS = s_0
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions')
        CSI = s_0
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions')
        CSCF = s_0
    
    colname = s_1.columns[0]
    #print(colname)
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        print('CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions')
        BS = s_1
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions')
        CSI = s_1
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions')
        CSCF = s_1
    
    colname = s_2.columns[0]
    #print(colname)
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        print('CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions')
        BS = s_2
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions')
        CSI = s_2
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions')
        CSCF = s_2
    
    colname = s_3.columns[0]
    #print(colname)
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        print('CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions')
        BS = s_3
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions')
        CSI = s_3
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions')
        CSCF = s_3
    
    colname = s_4.columns[0]
    #print(colname)
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        print('CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions')
        BS = s_4
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions')
        CSI = s_4
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions')
        CSCF = s_4
    
    colname = s_5.columns[0]
    #print(colname)
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        print('CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions')
        BS = s_5
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions')
        CSI = s_5
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions')
        CSCF = s_5
    
    colname = s_6.columns[0]
    #print(colname)
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        print('CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions')
        BS = s_6
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions')
        CSI = s_6
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions')
        CSCF = s_6
        
    colname = s_7.columns[0]
    #print(colname)
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        print('CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions')
        BS = s_7
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions')
        CSI = s_7
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        print('CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions')
        CSCF = s_7
        
       
    #print(input_date[:-5])

    
    BS.to_csv(url[:-5] + '-0.csv', index = False)
    CSI.to_csv(url[:-5] + '-1.csv', index = False)
    CSCF.to_csv(url[:-5] + '-2.csv', index = False)


# In[ ]:




