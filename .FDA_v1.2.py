#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# THIS DOCUMENT REFERS TO FINANCIAL DATA ANALYSIS SOFTWARE AIMED AT PREDICTING STOCK PRICE OF COMPANY X.
# IT RUNS OVER QUATERLY AND ANNUAL FINANCIAL STATEMENTS DOWNLOADED ON SEC.GOV WEBSITE FOR ALPHABET COMPANY.
# URL: https://www.sec.gov/edgar/browse/?CIK=1652044&owner=exclude

# TO RUN THE SOFTWARE PROPERLY, DOWNLOAD ALL FINANCIAL STATEMENTS AND RENAME BY [DATE] IN ONE SAME FOLDER

# SOFTWARE UPDATES NEED TO BE CONDUCTED TO ESTABLISH:
# *SIMPLIFIED SOFTWARE
# *DYNAMIC SOFTWARE
# (ADD FUNCTIONS)
# (ADD DESCRIPTIONS, PREDICTED OUTPUTS)
# (ADD VARIABLES, CORRESPONDING NAMES) & *ALSO CHECK FOR OTHER FUNCTIONS BEING CALLED


# In[ ]:


# S1 _ XLSX Worksheets (CORRESPONDS TO EXTRACTING ALL RELEVANT WORKSHEETS FROM EXCEL DOCUMENTS)
# * [OUTPUTS] :: BALANCE SHEET, STATEMENT OF INCOME, STATEMENT OF CASH FLOW
# *ONLY KEEP XLSX DOCUMENTS FROM SEC.GOV
# *REMOVE XLS DOCUMENTS (DUE TO INCOMPATIBLE FORMAT)


# In[ ]:


# IMPORT ALL RELEVANT LIBRARIES
import glob
import os

import numpy as np
import pandas as pd
import sklearn as sk

from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot


# In[ ]:


# INITIALIZE LIST TO LOOP OVER ALL RELEVANT DOCUMENTS
result = []

# SPECIFY DIRECTORY TO CURRENT FOLDER
mydir = os.getcwd()

# VERIFY FOR DOCUMENTS IN '.xlsx' FORMAT AND UPDATE LIST 'result'. SORTED[LIST]
for file in os.listdir(mydir):
    if file.endswith(".xlsx"):
        result.append(os.path.join(file))
        
sorted_list = sorted(result)


# In[ ]:


# SPECIFY LENGTH OF INITIALIZED LIST TO LOOP OVER ALL RELEVANT DOCUMENTS
length = len(sorted_list)

for i in range(length):
    input_date = sorted_list[i]
    
    # UPDATE URL() TO SPECIFY CURRENT DOCUMENT
    url = input_date
    file = pd.read_excel(url)
    
#### *NEXT ARGUMENT CAN BE SIMPLIFIED. CREATE FUNCTION WITH CORRESPONDING PARAMETERS
    # BALANCE SHEET, INCOME STATEMENT AND CASH FLOW STATEMENT ARE ALWAYS LOCATED WITHIN 8th FIRST WORKSHEETS
    s_0 = pd.read_excel(url, sheet_name=0)
    s_1 = pd.read_excel(url, sheet_name=1)
    s_2 = pd.read_excel(url, sheet_name=2)
    s_3 = pd.read_excel(url, sheet_name=3)
    s_4 = pd.read_excel(url, sheet_name=4)
    s_5 = pd.read_excel(url, sheet_name=5)
    s_6 = pd.read_excel(url, sheet_name=6)
    s_7 = pd.read_excel(url, sheet_name=7)
    
#### *NEXT ARGUMENT CAN BE SIMPLIFIED. CREATE FUNCTION WITH CORRESPONDING PARAMETERS
#### *CALL VARIABLES FROM PREVIOUS FUNCTIONS s_0, s_1, ..., s_7

    # STARTING WITH 1st WORKSHEET, CHECK IF TITLE CORRESPONDS TO EITHER [BS], [CSI] OR [CSCF]
    # S_0 = WORKSHEET[0].
    colname = s_0.columns[0]
    # CHECK BALANCE SHEET, STATEMENT OF INCOME, STATEMENT OF CASH FLOW ('else if' RATHER THAN 'if'??)
    # SPECIFY THE EXACT NAME OF WORKSHEET IS REQUIRED FOR EXTRACTION
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        BS = s_0
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        CSI = s_0
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        CSCF = s_0
    
    # SAME, BUT WITH WORKSHEET[1]
    colname = s_1.columns[0]
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        BS = s_1
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        CSI = s_1
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        CSCF = s_1
    
    # SAME, BUT WITH WORKSHEET[2]
    colname = s_2.columns[0]
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        BS = s_2
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        CSI = s_2
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        CSCF = s_2
    
    # SAME, BUT WITH WORKSHEET[3]
    colname = s_3.columns[0]
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        BS = s_3
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        CSI = s_3
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        CSCF = s_3
    
    # SAME, BUT WITH WORKSHEET[4]
    colname = s_4.columns[0]
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        BS = s_4
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        CSI = s_4
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        CSCF = s_4
    
    # SAME, BUT WITH WORKSHEET[5]
    colname = s_5.columns[0]
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        BS = s_5
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        CSI = s_5
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        CSCF = s_5
    
    # SAME, BUT WITH WORKSHEET[6]
    colname = s_6.columns[0]
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        BS = s_6
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        CSI = s_6
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        CSCF = s_6
        
    # SAME, BUT WITH WORKSHEET[7]
    colname = s_7.columns[0]
    if colname == 'CONSOLIDATED BALANCE SHEETS - USD ($) $ in Millions':
        BS = s_7
    if colname == 'CONSOLIDATED STATEMENTS OF INCOME - USD ($) $ in Millions':
        CSI = s_7
    if colname == 'CONSOLIDATED STATEMENTS OF CASH FLOWS - USD ($) $ in Millions':
        CSCF = s_7
    
    # SAVE OUTPUTS (BS, CSI, CSCF) AS '-0.csv', '-1.csv', '-2.csv' RESPECTIVELY
    BS.to_csv(url[:-5] + '-0.csv', index = False)
    CSI.to_csv(url[:-5] + '-1.csv', index = False)
    CSCF.to_csv(url[:-5] + '-2.csv', index = False)


# In[ ]:


# S2 _ Financial Variables & Ratios (CORRESPONDS TO EXTRACTING ALL RELEVANT VALUES FROM XLSX)
# * [OUTPUTS] :: COMPANY X's VARIABLE-DF, RATIOS-DF & RATIOS-TF (FUNDAMENTAL AND TECHNIAL ANALYSIS)
# * '-DF' REFERING TO FUNDAMENTAL & '-TF' REFERING TO TECHNICAL
# * LOOP OVER ALL XLSX


# In[ ]:


# RESET LIST 'result[]' (NEW LIST)
result = []

# VERIFY FOR DOCUMENTS ENDING IN '-0.xlsx' (BALANCE SHEET) AND UPDATE LIST 'result'. SORTED[LIST]
for file in os.listdir(mydir):
    if file.endswith("-0.csv"):
        result.append(os.path.join(file))
        
sorted_list_0 = sorted(result)

# SAME, BUT FOR DOCUMENTS ENDING IN '-1.xlsx' (STATEMENT OF INCOME)
result = []
for file in os.listdir(mydir):
    if file.endswith("-1.csv"):
        result.append(os.path.join(file))
        
sorted_list_1 = sorted(result)

# SAME, BUT FOR DOCUMENTS ENDING IN '-2.xlsx' (STATEMENT OF CASH FLOW)
result = []
for file in os.listdir(mydir):
    if file.endswith("-2.csv"):
        result.append(os.path.join(file))
        
sorted_list_2 = sorted(result)


# In[ ]:


## BELOW IS THE PROGRAM/CODE TO RETRIEVE ALL RATIOS FOR BS, CSI & CSCF

# LENGTH OF BS, CSI, CSCF ARE ALL EQUAL. CREATE VARIABLE 'length'[int]
length = len(sorted_list_0)

# LOOP OVER ALL DOCUMENTS USING 'range(length)'
for i in range(length):

# INITIALIZE ALL THREE LISTS
input_date_0 = sorted_list_0[i]
input_date_1 = sorted_list_1[i]
input_date_2 = sorted_list_2[i]

# SAVE [DATE]
input_date = input_date_0[:-8]

##################################################

# IMPORT CORRESPONDING DOCUMENT AS PANDA DATAFRAME, DROP IRRELEVANT COLUMNS, SET AND RENAME AXIS 'DATE'|'DEFAULT'
file = pd.read_csv(input_date_0)
file = file.drop(file.columns[2:], axis=1)
file = file.set_axis([input_date_0, 'Default'], axis=1, inplace=False)

# CONVERT FIRST COLUMN 'input_date_0' FROM ARGUMENT ABOVE TO LIST
col_one_list_0 = file[input_date_0].tolist()

# SEARCH FOR SUBSETS IN CORRESPONDING COLUMN, THESE ARE THE FINANCIAL VARIABLES NEEDED FOR FURTHER CALCULATIONS
## SUBSETS WILL VARY DEPENDING ON THE FORMAT OF FINANCIAL STATEMENTS, THIS HAS TO BE MODIFIED MANUALLY FOR NOW
## (LOOK AT FINANCIAL STATEMENTS TO CHOOSE OPTIMIZED SUBSETS)
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

# CONDUCTING SEARCH
res00 = [i for i in col_one_list_0 if subs00 in i]
res01 = [i for i in col_one_list_0 if subs01 in i]
res02 = [i for i in col_one_list_0 if subs02 in i]
res03 = [i for i in col_one_list_0 if subs03 in i]
res04 = [i for i in col_one_list_0 if subs04 in i]
res05 = [i for i in col_one_list_0 if subs05 in i]
res06 = [i for i in col_one_list_0 if subs06 in i]
res07 = [i for i in col_one_list_0 if subs07 in i]
res08 = [i for i in col_one_list_0 if subs08 in i]
res09 = [i for i in col_one_list_0 if subs09 in i]
res10 = [i for i in col_one_list_0 if subs10 in i]
res11 = [i for i in col_one_list_0 if subs11 in i]
res12 = [i for i in col_one_list_0 if subs12 in i]
res13 = [i for i in col_one_list_0 if subs13 in i]
res14 = [i for i in col_one_list_0 if subs14 in i]

# IF THERE ARE TWO INSTANCES FOR SUBSETS, KEEP SUBSET[0] ::CREATE FUNCTION
if len(res00) >= 2:
    res00 = res00[0]

if len(res06) >= 2:
    res06 = res06[0]

if len(res14) >= 2:
    res14 = res14[0]

# RENAME ALL SUBSETS
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

# REMOVE NOT APPLICABLE ROWS USING 'notna()' FUNCTION IN DEFAULT COLUMN
file = file[file['Default'].notna()]

# CREATE NEW NUMPY ARRAY WITH ALL FINANCIAL VARIABLES
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

# CHECK IF 'Prepaid. Expenses' EXISTS AND ADJUST NUMPY ARRAY
if res14:
    col_one_arr_01 = col_one_arr
else:
    col_one_arr_00 = np.array([['Prepaid expenses', '0']])
    col_one_arr_01 = np.append(col_one_arr,col_one_arr_00, axis=0)

# SAME WITH 'res10' (Short-term debt)
if res10:
    col_one_arr_02 = col_one_arr_01
else:
    col_one_arr_00 = np.array([['Short-term debt', '0']])
    col_one_arr_02 = np.append(col_one_arr_01,col_one_arr_00, axis=0)

# SAME WITH 'res12' (Convertible stocks)
if res12:
    col_one_arr_03 = col_one_arr_02
else:
    col_one_arr_00 = np.array([['Convertible stocks', '0']])
    col_one_arr_03 = np.append(col_one_arr_02,col_one_arr_00, axis=0)

# FORMAT NUMPY ARRAYS (REMOVE DUPLICATES AND SORTED(*))
col_one_arr_CSI_04 = np.vstack({tuple(row) for row in col_one_arr_03})
col_one_arr_BS = np.array(sorted(col_one_arr_CSI_04 ,key=lambda x: x[0]))

##################################################

# SAME WITH 'CONSOLIDATED STATEMENT OF INCOME' [CSI]
file = pd.read_csv(input_date_1)
file = file.drop(file.columns[2:], axis=1)
file = file.set_axis([input_date_1, 'Default'], axis=1, inplace=False)
file = file.dropna()

col_one_list_1 = file[input_date_1].tolist()

# RENAME FIRST COLUMN
col_one_list_1[0] = "Additional Info"

# ENTER EXISTING AND DUPLICATE SUBSETS
Rev = 'Revenues'
Rev_0 = 'Revenue'
NI = 'Net income'
RD = 'Research and development'

# SEARCH OTHER SUBSETS PRESENT IN [CSI]
subs00 = 'Cost of'
subs01 = 'Income from operations'
subs02 = 'Income before'
subs03 = 'asic'
subs04 = 'iluted'
subs05 = 'Less'

res00 = [i for i in col_one_list_1 if subs00 in i]
res01 = [i for i in col_one_list_1 if subs01 in i]
res02 = [i for i in col_one_list_1 if subs02 in i]
res03 = [i for i in col_one_list_1 if subs03 in i]
res04 = [i for i in col_one_list_1 if subs04 in i]
res05 = [i for i in col_one_list_1 if subs05 in i]

# OVER TWO INSTANCES, KEEP [0] (IN THIS CASE, 'Net Income/NI')
## THIS MIGHT DIFFER DEPENDING ON SUBSET CHOSEN AND FORMAT OF FINANCIAL STATEMENTS
if len(NI) >= 2:
    NI = NI[0]

# RENAME ALL SUBSETS
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

# CREATE NEW NUMPY ARRAY WITH ALL VARIABLES
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

# CHECK IF 'res05' EXISTS AND ADJUST NUMPY ARRAY
if res05:
    col_one_arr_01 = col_one_arr
else:
    col_one_arr_00 = np.array([['Less: Adjustment Payments', '0']])
    col_one_arr_01 = np.append(col_one_arr,col_one_arr_00, axis=0)
    
# FORMATING NUMPY ARRAY (REMOVE DUPLICATES AND SORTED(*))
col_one_arr_CSI_00 = np.vstack({tuple(row) for row in col_one_arr_01})
col_one_arr_CSI_01 = np.array(sorted(col_one_arr_CSI_00 ,key=lambda x: x[0]))

# ADJUST DUPLICATE ELEMENTS IN NUMPY ARRAY (ref. 'Net Income/NI')
#### *NEXT ARGUMENT CAN BE SIMPLIFIED. CREATE FUNCTION WITH CORRESPONDING PARAMETERS
#### WARNING!!! FORMATING.
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

        if col_one_arr_CSI_01[ni_loc_0][1] == Net_income_v_2:
            col_one_arr_CSI_0 = np.delete(col_one_arr_CSI_01, ni_loc_1, 0)
        else:
            col_one_arr_CSI_0 = np.delete(col_one_arr_CSI_01, ni_loc_0, 0)
        col_one_arr_CSI = col_one_arr_CSI_0
        
    else:
        ni_loc_0 = np.where(col_one_arr_CSI_01 == 'Net income')[0]
        col_one_arr_CSI = col_one_arr_CSI_01

##################################################

# SAME WITH 'CONSOLIDATED STATEMENT OF CASH FLOW' [CSCF]
file = pd.read_csv(input_date_2)
file = file.drop(file.columns[2:], axis=1)
file = file.set_axis([input_date_2, 'Default'], axis=1, inplace=False)

col_one_list_2 = file[input_date_2].tolist()
col_one_list_2[0] = "Additional Info"

# SEARCH OTHER SUBSETS PRESENT IN [CSCF]
subs00 = 'Net income'
subs01 = 'Depreciation'
subs02 = 'Amortization'
subs03 = 'Prepaid'
subs04 = 'by operating activities'
subs05 = 'in investing activities'
subs06 = 'in financing activities'
subs07 = 'Purchases of property'

res00 = [i for i in col_one_list_2 if subs00 in i]
res01 = [i for i in col_one_list_2 if subs01 in i]
res02 = [i for i in col_one_list_2 if subs02 in i]
res03 = [i for i in col_one_list_2 if subs03 in i]
res04 = [i for i in col_one_list_2 if subs04 in i]
res05 = [i for i in col_one_list_2 if subs05 in i]
res06 = [i for i in col_one_list_2 if subs06 in i]
res07 = [i for i in col_one_list_2 if subs07 in i]

# RENAME ALL SUBSETS
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

# CREATE NEW NUMPY ARRAY WITH ALL VARIABLES
col_one_list_2 = file.loc[file[input_date_2].isin(['Net income',
                                      'Depreciation',
                                      'Amortization',
                                      'Prepaid expenses',
                                      'Net cash provided by operating activities',
                                      'Net cash provided by investing activities',
                                      'Net cash provided by financing activities',
                                     'Purchase of property, plant and equipment'])].to_numpy()

# CHECK IF 'res03' EXISTS AND ADJUST NUMPY ARRAY
if res03:
    col_one_arr_01 = col_one_list_2
else:
    col_one_arr_00 = np.array([['Prepaid expenses', '0']])
    col_one_arr_01 = np.append(col_one_arr,col_one_arr_00, axis=0)

# FORMATING NUMPY ARRAY (SORTED(*))
col_one_arr_CSCF = np.array(sorted(col_one_arr_01 ,key=lambda x: x[0]))

##################################################

# SAVE ALL FINANCIAL VARIABLES FROM [BS]
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

# SAVE ALL FINANCIAL VARIABLES FROM [CSI]
Basic_EPS = float(col_one_arr_CSI[0,1])
Cost_of_revenues = float(col_one_arr_CSI[1,1])
Diluted_EPS = float(col_one_arr_CSI[2,1])
Income_before_taxes = float(col_one_arr_CSI[3,1])
Adjustment_Payments = float(col_one_arr_CSI[4,1])
Net_income = float(col_one_arr_CSI[5,1])
Operating_income = float(col_one_arr_CSI[6,1])
Research_Development = float(col_one_arr_CSI[7,1])
Revenues = float(col_one_arr_CSI[8,1])

# SAVE ALL FINANCIAL VARIABLES FROM [CSCF]
Net_income_CSCF = float(col_one_arr_CSCF[0,1])
Depreciation = float(col_one_arr_CSCF[1,1])
Amortization = float(col_one_arr_CSCF[2,1])
Prepaid_expenses_CSCF = float(col_one_arr_CSCF[3,1])
Net_cash_operating_activities = float(col_one_arr_CSCF[4,1])
Purchase_of_PPE = float(col_one_arr_CSCF[5,1])
Net_cash_investing_activities = float(col_one_arr_CSCF[6,1])
Net_cash_financing_activities = float(col_one_arr_CSCF[7,1])

##################################################

## CALCULATE AVERAGE SHARE PRICE IN ORDER TO ADD TO FUNDAMENTAL ANALYSIS ('-DF')
# EXTRACT ALL RELEVANT TECHNICAL VARIABLES FROM COMPANY'S SHARE PRICE (DOC. FROM YAHOO FINANCE)
file = pd.read_csv('Alphabet Inc.csv')

# VERIFY DATE AT WHICH MONTH IS ENDING
date_prefix = input_date_0[:-8]
date_ls = ["31", "30", "29", "28"]
upd_date_0 = date_prefix + date_ls[0]
upd_date_1 = date_prefix + date_ls[1]
upd_date_2 = date_prefix + date_ls[2]
upd_date_3 = date_prefix + date_ls[3]

if upd_date_0 in file.values:
    col_one_arr_P = file[file['Date'].str.contains(upd_date_0)].to_numpy()
else:
    if upd_date_1 in file.values:
        col_one_arr_P = file[file['Date'].str.contains(upd_date_1)].to_numpy()
    else:
        if upd_date_2 in file.values:
            col_one_arr_P = file[file['Date'].str.contains(upd_date_2)].to_numpy()
        else:
            if upd_date_3 in file.values:
                col_one_arr_P = file[file['Date'].str.contains(upd_date_3)].to_numpy()

# CALCULATE AVERGAGE SHARE PRICE FROM OPENING AND CLOSING PRICE
Open_P = col_one_arr_P[0,1]
Close_P = col_one_arr_P[0,-3]
Avg_P = ((Open_P + Close_P)/2)

# APPEND RESULTS TO NEW NUMPY ARRAY
col_one_arr_P_Modified = np.append(col_one_arr_P, [Avg_P])
col_one_arr_P_Modified

##################################################

#### *NEXT ARGUMENT CAN BE SIMPLIFIED. CREATE FUNCTION WITH CORRESPONDING PARAMETERS
# FORMATING OF 'res13' (Number of Shares Outstanding) -> listToString
def listToString(res13): 
    str1 = "" 
    for ele in res13: 
        str1 += ele  
    return str1 

str00 = listToString(res13)
str01 = str00.replace(",", "")
str02 = str(str01.split("; ",1)[1])[0:6]
Outstanding_shares = int(str02)

# CALCULATE RETAINED EARNINGS '-3 months' INTERVAL .calc(CHANGE) FROM [BS]
file = pd.read_csv(input_date_0)
file = file.drop(file.columns[1], axis=1)
file = file.set_axis([input_date_0, 'Default'], axis=1, inplace=False)
col_one_list = file[input_date_0].tolist()

# SEARCH AND EXTRACT SUBSET 'subs99'|'Restained earnings'
subs99 = 'Retained earnings'
res99 = [i for i in col_one_list if subs99 in i]
col_one_arr = file.loc[file[input_date_0].isin(['Retained earnings'])].to_numpy()
RE_start = float(col_one_arr[0,1])
## Additional relevant information on Dividends
#https://www.investopedia.com/ask/answers/012015/how-do-i-calculate-dividend-payout-ratio-income-statement.asp
#Dividends Paid or Payout Ratio => DP = (NI + RE) - RE.close :::::: DP.start = (NI.start + RE.start) - RE.close

# CALCULATE NET INCOME '-3 months' INTERVAL .calc(CHANGE) FROM [CSI]
file = pd.read_csv(input_date_1)
file = file.drop(file.columns[3:], axis=1)
file = file.drop(file.columns[1], axis=1)
file = file.set_axis([input_date_1, 'Default'], axis=1, inplace=False)
col_one_arr = file.loc[file[input_date_1].isin(['Net income'])].to_numpy()

# SET PRE-EXISTING FINANCIAL VARIABLES (NI, RE, DP)
NI_start = float(col_one_arr[0,1])
RE_close = Retained_earnings
DP_VALUE = (NI_start + RE_start) - RE_close

##################################################

# CALCULATE ADDITIONAL/MISSING DATA FROM [BS]
file = pd.read_csv(input_date_0)
file = file.drop(file.columns[1], axis=1)
file = file.set_axis([input_date_0, 'Default'], axis=1, inplace=False)

file = file[file['Default'].notna()]
col_one_list = file[input_date_0].tolist()

# SEARCH OTHER SUBSETS PRESENT IN [BS]
subs98 = 'Total current a'
subs97 = 'Total current l'
subs96 = 'Property'
res98 = [i for i in col_one_list if subs98 in i]
res97 = [i for i in col_one_list if subs97 in i]
res96 = [i for i in col_one_list if subs96 in i]

# FORMATING SUBSETS
str00 = listToString(res98)
str01 = listToString(res97)
str02 = listToString(res96)

# RENAME ALL SUBSETS
file.replace(str00, "Current assets", inplace=True)
file.replace(str01, "Current liabilities", inplace=True)
file.replace(str02, "Property, plant and equipment", inplace=True)

# CREATE NUMPY ARRAY WITH NEW VARIABLES
col_one_arr = file.loc[file[input_date_0].isin(["Current assets"])].to_numpy()
Current_assets_start = float(col_one_arr[0,1])
col_one_arr = file.loc[file[input_date_0].isin(["Current liabilities"])].to_numpy()
Current_liabilities_start = float(col_one_arr[0,1])
col_one_arr = file.loc[file[input_date_0].isin(["Property, plant and equipment"])].to_numpy()
Property_plant_and_equipment_start = float(col_one_arr[0,1])

# CALCULATE ADDITIONAL/MISSING DATA FROM [CSCF] (Old Depreciation Value)
file = pd.read_csv(input_date_2)
file = file.drop(file.columns[3:], axis=1)
file = file.drop(file.columns[1], axis=1)
file = file.set_axis([input_date_2, 'Default'], axis=1, inplace=False)    

col_one_list = file[input_date_2].tolist()
col_one_list[0] = "Additional Info"

# SEARCH OTHER SUBSETS PRESENT IN [CSCF]
subs95 = 'Depreciation'
res95 = [i for i in col_one_list if subs95 in i]

# FORMATING SUBSET(S)
str03 = listToString(res95)

# RENAME SUBSET(S)
file.replace(str03, "Depreciation", inplace=True)

# CREATE NUMPY ARRAY WITH NEW VARIABLE(S)
col_one_arr = file.loc[file[input_date_2].isin(["Depreciation"])].to_numpy()
Depreciation_start = float(col_one_arr[0,1])

##################################################

# CREATE DATAFRAME WITH ALL FINANCIAL VARIABLES FROM [BS], [CSI] & [CSCF]
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

##################################################

#### *NEXT ARGUMENT CAN BE SIMPLIFIED. CREATE FUNCTION WITH CORRESPONDING PARAMETERS (+ DERIVED VARIABLES?)
# CALCULATE FINANCIAL RATIOS FROM PRE-DEFINED EQUATIONS & FORMULAS

#PE_1_VALUE (Calculate EPS using Net Income & Number of shares issues and outstanding)
PE_1_VALUE = Avg_P / (Net_income / Outstanding_shares) / 1000 #Units
#PE_2_VALUE (Calculate PE_2 using Market Price & Diluted EPS [CSI])
PE_2_0_VALUE = Avg_P / Diluted_EPS
PE_2_1_VALUE = Avg_P / Basic_EPS

         #Price/Earnings to Growth
#PEG_1_VALUE (Calculate PEG using Expected Growth Rate as input)     #print('Enter EGR:')
#MISSING VALUE EGR can only be determined at the present moment using Expected Growth Rate from: Citibank, Goldman Sachs, JPM, MorganStanley, BNP Paribas - Expected EPS Growth
#Other sources include the Wall Street Journal WSJ and Yahoo Finance

#PEG_2_VALUE (Calculate from past 3-6-9-12 months growth rate using linear and non-linear regressions)
#MISSING VALUE Data from the past 3-6-9-12 months
#Other source: https://www.investopedia.com/terms/p/price-earningsratio.asp

EV_1_VALUE = Avg_P * Outstanding_shares
EV_2_VALUE = Avg_P * Class_A_and_Class_B_stocks
EBIT_VALUE = Net_income_CSCF #Interest (N.A)
EBITDA_VALUE = EBIT_VALUE - Depreciation - Amortization
EV_1_EBITDA_VALUE = EV_1_VALUE / EBITDA_VALUE
EV_2_EBITDA_VALUE = EV_2_VALUE / EBITDA_VALUE

DE_VALUE = (Long_term_debt + Short_term_debt) / EBITDA_VALUE
NE_VALUE = (Long_term_debt + Short_term_debt - Cash_and_cash_equivalents) / EBITDA_VALUE
QR_1_VALUE = (Cash_and_cash_equivalents + Marketable_securities + Accounts_receivable) / Current_liabilities
QR_2_VALUE = (Current_assets - Prepaid_expenses) / Current_liabilities

         #Dividend-related ratios
EPS_VALUE = (Net_income - Convertible_stocks) / Outstanding_shares
#https://www.investopedia.com/ask/answers/032515/what-difference-between-earnings-share-and-dividends-share.asp
#Dividends Paid or Payout Ratio => DP = (NI + RE) - RE.close :::::: DP.start = (NI.start + RE.start) - RE.close
#https://www.investopedia.com/ask/answers/012015/how-do-i-calculate-dividend-payout-ratio-income-statement.asp
DPS_VALUE = DP_VALUE / Outstanding_shares
DY_1_VALUE = Net_income / ((RE_close - RE_start) / RE_close) * 4 # for 4 Quarters/Year
#Approximation. Dividend Yield should be calculated within -12 months, not -3months
DY_2_VALUE = DPS_VALUE / Avg_P * 1000 #Units
Div_VALUE = -(Net_cash_financing_activities)

         #Other Ratios (MCAP, ROE, Margins...) Verify Ratio Formulas
MCAP_VALUE = Avg_P / Outstanding_shares
ROE_VALUE = Net_income / Total_stockholder_equity * 4 # or 4 Quarters/Year :::: Other formula(s) exist
NetMargin_VALUE = (Revenues - Cost_of_revenues) / Revenues
OperatingMargin_VALUE = Net_cash_operating_activities - Revenues

#MISSING VALUE: Income before Tax for -6 months (Income_before_taxes is only -3 months). Use current Tax Rate
Tax_VALUE = 1 - (Net_income / Income_before_taxes)
FCF_2_VALUE = (Property_plant_and_equipment + (Depreciation/2)) - (Property_plant_and_equipment_start + (Depreciation_start/2)) #CHANGE(CAPEX) also looking at old Depreciation

#CHANGE(Assets-Liabilities) - ()#CHANGE(CAPEX)
FCF_0_VALUE = EBIT_VALUE * (1 - Tax_VALUE) - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
FCF_1_VALUE = Revenues - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
#print(Research_Development)
### USE BOTH 'Outstanding_shares' & 'Class_A_and_Class_B_stocks' FOR RELATED RATIOS?

##################################################

# UPDATED :: FINANCIAL RATIOS - EQUATIONS & FORMULAS
# THIS INCLUDES DERIVED VALUES FOR SIMILAR VARIABLES

# () PE_1_VALUE = Avg_P / (Net_income / Outstanding_shares) / 1000
PE_2_2_VALUE = Avg_P / EPS_VALUE
# (CSCF) EBIT_VALUE = Net_income_CSCF && (CSI) EBIT_VALUE_0 = Income_before_taxes
EBIT_VALUE_0 = Income_before_taxes
# (CSCF) EBITDA_VALUE = EBIT_VALUE - Depreciation - Amortization
EBITDA_VALUE_0 = EBIT_VALUE_0 - Depreciation - Amortization
EV_1_EBITDA_VALUE_0 = EV_1_VALUE / EBITDA_VALUE_0
EV_2_EBITDA_VALUE_0 = EV_2_VALUE / EBITDA_VALUE_0

DE_VALUE_0 = (Long_term_debt + Short_term_debt) / EBITDA_VALUE_0
NE_VALUE_0 = (Long_term_debt + Short_term_debt - Cash_and_cash_equivalents) / EBITDA_VALUE_0
Div_VALUE_1 = Net_income - (Basic_EPS * Outstanding_shares)
Div_VALUE_2 = Net_income - (Diluted_EPS * Outstanding_shares)

DPS_00 = EPS_VALUE * (Div_VALUE / Net_income)
DPS_02 = EPS_VALUE * (Div_VALUE_1 / Net_income) 
DPS_03 = EPS_VALUE * (Div_VALUE_2 / Net_income) 
DPS_10 = Basic_EPS * (Div_VALUE / Net_income)
DPS_12 = Basic_EPS * (Div_VALUE_1 / Net_income)
DPS_13 = Basic_EPS * (Div_VALUE_2 / Net_income)
DPS_20 = Diluted_EPS * (Div_VALUE / Net_income)
DPS_22 = Diluted_EPS * (Div_VALUE_1 / Net_income)
DPS_23 = Diluted_EPS * (Div_VALUE_2 / Net_income)

DY_2_VALUE_00 = DPS_00 / Avg_P #Units
DY_2_VALUE_02 = DPS_02 / Avg_P
DY_2_VALUE_03 = DPS_03 / Avg_P
DY_2_VALUE_04 = DPS_10 / Avg_P
DY_2_VALUE_06 = DPS_12 / Avg_P
DY_2_VALUE_07 = DPS_13 / Avg_P
DY_2_VALUE_08 = DPS_20 / Avg_P
DY_2_VALUE_10 = DPS_22 / Avg_P
DY_2_VALUE_11 = DPS_23 / Avg_P

# Following MCAP uses '*' rather than P/O_S Ratio
#FCF_0_VALUE = EBIT_VALUE_0 * (1 - Tax_VALUE) - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
### CHECK FOR (Net Income (I/S))   //DONE//
### CHECK FOR [Outstanding_shares] [Dividends] [EPS && DPS] [ADD AND USE ALL SAME VARIABLES OF DIFFERENT VALUE(S)]

BV_0 = Total_assets - Total_liabilities
GPM_0 = (Revenues - Cost_of_revenues) / Revenues
OPM_0 = Income_before_taxes / Revenues
PM_0 = Net_income / Revenues
ROA_0 = Net_income / Total_assets
ROI_0 = Net_income / Total_stockholder_equity
ROC_0 = Net_income / (Total_stockholder_equity + Short_term_debt + Long_term_debt)
ROCE_0 = Operating_income / (Total_assets - Current_liabilities)

PSD_0 = Net_income - Outstanding_shares
RR_0 = (Net_income - Div_VALUE) / Net_income
RR_2 = (Net_income - Div_VALUE_1) / Net_income
RR_3 = (Net_income - Div_VALUE_2) / Net_income
MVPS_0 = MCAP_VALUE / Outstanding_shares
MVPS_PRICE_0 = MVPS_0 / Avg_P

PE_00 = MVPS_0 / EPS_VALUE
PE_01 = MVPS_0 / Basic_EPS
PE_02 = MVPS_0 / Diluted_EPS
SGR_0 = ROE_VALUE * RR_0
SGR_2 = ROE_VALUE * RR_2
SGR_3 = ROE_VALUE * RR_3
BVPS_0 = Total_stockholder_equity / Outstanding_shares
MB_0 = (MCAP_VALUE / Outstanding_shares) / BVPS_0

# New Dividend Yield (DY) Formulas using MVPS
DY_0 = DPS_VALUE / MVPS_0
DY_0_00 = DPS_00 / MVPS_0
DY_0_02 = DPS_02 / MVPS_0
DY_0_03 = DPS_03 / MVPS_0
DY_0_04 = DPS_10 / MVPS_0
DY_0_06 = DPS_12 / MVPS_0
DY_0_07 = DPS_13 / MVPS_0
DY_0_08 = DPS_20 / MVPS_0
DY_0_10 = DPS_22 / MVPS_0
DY_0_11 = DPS_23 / MVPS_0

Equity_multiplier = Total_assets / Total_stockholder_equity
Total_asset_turnover = Revenues / Total_assets
#    ·       Apply YOY, HA && VA Analysis

##################################################

## ADD LIQUIDITY [LEVERAGE], SOLVENCY [LEVERAGE] AND EFFICIENCY RATIO [BS] [CSI]

#Liquidity Ratio [BS] [CSI]
Cur_R = Current_assets / Current_liabilities
Inventory = Total_assets - Cash_and_cash_equivalents - Accounts_receivable
QR = (Current_assets - Inventory) / Current_liabilities
Cas_R = Cash_and_cash_equivalents / Current_liabilities
NWC = Current_assets - Current_liabilities
NWC_TA = NWC / Total_assets
IM = (Current_assets / Operating_income) / (Current_assets / ((Cost_of_revenues + Operating_income) / 365))

#Solvency Ratios [BS] [CSI]
Total_debt = Short_term_debt + Long_term_debt
DR = Total_debt / Total_assets
ER = Total_stockholder_equity / Total_assets
DER = Total_debt / Total_stockholder_equity
EM = Total_assets / Total_stockholder_equity
NFA = Total_assets - Current_assets
FE = NFA / Total_stockholder_equity
LTDR = Long_term_debt / (Long_term_debt + Total_stockholder_equity)
Interest = - (Operating_income - Income_before_taxes)
TIE = Operating_income / Interest
CC = (Operating_income + Depreciation) / Interest
Principal = Current_liabilities - Short_term_debt
TDS = (Interest * (1 - Tax_VALUE)) + Principal
DSCR = (Operating_income / TDS) / (Operating_income / (Interest + Principal))

#Efficiency Ratios [BS] [CSI]
IT = Cost_of_revenues / Inventory
DSI = 365 / IT
Sales = Revenues - Operating_income - Cost_of_revenues - Research_Development
RT = Sales / Accounts_receivable
DSR = 365 / RT
#Payables Turnover = COGS / Accounts Payable
# Retrieve Accounts Payable from [BS]
#PT = Cost_of_revenues / (...)
#Day’s Sales in Payables (Days Payables Outstanding, or DIO) = 365 / Payables Turnover
#Cash Conversion Cycle (CCC) = Day’s Sales in Inventory + Day’s Sales in Receivables - Day’s Sales in Payables
TATO = Sales / Total_assets
#Capital Intensity = Total Assets / Sales
CI = Total_assets / Sales
#Fixed Asset Turnover = Sales / Net Fixed Assets
FAT = Sales / NFA
#NWC Turnover = Sales / NWC
NWCT = Sales / NWC

## NOTES
# Separate previous RATIOS into two sections: PROFITABILITY and MARKET VALUE RATIOS.
# Separate new RATIOS into two, and three sub-sections.
# Loop over all data
# VERIFY ALL PROCESSED DATA (e.g. Date[1], Date[n-1], Date[n])

# Start using PMP Course to write BUSINESS PLAN & STRATEGY intended for new STAKEHOLDERS.
# Finish building prototype for all 10 companies.

EBIT_DEFAULT = Operating_income
EBITDA_DEFAULT = EBIT_DEFAULT - Depreciation - Amortization
EV_1_EBITDA_DEFAULT = EV_1_VALUE / EBITDA_DEFAULT
EV_2_EBITDA_DEFAULT = EV_2_VALUE / EBITDA_DEFAULT

DE_DEFAULT = (Long_term_debt + Short_term_debt) / EBITDA_DEFAULT
NE_DEFAULT = (Long_term_debt + Short_term_debt - Cash_and_cash_equivalents) / EBITDA_DEFAULT
FCF_3_VALUE = EBIT_VALUE_0 * (1 - Tax_VALUE) - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
FCF_DEFAULT = EBIT_DEFAULT * (1 - Tax_VALUE) - (Amortization/2) - ((Current_assets - Current_liabilities) - (Current_assets_start - Current_liabilities_start)) - (Property_plant_and_equipment - Property_plant_and_equipment_start)
### USE BOTH 'Outstanding_shares' & 'Class_A_and_Class_B_stocks' FOR RELATED RATIOS?

##################################################

# CREATE DATAFRAME WITH ALL FINANCIAL RATIOS CALCULATED FROM EXTRACTED VARIABLES
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

# SAVE OUTPUT AS [DATE] + Ratio-DF.csv'
filename = input_date_0[:-6] + "-Ratio-DF.csv"
df.to_csv(filename)


# In[ ]:


# S3 _ CSV Combined Ratio & [-3] Alphabet-TF (CORRESPONDS TO COMBINING RELEVANT '-TF.csv' DOCUMENTS)
# * [OUTPUTS] :: COMBINED FUNDAMENTAL AND TECHNICAL RATIO OVER [-3] MONTH INTERVAL
# * LOOP OVER ALL DOCUMENTS


# In[ ]:


# RESET SORTED LIST FOR LOOP
mydir = os.getcwd()
result = []

for file in os.listdir(mydir):
    if file.endswith("-Ratio-DF.csv"):
        result.append(os.path.join(file))
        
sorted_list_0 = sorted(result)
length = len(sorted_list_0)

# SET STARTING DATE MANUALLY (UPDATE REQUIRED TO ADJUST DYNAMIC SOFTWARE)
ls = ['2016-03-31']
for i in range(length):
    input_date = sorted_list_0[i][:-13]
    ls.append(input_date)


# In[ ]:


# WARNING!!! THIS HAS ALREADY BEEN DONE PREVIOUSLY (ref. # S2 _ Financial Variables & Ratios)
# AS OPPOSED TO LATEST 'Adj Close' PRICE [-3] ENDING MONTHS, THIS RETRIEVES LATEST 'Date' FOR COMBINED'-DF' AND '-TF'
file = pd.read_csv('Alphabet Inc.csv')
date_prefix = ls[0][:-2]
date_ls = ["31", "30", "29", "28"]

upd_date_0 = date_prefix + date_ls[0]
upd_date_1 = date_prefix + date_ls[1]
upd_date_2 = date_prefix + date_ls[2]
upd_date_3 = date_prefix + date_ls[3]

if upd_date_0 in file.values:
    col_one_arr_P = file[file['Date'].str.contains(upd_date_0)].to_numpy()
    print(upd_date_0 + " exists.")
    index = file[file['Date'] == upd_date_1].index[0]
else:
    if upd_date_1 in file.values:
        col_one_arr_P = file[file['Date'].str.contains(upd_date_1)].to_numpy()
        print("Month finishes in -30")
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

# FORMATING REQUIRED TO ADJUST '-DF' INDEX 'Date' [SORTED(*)]
df_age_negative = file[ file['Date'] < ls[0] ] # Step 1
df = file.drop(df_age_negative.index, axis=0) # Step 2

df_age_positive = file[ file['Date'] > ls[1] ]
df = df.drop(df_age_positive.index, axis=0)


# In[ ]:


# FORMATING REQUIRED TO RADJUST '-DF' INDEX 'Date' (ONLY SPECIFIC TO ALPHABET COMPANY (t-1))
length = len(sorted_list_0)
for i in range(length):

    df_age_negative = file[ file['Date'] < ls[i] ] # Step 1
    df = file.drop(df_age_negative.index, axis=0) # Step 2
    df_age_positive = file[ file['Date'] > ls[i+1] ]
    df = df.drop(df_age_positive.index, axis=0)
    
    end_date = ls[i+1]
    df.to_csv(end_date + "-Alphabet.csv")


# In[ ]:


# [0] FORMATING COMBINED DATAFRAME
file_0 = pd.read_csv(sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)
title = sorted_list_0[0][:-13]
file_0 = file_0.set_axis(['Financial Ratio', title], axis=1, inplace=False)


# In[ ]:


# [1] FORMATING COMBINED DATAFRAME
file_1 = pd.read_csv(sorted_list_0[1])
file_1 = file_1.drop(file_1.columns[0], axis=1)
file_1 = file_1.drop(file_1.columns[0], axis=1)
title = sorted_list_0[1][:-13]

# '... /unit'??
file_1.rename({'Financial Ratio /unit': title}, axis=1, inplace=True)
file_0 = file_0.join(file_1)


# In[ ]:


# [2] FORMATING COMBINED DATAFRAME
file_3 = pd.read_csv(sorted_list_0[2])
file_3 = file_3.drop(file_3.columns[0], axis=1)
file_3 = file_3.drop(file_3.columns[0], axis=1)

title = sorted_list_0[2][:-13]
file_0 = file_0.join(file_3)


# In[ ]:


# FORMATING COMBINED DATAFRAME AT [0]
file_0 = pd.read_csv(sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)
title = sorted_list_0[0][:-13]
file_0 = file_0.set_axis(['Financial Ratio', title], axis=1, inplace=False)

sorted_list_1 = sorted_list_0[1:]

# LOOP OVER ALL DOCUMENTS TO FORMAT COMBINED DATAFRAME FROM [1]...[n]
length = len(sorted_list_1)
for i in range(length):
    file_1 = pd.read_csv(sorted_list_1[i])
    file_1 = file_1.drop(file_1.columns[0], axis=1)
    file_1 = file_1.drop(file_1.columns[0], axis=1)

    title = sorted_list_1[i][:-13]
    file_1.rename({'Financial Ratio /unit': title}, axis=1, inplace=True)
    file_0 = file_0.join(file_1)
    file_0.to_csv('Combined_Ratio.csv')


# In[ ]:


# S4 _ CSV Loop /Ratio-TF && /Variables-DF (CORRESPONDS TO COMBINING RELEVANT '.csv' DOCUMENTS)
# * [OUTPUTS] :: COMBINED FUNDAMENTAL VARIABLES AND TECHNICAL RATIO OVER [-3] MONTH INTERVAL
# * LOOP OVER ALL DOCUMENTS


# In[ ]:


## '-Alphabet.csv' REFERING TO WEEKLY TECHNICAL DATA THROUGH INTERVAL [-3]
# RESET SORTED LIST FOR LOOP (Combined /Variables-TF)
mydir = os.getcwd()
result = []

for file in os.listdir(mydir):
    if file.endswith("-Alphabet.csv"):
        result.append(os.path.join(file))
        
sorted_list_0 = sorted(result)


# In[ ]:


# COMBINED DATAFRAME FOR /Variables' TECHNICAL ANALYSIS '-TF'
length = len(sorted_list_0)

for i in range(length):
    file = pd.read_csv(sorted_list_0[i])
    file = file.drop(file.columns[0], axis=1)
    start_date = file.iloc[0][0]
    end_date = file.iloc[-1][0]

    # RETRIEVE TECHNICAL DATA THAT IS CONSISTENT (ON'Friday's), PRIOR TO CLOSING MARKETS.
    file['Date'] = pd.to_datetime(file['Date'])
    file_0 = file['Date'].dt.day_name()
    file_1 = file.merge(file_0.rename('Weekday'), left_index=True, right_index=True)
    end_week = file_1.loc[file_1['Weekday'] == 'Friday']
    col_one_list = end_week['Date'].tolist()
    
    file_2 = file_1.set_index('Date')
    length = len(col_one_list)
    
    for j in range(length):
        if file_2.index.get_loc(col_one_list[j]) >=5:
            
            # IF ENOUGH DATA TO CALCULATE PAST WEEK'S 'Adj. Close' AVG
            AdjClose = file_2.at[col_one_list[j], 'Adj Close']
            Index = file_2.index.get_loc(col_one_list[j])
            
            # MANUALLY SET 'Index.range[1-4]' & 'n=5'
            index1 = int(Index)-1
            index2 = int(Index)-2
            index3 = int(Index)-3
            index4 = int(Index)-4
            index_ls = list(file_2.index)
            
            V0 = file_2.at[index_ls[index1], 'Adj Close']
            V1 = file_2.at[index_ls[index2], 'Adj Close']
            V2 = file_2.at[index_ls[index3], 'Adj Close']
            V3 = file_2.at[index_ls[index4], 'Adj Close']
            
#### *NEXT ARGUMENT CAN BE SIMPLIFIED. CREATE FUNCTION WITH CORRESPONDING PARAMETERS
            A1 = (AdjClose + V0 + V1 + V2 + V3) / 5
            N_days = 1/(5-1)
            A2 = N_days * ((AdjClose - A1)**2 + (V0 - A1)**2 + (V1 - A1)**2 + (V2 - A1)**2 + (V3 - A1)**2)
            A3 = (A2 / A1) * 100
            
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
            
#### *NEXT ARGUMENT CAN BE SIMPLIFIED. CREATE FUNCTION WITH CORRESPONDING PARAMETERS
            A4 = N_days * ((max(High, V5, V6, V7, V8) - min(Low, V9, V10, V11, V12))**2)
            A5 = (A4 / A1) * 100
            A6 = (A1 - min(Low, V9, V10, V11, V12))/(max(High, V5, V6, V7, V8) - min(Low, V9, V10, V11, V12))
            
            # OPEN CLOSE VALUES N-4
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

#### *NEXT ARGUMENT CAN BE SIMPLIFIED. CREATE FUNCTION WITH CORRESPONDING PARAMETERS
            A7 = N_days * ((max(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20) - min(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20))**2)
            A8 = (A7 / A1) * 100
            A9 = (A1 - min(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20))/(max(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20) - min(Open, V13, V14, V15, V16, Close, V17, V18, V19, V20))
            A10 = (A1 - min(AdjClose, V0, V1, V2, V3))/(max(AdjClose, V0, V1, V2, V3) - min(AdjClose, V0, V1, V2, V3))
            
            # SET ALL RELEVANT TECHNICAL DATA CORRESPONDING TO 'VOLATILITY IN SHARE PRICE'
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
            # IF ENOUGH DATA TO CALCULATE PAST WEEK'S 'Adj. Close' AVG, EMPTY.
    file_2 = file_2.drop(columns=['Open', 'High', 'Low', 'Close', 'Volume', 'Weekday'])
    
    # SAVE DOCUMENT '-TF.csv'
    file_2['Adj.Avg'].replace('', np.nan, inplace=True)
    file_2 = file_2.dropna(subset=['Adj.Avg'])
    file_2.to_csv(sorted_list_0[i][:-13] + "-Ratio-TF.csv")


# In[ ]:


# S5 _ CSV '-DF' Analysis (CORRESPONDS TO COMBINED '-Alphabet.csv')
# * [OUTPUTS] :: COMBINED TECHNICAL VARIABLES (Open, High...), SAVE AS 'Alphabet-Ending-Months.csv'
# * ADD 'Alphabet-Ending-Months.csv' TO COMBINED '-DF'


# In[ ]:


# RESET SORTED LIST FOR LOOP ('-Alphabet.csv')
mydir = os.getcwd()
result = []

for file in os.listdir(mydir):
    if file.endswith("-Alphabet.csv"):
        result.append(os.path.join(file))
        
sorted_list_0 = sorted(result)


# In[ ]:


# LOOP OVER ALL '-Alphabet.csv' DOCUMENTS AND ONLY KEEP END OF [-3] MONTH INTERVAL
length = len(sorted_list_0)

for i in range(length):
    if i == 0:
        file = pd.read_csv(sorted_list_0[i])
        size = len(file.index)
        size_1 = size - 1 ##
        file = file.drop(labels=range(0,size_1), axis=0)
        file_1 = file
    else:
        file = pd.read_csv(sorted_list_0[i])
        size = len(file.index)
        size_1 = size - 1 ##
        file = file.drop(labels=range(0,size_1), axis=0)
        file_1 = file_1.append(file)

file_1.drop(columns=file_1.columns[0], axis=1, inplace=True)
file_1.to_csv('Alphabet-Ending-Months.csv', index=False)


# In[ ]:


# RESET SORTED LIST FOR LOOP ('-Ratio-DF.csv')
mydir = os.getcwd()
result = []

for file in os.listdir(mydir):
    if file.endswith("-Ratio-DF.csv"):
        result.append(os.path.join(file))
        
sorted_list_0 = sorted(result)


# In[ ]:


# FORMATING OF COMBINED '-Ratio-DF' DOCUMENTS (APPLICATION TO ls[0])
file_0 = pd.read_csv(sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)
title = sorted_list_0[0][:-13]
file_0 = file_0.set_axis(['Financial Ratio', title], axis=1, inplace=False)

## APPLICATION FROM 2nd TO nth IN LIST (ls[1])...(ls[n])
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
    # MANUAL ENTRY [-116] TO SHIFT MERGED DOCUMENTS DUE TO DUPLICATES
    file_2[title] = file_2[title].shift(-116)
    file_0 = file_2[file_2['Financial Ratio'].notna()]

filename = "-All-Ratios.csv"
file_0.to_csv("Y" + filename)
# FORMATING :: ROTATION OVER Y-AXIS AND SAVE DOCUMENT FROM RESULT
file_0 = file_0.T
file_0.to_csv("X" + filename)


# In[ ]:


# RESET SORTED LIST FOR LOOP ('-Ratio-DF.csv')
mydir = os.getcwd()
result = []

for file in os.listdir(mydir):
    if file.endswith("-Ratio-DF.csv"):
        result.append(os.path.join(file))
        
sorted_list_0 = sorted(result)
length = len(sorted_list_0)
# INPUT 1 [-3m] PRIOR TO THE FIRST DATE. USED FOR INITIAL ls[0] ANALYSIS
# SET STARTING DATE MANUALLY (UPDATE REQUIRED TO ADJUST DYNAMIC SOFTWARE)
ls = ['2016-03-31']

for i in range(length):
    input_date = sorted_list_0[i][:-13]
    ls.append(input_date)


# In[ ]:


# WARNING!!! THIS HAS ALREADY BEEN DONE PREVIOUSLY (ref. # S3 _ CSV Combined Ratio & [-3] Alphabet-TF)
# CREATE RECURRENT DEF OR FUNCTION THAT CAN BE CALLED (LOOK AT PARAMETERS AND DEPENDENCIES)
# * EXTRACT AND CREATE 'csv' DOCUMENT WITH QUARTERLY [-3m] FINANCIAL VARIABLES, LATER COMBINED-FV
file = pd.read_csv('Alphabet Inc.csv')
date_prefix = ls[0][:-2]
date_ls = ["31", "30", "29", "28"]

upd_date_0 = date_prefix + date_ls[0]
upd_date_1 = date_prefix + date_ls[1]
upd_date_2 = date_prefix + date_ls[2]
upd_date_3 = date_prefix + date_ls[3]

if upd_date_0 in file.values:
    col_one_arr_P = file[file['Date'].str.contains(upd_date_0)].to_numpy()
    print(upd_date_0 + " exists.")
    index = file[file['Date'] == upd_date_1].index[0]
else:
    if upd_date_1 in file.values:
        col_one_arr_P = file[file['Date'].str.contains(upd_date_1)].to_numpy()
        print("Month finishes in -30")
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

df_age_negative = file[ file['Date'] < ls[0] ] # Step 1
df = file.drop(df_age_negative.index, axis=0) # Step 2

df_age_positive = file[ file['Date'] > ls[1] ]
df = df.drop(df_age_positive.index, axis=0)


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


# WARNING!!! SIMILAR TO :: (ref. # S2 _ Financial Variables & Ratios). CREATE NEW DEF/FUNC?
# AS OPPOSED TO LATEST 'Adj Close' PRICE [-3] ENDING MONTHS OR 'Date', THIS RETRIEVES CORRESPONDING [INDEX]
# * APPEND [INDEX] TO ls(result)
file = pd.read_csv('Alphabet Inc.csv')
result = []

for i in range(length):
    input_date = sorted_list_0[i][:-13]
    date_prefix = ls[i][:-2]
    date_ls = ["31", "30", "29", "28"]

    upd_date_0 = date_prefix + date_ls[0]
    upd_date_1 = date_prefix + date_ls[1]
    upd_date_2 = date_prefix + date_ls[2]
    upd_date_3 = date_prefix + date_ls[3]
    
    if upd_date_0 in file.values:
        col_one_arr_P = file[file['Date'].str.contains(upd_date_0)].to_numpy()
        index = file[file['Date'] == upd_date_0].index[0]
        result.append(index)
        
    else:
        if upd_date_1 in file.values:
            col_one_arr_P = file[file['Date'].str.contains(upd_date_1)].to_numpy()
            index = file.loc[file['Date']==upd_date_1]
            index = file[file['Date'] == upd_date_1].index[0]
            result.append(index)
            
        else:
            if upd_date_2 in file.values:
                col_one_arr_P = file[file['Date'].str.contains(upd_date_2)].to_numpy()
                index = file[file['Date'] == upd_date_2].index[0]
                result.append(index)
                
            else:
                if upd_date_3 in file.values:
                    col_one_arr_P = file[file['Date'].str.contains(upd_date_3)].to_numpy()
                    index = file[file['Date'] == upd_date_3].index[0]
                    result.append(index)


# In[ ]:


# FORMATING OF 'X-All-Ratios.csv' (_header)
file = pd.read_csv('X-All-Ratios.csv')

new_header = file.iloc[0]
file = file[1:]
file.columns = new_header


# In[ ]:


# FORMATING OF 'Alphabet-Ending-Months.csv' (_index, _columns)
file_1 = pd.read_csv('Alphabet-Ending-Months.csv')

file_2 = file_1.reset_index()
file_2.drop(columns=file_2.columns[0], axis=1, inplace=True)
file_2.drop(columns=file_2.columns[0], axis=1, inplace=True)
numbers = file_2["Open"]
numbers_0 = numbers.squeeze()


# In[ ]:


# CONCAT RELEVANT COLUMNS TO COMBINED '-DF' (High, Low, Close, Adj. Close && Volume)
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
# SAVE RESULT FOR FURTHER ANALYSIS (APPLICATION OF CORRELATION) (ref. # S6 _ CSV Ratio-TF-Variables && Correlation)
result.to_csv('Alphabet-DF-Analysis.csv', index=False)


# In[ ]:


#S6 _ CSV Ratio-TF-Variables && Correlation (CORRESPONDS TO DOCUMENTS REQUIRED FOR TECHNICAL ANALYSIS)
# 'Alphabet-Ending-Months.csv' LATER ADDED TO '-DF'
# * [OUTPUTS] :: [CROSS(/INTER)-ANALYSIS] CORRELATION BETWEEN FINANCIAL VARIABLES AND SHARE PRICE
# * CORRELATIONS INTERPRETED AS PERCENTAGE (%)


# In[ ]:


# SUB-PART:1 :: Build Full Table (COMBINED Variables-DF)
mydir = os.getcwd()
result = []

for file in os.listdir(mydir):
    if file.endswith("-Variables-DF.csv"):
        result.append(os.path.join(file))
        
sorted_list_0 = sorted(result)


# In[ ]:


# FORMATING sorted_list_0[0]
file_0 = pd.read_csv(sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)

title = sorted_list_0[0][:-17]
file_0 = file_0.set_axis(['Financial Variable', title], axis=1, inplace=False)


# In[ ]:


# FORMATING sorted_list_0[1] && CONCATENATE TO PREVIOUS DOCUMENT
## SIMILAR TO DEF|FUNCTION HERE-ABOVE. SIMPLIFICATION REQUIRED.
file_1 = pd.read_csv(sorted_list_0[1])
file_1 = file_1.drop(file_1.columns[0], axis=1)
file_1 = file_1.drop(file_1.columns[0], axis=1)

title = sorted_list_0[1][:-17]
file_1.rename({'Financial Variables /unit': title}, axis=1, inplace=True)
file_0 = file_0.join(file_1)


# In[ ]:


# FORMATING sorted_list_0[2] && CONCATENATE TO PREVIOUS DOCUMENT
## SIMILAR TO DEF|FUNCTION HERE-ABOVE. SIMPLIFICATION REQUIRED.
file_3 = pd.read_csv(sorted_list_0[2])
file_3 = file_3.drop(file_3.columns[0], axis=1)
file_3 = file_3.drop(file_3.columns[0], axis=1)

title = sorted_list_0[2][:-17]
file_0 = file_0.join(file_3)


# In[ ]:


# FORMATING sorted_list_0[i] (LOOP FROM [3]...[n]) && CORRESPONDING 'CONCATENATE'
file_0 = pd.read_csv(sorted_list_0[0])
file_0 = file_0.drop(file_0.columns[0], axis=1)
title = sorted_list_0[0][:-17]
file_0 = file_0.set_axis(['Financial Variable', title], axis=1, inplace=False)

sorted_list_1 = sorted_list_0[1:]
length = len(sorted_list_1)

for i in range(length):
    print(sorted_list_1[i])
    file_1 = pd.read_csv(sorted_list_1[i])
    file_1 = file_1.drop(file_1.columns[0], axis=1)
    file_1 = file_1.drop(file_1.columns[0], axis=1)

    title = sorted_list_1[i][:-17]
    file_1.rename({'Financial Variables /unit': title}, axis=1, inplace=True)
    file_0 = file_0.join(file_1)
    file_0.to_csv('Combined_Variable.csv')
    
# FORMATING :: ROTATION OVER Y-AXIS AND SAVE DOCUMENT 'file_2'
file_2 = file_0.T
file_2.to_csv("Combined_Variable-X-All.csv")


# In[ ]:


# SUB-PART:3 :: Build Full Table (COMBINED Ratio-TF)
mydir = os.getcwd()
result = []

for file in os.listdir(mydir):
    if file.endswith("-Ratio-TF.csv"):
        result.append(os.path.join(file))
        
sorted_list_0 = sorted(result)


# In[ ]:


# COMBINED 'Ratio-TF.csv' FOR FURTHER TECHNICAL ANALYSIS
file_0 = pd.read_csv(sorted_list_0[0])
title = sorted_list_0[0][:-13]
sorted_list_0.remove(sorted_list_0[0])
length = len(sorted_list_0)

for i in range(length):
    input_date = sorted_list_0[i]
    file_1 = pd.read_csv(sorted_list_0[i])
    title = sorted_list_0[i][:-13]
    if i == 0:
        file_2 = file_0.append(file_1)
    else:
        file_2 = file_2.append(file_1)

# SAVE CORRESPONDING FILE|DOCUMENT
filename = "-All-Ratios.csv"
file_2.to_csv("S5 _ Y" + filename, index=False, encoding='utf-8-sig')
# FORMATING :: ROTATION OVER Y-AXIS AND SAVE DOCUMENT 'file_2'
file_2 = file_2.T
file_2.to_csv("S5 _ X" + filename, header=False, encoding='utf-8-sig')


# In[ ]:


# SAVE 'P2 _ Correlation.csv' FOR FURTHER ANALYSIS 
# * LATER USE FINANCIAL VARIABLES HIGHLY POSITIVELY vs. NEGATIVELY CORRELATED TO PREDICT SHARE PRICE USING ML&&AI
data = pd.read_csv("Alphabet-DF-Analysis.csv")
data.columns

#dataset = pd.DataFrame(data,columns=['GPM_0','OPM_0', 'OPER_MARGIN_VALUE', 'PM_0', 'ROA_0',
       #'ROI_0', 'ROE_VALUE', 'ROC_0', 'ROCE_0', 'EV_1_VALUE', 'EV_2_VALUE', 'EBIT_DEFAULT', 
        #'EBIT_VALUE', 'EBIT_VALUE_0', 'EBITDA_DEFAULT', 'EBITDA_VALUE', 'EBITDA_VALUE_0',
        #'EV_1_EBITDA_VALUE', 'EV_2_EBITDA_VALUE', 'EV_1_EBITDA_VALUE_0', 'EV_2_EBITDA_VALUE_0',
        #'EV_1_EBITDA_DEFAULT', 'EV_2_EBITDA_DEFAULT', 'EPS_VALUE', 'DPS_VALUE', ...####### ])
dataset = pd.DataFrame(data)
        
# SUMMARY OF DATASET
dis_summary = dataset.describe()
dis_summary.to_csv('S5 _ CSV z.##/P1 _ Distribution.csv')

# HISTOGRAMS FOR VARIABLES
dataset.hist()
dis00 = pd.DataFrame(data,columns=['GPM_0'])
dis00 = dis00.hist()

# SAVE DESCRIPTION AND VALUES(%) OF CORRELATIONS TO RESPECTIVE FOLDER
correlation_df = data.corr()
correlation_df.to_csv('S5 _ CSV z.##/P2 _ Correlation.csv')


# In[ ]:


################################################## T00 LR_0
# SEE FOLDER '_AI_Algorithms'
# (ANALYSIS FROM CORRELATIONS FOR [High][Low][Close][Adj Close][Volume] TO Financial Ratios IS  [-y] < x < [y])


# In[ ]:




