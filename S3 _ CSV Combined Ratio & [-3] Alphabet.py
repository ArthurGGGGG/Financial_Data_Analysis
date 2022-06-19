#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## WEEK 4

# https://canvas.uts.edu.au/courses/18711/pages/online-workshop-schedule


# In[ ]:


import os
import pandas as pd

mydir = os.getcwd()

result = []
#Adjust directory to specify folder.
#for file in os.listdir('Desktop (alt)/Alphabet Inc (GOOG)/'):
for file in os.listdir('Alphabet Inc (GOOG)/'):
    if file.endswith("-Ratio-DF.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_0 = sorted(result)
sorted_list_0


# In[ ]:





# In[ ]:


import os
import pandas as pd
import numpy as np

mydir = os.getcwd()

result = []
for file in os.listdir('Alphabet Inc (GOOG)/'):
    if file.endswith("-Ratio-DF.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_0 = sorted(result)
sorted_list_0


#input_date = sorted_list_0[0][:-13]
#print(input_date)


length = len(sorted_list_0)
##### ls = []
##### Input 1 [-3m] prior to the first date. Used for initial ls[0] analysis
ls = ['2016-03-31']

for i in range(length):
    input_date = sorted_list_0[i][:-13]
    #print(input_date)

    ls.append(input_date)

ls


# In[ ]:


file = pd.read_csv('Alphabet Inc (GOOG)/Alphabet Inc.csv')

## TRY STATEMENT FOR date_input-29 -28 -27 -26...
date_prefix = ls[0][:-2]

date_ls = ["31", "30", "29", "28"]

upd_date_0 = date_prefix + date_ls[0]
upd_date_1 = date_prefix + date_ls[1]
upd_date_2 = date_prefix + date_ls[2]
upd_date_3 = date_prefix + date_ls[3]
    
print(upd_date_0)
    
print('\n')

if upd_date_0 in file.values:
    col_one_arr_P = file[file['Date'].str.contains(upd_date_0)].to_numpy()
    print(upd_date_0 + " exists.")
    index = file[file['Date'] == upd_date_1].index[0]
else:
    if upd_date_1 in file.values:
        col_one_arr_P = file[file['Date'].str.contains(upd_date_1)].to_numpy()
        print("Month finishes in -30")
        #index = file.loc[file['Date']==upd_date_1]
        #index = file[file['Date'] == upd_date_1].index[0]
        index = file[file['Date'] == upd_date_1].index.to_numpy()
    else:
        if upd_date_2 in file.values:
            col_one_arr_P = file[file['Date'].str.contains(upd_date_2)].to_numpy()
            print("Month finishes in -29")
            index = file[file['Date'] == upd_date_1].index[0]
        else:
            if upd_date_3 in file.values:
                col_one_arr_P = file[file['Date'].str.contains(upd_date_3)].to_numpy()
                print("Month finishes in -28")
                index = file[file['Date'] == upd_date_1].index[0]


print(col_one_arr_P)                
#update_df = file.drop([file.index[0:570], file.index[634:]])
#file.drop([570 , 634:], inplace=True)
df_age_negative = file[ file['Date'] < ls[0] ] # Step 1
df = file.drop(df_age_negative.index, axis=0) # Step 2

df_age_positive = file[ file['Date'] > ls[1] ]
df = df.drop(df_age_positive.index, axis=0)
df


# In[ ]:


# ONLY SPECIFIC TO ALPHABET COMPANY (t-1)

length = len(sorted_list_0)

for i in range(length):

    df_age_negative = file[ file['Date'] < ls[i] ] # Step 1
    df = file.drop(df_age_negative.index, axis=0) # Step 2

    df_age_positive = file[ file['Date'] > ls[i+1] ]
    df = df.drop(df_age_positive.index, axis=0)
    
    
    end_date = ls[i+1]
    df.to_csv('Alphabet Inc (GOOG)/' + end_date + "-Alphabet.csv")


# In[ ]:


### USE METHOD HERE-ABOVE
### IGNORE METHODS PRESENTED BELOW


# In[ ]:





# In[ ]:


#file = pd.read_csv('Alphabet Inc.csv')

## TRY STATEMENT FOR date_input-29 -28 -27 -26...

#result = []

#for i in range(length):
    #input_date = sorted_list_0[i][:-13]
    
    #date_prefix = ls[i][:-2]

    #date_ls = ["31", "30", "29", "28"]

    #upd_date_0 = date_prefix + date_ls[0]
    #upd_date_1 = date_prefix + date_ls[1]
    #upd_date_2 = date_prefix + date_ls[2]
    #upd_date_3 = date_prefix + date_ls[3]

    #print(date_prefix)
    #print(upd_date_0)
    
    
    
    #if upd_date_0 in file.values:
        #col_one_arr_P = file[file['Date'].str.contains(upd_date_0)].to_numpy()
        #print(upd_date_0 + " exists.")
        #index = file[file['Date'] == upd_date_0].index[0]
        #result.append(index)
        
        #print('\n')
        
    #else:
        #if upd_date_1 in file.values:
            #col_one_arr_P = file[file['Date'].str.contains(upd_date_1)].to_numpy()
            #print("Month finishes in -30")
            #index = file.loc[file['Date']==upd_date_1]
            #index = file[file['Date'] == upd_date_1].index[0]
            #index = file[file['Date'] == upd_date_1].index.to_numpy()
            #print(index)
            #result.append(index)
            
            #print('\n')
            
        #else:
            #if upd_date_2 in file.values:
                #col_one_arr_P = file[file['Date'].str.contains(upd_date_2)].to_numpy()
                #print("Month finishes in -29")
                #index = file[file['Date'] == upd_date_2].index[0]
                #result.append(index)
                
                #print('\n')
                
            #else:
                #if upd_date_3 in file.values:
                    #col_one_arr_P = file[file['Date'].str.contains(upd_date_3)].to_numpy()
                    #print("Month finishes in -28")
                    #index = file[file['Date'] == upd_date_3].index[0]
                    #result.append(index)
                    
                    #print('\n')
                    

#print(result)


# In[ ]:





# In[ ]:


#combined_csv = pd.concat([pd.read_csv('Alphabet Inc (GOOG)/' + f) for f in sorted_list_0 ])
#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')


# In[ ]:


file_0 = pd.read_csv('Alphabet Inc (GOOG)/' + sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)

title = sorted_list_0[0][:-13]
file_0 = file_0.set_axis(['Financial Ratio', title], axis=1, inplace=False)
file_0


# In[ ]:


print(sorted_list_0[1])
file_1 = pd.read_csv('Alphabet Inc (GOOG)/' + sorted_list_0[1])
file_1 = file_1.drop(file_1.columns[0], axis=1)
file_1 = file_1.drop(file_1.columns[0], axis=1)

title = sorted_list_0[1][:-13]
file_1.rename({'Financial Ratio /unit': title}, axis=1, inplace=True)
print(file_1)

#file_2 = file_0.append(file_1)
##file_2[title] = file_2[title].shift(-25)
#file_2 = file_2[file_2['Financial Ratio'].notna()]
#print(file_2)
file_0 = file_0.join(file_1)
print(file_0)


# In[ ]:


print(sorted_list_0[2])
file_3 = pd.read_csv('Alphabet Inc (GOOG)/' + sorted_list_0[2])
file_3 = file_3.drop(file_3.columns[0], axis=1)
file_3 = file_3.drop(file_3.columns[0], axis=1)

title = sorted_list_0[2][:-13]
print(file_3)

#file_2 = file_0.append(file_1)
##file_2[title] = file_2[title].shift(-25)
#file_2 = file_2[file_2['Financial Ratio'].notna()]
#print(file_2)
file_0 = file_0.join(file_3)
print(file_0)


# In[ ]:





# In[ ]:


#print(sorted_list_0[2])
#file_3 = pd.read_csv('Desktop (alt)/Alphabet Inc (GOOG)/' + sorted_list_0[2])
#file_3 = file_3.drop(file_3.columns[0], axis=1)
#file_3 = file_3.drop(file_3.columns[0], axis=1)

#title = sorted_list_0[2][:-13]
#file_3.rename({'Financial Ratio /unit': title}, axis=1, inplace=True)
#print(file_3)

#file_4 = file_0.append(file_3)
#file_4[title] = file_4[title].shift(-25)
#file_4 = file_4[file_4['Financial Ratio'].notna()]
#print(file_4)


# In[ ]:


#combined_csv = pd.concat([pd.read_csv('Alphabet Inc (GOOG)/' + f) for f in sorted_list_0 ])
#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')


file_0 = pd.read_csv('Alphabet Inc (GOOG)/' + sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)
title = sorted_list_0[0][:-13]
file_0 = file_0.set_axis(['Financial Ratio', title], axis=1, inplace=False)
print(file_0)

sorted_list_1 = sorted_list_0[1:]
#print(sorted_list_1)

length = len(sorted_list_1)
for i in range(length):
    print(sorted_list_1[i])
    file_1 = pd.read_csv('Alphabet Inc (GOOG)/' + sorted_list_1[i])
    file_1 = file_1.drop(file_1.columns[0], axis=1)
    file_1 = file_1.drop(file_1.columns[0], axis=1)

    title = sorted_list_1[i][:-13]
    file_1.rename({'Financial Ratio /unit': title}, axis=1, inplace=True)
    print(file_1)

    #file_2 = file_0.append(file_1)
    ##file_2[title] = file_2[title].shift(-25)
    #file_2 = file_2[file_2['Financial Ratio'].notna()]
    #print(file_2)
    file_0 = file_0.join(file_1)
    print(file_0)
    
    file_0.to_csv('Alphabet Inc (GOOG)/Combined_Ratio.csv')
    
    


# In[ ]:




