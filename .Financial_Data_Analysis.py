#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#S1 _ XLSX Worksheets


# In[ ]:


import pandas as pd
import glob
import os


# In[ ]:


mydir = os.getcwd()

#Update listdir() to specify folder.
for file in os.listdir(mydir):
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
for file in os.listdir(mydir):
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
    url = input_date
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





# In[ ]:


#S0.Untitled1


# In[ ]:


import numpy as np
import pandas as pd
import os


# In[ ]:


mydir = os.getcwd()

result = []
for file in os.listdir(mydir):
    if file.endswith("-0.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_0 = sorted(result)
sorted_list_0

result = []
for file in os.listdir(mydir):
    if file.endswith("-1.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_1 = sorted(result)
sorted_list_1

result = []
for file in os.listdir(mydir):
    if file.endswith("-2.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_2 = sorted(result)
#sorted_list_2


# In[ ]:


length = len(sorted_list_0)

for i in range(length):
    input_date_0 = sorted_list_0[i]
    input_date_1 = sorted_list_1[i]
    input_date_2 = sorted_list_2[i]
    input_date = input_date_0[:-8]
    
    
    
    
    
    
    
    
    
    
    ## BELOW IS THE PROGRAM/CODE TO RETRIEVE ALL RATIOS FOR BS, CSI & CSCF
    
    
    
    
    
    
    print('\n')
    print('\n')
    print(input_date_0)
    
    file = pd.read_csv(input_date_0)
    file = file.drop(file.columns[2:], axis=1)
    file = file.set_axis([input_date_0, 'Default'], axis=1, inplace=False)


    col_one_list_0 = file[input_date_0].tolist()
    #col_one_arr = file[input_date_0].to_numpy()
    #print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")
    #print(f"\ncol_one_arr:\n{col_one_arr}\ntype:{type(col_one_arr)}")

    #Enter subs

    #subs_00 = 'Total liabilities and s'

    subs00 = 'Marketable securities'
    subs01 = 'Cash and cash equivalents'
    subs02 = 'Accounts receivable'
    subs03 = 'Total current a'
    subs04 = 'Total current l'
    subs05 = 'Total assets'
    subs06 = 'Total liabilities'
    subs07 = 'Retaine'
    subs08 = 'Total stockholder'
    subs09 = 'Property'
    subs10 = 'Short'
    subs11 = 'Long'
    subs12 = 'Convertible preferred stock, $0.001'
    subs13 = 'and Class B'

    subs14 = 'Prepaid'

    #res_00 = [i for i in col_one_list if subs_00 in i]
    #print(res_00)
    #file.replace(res_00, "NaN", inplace=True)


    res00 = [i for i in col_one_list_0 if subs00 in i]
    #print(res00)
    res01 = [i for i in col_one_list_0 if subs01 in i]
    #print(res01)
    res02 = [i for i in col_one_list_0 if subs02 in i]
    #print(res02)
    res03 = [i for i in col_one_list_0 if subs03 in i]
    #print(res03)
    res04 = [i for i in col_one_list_0 if subs04 in i]
    #print(res04)
    res05 = [i for i in col_one_list_0 if subs05 in i]
    #print(res05)
    res06 = [i for i in col_one_list_0 if subs06 in i]
    #print(res06)
    res07 = [i for i in col_one_list_0 if subs07 in i]
    #print(res07)
    res08 = [i for i in col_one_list_0 if subs08 in i]
    #print(res08)
    res09 = [i for i in col_one_list_0 if subs09 in i]
    #print(res09)
    res10 = [i for i in col_one_list_0 if subs10 in i]
    #print(res10)
    res11 = [i for i in col_one_list_0 if subs11 in i]
    #print(res11)
    res12 = [i for i in col_one_list_0 if subs12 in i]
    #print(res12)
    res13 = [i for i in col_one_list_0 if subs13 in i]
    #print(res13)

    res14 = [i for i in col_one_list_0 if subs14 in i]
    #print(res14)
    
    if len(res00) >= 2:
        res00 = res00[0]
        #print(res00)
    
    if len(res06) >= 2:
        res06 = res06[0]
        #print(res06)
    
    if len(res14) >= 2:
        res14 = res14[0]
        #print(res14)


    file.replace(res00, 
           "Marketable securities", inplace=True)
    file.replace(res01, 
           "Cash and cash equivalents", inplace=True)
    file.replace(res02, 
           "Accounts receivable", inplace=True)
    file.replace(res03, 
           "Current assets", inplace=True)
    file.replace(res04, 
           "Current liabilities", inplace=True)
    file.replace(res05, 
           "Total assets", inplace=True)
    file.replace(res06, 
           "Total liabilities", inplace=True)
    file.replace(res07, 
           "Retained earnings", inplace=True)
    file.replace(res08, 
           "Total stockholder's equity", inplace=True)
    file.replace(res09, 
           "Property, plant and equipment", inplace=True)
    file.replace(res10, 
           "Short-term debt", inplace=True)
    file.replace(res11, 
           "Long-term debt", inplace=True)
    file.replace(res12, 
           "Convertible stocks", inplace=True)
    file.replace(res13, 
           "Class A and Class B stocks", inplace=True)

    file.replace(res14, 
           "Prepaid expenses", inplace=True)
    #file
    #file.loc[file[input_date_0] == 'Marketable securities']
    ## PREPAID EXPENSES DOES NOT EXIST

    file = file[file['Default'].notna()]

    col_one_arr = file.loc[file[input_date_0].isin(['Marketable securities',
                                          'Cash and cash equivalents',
                                          'Accounts receivable',
                                          'Current assets',
                                          'Current liabilities',
                                          'Total assets',
                                          'Total liabilities',
                                          'Retained earnings',
                                          "Total stockholder's equity",
                                          'Property, plant and equipment',
                                          'Short-term debt',
                                          'Long-term debt',
                                          'Convertible stocks',
                                          'Class A and Class B stocks',
                                         'Prepaid expenses'])].to_numpy()

    if res14:
        col_one_arr_01 = col_one_arr
        #print("Prepaid. Expenses exists.")
    else:
        col_one_arr_00 = np.array([['Prepaid expenses', '0']])
        col_one_arr_01 = np.append(col_one_arr,col_one_arr_00, axis=0)
        #print("Prepaid. Expenses has been added.")
        #print(col_one_arr_01)


    if res10:
        col_one_arr_02 = col_one_arr_01
        #print("Short-term Debt exists.")
    else:
        col_one_arr_00 = np.array([['Short-term debt', '0']])
        col_one_arr_02 = np.append(col_one_arr_01,col_one_arr_00, axis=0)
        #print("Short-term Debt has been added.")
        #print(col_one_arr_02)

    if res12:
        col_one_arr_03 = col_one_arr_02
        #print("Convertible Stocks exists.")
    else:
        col_one_arr_00 = np.array([['Convertible stocks', '0']])
        col_one_arr_03 = np.append(col_one_arr_02,col_one_arr_00, axis=0)
        #print("Convertible Stocks has been added.")
        #print(col_one_arr_03)




    col_one_arr_CSI_04 = np.vstack({tuple(row) for row in col_one_arr_03})
    col_one_arr_BS = np.array(sorted(col_one_arr_CSI_04 ,key=lambda x: x[0]))
    #col_one_arr_BS = col_one_arr


    ## CONVERTIBLE STOCKS NEED TO BE DEFINED (MAX) OR *HIGHEST VALUE - IF MULTIPLE

    #obj = len(col_one_arr)
    #np.insert(col_one_arr, obj, ["PE_1", "PE_1_VALUE"], 0)





    #new_arr00 = np.append(col_one_arr, [["PE_1", "PE_1_VALUE"]],0)

    #new_arr01 = np.append(new_arr00, [["PE_1", "PE_1_VALUE"]],0)
    #new_arr02 = np.append(new_arr01, [["PE_2", "PE_2_VALUE"]],0)
    #new_arr03 = np.append(new_arr02, [["PEG_1", "PEG_1_VALUE"]],0)
    #new_arr04 = np.append(new_arr03, [["PEG_2", "PEG_2_VALUE"]],0)
    #new_arr05 = np.append(new_arr04, [["EV", "EB_VALUE"]],0)
    #new_arr06 = np.append(new_arr05, [["EBIT", "EBIT_VALUE"]],0)
    #new_arr07 = np.append(new_arr06, [["EBITDA", "EBITDA_VALUE"]],0)
    #new_arr08 = np.append(new_arr07, [["DE", "DE_VALUE"]],0)
    #new_arr09 = np.append(new_arr08, [["NE", "NE_VALUE"]],0)
    #new_arr10 = np.append(new_arr09, [["QR_1", "QR_1_VALUE"]],0)
    #new_arr11 = np.append(new_arr10, [["QR_2", "QR_2_VALUE"]],0)

    #new_arr12 = np.append(new_arr11, [["DY", "DY_VALUE"]],0)
    #new_arr13 = np.append(new_arr12, [["DPS", "DPS_VALUE"]],0)
    #new_arr14 = np.append(new_arr13, [["EPS", "EPS_VALUE"]],0)
    #new_arr15 = np.append(new_arr14, [["MCAP", "MCAP_VALUE"]],0)
    #new_arr16 = np.append(new_arr15, [["ROE", "ROE_VALUE"]],0)
    #new_arr17 = np.append(new_arr16, [["NetMargin", "NetMargin_VALUE"]],0)
    #new_arr18 = np.append(new_arr17, [["OperatingMargin", "OperatingMargin_VALUE"]],0)

    #new_arr18

    file = pd.read_csv(input_date_1)
    file = file.drop(file.columns[2:], axis=1)
    file = file.set_axis([input_date_1, 'Default'], axis=1, inplace=False)
    file = file.dropna()

    col_one_list_1 = file[input_date_1].tolist()
    #print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")

    col_one_list_1[0] = "Additional Info"

    #Enter subs
    Rev = 'Revenues'
    #print(Rev)

    Rev_0 = 'Revenue'
    #print(Rev_0)

    NI = 'Net income'
    #print(NI)
    
    RD = 'Research and development'
    #print(RD)

    subs00 = 'Cost of'
    subs01 = 'Income from operations'
    subs02 = 'Income before'
    subs03 = 'asic'
    subs04 = 'iluted'
    subs05 = 'Less'

    res00 = [i for i in col_one_list_1 if subs00 in i]
    #print(res00)
    res01 = [i for i in col_one_list_1 if subs01 in i]
    #print(res01)
    res02 = [i for i in col_one_list_1 if subs02 in i]
    #print(res02)
    res03 = [i for i in col_one_list_1 if subs03 in i]
    #print(res03)
    res04 = [i for i in col_one_list_1 if subs04 in i]
    #print(res04)
    res05 = [i for i in col_one_list_1 if subs05 in i]
    #print(res05)
    
    
    if len(NI) >= 2:
        NI = NI[0]
    #print(NI)
    
    
    file.replace(RD, 
           "Research and development", inplace=True)

    file.replace(Rev_0, 
           "Revenues", inplace=True)


    file.replace(Rev, 
           "Revenues", inplace=True)
    file.replace(NI, 
           "Net income", inplace=True)
    file.replace(res00, 
           "Cost of revenues", inplace=True)
    file.replace(res01, 
           "Operating income", inplace=True)
    file.replace(res02, 
           "Income before taxes", inplace=True)
    file.replace(res03, 
           "Basic EPS", inplace=True)
    file.replace(res04, 
           "Diluted EPS", inplace=True)
    file.replace(res05, 
           "Less: Adjustment Payments", inplace=True)


    col_one_arr = file.loc[file[input_date_1].isin(['Revenues',
                                          'Net income',
                                          'Research and development',
                                          'Cost of revenues',
                                          'Research and development',
                                          'Operating income',
                                          'Income before taxes',
                                          'Basic EPS',
                                          'Diluted EPS',
                                         'Less: Adjustment Payments'])].to_numpy()

    #print(col_one_arr)
    #print(res05)
    #print(type(res05))

    if res05:
        col_one_arr_01 = col_one_arr
        #print("Adj. Payments exists.")
    else:
        col_one_arr_00 = np.array([['Less: Adjustment Payments', '0']])
        col_one_arr_01 = np.append(col_one_arr,col_one_arr_00, axis=0)
        #print("Adj. Payments has been added.")
        #print(col_one_arr_01)

    col_one_arr_CSI_00 = np.vstack({tuple(row) for row in col_one_arr_01})
    col_one_arr_CSI_01 = np.array(sorted(col_one_arr_CSI_00 ,key=lambda x: x[0]))
    #print(col_one_arr_CSI_01)

    ###
    
    counts = {}
    for elem in col_one_arr_CSI_00:
        counts[elem[0]] = counts.get(elem[0], 0) + 1
    new_array = []

    for elem in col_one_arr_CSI_00:
        if counts[elem[0]] > 1:
            new_array.append(elem)

            ni_loc_0 = np.where(col_one_arr_CSI_01 == 'Net income')[0][0]
            ni_loc_1 = np.where(col_one_arr_CSI_01 == 'Net income')[0][1]

            Net_income_v_0 = col_one_arr_CSI_01[ni_loc_0][1]
            Net_income_v_1 = col_one_arr_CSI_01[ni_loc_1][1]

            if Net_income_v_0 > Net_income_v_1:
                Net_income_v_2 = Net_income_v_0
            else:
                Net_income_v_2 = Net_income_v_1
            #print(Net_income_v_2)

            if col_one_arr_CSI_01[ni_loc_0][1] == Net_income_v_2:
                col_one_arr_CSI_0 = np.delete(col_one_arr_CSI_01, ni_loc_1, 0)
                #print('NI_LOC_0')
            else:
                col_one_arr_CSI_0 = np.delete(col_one_arr_CSI_01, ni_loc_0, 0)
                #print('NI_LOC_1')
            col_one_arr_CSI = col_one_arr_CSI_0
        else:
            ni_loc_0 = np.where(col_one_arr_CSI_01 == 'Net income')[0]
            col_one_arr_CSI = col_one_arr_CSI_01

    #print(col_one_arr_CSI)




    #['Net income'] in col_one_arr_CSI[6]

    #print(input_date_2)
    file = pd.read_csv(input_date_2)
    #print(file)
    file = file.drop(file.columns[2:], axis=1)
    file = file.set_axis([input_date_2, 'Default'], axis=1, inplace=False)
    #print(file)
    col_one_list_2 = file[input_date_2].tolist()
    #print(col_one_list_0)
    #print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")

    col_one_list_2[0] = "Additional Info"
    #col_one_list = list(dict.fromkeys(col_one_list_0))
    #print(col_one_list)

    subs00 = 'Net income'
    subs01 = 'Depreciation'
    subs02 = 'Amortization'
    subs03 = 'Prepaid'
    subs04 = 'by operating activities'
    subs05 = 'in investing activities'
    subs06 = 'in financing activities'
    subs07 = 'Purchases of property'

    res00 = [i for i in col_one_list_2 if subs00 in i]
    #print(res00)
    res01 = [i for i in col_one_list_2 if subs01 in i]
    #print(res01)
    res02 = [i for i in col_one_list_2 if subs02 in i]
    #print(res02)
    res03 = [i for i in col_one_list_2 if subs03 in i]
    #print(res03)
    res04 = [i for i in col_one_list_2 if subs04 in i]
    #print(res04)
    res05 = [i for i in col_one_list_2 if subs05 in i]
    #print(res05)
    res06 = [i for i in col_one_list_2 if subs06 in i]
    #print(res06)
    res07 = [i for i in col_one_list_2 if subs07 in i]
    #print(res07)

    file.replace(res00, 
           "Net income", inplace=True)
    file.replace(res01, 
           "Depreciation", inplace=True)
    file.replace(res02, 
           "Amortization", inplace=True)
    file.replace(res03, 
           "Prepaid expenses", inplace=True)
    file.replace(res04, 
           "Net cash provided by operating activities", inplace=True)
    file.replace(res05, 
           "Net cash provided by investing activities", inplace=True)
    file.replace(res06, 
           "Net cash provided by financing activities", inplace=True)
    file.replace(res07, 
           "Purchase of property, plant and equipment", inplace=True)

    col_one_list_2 = file.loc[file[input_date_2].isin(['Net income',
                                          'Depreciation',
                                          'Amortization',
                                          'Prepaid expenses',
                                          'Net cash provided by operating activities',
                                          'Net cash provided by investing activities',
                                          'Net cash provided by financing activities',
                                         'Purchase of property, plant and equipment'])].to_numpy()



    #print(col_one_list_2)
    
    if res03:
        col_one_arr_01 = col_one_list_2
        #print("Prepaid. Expenses exists.")
    else:
        col_one_arr_00 = np.array([['Prepaid expenses', '0']])
        col_one_arr_01 = np.append(col_one_arr,col_one_arr_00, axis=0)
        #print("Prepaid. Expenses has been added.")
        #print(col_one_arr_01)


    col_one_arr_CSCF = np.array(sorted(col_one_arr_01 ,key=lambda x: x[0]))

    #print(col_one_arr_BS)

    Accounts_receivable = float(col_one_arr_BS[0,1])
    Cash_and_cash_equivalents = float(col_one_arr_BS[1,1])
    Class_A_and_Class_B_stocks = float(col_one_arr_BS[2,1])
    Convertible_stocks = float(col_one_arr_BS[3,1])
    Current_assets = float(col_one_arr_BS[4,1])
    Current_liabilities = float(col_one_arr_BS[5,1])
    Long_term_debt = float(col_one_arr_BS[6,1])
    Marketable_securities = float(col_one_arr_BS[7,1])
    Prepaid_expenses = float(col_one_arr_BS[8,1])
    Property_plant_and_equipment = float(col_one_arr_BS[9,1])
    Retained_earnings = float(col_one_arr_BS[10,1])
    Short_term_debt = float(col_one_arr_BS[11,1])
    Total_assets = float(col_one_arr_BS[12,1])
    Total_liabilities = float(col_one_arr_BS[13,1])
    Total_stockholder_equity = float(col_one_arr_BS[14,1])

    #print(col_one_arr_CSI)
    
    #Consolidated Statement of Income CSI
    Basic_EPS = float(col_one_arr_CSI[0,1])
    Cost_of_revenues = float(col_one_arr_CSI[1,1])
    Diluted_EPS = float(col_one_arr_CSI[2,1])
    Income_before_taxes = float(col_one_arr_CSI[3,1])
    Adjustment_Payments = float(col_one_arr_CSI[4,1])
    Net_income = float(col_one_arr_CSI[5,1])
    Operating_income = float(col_one_arr_CSI[6,1])
    Research_Development = float(col_one_arr_CSI[7,1])
    Revenues = float(col_one_arr_CSI[8,1])

    #print(col_one_arr_CSCF)
    
    #Consolidated Statement of Cash Flow CSCF
    Net_income_CSCF = float(col_one_arr_CSCF[0,1])
    Depreciation = float(col_one_arr_CSCF[1,1])
    Amortization = float(col_one_arr_CSCF[2,1])
    Prepaid_expenses_CSCF = float(col_one_arr_CSCF[3,1])
    Net_cash_operating_activities = float(col_one_arr_CSCF[4,1])
    Purchase_of_PPE = float(col_one_arr_CSCF[5,1])
    Net_cash_investing_activities = float(col_one_arr_CSCF[6,1])
    Net_cash_financing_activities = float(col_one_arr_CSCF[7,1])
    


    #Avg Share Price

    file = pd.read_csv('Alphabet Inc.csv')

    ## TRY STATEMENT FOR date_input-29 -28 -27 -26...
    date_prefix = input_date_0[:-8]
    date_ls = ["31", "30", "29", "28"]

    upd_date_0 = date_prefix + date_ls[0]
    upd_date_1 = date_prefix + date_ls[1]
    upd_date_2 = date_prefix + date_ls[2]
    upd_date_3 = date_prefix + date_ls[3]
    
    #print(upd_date_0)
    
    print('\n')

    if upd_date_0 in file.values:
        col_one_arr_P = file[file['Date'].str.contains(upd_date_0)].to_numpy()
        #print(upd_date_0 + " exists.")
    else:
        if upd_date_1 in file.values:
            col_one_arr_P = file[file['Date'].str.contains(upd_date_1)].to_numpy()
            #print("Month finishes in -30")
        else:
            if upd_date_2 in file.values:
                col_one_arr_P = file[file['Date'].str.contains(upd_date_2)].to_numpy()
                #print("Month finishes in -29")
            else:
                if upd_date_3 in file.values:
                    col_one_arr_P = file[file['Date'].str.contains(upd_date_3)].to_numpy()
                    #print("Month finishes in -28")


    Open_P = col_one_arr_P[0,1]
    Close_P = col_one_arr_P[0,-3]

    Avg_P = ((Open_P + Close_P)/2)

    col_one_arr_P_Modified = np.append(col_one_arr_P, [Avg_P])
    col_one_arr_P_Modified

    #Saved Number of Shares Outstanding (res13)

    def listToString(res13): 
        str1 = "" 
        for ele in res13: 
            str1 += ele  
        return str1 

    str00 = listToString(res13)

    str01 = str00.replace(",", "")
    str02 = str(str01.split("; ",1)[1])[0:6]
    Outstanding_shares = int(str02)

    #Retained Earnings -3 months prior .calc(CHANGE)

    #file.loc[file[input_date_0] == 'Retained earnings']
    file = pd.read_csv(input_date_0)
    file = file.drop(file.columns[1], axis=1)
    file = file.set_axis([input_date_0, 'Default'], axis=1, inplace=False)
    col_one_list = file[input_date_0].tolist()
    #print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")

    subs99 = 'Retained earnings'
    res99 = [i for i in col_one_list if subs99 in i]
    col_one_arr = file.loc[file[input_date_0].isin(['Retained earnings'])].to_numpy()
    RE_start = float(col_one_arr[0,1])


    #https://www.investopedia.com/ask/answers/012015/how-do-i-calculate-dividend-payout-ratio-income-statement.asp
    #Dividends Paid or Payout Ratio => DP = (NI + RE) - RE.close :::::: DP.start = (NI.start + RE.start) - RE.close

    #Net Income -3 months prior .calc(CHANGE)

    file = pd.read_csv(input_date_1)
    file = file.drop(file.columns[3:], axis=1)
    file = file.drop(file.columns[1], axis=1)

    file = file.set_axis([input_date_1, 'Default'], axis=1, inplace=False)
    col_one_arr = file.loc[file[input_date_1].isin(['Net income'])].to_numpy()

    NI_start = float(col_one_arr[0,1])

    RE_close = Retained_earnings
    DP_VALUE = (NI_start + RE_start) - RE_close


    #Free Cash Flow FCF - Additional Data from BS & CSCF

    file = pd.read_csv(input_date_0)
    file = file.drop(file.columns[1], axis=1)
    file = file.set_axis([input_date_0, 'Default'], axis=1, inplace=False)

    file = file[file['Default'].notna()]

    col_one_list = file[input_date_0].tolist()
    #print(f"\ncol_one_list:\n{col_one_list}\ntype:{type(col_one_list)}")

    subs98 = 'Total current a'
    subs97 = 'Total current l'
    subs96 = 'Property'

    res98 = [i for i in col_one_list if subs98 in i]
    res97 = [i for i in col_one_list if subs97 in i]
    res96 = [i for i in col_one_list if subs96 in i]

    str00 = listToString(res98)
    str01 = listToString(res97)
    str02 = listToString(res96)

    file.replace(str00, "Current assets", inplace=True)
    file.replace(str01, "Current liabilities", inplace=True)
    file.replace(str02, "Property, plant and equipment", inplace=True)

    col_one_arr = file.loc[file[input_date_0].isin(["Current assets"])].to_numpy()
    Current_assets_start = float(col_one_arr[0,1])
    col_one_arr = file.loc[file[input_date_0].isin(["Current liabilities"])].to_numpy()
    Current_liabilities_start = float(col_one_arr[0,1])
    col_one_arr = file.loc[file[input_date_0].isin(["Property, plant and equipment"])].to_numpy()
    Property_plant_and_equipment_start = float(col_one_arr[0,1])



    #For OLD Depreciation Value

    file = pd.read_csv(input_date_2)

    file = file.drop(file.columns[3:], axis=1)
    file = file.drop(file.columns[1], axis=1)

    file = file.set_axis([input_date_2, 'Default'], axis=1, inplace=False)    
    col_one_list = file[input_date_2].tolist()

    col_one_list[0] = "Additional Info"

    subs95 = 'Depreciation'
    res95 = [i for i in col_one_list if subs95 in i]
    str03 = listToString(res95)
    file.replace(str03, "Depreciation", inplace=True)
    col_one_arr = file.loc[file[input_date_2].isin(["Depreciation"])].to_numpy()
    Depreciation_start = float(col_one_arr[0,1])
    
    
    
    
    
    
    
    
    

#############################################################################

    d = {input_date_0[:-6]: [  

        # BALANCE SHEET

                                 'Accounts_receivable', #Balance_Sheet
                                 'Cash_and_cash_equivalents', #Balance_Sheet
                                 'Class_A_and_Class_B_stocks', #Balance_Sheet
                                 'Convertible_stocks', #Balance_Sheet
                                 'Outstanding_shares', #Balance_Sheet
                                 'Current_assets', #Balance_Sheet
                                 'Current_liabilities', #Balance_Sheet
                                 'Long_term_debt', #Balance_Sheet
                                 'Marketable_securities', #Balance_Sheet
                                 'Prepaid_expenses', #Balance_Sheet
                                 'Property_plant_and_equipment', #Balance_Sheet
                                 'Retained_earnings', #Balance_Sheet
                                 'Short_term_debt', #Balance_Sheet
                                 'Total_assets', #Balance_Sheet
                                 'Total_liabilities', #Balance_Sheet
                                 'Total_stockholder_equity', #Balance_Sheet

        # INCOME STATEMENT

                                 'Basic_EPS', #Income_Statement
                                 'Cost_of_revenues', #Income_Statement
                                 'Diluted_EPS', #Income_Statement
                                 'Income_before_taxes', #Income_Statement
                                 'Adjustment_Payments', #Income_Statement
                                 'Net_income', #Income_Statement
                                 'Operating_income', #Income_Statement
                                 'Research_Development', #Income_Statement
                                 'Revenues', #Income_Statement

        # CASH-FLOW STATEMENT

                                 'Net_income_CSCF', #Cash_Flow_Statement
                                 'Depreciation', #Cash_Flow_Statement
                                 'Amortization', #Cash_Flow_Statement
                                 'Prepaid_expenses_CSCF', #Cash_Flow_Statement
                                 'Net_cash_operating_activities', #Cash_Flow_Statement
                                 'Purchase_of_PPE', #Cash_Flow_Statement
                                 'Net_cash_investing_activities', #Cash_Flow_Statement
                                 'Net_cash_financing_activities'], #Cash_Flow_Statement

    ##########################################################################################

             'Financial Variables /unit': [

        # BALANCE SHEET

                                 Accounts_receivable, #Balance_Sheet
                                 Cash_and_cash_equivalents, #Balance_Sheet
                                 Class_A_and_Class_B_stocks, #Balance_Sheet
                                 Convertible_stocks, #Balance_Sheet
                                 Outstanding_shares, #Balance_Sheet
                                 Current_assets, #Balance_Sheet
                                 Current_liabilities, #Balance_Sheet
                                 Long_term_debt, #Balance_Sheet
                                 Marketable_securities, #Balance_Sheet
                                 Prepaid_expenses, #Balance_Sheet
                                 Property_plant_and_equipment, #Balance_Sheet
                                 Retained_earnings, #Balance_Sheet
                                 Short_term_debt, #Balance_Sheet
                                 Total_assets, #Balance_Sheet
                                 Total_liabilities, #Balance_Sheet
                                 Total_stockholder_equity, #Balance_Sheet

        # INCOME STATEMENT

                                 Basic_EPS, #Income_Statement
                                 Cost_of_revenues, #Income_Statement
                                 Diluted_EPS, #Income_Statement
                                 Income_before_taxes, #Income_Statement
                                 Adjustment_Payments, #Income_Statement
                                 Net_income, #Income_Statement
                                 Operating_income, #Income_Statement
                                 Research_Development, #Income_Statement
                                 Revenues, #Income_Statement

        # CASH-FLOW STATEMENT

                                 Net_income_CSCF, #Cash_Flow_Statement
                                 Depreciation, #Cash_Flow_Statement
                                 Amortization, #Cash_Flow_Statement
                                 Prepaid_expenses_CSCF, #Cash_Flow_Statement
                                 Net_cash_operating_activities, #Cash_Flow_Statement
                                 Purchase_of_PPE, #Cash_Flow_Statement
                                 Net_cash_investing_activities, #Cash_Flow_Statement
                                 Net_cash_financing_activities #Cash_Flow_Statement
             ]}

    df= pd.DataFrame(data=d)
    print(df)

    filename = input_date_0[:-6] + "-Variables-DF.csv"
    df.to_csv(filename)













    
    
    #Ratios Equation & Formula

#############################################################################


    #Ratios Equation & Formula


             #Price to Earnings
    #PE_1_VALUE (Calculate EPS using Net Income & Number of shares issues and outstanding)
    #PE_1_VALUE = Avg_P/(Revenues/Class_A_and_Class_B_stocks)
    PE_1_VALUE = Avg_P / (Net_income / Outstanding_shares) / 1000 #Units
    print(PE_1_VALUE)

    #PE_2_VALUE (Calculate PE_2 using Market Price & Diluted EPS [CSI])
    PE_2_0_VALUE = Avg_P / Diluted_EPS
    print(PE_2_0_VALUE)

    PE_2_1_VALUE = Avg_P / Basic_EPS
    print(PE_2_1_VALUE)


    print('\n')

             #Price/Earnings to Growth
    #PEG_1_VALUE (Calculate PEG using Expected Growth Rate as input)     #print('Enter EGR:')
    #MISSING VALUE EGR can only be determined at the present moment using Expected Growth Rate from: Citibank, Goldman Sachs, JPM, MorganStanley, BNP Paribas - Expected EPS Growth
    #Other sources include the Wall Street Journal WSJ and Yahoo Finance


    #PEG_2_VALUE (Calculate from past 3-6-9-12 months growth rate using linear and non-linear regressions)
    #MISSING VALUE Data from the past 3-6-9-12 months
    #Other source: https://www.investopedia.com/terms/p/price-earningsratio.asp


             #EV and EBITDA-related ratios
    EV_1_VALUE = Avg_P * Outstanding_shares
    print(EV_1_VALUE)
    EV_2_VALUE = Avg_P * Class_A_and_Class_B_stocks
    print(EV_2_VALUE)

    EBIT_VALUE = Net_income_CSCF #Interest (N.A)
    print(EBIT_VALUE)
    EBITDA_VALUE = EBIT_VALUE - Depreciation - Amortization
    print(EBITDA_VALUE)

    EV_1_EBITDA_VALUE = EV_1_VALUE / EBITDA_VALUE
    print(EV_1_EBITDA_VALUE)
    EV_2_EBITDA_VALUE = EV_2_VALUE / EBITDA_VALUE
    print(EV_2_EBITDA_VALUE)

    print('\n')

    DE_VALUE = (Long_term_debt + Short_term_debt) / EBITDA_VALUE
    print(DE_VALUE)
    NE_VALUE = (Long_term_debt + Short_term_debt - Cash_and_cash_equivalents) / EBITDA_VALUE
    print(NE_VALUE)
    QR_1_VALUE = (Cash_and_cash_equivalents + Marketable_securities + Accounts_receivable) / Current_liabilities
    print(QR_1_VALUE)
    QR_2_VALUE = (Current_assets - Prepaid_expenses) / Current_liabilities
    print(QR_2_VALUE)

    print('\n')


             #Dividend-related ratios
    EPS_VALUE = (Net_income - Convertible_stocks) / Outstanding_shares
    #https://www.investopedia.com/ask/answers/032515/what-difference-between-earnings-share-and-dividends-share.asp
    print(EPS_VALUE)
    #Dividends Paid or Payout Ratio => DP = (NI + RE) - RE.close :::::: DP.start = (NI.start + RE.start) - RE.close
    #https://www.investopedia.com/ask/answers/012015/how-do-i-calculate-dividend-payout-ratio-income-statement.asp
    DPS_VALUE = DP_VALUE / Outstanding_shares
    print(DPS_VALUE)

    DY_1_VALUE = Net_income / ((RE_close - RE_start) / RE_close) * 4 # for 4 Quarters/Year
    print(DY_1_VALUE) #Approximation. Dividend Yield should be calculated within -12 months, not -3months
    DY_2_VALUE = DPS_VALUE / Avg_P * 1000 #Units
    print(DY_2_VALUE)

    Div_VALUE = -(Net_cash_financing_activities)
    print(Div_VALUE)

    print('\n')


             #Other Ratios (MCAP, ROE, Margins...) Verify Ratio Formulas
    MCAP_VALUE = Avg_P / Outstanding_shares
    print(MCAP_VALUE)
    ROE_VALUE = Net_income / Total_stockholder_equity * 4 # or 4 Quarters/Year :::: Other formula(s) exist
    print(ROE_VALUE)
    NetMargin_VALUE = (Revenues - Cost_of_revenues) / Revenues
    print(NetMargin_VALUE)
    OperatingMargin_VALUE = Net_cash_operating_activities - Revenues
    print(OperatingMargin_VALUE)

    print('\n')


    #MISSING VALUE: Income before Tax for -6 months (Income_before_taxes is only -3 months). Use current Tax Rate
    print(Net_income)
    print(Income_before_taxes)
    Tax_VALUE = 1 - (Net_income / Income_before_taxes)
    print(Tax_VALUE)

    FCF_2_VALUE = (Property_plant_and_equipment + (Depreciation/2)) - (Property_plant_and_equipment_start + (Depreciation_start/2)) #CHANGE(CAPEX) also looking at old Depreciation
    print(FCF_2_VALUE)

    #CHANGE(Assets-Liabilities) - ()#CHANGE(CAPEX)
    FCF_0_VALUE = EBIT_VALUE * (1 - Tax_VALUE) - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
    print(FCF_0_VALUE)
    FCF_1_VALUE = Revenues - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
    print(FCF_1_VALUE)

    #R&D
    print(Research_Development)


    ### USE BOTH 'Outstanding_shares' & 'Class_A_and_Class_B_stocks' FOR RELATED RATIOS?



#############################################################################
    
    
    
    
    
    
    
    # UPDATED :: Ratios Equation & Formula

    # () PE_1_VALUE = Avg_P / (Net_income / Outstanding_shares) / 1000
    ##

    PE_2_2_VALUE = Avg_P / EPS_VALUE
    #print(PE_2_2_VALUE)

    # (CSCF) EBIT_VALUE = Net_income_CSCF && (CSI) EBIT_VALUE_0 = Income_before_taxes

    EBIT_VALUE_0 = Income_before_taxes
    #print(EBIT_VALUE_0)

    # (CSCF) EBITDA_VALUE = EBIT_VALUE - Depreciation - Amortization

    EBITDA_VALUE_0 = EBIT_VALUE_0 - Depreciation - Amortization
    #print(EBITDA_VALUE_0)

    # () 

    EV_1_EBITDA_VALUE_0 = EV_1_VALUE / EBITDA_VALUE_0
    #print(EV_1_EBITDA_VALUE_0)
    EV_2_EBITDA_VALUE_0 = EV_2_VALUE / EBITDA_VALUE_0
    #print(EV_2_EBITDA_VALUE_0)

    # () 

    DE_VALUE_0 = (Long_term_debt + Short_term_debt) / EBITDA_VALUE_0
    #print(DE_VALUE_0)
    NE_VALUE_0 = (Long_term_debt + Short_term_debt - Cash_and_cash_equivalents) / EBITDA_VALUE_0
    #print(NE_VALUE_0)

    # () 

    #Div_VALUE_0 = Net_income - (EPS_VALUE * Outstanding_shares)
    #print(Div_VALUE_0)
    Div_VALUE_1 = Net_income - (Basic_EPS * Outstanding_shares)
    #print(Div_VALUE_1)
    Div_VALUE_2 = Net_income - (Diluted_EPS * Outstanding_shares)
    #print(Div_VALUE_2)

    #print('\n')

    # ()
    #DPS_7 = EPS_VALUE * (Div_VALUE / EPS_VALUE) 

    DPS_00 = EPS_VALUE * (Div_VALUE / Net_income)
    #print(DPS_00)
    #DPS_01 = EPS_VALUE * (Div_VALUE_0 / Net_income) 
    #print(DPS_01)
    DPS_02 = EPS_VALUE * (Div_VALUE_1 / Net_income) 
    #print(DPS_02)
    DPS_03 = EPS_VALUE * (Div_VALUE_2 / Net_income) 
    #print(DPS_03)

    DPS_10 = Basic_EPS * (Div_VALUE / Net_income)
    #print(DPS_10)
    #DPS_11 = Basic_EPS * (Div_VALUE_0 / Net_income)
    #print(DPS_11)
    DPS_12 = Basic_EPS * (Div_VALUE_1 / Net_income)
    #print(DPS_12)
    DPS_13 = Basic_EPS * (Div_VALUE_2 / Net_income)
    #print(DPS_13)

    DPS_20 = Diluted_EPS * (Div_VALUE / Net_income)
    #print(DPS_20)
    #DPS_21 = Diluted_EPS * (Div_VALUE_0 / Net_income)
    #print(DPS_21)
    DPS_22 = Diluted_EPS * (Div_VALUE_1 / Net_income)
    #print(DPS_22)
    DPS_23 = Diluted_EPS * (Div_VALUE_2 / Net_income)
    #print(DPS_23)

    #DPS_30 = Div_VALUE / Outstanding_shares
    #print(DPS_30)
    #DPS_31 = Div_VALUE_0 / Outstanding_shares
    #print(DPS_31)
    #DPS_32 = Div_VALUE_1 / Outstanding_shares
    #print(DPS_32)
    #DPS_33 = Div_VALUE_2 / Outstanding_shares
    #print(DPS_33)

    #print('\n')

    # () 

    DY_2_VALUE_00 = DPS_00 / Avg_P #Units
    #DY_2_VALUE_01 = DPS_01 / Avg_P
    DY_2_VALUE_02 = DPS_02 / Avg_P
    DY_2_VALUE_03 = DPS_03 / Avg_P
    #print(DY_2_VALUE_00)
    #print(DY_2_VALUE_01)
    #print(DY_2_VALUE_02)
    #print(DY_2_VALUE_03)

    DY_2_VALUE_04 = DPS_10 / Avg_P
    #DY_2_VALUE_05 = DPS_11 / Avg_P
    DY_2_VALUE_06 = DPS_12 / Avg_P
    DY_2_VALUE_07 = DPS_13 / Avg_P
    #print(DY_2_VALUE_04)
    #print(DY_2_VALUE_05)
    #print(DY_2_VALUE_06)
    #print(DY_2_VALUE_07)

    DY_2_VALUE_08 = DPS_20 / Avg_P
    #DY_2_VALUE_09 = DPS_21 / Avg_P
    DY_2_VALUE_10 = DPS_22 / Avg_P
    DY_2_VALUE_11 = DPS_23 / Avg_P
    #print(DY_2_VALUE_08)
    #print(DY_2_VALUE_09)
    #print(DY_2_VALUE_10)
    #print(DY_2_VALUE_11)

    #DY_2_VALUE_12 = DPS_30 / Avg_P
    #DY_2_VALUE_13 = DPS_31 / Avg_P
    #DY_2_VALUE_14 = DPS_32 / Avg_P
    #DY_2_VALUE_15 = DPS_33 / Avg_P
    #print(DY_2_VALUE_12)
    #print(DY_2_VALUE_13)
    #print(DY_2_VALUE_14)
    #print(DY_2_VALUE_15)

    #print('\n')

    # () 
    # Following MCAP uses '*' rather than P/O_S Ratio
    #MCAP_VALUE_0 = Outstanding_shares * Avg_P
    #print(MCAP_VALUE_0)

    # () 

    #FCF_0_VALUE = EBIT_VALUE_0 * (1 - Tax_VALUE) - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
    #print(FCF_0_VALUE)

    #print('\n')

    # () 

    ### CHECK FOR (Net Income (I/S))   //DONE//
    ### CHECK FOR [Outstanding_shares] [Dividends] [EPS && DPS] [ADD AND USE ALL SAME VARIABLES OF DIFFERENT VALUE(S)]

    # Book Value BV
    BV_0 = Total_assets - Total_liabilities
    #print(BV_0)

    #print('\n')

    #GPM_0 = Gross Profit / Sales
    GPM_0 = (Revenues - Cost_of_revenues) / Revenues
    #print(GPM_0)

    # Operating Profit Margin
    OPM_0 = Income_before_taxes / Revenues
    #print(OPM_0)

    # Profit Margin
    PM_0 = Net_income / Revenues
    #print(PM_0)

    # Return on Assets
    ROA_0 = Net_income / Total_assets
    #print(ROA_0)

    # Return on Investments
    ROI_0 = Net_income / Total_stockholder_equity
    #print(ROI_0)

    # Return on Capital
    ROC_0 = Net_income / (Total_stockholder_equity + Short_term_debt + Long_term_debt)
    #print(ROC_0)
    # ADD FORMULAS BELOW
    #ROC_1 = (Price [Year] – Price [Previous Year]) / Price [Previous Year]
    #print(ROC_1)
    #ROC_2 = (Price [Year] – Price [Base Year]) / Price [Base Year]
    #print(ROC_2)

    # Return on Capital Employed
    ROCE_0 = Operating_income / (Total_assets - Current_liabilities)
    #print(ROCE_0)

    #print('\n')

    # Operating Profit
    # ADD FORMULA BELOW
    #OP_0 = Revenue – Operating Costs – COGS – Other Day-to-day Expenses
    #print()
    #OP_0 = Income_before_taxes 
    #print(OP_0)

    # Dividend Pay-out
    #DPO_0 = Div_VALUE / Net_income
    #DPO_1 = Div_VALUE_0 / Net_income
    #DPO_2 = Div_VALUE_1 / Net_income
    #DPO_3 = Div_VALUE_2 / Net_income
    #print(DPO_0)
    #print(DPO_1)
    #print(DPO_2)
    #print(DPO_3)

    #print('\n')

    # Preferred Stock Dividends
    PSD_0 = Net_income - Outstanding_shares
    #print(PSD_0)

    # Retention Ratio
    RR_0 = (Net_income - Div_VALUE) / Net_income
    #RR_1 = (Net_income - Div_VALUE_0) / Net_income
    RR_2 = (Net_income - Div_VALUE_1) / Net_income
    RR_3 = (Net_income - Div_VALUE_2) / Net_income
    #print(RR_0)
    #print(RR_1)
    #print(RR_2)
    #print(RR_3)

    #print('\n')

    # Market Value per Share
    MVPS_0 = MCAP_VALUE / Outstanding_shares
    #print(MVPS_0)
    #MVPS_1 = MCAP_VALUE_0 / Outstanding_shares
    #print(MVPS_1)

    MVPS_PRICE_0 = MVPS_0 / Avg_P
    #print(MVPS_PRICE_0)
    #MVPS_PRICE_1 = MVPS_1 / Avg_P
    #print(MVPS_PRICE_1)

    # Price Earnings 
    PE_00 = MVPS_0 / EPS_VALUE
    #print(PE_00)
    PE_01 = MVPS_0 / Basic_EPS
    #print(PE_01)
    PE_02 = MVPS_0 / Diluted_EPS
    #print(PE_02)

    #PE_10 = MVPS_1 / EPS_VALUE
    #print(PE_10)
    #PE_11 = MVPS_1 / Basic_EPS
    #print(PE_11)
    #PE_12 = MVPS_1 / Diluted_EPS
    #print(PE_12)

    #print('\n')

    # Sustainable Growth Rate
    SGR_0 = ROE_VALUE * RR_0
    #print(SGR_0)
    #SGR_1 = ROE_VALUE * RR_1
    #print(SGR_1)
    SGR_2 = ROE_VALUE * RR_2
    #print(SGR_2)
    SGR_3 = ROE_VALUE * RR_3
    #print(SGR_3)

    #print('\n')

    # Book Value per Share
    BVPS_0 = Total_stockholder_equity / Outstanding_shares
    #print(BVPS_0)

    #print('\n')

    # Market Book
    MB_0 = (MCAP_VALUE / Outstanding_shares) / BVPS_0
    #print(MB_0)
    #MB_1 = (MCAP_VALUE_0 / Outstanding_shares) / BVPS_0
    #print(MB_1)
    #MB_2 = Avg_P / BVPS_0
    #print(MB_2)

    #print('\n')

    # New Dividend Yield (DY) Formulas using MVPS
    DY_0 = DPS_VALUE / MVPS_0
    #print(DY_0)

    DY_0_00 = DPS_00 / MVPS_0
    #DY_0_01 = DPS_01 / MVPS_0
    DY_0_02 = DPS_02 / MVPS_0
    DY_0_03 = DPS_03 / MVPS_0
    #print(DY_0_00)
    #print(DY_0_01)
    #print(DY_0_02)
    #print(DY_0_03)

    DY_0_04 = DPS_10 / MVPS_0
    #DY_0_05 = DPS_11 / MVPS_0
    DY_0_06 = DPS_12 / MVPS_0
    DY_0_07 = DPS_13 / MVPS_0
    #print(DY_0_04)
    #print(DY_0_05)
    #print(DY_0_06)
    #print(DY_0_07)

    DY_0_08 = DPS_20 / MVPS_0
    #DY_0_09 = DPS_21 / MVPS_0
    DY_0_10 = DPS_22 / MVPS_0
    DY_0_11 = DPS_23 / MVPS_0
    #print(DY_0_08)
    #print(DY_0_09)
    #print(DY_0_10)
    #print(DY_0_11)

    #DY_0_12 = DPS_30 / MVPS_0
    #DY_0_13 = DPS_31 / MVPS_0
    #DY_0_14 = DPS_32 / MVPS_0
    #DY_0_15 = DPS_33 / MVPS_0
    #print(DY_0_12)
    #print(DY_0_13)
    #print(DY_0_14)
    #print(DY_0_15)

    #print('\n')
    # ()

    #DY_1 = DPS_VALUE / MVPS_1
    #print(DY_1)

    #DY_1_00 = DPS_00 / MVPS_1
    #DY_1_01 = DPS_01 / MVPS_1
    #DY_1_02 = DPS_02 / MVPS_1
    #DY_1_03 = DPS_03 / MVPS_1
    #print(DY_1_00)
    #print(DY_1_01)
    #print(DY_1_02)
    #print(DY_1_03)

    #DY_1_04 = DPS_10 / MVPS_1
    #DY_1_05 = DPS_11 / MVPS_1
    #DY_1_06 = DPS_12 / MVPS_1
    #DY_1_07 = DPS_13 / MVPS_1
    #print(DY_1_04)
    #print(DY_1_05)
    #print(DY_1_06)
    #print(DY_1_07)

    #DY_1_08 = DPS_20 / MVPS_1
    #DY_1_09 = DPS_21 / MVPS_1
    #DY_1_10 = DPS_22 / MVPS_1
    #DY_1_11 = DPS_23 / MVPS_1
    #print(DY_1_08)
    #print(DY_1_09)
    #print(DY_1_10)
    #print(DY_1_11)

    #DY_1_12 = DPS_30 / MVPS_1
    #DY_1_13 = DPS_31 / MVPS_1
    #DY_1_14 = DPS_32 / MVPS_1
    #DY_1_15 = DPS_33 / MVPS_1
    #print(DY_1_12)
    #print(DY_1_13)
    #print(DY_1_14)
    #print(DY_1_15)

    #print('\n')

    Equity_multiplier = Total_assets / Total_stockholder_equity
    #print(Equity_multiplier)
    Total_asset_turnover = Revenues / Total_assets
    #print(Total_asset_turnover)
    #    ·       Apply YOY, HA && VA Analysis

    ## TO BE CONTINUED (DEFINE SINGLE VARIABLES)
    
    
    
    
    
    
    
    
    
    
    
    ## ADD LIQUIDITY [LEVERAGE], SOLVENCY [LEVERAGE] AND EFFICIENCY RATIO [BS] [CSI]

    #Liquidity Ratio [BS] [CSI]

    #Current Ratio = Current Assets / Current Liabilities
    Cur_R = Current_assets / Current_liabilities
    print(Cur_R)
    #Quick Ratio = (Current Assets - Inventory) / Current Liabilities
    Inventory = Total_assets - Cash_and_cash_equivalents - Accounts_receivable
    QR = (Current_assets - Inventory) / Current_liabilities
    print(QR)
    #Cash Ratio = Cash / Current Liabilities
    Cas_R = Cash_and_cash_equivalents / Current_liabilities
    print(Cas_R)
    #Net Worth Capital (NWC) = Current Assets - Current Liabilities
    NWC = Current_assets - Current_liabilities
    print(NWC)
    #NWC to Total Assets = NWC / Total Assets
    NWC_TA = NWC / Total_assets
    print(NWC_TA)
    #Interval Measure = (Current Assets / Average Daily Operating Costs) / [Current Assets / [(COGS + Operating Expense) / 365]]
    IM = (Current_assets / Operating_income) / (Current_assets / ((Cost_of_revenues + Operating_income) / 365))
    print(IM)

    print('\n')

    #Solvency Ratios [BS] [CSI]

    #Debt Ratio (DR) = Total Debt / Total Assets
    Total_debt = Short_term_debt + Long_term_debt
    DR = Total_debt / Total_assets
    print(DR)
    #Equity Ratio = Total Equity / Total Assets
    ER = Total_stockholder_equity / Total_assets
    print(ER)
    #Debt-to-Equity Ratio = Total Debt / Total Equity
    DER = Total_debt / Total_stockholder_equity
    print(DER)
    #Equity Multiplier (Financial Leverage) = Total Assets / Total Equity
    EM = Total_assets / Total_stockholder_equity
    print(EM)
    #Fixed to Equity = Net Fixed Assets / Total Equity
    NFA = Total_assets - Current_assets
    FE = NFA / Total_stockholder_equity
    print(FE)
    #Long-Term Debt Ratio = Long-Term Debt / (Long-Term Debt + Total Equity)
    LTDR = Long_term_debt / (Long_term_debt + Total_stockholder_equity)
    print(LTDR)
    #Times Interest Earned (Interest Coverage) = EBIT / Interest
    Interest = - (Operating_income - Income_before_taxes)
    TIE = Operating_income / Interest
    print(TIE)
    #Cash Coverage = (EBIT + Depreciation) / Interest
    CC = (Operating_income + Depreciation) / Interest
    print(CC)
    #Debt Service Coverage Ratio  = (Operating Income / Total Debt Service Costs) / [Operating Income / (Interest + Principal)]
    Principal = Current_liabilities - Short_term_debt
    TDS = (Interest * (1 - Tax_VALUE)) + Principal
    DSCR = (Operating_income / TDS) / (Operating_income / (Interest + Principal))
    print(DSCR)

    print('\n')

    #Efficiency Ratios [BS] [CSI]

    #Inventory Turnover = COGS / Inventory
    IT = Cost_of_revenues / Inventory
    print(IT)
    #Day’s Sales in Inventory (Days Inventory Outstanding, or DIO) = 365 / Inventory Turnover
    DSI = 365 / IT
    print(DSI)
    #Receivables Turnover = Sales / Accounts Receivables
    Sales = Revenues - Operating_income - Cost_of_revenues - Research_Development
    RT = Sales / Accounts_receivable
    print(RT)
    #Day’s Sales in Receivables (Days Sales Outstanding, or DIO) = 365 / Receivables Turnover
    DSR = 365 / RT
    print(DSR)
    #Payables Turnover = COGS / Accounts Payable
    # Retrieve Accounts Payable from [BS]
    #PT = Cost_of_revenues / (...)
    #Day’s Sales in Payables (Days Payables Outstanding, or DIO) = 365 / Payables Turnover
    #Cash Conversion Cycle (CCC) = Day’s Sales in Inventory + Day’s Sales in Receivables - Day’s Sales in Payables
    #Total Asset Turnover (TATO) = Sales / Total Assets
    TATO = Sales / Total_assets
    print(TATO)
    #Capital Intensity = Total Assets / Sales
    CI = Total_assets / Sales
    print(CI)
    #Fixed Asset Turnover = Sales / Net Fixed Assets
    FAT = Sales / NFA
    print(FAT)
    #NWC Turnover = Sales / NWC
    NWCT = Sales / NWC
    print(NWCT)



    ## NOTES
    # Separate previous RATIOS into two sections: PROFITABILITY and MARKET VALUE RATIOS.
    # Separate new RATIOS into two, and three sub-sections.
    # Loop over all data
    # VERIFY ALL PROCESSED DATA (e.g. Date[1], Date[n-1], Date[n])

    # Start using PMP Course to write BUSINESS PLAN & STRATEGY intended for new STAKEHOLDERS.
    # Finish building prototype for all 10 companies.
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    EBIT_DEFAULT = Operating_income
    print(EBIT_DEFAULT) #Market Value
    EBITDA_DEFAULT = EBIT_DEFAULT - Depreciation - Amortization
    print(EBITDA_DEFAULT) #Market Value

    # () 

    EV_1_EBITDA_DEFAULT = EV_1_VALUE / EBITDA_DEFAULT
    print(EV_1_EBITDA_DEFAULT) #Market Value
    EV_2_EBITDA_DEFAULT = EV_2_VALUE / EBITDA_DEFAULT
    print(EV_2_EBITDA_DEFAULT) #Market Value

    print('\n')
    # () 

    DE_DEFAULT = (Long_term_debt + Short_term_debt) / EBITDA_DEFAULT
    print(DE_DEFAULT) #Solvency [Leverage]
    NE_DEFAULT = (Long_term_debt + Short_term_debt - Cash_and_cash_equivalents) / EBITDA_DEFAULT
    print(NE_DEFAULT) #Solvency [Leverage]

    FCF_3_VALUE = EBIT_VALUE_0 * (1 - Tax_VALUE) - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
    print(FCF_3_VALUE) #Solvency [Leverage]
    FCF_DEFAULT = EBIT_DEFAULT * (1 - Tax_VALUE) - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
    print(FCF_DEFAULT) #Solvency [Leverage]
    
    


    ### USE BOTH 'Outstanding_shares' & 'Class_A_and_Class_B_stocks' FOR RELATED RATIOS?
    
    #print('\n')
    
    
    d = {input_date_0[:-6]: [  
    
    
    # PROFITABILITY
    
                             'GPM_0', #Profitability
                             'OPM_0', #Profitability
                             'OPER_MARGIN_VALUE', #Profitability
                             'PM_0', #Profitability
                             'ROA_0', #Profitability
                             'ROI_0', #Profitability
                             'ROE_VALUE', #Profitability
                             'ROC_0', #Profitability
                             'ROCE_0', #Profitability
    
    
    # MARKET VALUE MEASURES
    
                             'EV_1_VALUE', #Market Value
                             'EV_2_VALUE', #Market Value
                             'EBIT_DEFAULT', ##############################
                             'EBIT_VALUE', #Market Value
                             'EBIT_VALUE_0', #Market Value
                             'EBITDA_DEFAULT', ##############################
                             'EBITDA_VALUE', #Market Value
                             'EBITDA_VALUE_0', #Market Value
                             'EV_1_EBITDA_VALUE', #Market Value
                             'EV_2_EBITDA_VALUE', #Market Value
                             'EV_1_EBITDA_VALUE_0', #Market Value
                             'EV_2_EBITDA_VALUE_0', #Market Value
                             'EV_1_EBITDA_DEFAULT', ##############################
                             'EV_2_EBITDA_DEFAULT', ##############################

                             'EPS_VALUE', #Market Value
                             'DPS_VALUE', #Market Value
                             'DPS_00', #Market Value
                             'DPS_02', #Market Value
                             'DPS_03', #Market Value
                             'DPS_10', #Market Value
                             'DPS_12', #Market Value
                             'DPS_13', #Market Value
                             'DPS_20', #Market Value
                             'DPS_22', #Market Value
                             'DPS_23', #Market Value
                             'PE_1_VALUE', #Market Value
                             'PE_2_0_VALUE', #Market Value
                             'PE_2_1_VALUE', #Market Value
                             'PE_00', #Market Value
                             'PE_01', #Market Value
                             'PE_02', #Market Value
                             ############################## MISSING DPO ##############################
    
                             'RR_0', #Market Value
                             'RR_2', #Market Value
                             'RR_3', #Market Value
                             'DY_1_VALUE', #Market Value
                             'DY_2_VALUE', #Market Value
                             'DY_2_VALUE_00', #Market Value
                             'DY_2_VALUE_02', #Market Value
                             'DY_2_VALUE_03', #Market Value
                             'DY_2_VALUE_04', #Market Value
                             'DY_2_VALUE_06', #Market Value
                             'DY_2_VALUE_07', #Market Value
                             'DY_2_VALUE_08', #Market Value
                             'DY_2_VALUE_10', #Market Value
                             'DY_2_VALUE_11', #Market Value
                             'DY_0', #Market Value
                             'DY_0_00', #Market Value
                             'DY_0_02', #Market Value
                             'DY_0_03', #Market Value
                             'DY_0_04', #Market Value
                             'DY_0_06', #Market Value
                             'DY_0_07', #Market Value
                             'DY_0_08', #Market Value
                             'DY_0_10', #Market Value
                             'DY_0_11', #Market Value
                             'Div_VALUE', #Market Value
                             'Div_VALUE_1', #Market Value
                             'Div_VALUE_2', #Market Value
                             'PSD_0', #Market Value

                             'MCAP_VALUE', #Market Value
                             'BV_0', #Market Value
                             'MB_0', #Market Value
                             'MVPS_0', #Market Value
                             'MVPS_PRICE_0', #Market Value
                             'BVPS_0', #Market Value
                             'SGR_0', #Market Value
                             'SGR_2', #Market Value
                             'SGR_3', #Market Value
                             'RD_VALUE', #Market Value
    
    
    # LEVERAGE
    
        # i) LIQUIDITY RATIOS
    
                             'Cur_R_VALUE', #Liquidity [Leverage]
                             'QR_1_VALUE', #Liquidity [Leverage]
                             'QR_2_VALUE', #Liquidity [Leverage]
                             'QR_VALUE', #Liquidity [Leverage]
                             'Cas_R_VALUE', #Liquidity [Leverage]
                             'NWC_VALUE', #Liquidity [Leverage]
                             'NWC_TA_VALUE', #Liquidity [Leverage]
                             'IM_VALUE', #Liquidity [Leverage]
    
    
        # ii) SOLVENCY RATIOS
    
                             'DE_VALUE', #Solvency [Leverage]
                             'DE_VALUE_0', #Solvency [Leverage]
                             'NE_VALUE_0', #Solvency [Leverage]
                             'DE_DEFAULT', ##############################
                             'NE_DEFAULT', ##############################
    
                             'DR_VALUE', #Solvency [Leverage]
                             'ER_VALUE', #Solvency [Leverage]
                             'DER_VALUE', #Solvency [Leverage]
                             'EM_VALUE', #Solvency [Leverage]
                             'FE_VALUE', #Solvency [Leverage]
                             'LTDR_VALUE', #Solvency [Leverage]
                             'TIE_VALUE', #Solvency [Leverage]
                             'CC_VALUE', #Solvency [Leverage]
                             'DSCR_VALUE', #Solvency [Leverage]
    
                             'EQUITY_MULTIPLIER', #Solvency [Leverage]
                             'Tax_VALUE', #Solvency [Leverage]
                             'FCF_0_VALUE', #Solvency [Leverage]
                             'FCF_1_VALUE', #Solvency [Leverage]
                             'FCF_2_VALUE', #Solvency [Leverage]
                             'FCF_3_VALUE', ##############################
                             'FCF_DEFAULT', ##############################
    
    
    # EFFICIENCY
    
                             'IT_VALUE', #Efficiency
                             'DSI_VALUE', #Efficiency
                             'RT_VALUE', #Efficiency
                             'DSR_VALUE', #Efficiency
                             'TOT_ASSET_TURNOVER', #Efficiency
                             'TATO_VALUE', #Efficiency
                             'CI_VALUE', #Efficiency
                             'FAT_VALUE', #Efficiency
                            'NWCT_VALUE'], #Efficiency

##########################################################################################
     
         'Financial Ratio /unit': [
             
    # PROFITABILITY
    
                             GPM_0, #Profitability
                             OPM_0, #Profitability
                             OperatingMargin_VALUE, #Profitability
                             PM_0, #Profitability
                             ROA_0, #Profitability
                             ROI_0, #Profitability
                             ROE_VALUE, #Profitability
                             ROC_0, #Profitability
                             ROCE_0, #Profitability
    
    
    # MARKET VALUE MEASURES
    
                             EV_1_VALUE, #Market Value
                             EV_2_VALUE, #Market Value
                             EBIT_DEFAULT, ##############################
                             EBIT_VALUE, #Market Value
                             EBIT_VALUE_0, #Market Value
                             EBITDA_DEFAULT, ##############################
                             EBITDA_VALUE, #Market Value
                             EBITDA_VALUE_0, #Market Value
                             EV_1_EBITDA_VALUE, #Market Value
                             EV_2_EBITDA_VALUE, #Market Value
                             EV_1_EBITDA_VALUE_0, #Market Value
                             EV_2_EBITDA_VALUE_0, #Market Value
                             EV_1_EBITDA_DEFAULT, ##############################
                             EV_2_EBITDA_DEFAULT, ##############################

                             EPS_VALUE, #Market Value
                             DPS_VALUE, #Market Value
                             DPS_00, #Market Value
                             DPS_02, #Market Value
                             DPS_03, #Market Value
                             DPS_10, #Market Value
                             DPS_12, #Market Value
                             DPS_13, #Market Value
                             DPS_20, #Market Value
                             DPS_22, #Market Value
                             DPS_23, #Market Value
                             PE_1_VALUE, #Market Value
                             PE_2_0_VALUE, #Market Value
                             PE_2_1_VALUE, #Market Value
                             PE_00, #Market Value
                             PE_01, #Market Value
                             PE_02, #Market Value
                             ############################## MISSING DPO ##############################
    
                             RR_0, #Market Value
                             RR_2, #Market Value
                             RR_3, #Market Value
                             DY_1_VALUE, #Market Value
                             DY_2_VALUE, #Market Value
                             DY_2_VALUE_00, #Market Value
                             DY_2_VALUE_02, #Market Value
                             DY_2_VALUE_03, #Market Value
                             DY_2_VALUE_04, #Market Value
                             DY_2_VALUE_06, #Market Value
                             DY_2_VALUE_07, #Market Value
                             DY_2_VALUE_08, #Market Value
                             DY_2_VALUE_10, #Market Value
                             DY_2_VALUE_11, #Market Value
                             DY_0, #Market Value
                             DY_0_00, #Market Value
                             DY_0_02, #Market Value
                             DY_0_03, #Market Value
                             DY_0_04, #Market Value
                             DY_0_06, #Market Value
                             DY_0_07, #Market Value
                             DY_0_08, #Market Value
                             DY_0_10, #Market Value
                             DY_0_11, #Market Value
                             Div_VALUE, #Market Value
                             Div_VALUE_1, #Market Value
                             Div_VALUE_2, #Market Value
                             PSD_0, #Market Value

                             MCAP_VALUE, #Market Value
                             BV_0, #Market Value
                             MB_0, #Market Value
                             MVPS_0, #Market Value
                             MVPS_PRICE_0, #Market Value
                             BVPS_0, #Market Value
                             SGR_0, #Market Value
                             SGR_2, #Market Value
                             SGR_3, #Market Value
                             Research_Development, #Market Value
    
    
    # LEVERAGE
    
        # i) LIQUIDITY RATIOS
    
                             Cur_R, #Liquidity [Leverage]
                             QR_1_VALUE, #Liquidity [Leverage]
                             QR_2_VALUE, #Liquidity [Leverage]
                             QR, #Liquidity [Leverage]
                             Cas_R, #Liquidity [Leverage]
                             NWC, #Liquidity [Leverage]
                             NWC_TA, #Liquidity [Leverage]
                             IM, #Liquidity [Leverage]
    
    
        # ii) SOLVENCY RATIOS
    
                             DE_VALUE, #Solvency [Leverage]
                             DE_VALUE_0, #Solvency [Leverage]
                             NE_VALUE_0, #Solvency [Leverage]
                             DE_DEFAULT, ##############################
                             NE_DEFAULT, ##############################
    
                             DR, #Solvency [Leverage]
                             ER, #Solvency [Leverage]
                             DER, #Solvency [Leverage]
                             EM, #Solvency [Leverage]
                             FE, #Solvency [Leverage]
                             LTDR, #Solvency [Leverage]
                             TIE, #Solvency [Leverage]
                             CC, #Solvency [Leverage]
                             DSCR, #Solvency [Leverage]
    
                             Equity_multiplier, #Solvency [Leverage]
                             Tax_VALUE, #Solvency [Leverage]
                             FCF_0_VALUE, #Solvency [Leverage]
                             FCF_1_VALUE, #Solvency [Leverage]
                             FCF_2_VALUE, #Solvency [Leverage]
                             FCF_3_VALUE, ##############################
                             FCF_DEFAULT, ##############################
    
    
    # EFFICIENCY
    
                             IT, #Efficiency
                             DSI, #Efficiency
                             RT, #Efficiency
                             DSR, #Efficiency
                             Total_asset_turnover, #Efficiency
                             TATO, #Efficiency
                             CI, #Efficiency
                             FAT, #Efficiency
                             NWCT #Efficiency
             
         ]}
    
    df= pd.DataFrame(data=d)
    #print(df)
    
    filename = input_date_0[:-6] + "-Ratio-DF.csv"
    df.to_csv(filename)


# In[ ]:





# In[ ]:


#S2 _ CSV Combined Ratio & [-3] Alphabet


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
for file in os.listdir(mydir):
    if file.endswith("-Ratio-DF.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_0 = sorted(result)
#sorted_list_0


# In[ ]:





# In[ ]:


import os
import pandas as pd
import numpy as np

mydir = os.getcwd()

result = []
for file in os.listdir(mydir):
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


file = pd.read_csv('Alphabet Inc.csv')

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
    df.to_csv(end_date + "-Alphabet.csv")


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


file_0 = pd.read_csv(sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)

title = sorted_list_0[0][:-13]
file_0 = file_0.set_axis(['Financial Ratio', title], axis=1, inplace=False)
file_0


# In[ ]:


print(sorted_list_0[1])
file_1 = pd.read_csv(sorted_list_0[1])
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
file_3 = pd.read_csv(sorted_list_0[2])
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


file_0 = pd.read_csv(sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)
title = sorted_list_0[0][:-13]
file_0 = file_0.set_axis(['Financial Ratio', title], axis=1, inplace=False)
print(file_0)

sorted_list_1 = sorted_list_0[1:]
#print(sorted_list_1)

length = len(sorted_list_1)
for i in range(length):
    print(sorted_list_1[i])
    file_1 = pd.read_csv(sorted_list_1[i])
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
    
    file_0.to_csv('Combined_Ratio.csv')
    
    


# In[ ]:





# In[ ]:


#S3 _ CSV Loop.Ratio-TF


# In[ ]:


#Variables-DF => Build Full Table

import os

mydir = os.getcwd()

result = []
for file in os.listdir(mydir):
    if file.endswith("-Alphabet.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_0 = sorted(result)
#sorted_list_0


# In[ ]:


length = len(sorted_list_0)
print(length)


# In[ ]:


import pandas as pd
import numpy as np




for i in range(length):
    
    
    file = pd.read_csv(sorted_list_0[i])
    file = file.drop(file.columns[0], axis=1)
    
    
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
    
    
    end_week = file_1.loc[file_1['Weekday'] == 'Friday']
    col_one_list = end_week['Date'].tolist()
    
    
    file_2 = file_1.set_index('Date')
    length = len(col_one_list)
    for j in range(length):
        #print(file_2.at[col_one_list[i], 'Adj Close'])
        #print(file_2.index.get_loc(col_one_list[i]))
        if file_2.index.get_loc(col_one_list[j]) >=5:
            #print("Enough data to calculate past week's Adj.Avg")
            AdjClose = file_2.at[col_one_list[j], 'Adj Close']
            #print(AdjClose)
            Index = file_2.index.get_loc(col_one_list[j])
            #print(Index)
            index1 = int(Index)-1
            index2 = int(Index)-2
            index3 = int(Index)-3
            index4 = int(Index)-4
            index_ls = list(file_2.index)
            #print(index_ls[index1])
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
            High = file_2.at[col_one_list[j], 'High']
            V5 = file_2.at[index_ls[index1], 'High']
            V6 = file_2.at[index_ls[index2], 'High']
            V7 = file_2.at[index_ls[index3], 'High']
            V8 = file_2.at[index_ls[index4], 'High']
            Low = file_2.at[col_one_list[j], 'Low']
            V9 = file_2.at[index_ls[index1], 'Low']
            V10 = file_2.at[index_ls[index2], 'Low']
            V11 = file_2.at[index_ls[index3], 'Low']
            V12 = file_2.at[index_ls[index4], 'Low']
            A4 = N_days * ((max(High, V5, V6, V7, V8) - min(Low, V9, V10, V11, V12))**2)
            A5 = (A4 / A1) * 100
            A6 = (A1 - min(Low, V9, V10, V11, V12))/(max(High, V5, V6, V7, V8) - min(Low, V9, V10, V11, V12))
            #OPEN CLOSE VALUES N-4
            Open = file_2.at[col_one_list[j], 'Open']
            V13 = file_2.at[index_ls[index1], 'Open']
            V14 = file_2.at[index_ls[index2], 'Open']
            V15 = file_2.at[index_ls[index3], 'Open']
            V16 = file_2.at[index_ls[index4], 'Open']
            Close = file_2.at[col_one_list[j], 'Close']
            V17 = file_2.at[index_ls[index1], 'Close']
            V18 = file_2.at[index_ls[index2], 'Close']
            V19 = file_2.at[index_ls[index3], 'Close']
            V20 = file_2.at[index_ls[index4], 'Close']
            A7 = N_days * ((max(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20) - min(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20))**2)
            A8 = (A7 / A1) * 100
            A9 = (A1 - min(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20))/(max(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20) - min(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20))
            A10 = (A1 - min(AdjClose, V0, V1, V2, V3))/(max(AdjClose, V0, V1, V2, V3) - min(AdjClose, V0, V1, V2, V3))
            file_2.at[col_one_list[j], 'Adj.Avg'] = A1
            file_2.at[col_one_list[j], 'Std.Dev'] = A2
            file_2.at[col_one_list[j], 'CV'] = A3
            file_2.at[col_one_list[j], 'H-L-Std.Dev'] = A4
            file_2.at[col_one_list[j], 'H-L-CV'] = A5
            file_2.at[col_one_list[j], 'H-L-Diff.'] = A6
            file_2.at[col_one_list[j], 'O-C-Std.Dev'] = A7
            file_2.at[col_one_list[j], 'O-C-CV'] = A8
            file_2.at[col_one_list[j], 'O-C-Diff.'] = A9
            file_2.at[col_one_list[j], 'Norm.'] = A10
        else:
            print("Not enough data to calculate past week's Adj.Avg")
    file_2 = file_2.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume', 'Weekday'])
    
    
    file_2['Adj.Avg'].replace('', np.nan, inplace=True)
    file_2 = file_2.dropna(subset=['Adj.Avg'])
    file_2.to_csv(sorted_list_0[i][:-13] + "-Ratio-TF.csv")
    print(sorted_list_0[i])
    #print(i)
    print(file_2)


# In[ ]:





# In[ ]:


#S4 _ CSV DF Analysis


# In[ ]:


## WEEK 4

# https://canvas.uts.edu.au/courses/18711/pages/online-workshop-schedule


# In[ ]:


import os
import pandas as pd

mydir = os.getcwd()

result = []
for file in os.listdir(mydir):
    if file.endswith("-Alphabet.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_0 = sorted(result)
#sorted_list_0


# In[ ]:


length = len(sorted_list_0)

for i in range(length):
    
    if i == 0:
        file = pd.read_csv(sorted_list_0[i])

        size = len(file.index)
        size_1 = size - 1
        file = file.drop(labels=range(0,size_1), axis=0)
        file_1 = file
        
    else:
        file = pd.read_csv(sorted_list_0[i])
        size = len(file.index)
        size_1 = size - 1
        file = file.drop(labels=range(0,size_1), axis=0)
        file_1 = file_1.append(file)

file_1.drop(columns=file_1.columns[0], axis=1, inplace=True)
file_1.to_csv('Alphabet-Ending-Months.csv', index=False)
#print(len(file_1))
#file_1


# In[ ]:


import os
import pandas as pd

mydir = os.getcwd()

result = []
for file in os.listdir(mydir):
    if file.endswith("-Ratio-DF.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_0 = sorted(result)
sorted_list_0


# In[ ]:


file_0 = pd.read_csv(sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)

title = sorted_list_0[0][:-13]
file_0 = file_0.set_axis(['Financial Ratio', title], axis=1, inplace=False)
file_0


sorted_list_0.remove(sorted_list_0[0])
length = len(sorted_list_0)

for i in range(length):
    input_date = sorted_list_0[i]
    
    
    
    file_1 = pd.read_csv(sorted_list_0[i])
    file_1 = file_1.drop(file_1.columns[0], axis=1)
    file_1 = file_1.drop(file_1.columns[0], axis=1)

    title = sorted_list_0[i][:-13]
    
    file_1.rename({'Financial Ratio /unit': title}, axis=1, inplace=True)

    file_2 = file_0.append(file_1)
    
    #file_2[title] = file_2[title].shift(-26)
    file_2[title] = file_2[title].shift(-116)
    file_0 = file_2[file_2['Financial Ratio'].notna()]

filename = "-All-Ratios.csv"
file_0.to_csv("Y" + filename)

file_0 = file_0.T
file_0.to_csv("X" + filename)

file_0


# In[ ]:


import os
import pandas as pd
import numpy as np

mydir = os.getcwd()

result = []
for file in os.listdir(mydir):
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





# In[ ]:


file = pd.read_csv('Alphabet Inc.csv')

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
    df.to_csv(end_date + "-Alphabet.csv")


# In[ ]:


### USE METHOD HERE-ABOVE
### IGNORE METHODS PRESENTED BELOW


# In[ ]:


file = pd.read_csv('Alphabet Inc.csv')

## TRY STATEMENT FOR date_input-29 -28 -27 -26...

result = []

for i in range(length):
    input_date = sorted_list_0[i][:-13]
    
    date_prefix = ls[i][:-2]

    date_ls = ["31", "30", "29", "28"]

    upd_date_0 = date_prefix + date_ls[0]
    upd_date_1 = date_prefix + date_ls[1]
    upd_date_2 = date_prefix + date_ls[2]
    upd_date_3 = date_prefix + date_ls[3]

    #print(date_prefix)
    #print(upd_date_0)
    
    
    
    if upd_date_0 in file.values:
        col_one_arr_P = file[file['Date'].str.contains(upd_date_0)].to_numpy()
        #print(upd_date_0 + " exists.")
        index = file[file['Date'] == upd_date_0].index[0]
        result.append(index)
        
        #print('\n')
        
    else:
        if upd_date_1 in file.values:
            col_one_arr_P = file[file['Date'].str.contains(upd_date_1)].to_numpy()
            #print("Month finishes in -30")
            index = file.loc[file['Date']==upd_date_1]
            index = file[file['Date'] == upd_date_1].index[0]
            #index = file[file['Date'] == upd_date_1].index.to_numpy()
            #print(index)
            result.append(index)
            
            #print('\n')
            
        else:
            if upd_date_2 in file.values:
                col_one_arr_P = file[file['Date'].str.contains(upd_date_2)].to_numpy()
                #print("Month finishes in -29")
                index = file[file['Date'] == upd_date_2].index[0]
                result.append(index)
                
                #print('\n')
                
            else:
                if upd_date_3 in file.values:
                    col_one_arr_P = file[file['Date'].str.contains(upd_date_3)].to_numpy()
                    #print("Month finishes in -28")
                    index = file[file['Date'] == upd_date_3].index[0]
                    result.append(index)
                    
                    #print('\n')
                    

print(result)


# In[ ]:





# In[ ]:


#combined_csv = pd.concat([pd.read_csv(f) for f in sorted_list_0 ])
#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')


# In[ ]:


#file_0 = pd.read_csv(sorted_list_0[0])
#file_0 = file_0.drop(file_0.columns[0], axis=1)

#title = sorted_list_0[0][:-13]
#file_0 = file_0.set_axis(['Financial Ratio', title], axis=1, inplace=False)
#file_0


# In[ ]:


#file_1 = pd.read_csv(sorted_list_0[1])
#file_1 = file_1.drop(file_1.columns[0], axis=1)
#file_1 = file_1.drop(file_1.columns[0], axis=1)

#title = sorted_list_0[1][:-13]
#file_1.rename({'Financial Ratio /unit': title}, axis=1, inplace=True)
#file_1

#file_2 = file_0.append(file_1)
#file_2[title] = file_2[title].shift(-25)
#file_2 = file_2[file_2['Financial Ratio'].notna()]
#file_2
#file_0.join(file_1)


# In[ ]:


#file_3 = pd.read_csv(sorted_list_0[2])
#file_3 = file_3.drop(file_3.columns[0], axis=1)
#file_3 = file_3.drop(file_3.columns[0], axis=1)

#title = sorted_list_0[2][:-13]
#file_3.rename({'Financial Ratio /unit': title}, axis=1, inplace=True)
#file_3

#file_4 = file_2.append(file_3)
#file_4[title] = file_4[title].shift(-25)
#file_4 = file_4[file_4['Financial Ratio'].notna()]
#file_4
#file_0.join(file_1)


# In[ ]:


file = pd.read_csv('X-All-Ratios.csv')
#print(len(file))

#new_header = file.iloc[0]
#file = file[1:]
#file.columns = new_header
#print(len(file))

new_header = file.iloc[0]
file = file[1:]
file.columns = new_header


# In[ ]:


file_1 = pd.read_csv('Alphabet-Ending-Months.csv')
#print(file_1)

file_2 = file_1.reset_index()
file_2.drop(columns=file_2.columns[0], axis=1, inplace=True)
file_2.drop(columns=file_2.columns[0], axis=1, inplace=True)
#print(file_2)
numbers = file_2["Open"]
#file = file.join(numbers)
numbers_0 = numbers.squeeze()
#print(numbers)


# In[ ]:


file = file.reset_index()
file.drop(columns=file.columns[0], axis=1, inplace=True)
result = pd.concat([file, numbers_0], axis=1)

numbers = file_2["High"]
numbers_0 = numbers.squeeze()
result = pd.concat([result, numbers_0], axis=1)

numbers = file_2["Low"]
numbers_0 = numbers.squeeze()
result = pd.concat([result, numbers_0], axis=1)

numbers = file_2["Close"]
numbers_0 = numbers.squeeze()
result = pd.concat([result, numbers_0], axis=1)

numbers = file_2["Adj Close"]
numbers_0 = numbers.squeeze()
result = pd.concat([result, numbers_0], axis=1)

numbers = file_2["Volume"]
numbers_0 = numbers.squeeze()
result = pd.concat([result, numbers_0], axis=1)


# In[ ]:


result.to_csv('Alphabet-DF-Analysis.csv', index=False)


# In[ ]:





# In[ ]:


#S5 _ CSV Ratio-TF-Variables && Correlation


# In[ ]:


import numpy as np
import pandas as pd
import sklearn as sk


# In[ ]:


#Variables-DF => Build Full Table

import os

mydir = os.getcwd()

result = []
for file in os.listdir(mydir):
    if file.endswith("-Variables-DF.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_0 = sorted(result)
#sorted_list_0


# In[ ]:


file_0 = pd.read_csv(sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)
#print(file_0)

title = sorted_list_0[0][:-17]
file_0 = file_0.set_axis(['Financial Variable', title], axis=1, inplace=False)
#file_0


# In[ ]:


#print(sorted_list_0[1])
file_1 = pd.read_csv(sorted_list_0[1])
file_1 = file_1.drop(file_1.columns[0], axis=1)
file_1 = file_1.drop(file_1.columns[0], axis=1)
#print(file_1)

title = sorted_list_0[1][:-17]
file_1.rename({'Financial Variables /unit': title}, axis=1, inplace=True)
#print(file_1)

#file_2 = file_0.append(file_1)
##file_2[title] = file_2[title].shift(-25)
#file_2 = file_2[file_2['Financial Ratio'].notna()]
#print(file_2)
file_0 = file_0.join(file_1)
#print(file_0)


# In[ ]:


#print(sorted_list_0[2])
file_3 = pd.read_csv(sorted_list_0[2])
file_3 = file_3.drop(file_3.columns[0], axis=1)
file_3 = file_3.drop(file_3.columns[0], axis=1)
#file_3.rename({'Financial Variables /unit': title}, axis=1, inplace=True)

title = sorted_list_0[2][:-17]
#print(file_3)

#file_2 = file_0.append(file_1)
##file_2[title] = file_2[title].shift(-25)
#file_2 = file_2[file_2['Financial Ratio'].notna()]
#print(file_2)
file_0 = file_0.join(file_3)
#print(file_0)


# In[ ]:


#combined_csv = pd.concat([pd.read_csv('Alphabet Inc (GOOG)/' + f) for f in sorted_list_0 ])
#combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')


file_0 = pd.read_csv(sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)
title = sorted_list_0[0][:-17]
file_0 = file_0.set_axis(['Financial Variable', title], axis=1, inplace=False)
print(file_0)

sorted_list_1 = sorted_list_0[1:]
#print(sorted_list_1)

length = len(sorted_list_1)
for i in range(length):
    print(sorted_list_1[i])
    file_1 = pd.read_csv(sorted_list_1[i])
    file_1 = file_1.drop(file_1.columns[0], axis=1)
    file_1 = file_1.drop(file_1.columns[0], axis=1)

    title = sorted_list_1[i][:-17]
    file_1.rename({'Financial Variables /unit': title}, axis=1, inplace=True)
    print(file_1)

    #file_2 = file_0.append(file_1)
    ##file_2[title] = file_2[title].shift(-25)
    #file_2 = file_2[file_2['Financial Ratio'].notna()]
    #print(file_2)
    file_0 = file_0.join(file_1)
    print(file_0)
    
    file_0.to_csv('Combined_Variable.csv')
    
file_2 = file_0.T
file_2.to_csv("Combined_Variable-X-All.csv")

file_2
   


# In[ ]:





# In[ ]:


#Ratio-TF => Build Full Table

import os
import pandas as pd

mydir = os.getcwd()

result = []
for file in os.listdir(mydir):
    if file.endswith("-Ratio-TF.csv"):
        result.append(os.path.join(file))
        #print(os.path.join(file))
        
sorted_list_0 = sorted(result)
sorted_list_0


# In[ ]:


file_0 = pd.read_csv(sorted_list_0[0])
#file_0 = file_0.iloc[1: , :]
# ERROR DELETE TOP AXIS (X)(ROW) INSTEAD OF FIRST ROW INSIDE DF

title = sorted_list_0[0][:-13]
#file_0 = file_0.set_axis([':: TECHNICAL RATIO ::', 'Adj Close', 'Adj.Avg', 'Std.Dev', 'CV', 'H-L-Std.Dev', 'H-L-CV', 'H-L-Diff.', 'O-C-Std.Dev', 'O-C-CV', 'O-C-Diff.', 'Norm.'], axis=1, inplace=False)
#file_0.columns.name = ':: TECHNICAL RATIO ::'
print(file_0)


sorted_list_0.remove(sorted_list_0[0])
length = len(sorted_list_0)

for i in range(length):
    print(sorted_list_0[i])
    print(i)
    input_date = sorted_list_0[i]
    
    
    
    file_1 = pd.read_csv(sorted_list_0[i])
    #file_1 = file_1.drop(file_1.columns[0], axis=1)
    #file_1 = file_1.drop(file_1.columns[0], axis=1)

    title = sorted_list_0[i][:-13]
    
    #file_1.rename({'Financial Ratio /unit': title}, axis=1, inplace=True)
    
    if i == 0:
        file_2 = file_0.append(file_1)
        print(file_2)
    else:
        file_2 = file_2.append(file_1)
        print(file_2)
    
    
    #file_2[title] = file_2[title].shift(-26)
    #file_2[title] = file_2[title].shift(-116)
    #file_0 = file_2[file_2['Financial Ratio'].notna()]

filename = "-All-Ratios.csv"
file_2.to_csv("S5 _ Y" + filename, index=False, encoding='utf-8-sig')

file_2 = file_2.T
file_2.to_csv("S5 _ X" + filename, header=False, encoding='utf-8-sig')

file_2


# In[ ]:





# In[ ]:


dir = os.path.join("","S5 _ CSV z.##")
if not os.path.exists(dir):
    os.mkdir(dir)


# In[ ]:


data = pd.read_csv("Alphabet-DF-Analysis.csv")
data.columns


# In[ ]:


#pd.set_option('display.max_columns', None)


# In[ ]:


# Performing a Standard scaler transform of the Abalone dataset

from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot
#std_scaler = StandardScaler()
#data_ = std_scaler.fit_transform(data)

# convert the array back to a dataframe

#dataset = pd.DataFrame(data,columns=['GPM_0','OPM_0', 'OPER_MARGIN_VALUE', 'PM_0', 'ROA_0',
       #'ROI_0', 'ROE_VALUE', 'ROC_0', 'ROCE_0', 'EV_1_VALUE', 'EV_2_VALUE', 'EBIT_DEFAULT', 
        #'EBIT_VALUE', 'EBIT_VALUE_0', 'EBITDA_DEFAULT', 'EBITDA_VALUE', 'EBITDA_VALUE_0',
        #'EV_1_EBITDA_VALUE', 'EV_2_EBITDA_VALUE', 'EV_1_EBITDA_VALUE_0', 'EV_2_EBITDA_VALUE_0',
        #'EV_1_EBITDA_DEFAULT', 'EV_2_EBITDA_DEFAULT', 'EPS_VALUE', 'DPS_VALUE', ...####### ])

dataset = pd.DataFrame(data)
#print(dataset)
        
# summarize
dis_summary = dataset.describe()
print(dis_summary)
dis_summary.to_csv('S5 _ CSV z.##/P1 _ Distribution.csv')

# histograms of the variables
dataset.hist()
#pyplot.show()

# Check mean & Standard dev


# In[ ]:


dis00 = pd.DataFrame(data,columns=['GPM_0'])
dis00 = dis00.hist()


#pyplot.show()


# In[ ]:





# In[ ]:


correlation_df = data.corr()
print(correlation_df)
correlation_df.to_csv('S5 _ CSV z.##/P2 _ Correlation.csv')

#Look at Correlations for [High][Low][Close][Adj Close][Volume] -> Financial Ratios IS  0.4 < x < -0.4
#TBD


# In[ ]:


############ A1_LR ############

# TO ADJUST
# FOLDER LOCATION AND FILE RETRIEVAL IS NOT OPTIMIZED IN THE FOLLOWING CODE
# CHECK print() FUNCTIONS


# In[ ]:


import pandas as pd


# In[ ]:


df = pd.read_csv("P2 _ Correlation.csv")
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
df = pd.read_csv("P2 _ Correlation.csv")
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

print(PC_List_Ind_0)

length = len(NC_List_Ind)
#print(length)
NC_List_Ind_0 = []

for i in range(length):
    index_int = str(NC_List_Ind[i])
    #print(index_int)
    index_int = index_int.replace("[", "") ## CHANGE TO INT
    index_int = index_int.replace("]", "") ## CHANGE TO INT
    index_int = int(index_int) ## CHANGE TO INT
    index_int = index_int + 1 ## ADD '1' AS INT TO ALL ELEMENTS IN LIST (SHIFT IN INDEX(n)) _ SEE "aima-data/R_DF_Analysis.csv"
    NC_List_Ind_0.append(index_int) ## APPEND TO NEW INT_LIST
    #int(index_int)

print(NC_List_Ind_0)


# In[ ]:



### TO DO ###




