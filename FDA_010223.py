#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import datetime
import requests
import json

import warnings
warnings.filterwarnings('ignore')

#import sys
#sys.stdout = sys.__stdout__


# In[ ]:


# https://stockanalysis.com/stocks/goog/financials/
# https://finance.yahoo.com/quote/GOOG/history?p=GOOG

# Load CSV data into a DataFrame
balance_sheet = pd.read_csv("FDA_v1.0/Alphabet Inc (GOOG)/goog-balance-sheet-quarterly.csv", index_col=0)
income_statement = pd.read_csv("FDA_v1.0/Alphabet Inc (GOOG)/goog-income-statement-quarterly.csv", index_col=0)
cash_flow_statement = pd.read_csv("FDA_v1.0/Alphabet Inc (GOOG)/goog-cash-flow-statement-quarterly.csv", index_col=0)
ratios = pd.read_csv("FDA_v1.0/Alphabet Inc (GOOG)/goog-ratios-quarterly.csv", index_col=0)
historical_data = pd.read_csv("FDA_v1.0/Alphabet Inc (GOOG)/GOOG.csv") 

## FIX ERRORS AND COMPLETE CODE (TO RETRIEVE FINANCIAL VARIABLES) HERE-BELOW:

# Get the last row of the DataFrame
latest_data = historical_data.tail(1)
# Access the 'close' column of the last row
price = latest_data['Close']

# Extract the necessary variables from the DataFrame
earnings_per_share = income_statement.loc["EPS (Diluted)"].iloc[0]
book_value_per_share = balance_sheet.loc["Book Value Per Share"].iloc[0]
revenue = income_statement.loc["Revenue"].iloc[0]
current_assets = balance_sheet.loc["Total Current Assets"].iloc[0]
current_liabilities = balance_sheet.loc["Total Current Liabilities"].iloc[0]
total_debt = balance_sheet.loc["Total Debt"].iloc[0]
total_equity = balance_sheet.loc["Shareholders' Equity"].iloc[0]
net_income = income_statement.loc["Net Income"].iloc[0]
operating_income = income_statement.loc["Operating Income"].iloc[0]
interest_expense = income_statement.loc["Interest Expense / Income"].iloc[0]
average_inventory = balance_sheet.loc["Inventory"].iloc[0]
total_assets = balance_sheet.loc["Total Assets"].iloc[0]

# Calculate Cash Flow per Share (for PCF Ratio)
cash_flow = cash_flow_statement.loc["Operating Cash Flow"].iloc[0]
common_stock = balance_sheet.loc["Common Stock"].iloc[0]
cash_flow_per_share = cash_flow / common_stock

# Calculate Cost of Goods Sold [Revenue - Gross Profit]
gross_profit = income_statement.loc["Gross Profit"].iloc[0]
cost_of_goods_sold = revenue - gross_profit


# In[ ]:


def get_top_competitors(ticker):
    # Use the ticker symbol to get the company's top competitors
    url = f'https://api.iextrading.com/1.0/stock/{ticker}/peers'
    response = requests.get(url)
    data = json.loads(response.text)
    top_competitors = data
    return top_competitors

#get_top_competitors(ticker)


# In[ ]:


## ADD RATIO THRESHOLDS IN FUNCTION PARAMETERS AND WITHIN THE FUNCTION ITSELF.

def evaluate_stock(price, earnings_per_share, book_value_per_share, revenue, current_assets, current_liabilities, total_debt, total_equity, net_income, cash_flow_per_share, cost_of_goods_sold, operating_income, interest_expense, average_inventory, total_assets):
    # calculate ratios
    pe_ratio = price / (earnings_per_share*4) # (*4 due to 4 quarters?)
    pb_ratio = price / book_value_per_share
    ps_ratio = price / revenue
    current_ratio = current_assets / current_liabilities
    debt_to_equity_ratio = total_debt / total_equity
    roe = net_income / total_equity
    pcf_ratio = price / cash_flow
    dividend_yield = net_income / price
    gross_margin = (revenue - cost_of_goods_sold) / revenue
    operating_margin = operating_income / revenue
    quick_ratio = (current_assets - average_inventory) / current_liabilities
    interest_coverage_ratio = operating_income / interest_expense
    inventory_turnover = cost_of_goods_sold / average_inventory
    asset_turnover = revenue / total_assets
    
    price_earnings = total_equity / net_income # (price to earnings. = 18.23)
    #print(price_earnings)
    
    # make decision on stock value
    # P/E ratio: A P/E ratio below 15 is generally considered to indicate that a company is undervalued. However, this threshold can vary depending on the industry, and it is generally considered to be lower for companies in growth industries and higher for companies in more mature industries.
    # P/B ratio: A P/B ratio below 1 is generally considered to indicate that a company is undervalued.
    # P/S ratio: A P/S ratio below 1 is generally considered to indicate that a company is undervalued.
    # Price to Cash Flow (P/CF) ratio: A P/CF ratio below 15 is generally considered to indicate that a company is undervalued.
    # Dividend Yield: A Dividend Yield above 5% is generally considered to indicate that a company's stock is undervalued.
    if pe_ratio.values[0] < 15 and pb_ratio.values[0] < 1 and ps_ratio.values[0] < 1 and pcf_ratio.values[0] < 15 and dividend_yield.values[0] > 0.05:
        stock_valuation = "The company is undervalued."
    else:
        stock_valuation = "The company may not be undervalued."
        print('Stock valuation :')
        if pe_ratio.values[0] >= 15:
            print("- [MARKET VALUE] - The price-to-earnings ratio is greater than or equal to 15, which may indicate that the company is overvalued.")
            print("pe_ratio :: " + str(pe_ratio.values[0]))
        elif pb_ratio.values[0] >= 1:
            print("- [MARKET VALUE] - The price-to-book value ratio is greater than or equal to 1, which may indicate that the company is overvalued.")
        elif ps_ratio.values[0] >= 1:
            print("- [MARKET VALUE] - The price-to-sales ratio is greater than or equal to 1, which may indicate that the company is overvalued.")
        elif pcf_ratio.values[0] >= 15:
            print("- [MARKET VALUE] - The price-to-cash flow ratio is greater than or equal to 15, which may indicate that the company is overvalued.")
        elif dividend_yield.values[0] <= 0.05:
            print("- [MARKET VALUE] - The dividend yield is less than or equal to 0.05, which may indicate that the company is not generating enough income to pay dividends.")
        
    # make decision on financial performance
    # Current ratio: A current ratio above 2 is generally considered to indicate that a company is in a strong financial position.
    # Debt-to-equity ratio: A debt-to-equity ratio below 0.5 is generally considered to indicate that a company is in a strong financial position.
    # Return on Equity (ROE): An ROE above 15% is generally considered to indicate that a company is in a strong financial position.
    # Quick Ratio: A Quick Ratio above 1 is generally considered to indicate that a company is in a strong financial position.
    # Interest coverage ratio: A Interest coverage ratio above 1 is generally considered to indicate that a company is in a strong financial position.
    # Inventory turnover: A Inventory turnover above the industry average is generally considered to indicate that a company is in a strong financial position.
    # Asset turnover: A Asset turnover above the industry average is generally considered to indicate that a company is in a strong financial position.
    print("")
    if current_ratio > 2 and debt_to_equity_ratio < 0.5 and roe > 0.15 and quick_ratio > 1 and interest_coverage_ratio > 1:
        print("The company is in a strong financial position.")
    # ++ inventory_turnover > industry_average and asset_turnover > industry_average??
        financial_performance = "The company is in a strong financial position."
    else:
        financial_performance = "The company may not be in a strong financial position."
        print('Financial performance :')
        if current_ratio <= 2:
            print("- [SOLVENCY (LIQUIDITY)] - The current ratio is less than or equal to 2, which may indicate that the company may not have enough current assets to pay off its current liabilities.")
        elif debt_to_equity_ratio >= 0.5:
            print("- [SOLVENCY] - The debt-to-equity ratio is greater than or equal to 0.5, which may indicate that the company may not be in a strong financial position.")
        elif roe <= 0.15:
            print("- [PROFITABILITY] - The return-on-equity ratio is less than or equal to 0.15, which may indicate that the company may not be in a strong financial position.")
            print("roe :: " + str(roe))
        elif quick_ratio <= 1:
            print("- [SOLVENCY (LIQUIDITY)] - The quick ratio is less than or equal to 1, which may indicate that the company may not be in a strong financial position.")
        elif interest_coverage_ratio <= 1:
            print("- [SOLVENCY] - The interest coverage ratio is less than or equal to 1, which may indicate that the company may not be in a strong financial position.")
#        else:
#            print("Inventory and/or Asset turnover is less than or equal to Industry Average")
    return stock_valuation, financial_performance

# Call the evaluate_stock function
stock_valuation, financial_performance = evaluate_stock(price, earnings_per_share, book_value_per_share, revenue, current_assets, current_liabilities, total_debt, total_equity, net_income, cash_flow, cost_of_goods_sold, operating_income, interest_expense, average_inventory, total_assets)
# Print the decision
print('')
print("Stock valuation : ", stock_valuation)
print("Financial performance : ", financial_performance)


# In[ ]:


def decision(df, date):
    #Extract the current date
    df = df[df['Date'] == date]
    if (df["macd"] > df["macd_signal"]).all() and (df["rsi"] > 50).all() and (df["obv"] > 0).all() and (df["cmf"] > 0).all():
        return "Buy"
    elif (df["macd"] < df["macd_signal"]).all() and (df["rsi"] < 50).all() and (df["obv"] < 0).all() and (df["cmf"] < 0).all():
        return "Sell"
    else:
        return "Hold"

# The top trend indicators for short-term buy and sell signals include moving averages, trendlines, and the 
#Relative Strength Index (RSI). Volume indicators include the on-balance volume (OBV) and the Chaikin Money Flow 
#(CMF). Volatility indicators include the Bollinger Bands and the Average True Range (ATR). Momentum indicators 
#include the RSI and the Moving Average Convergence Divergence (MACD).

# To increase accuracy in buy or sell decisions, you can combine several of these indicators by using them in 
#conjunction with one another. For example, you could use a moving average to identify the overall trend and then 
#use the RSI to confirm the strength of the trend. Additionally, you could use the OBV to confirm the strength of 
#the trend by showing the volume behind the price movement. To further increase accuracy, you could also use the 
#CMF to confirm the strength of the trend by showing the money flow behind the price movement.

# Import historical stock price data
data = pd.read_csv("FDA_v1.0/Alphabet Inc (GOOG)/GOOG.csv")

# Process data into a DataFrame
df = pd.DataFrame(data)

# Enter time range used for plots()
time_range = input("Enter the time range (days, weeks, or months): ")
num_time_range = int(input("Enter the number of " + time_range + ": "))
if time_range == "days":
    num_days = num_time_range
elif time_range == "weeks":
    num_days = num_time_range * 7
elif time_range == "months":
    num_days = num_time_range * 30
else:
    print("Invalid time range entered.")
    num_days = 0
print("The number of days in the selected time range is: ", num_days)

# Get the current date
now = datetime.datetime.now()
current_date = now.strftime("%Y-%m-%d")

# Check if the current date exists in the dataframe
if not (df['Date'] == current_date).any():
    # If not, use the latest date in the dataframe
    current_date = df['Date'].max()
    print("Current date not available, using latest available date:", current_date)

#
#plot_technical_indicators(df, num_days)

#
# Keep only the last n days of the dataframe
current_date = pd.to_datetime(df['Date']).max()
n_days_ago = current_date - pd.DateOffset(days = num_days)
df['Date'] = pd.to_datetime(df['Date'])
df = df[df['Date'] >= n_days_ago]

# Calculate the 12-day and 26-day exponential moving averages
df["ema12"] = df["Close"].ewm(span=12, adjust=False).mean()
df["ema26"] = df["Close"].ewm(span=26, adjust=False).mean()

# Calculate the MACD by taking the difference between the two moving averages
df["macd"] = df["ema12"] - df["ema26"]

# Calculate the 9-day moving average of the MACD
df["macd_signal"] = df["macd"].rolling(window=9).mean()

# Calculate the RSI
delta = df["Close"].diff()
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)
avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()
rs = avg_gain / avg_loss
df["rsi"] = 100 - (100 / (1 + rs))

# Calculate the OBV
df["obv"] = df["Volume"].where(delta > 0, -df["Volume"]).cumsum()

# Calculate the CMF
df["cmf"] = (df["Close"] - df["Low"] - df["High"] + df["Close"]) / (df["High"] - df["Low"]) * df["Volume"]

# Calculate the Stochastic Oscillator
sto_k = 100 * (df["Close"] - df["Low"].rolling(14).min()) / (df["High"].rolling(14).max() - df["Low"].rolling(14).min())
df["sto"] = sto_k.rolling(3).mean()

# Calculate the ATR
#atr = ta.volatility.average_true_range(df['High'], df['Low'], df['Close'], n=14)
df["atr"] = df['High'].rolling(window=14).max() - df['Low'].rolling(window=14).min()

# Calculate the Bollinger Bands
#bb = ta.volatility.bollinger_mavg(df['Close'], n=20, ndev=2, matype=ta.volatility.ATR)
rolling_mean = df["Close"].rolling(window=20).mean()
rolling_std = df["Close"].rolling(window=20).std()
df["upperband"] = rolling_mean + (rolling_std * 2)
df["lowerband"] = rolling_mean - (rolling_std * 2)

# Plot the data
plt.figure(figsize=(20,10))
plt.plot(df["Close"], label="Close")
plt.plot(df["macd"], label="MACD")
plt.plot(df["macd_signal"], label="MACD Signal")
plt.plot(df["rsi"], label="RSI")
plt.plot(df["obv"], label="OBV")
plt.plot(df["cmf"], label="CMF")
plt.legend(loc="best")
plt.show()
    
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(20, 10))

# Plot the Close price on the first subplot
axes[0, 0].plot(df["Close"], label="Close")
axes[0, 0].plot(df['upperband'], label='Upper Band', alpha=0.5)
axes[0, 0].plot(df['lowerband'], label='Lower Band', alpha=0.5)
axes[0, 0].set_title("Close Price")

# Plot the MACD and MACD signal on the second subplot
axes[0, 1].plot(df["macd"], label="MACD")
axes[0, 1].plot(df["macd_signal"], label="MACD Signal")
axes[0, 1].set_title("MACD and MACD Signal")

# Plot the RSI on the third subplot
axes[1, 0].plot(df["rsi"], label="RSI")
axes[1, 0].set_title("RSI")

# Plot the OBV and CMF on the fourth subplot if their range is similar
if abs(df["obv"].min() - df["obv"].max()) < abs(df["cmf"].min() - df["cmf"].max()):
    axes[1, 1].plot(df["obv"], label="OBV")
    axes[1, 1].plot(df["cmf"], label="CMF")
    axes[1, 1].set_title("OBV and CMF")
else:
    # Plot the OBV and CMF on separate subplots if their range is different
    axes[1, 1].plot(df["obv"], label="OBV")
    axes[1, 1].set_title("OBV")
    axes[2, 0].plot(df["cmf"], label="CMF")
    axes[2, 0].set_title("CMF")

# Plot the Average True Range on the sixth subplot
axes[2, 1].plot(df["atr"], label="ATR")
axes[2, 1].set_title("ATR")

plt.tight_layout()
plt.show()

# Print the decision
print("Decision for date :",current_date, ":", decision(df,current_date))


# In[ ]:


import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf#, plot_diagnostics
from statsmodels.tsa.arima.model import ARIMA

# Load the close price data into a pandas dataframe
df = pd.read_csv("FDA_v1.0/Alphabet Inc (GOOG)/GOOG.csv", index_col = 0)

# Fit the ARIMA model
model = ARIMA(df['Close'], order=(1, 0, 1))
fit = model.fit()

# Plot the actual close price and moving average from ARIMA close price
plt.figure(figsize=(20,10))
plt.plot(df['Close'], label='Actual Close Price')
plt.plot(fit.fittedvalues, label='ARIMA Close Price')
plt.legend(loc='best')
plt.show()

# Plot the autocorrelation and partial autocorrelation plots
plot_acf(fit.resid, lags=30)
plt.show()
plot_pacf(fit.resid, lags=30)
plt.show()

# Plot the ARIMA diagnostic plots
#plot_diagnostics(fit, lags=30)
#plt.show()


# In[ ]:


from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_absolute_error

# Load the close price data into a pandas dataframe
df = pd.read_csv("FDA_v1.0/Alphabet Inc (GOOG)/GOOG.csv", index_col = 0)

# Create a list to store the accuracy values for each model
accuracy_list = []

# Fit the ARIMA model
model = ARIMA(df['Close'], order=(1, 0, 1))
fit_arima = model.fit()
pred_arima = fit_arima.predict(start=df.shape[0], end=df.shape[0]+30)

# Fit the ARIMAX model
model_arimax = SARIMAX(df['Close'], exog=df['Volume'], order=(1, 0, 1))
fit_arimax = model_arimax.fit()
exog_forecast = df['Close'].iloc[-31:].values
pred_arimax = fit_arimax.predict(start=df.shape[0], end=df.shape[0]+30, exog=exog_forecast.reshape(-1, 1))

# Fit the SARIMA model
model_sarima = SARIMAX(df['Close'], seasonal_order=(1, 0, 1, 30), enforce_stationarity=False, enforce_invertibility=False)
fit_sarima = model_sarima.fit()
pred_sarima = fit_sarima.predict(start=df.shape[0], end=df.shape[0]+30)

# Fit the SARIMAX model
model_sarimax = SARIMAX(df['Close'], exog=df['Volume'], seasonal_order=(1, 0, 1, 30), enforce_stationarity=False, enforce_invertibility=False)
fit_sarimax = model_sarimax.fit()
exog_forecast = df['Close'].iloc[-31:].values
pred_sarimax = fit_sarimax.predict(start=df.shape[0], end=df.shape[0]+30, exog=exog_forecast.reshape(-1, 1))

# Get the last six months of data
#df_six_months = df[-180:]

# Calculate accuracy for each model
accuracy_arima = np.round(mean_absolute_error(df['Close'][-30:], pred_arima[:30]), 2)
accuracy_arimax = np.round(mean_absolute_error(df['Close'][-30:], pred_arimax[:30]), 2)
accuracy_sarima = np.round(mean_absolute_error(df['Close'][-30:], pred_sarima[:30]), 2)
accuracy_sarimax = np.round(mean_absolute_error(df['Close'][-30:], pred_sarimax[:30]), 2)
print('ARIMA :: ' + str(accuracy_arima))
print('ARIMAX :: ' + str(accuracy_arimax))
print('SARIMA :: ' + str(accuracy_sarima))
print('SARIMAX :: ' + str(accuracy_sarimax))

# Print the model with the best accuracy
#models = ['ARIMA', 'ARIMAX', 'SARIMA', 'SARIMAX']
#accuracies = [accuracy_arima, accuracy_arimax, accuracy_sarima, accuracy_sarimax]

#best_model = None
#best_error = float('inf')
# Calculate the mean absolute error for each model
#for name, model in models.items():
#    pred = model.predict(start=df.shape[0], end=df.shape[0]+30, exog=exog_forecast)
#    error = mean_absolute_error(df['Close'][-31:], pred)
#    if error < best_error:
#        best_error = error
#        best_model = name

# Print the model with the lowest mean absolute error
#print(f"Best model: {best_model}")

# Get the last six months of data
df_six_months = df[-180:]

# Plot the actual close price and moving average from ARIMA close price
plt.figure(figsize=(20,10))
#plt.plot(df_six_months['Close'], label='Actual Close Price', linewidth=2)
plt.plot(fit.fittedvalues[-90:], label='ARIMA Close Price', linewidth=2)
plt.plot(fit_arimax.fittedvalues[-90:], label='ARIMAX Close Price', linewidth=2)
plt.plot(fit_sarima.fittedvalues[-90:], label='SARIMA Close Price', linewidth=2)
plt.plot(fit_sarimax.fittedvalues[-90:], label='SARIMAX Close Price', linewidth=2, alpha=0.5)
plt.ylim(df_six_months['Close'].min() - 1, df_six_months['Close'].max() + 1)
plt.legend(loc='best')
plt.show()

# CONDUCT PREDICTIVE MODEL BASED ON 'MA' WITH LOWEST 'MAE' =>> 'SARIMAX'
#pred_sarimax = fit_sarimax.predict(start=df.shape[0], end=df.shape[0]+30, exog=exog_forecast.reshape(-1, 1))
print("SARIMAX predictions:", pred_sarimax)
# SARIMAX plot
plt.figure(figsize=(20,10))
plt.plot(df['Close'], label='Actual Close Price')
plt.plot(df.index[-31:], pred_sarimax, label='SARIMAX Predictions')
plt.legend(loc='best')
plt.show()


# In[ ]:


# CATEGORICAL, CLASSIFICATION PROCESS: [0] INDICATES LESS OR EQUAL TO PREVIOUS, [1] INDICATES HIGHER TO PREVIOUS

# list of files to be combined
files = ['FDA_v1.0/Alphabet Inc (GOOG)/goog-balance-sheet-quarterly.csv',
         'FDA_v1.0/Alphabet Inc (GOOG)/goog-income-statement-quarterly.csv', 
         'FDA_v1.0/Alphabet Inc (GOOG)/goog-cash-flow-statement-quarterly.csv',
         'FDA_v1.0/Alphabet Inc (GOOG)/goog-ratios-quarterly.csv']

# read the first file and create a dataframe
df = pd.read_csv(files[0])

# loop through the rest of the files and reset the index
for file in files[1:]:
    temp_df = pd.read_csv(file).reset_index(drop=True)
    df = df.append(temp_df)

# select only the columns that have numeric headers
df = df.filter(regex='[^a-zA-Z]')
# Identify and remove columns that have over 30% missing values
missing_values_count = df.isnull().sum()
cols_to_drop = missing_values_count[missing_values_count/len(df) > 0.2].index
df = df.drop(columns=cols_to_drop)

# create a list of headers from the combined dataframe
headers_list = list(df.columns)

# read the forth csv file
df_4 = pd.read_csv('FDA_v1.0/Alphabet Inc (GOOG)/GOOG.csv')
df_4['Date'] = pd.to_datetime(df_4['Date'])
df_4.set_index('Date', inplace=True)
# resample the dataframe to get the close price at the end of every quarter
df_quarterly = df_4.resample('Q').last()

# transpose the df_4 and keep only rows whose index is "Close"
df_quarterly = df_quarterly.transpose()
df_quarterly = df_quarterly.loc[["Close"]]

# add the transposed df_4 to the old df
df_quarterly.columns = df_quarterly.columns.astype(str)
df = pd.concat([df, df_quarterly], ignore_index=True)
df.at[df.index[-1], df.columns[0]] = "Close"
# Identify and remove the columns that have NaN values in the last row
cols_to_drop = df.iloc[-1].isnull()
df = df.drop(columns=cols_to_drop[cols_to_drop == True].index)
# Remove columns that have over 20% missing values
missing_values_count = df.isnull().sum()
cols_to_drop = missing_values_count[missing_values_count/len(df) > 0.2].index
df = df.drop(columns=cols_to_drop)

# Save file to csv.
df = (df.set_index(df.columns[0])).T
df = df.sort_index()
df.to_csv('/Users/qwerg/Desktop/Combined_C.csv')


# In[ ]:


# Load data into a DataFrame
#df = pd.read_csv('/Users/qwerg/Desktop/Combined_C.csv', index_col = 0)
corr_matrix = df.corr()
corr_matrix.to_csv('/Users/qwerg/Desktop/Correlation_C.csv')

# Get the last row of the DataFrame
last_row = corr_matrix.tail(1)
# Create an empty list to store the column names
column_names = []
# Iterate through each column in the last row
for col in last_row.columns:
    # Check if the value is greater than or equal to 0.9
    if (last_row[col].values >= 0.9).all():
        # Add the column name to the list
        column_names.append(col)

# Get the number of columns in the DataFrame
num_columns = df.shape[1]
# Get the number of elements in the list
num_elements = len(column_names)
# Calculate the ratio of elements in the list over the number of columns
ratio = num_elements / num_columns
print(str(int(ratio*100)) + "% of financial variables are highly correlated to the 'Close' price (e.g. > 0.9)")

df = df.loc[:, column_names]

df.to_csv('/Users/qwerg/Desktop/Combined_C_v2.csv')

# AT THIS STAGE, IT IS POSSIBLE TO CONDUCT MULTI-DIMENSIONAL REGRESSION TO PREDICT 'Close' VARIABLE.

# (...)

# AT THIS STAGE, WE SET THE VALUES TO EITHER '0' OR '1' DEPENDING IF THE VARIABLES INCREASED OVER THAT PERIOD OF
# TIME AND WHAT EFFECT IT HAD ON THE 'Close' VARIABLE, INCREASE/DECREASE?
# THIS IS MADE OF BINARY VALUES, EXPRESSING CLASSIFICATION 

# Iterate over columns
df_copy = df.copy()
for i in range(df.shape[1]):
    for j in range(df.shape[0]):
        if j == 0:
            df.iat[j,i] = pd.np.nan
        elif df_copy.iat[j,i] > df_copy.iat[j-1,i]:
            df.iat[j,i] = 1
        else:
            df.iat[j,i] = 0

#df.to_csv('/Users/qwerg/Desktop/Combined_Classification.csv')

# The goal is to input the new financial variables and financial ratios from the past 3 months and assign their 
# effects to the change in stock price after three months. Thus we need to shift the 'Close' by 1 up.
df['Close'] = df['Close'].shift(-1)
df.iloc[0] = pd.np.nan

n_headers_list = list((df.T).columns)
max_headers_list = max(n_headers_list)

if max_headers_list[-5:] == '03-31':
    next_q = max(n_headers_list)[0:5] + '06-30'
elif max_headers_list[-5:] == '06-30':
    next_q = max(n_headers_list)[0:5] + '09-30'
elif max_headers_list[-5:] == '09-30':
    next_q = max(n_headers_list)[0:5] + '12-31'
elif max_headers_list[-5:] == '12-31':
    next_q = int(max_headers_list[0:5] + 1) + '03-31'

df_quarterly = df_quarterly.transpose()

if df_quarterly._get_value(next_q, 'Close') > df_quarterly._get_value(max_headers_list, 'Close'):
    # Change the value of the bottom-right cell to a new value (5)
    df.iat[-1, -1] = 1
else:
    df.iat[-1, -1] = 0

df.to_csv('/Users/qwerg/Desktop/Combined_Classification.csv')

# We can notice that there is a very strong decrease in accuracy to predict the change in stock price over the 
# next three months if we base ourselves on a company's financial statements in the last three months

# Accuracy goes from 0.9 to 0.4 on average.

# This is due to the fact that it is much easier to predict a company's stock price over a period of time if we 
# can evaluate a company's performance throughout that same period of time using financial statements.

# However, there are a lot more irregularities and inconsistencies if we try to predict a company's stock price 
# ,in the future, by evaluating a company's performance over another period of time, in the past.


# In[ ]:


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load your dataframe
df = pd.read_csv("/Users/qwerg/Desktop/Combined_Classification.csv", index_col = 0)
df = df.iloc[1:]

# Define your features and target
X = df.drop(['Close'], axis=1)
y = df['Close']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a logistic regression model
log_reg = LogisticRegression()

# Fit the model to the training data
log_reg.fit(X_train, y_train)

# Get predictions for the test set
y_pred = log_reg.predict(X_test)

# Evaluate the model
score = log_reg.score(X_test, y_test)
print("Accuracy:", score)

# Load new data
#new_data = pd.read_csv("new_data.csv")

# Extract the independent variables from the new data
#X_new = new_data.drop(['Date'], axis=1)

# Make predictions on the new data using the trained logistic regression model
#y_pred_new = log_reg.predict(X_new)


# In[ ]:


from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.tree import plot_tree

# Load your dataframe
df = pd.read_csv("/Users/qwerg/Desktop/Combined_Classification.csv", index_col = 0)
df = df.iloc[1:]

# Define your features and target
X = df.drop(['Close'], axis=1)
y = df['Close']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree model
tree = DecisionTreeClassifier()

# Fit the model to the training data
tree.fit(X_train, y_train)

# Get predictions for the test set
y_pred = tree.predict(X_test)

# Evaluate the model
score = tree.score(X_test, y_test)
print("Accuracy:", score)

# Load new data
#new_data = pd.read_csv("new_data.csv")

# Extract the independent variables from the new data
#X_new = new_data.drop(['Date'], axis=1)

# Make predictions on the new data using the trained decision tree model
#y_pred_new = tree.predict(X_new)

fig = plt.figure(figsize=(25,20))
_ = plot_tree(tree, feature_names=X_train.columns, filled=True, class_names=['0', '1'])


# In[ ]:


from sklearn import svm

# Load your dataframe
df = pd.read_csv("/Users/qwerg/Desktop/Combined_Classification.csv", index_col = 0)
df = df.iloc[1:]

# Define your features and target
X = df.drop(['Close'], axis=1)
y = df['Close']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a support vector machine (SVM) model
svm_model = svm.SVC()

# Fit the model to the training data
svm_model.fit(X_train, y_train)

# Get predictions for the test set
y_pred = svm_model.predict(X_test)

# Evaluate the model
score = svm_model.score(X_test, y_test)
print("Accuracy:", score)

# Load new data
#new_data = pd.read_csv("new_data.csv")

# Extract the independent variables from the new data
#X_new = new_data.drop(['Date'], axis=1)

# Make predictions on the new data using the trained SVM model
#y_pred_new = svm_model.predict(X_new)


# In[ ]:


from sklearn.naive_bayes import GaussianNB

# Load your dataframe
df = pd.read_csv("/Users/qwerg/Desktop/Combined_Classification.csv", index_col = 0)
df = df.iloc[1:]

# Define your features and target
X = df.drop(['Close'], axis=1)
y = df['Close']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Gaussian Naive Bayes model
naive_bayes_model = GaussianNB()

# Fit the model to the training data
naive_bayes_model.fit(X_train, y_train)

# Get predictions for the test set
y_pred = naive_bayes_model.predict(X_test)

# Evaluate the model
score = naive_bayes_model.score(X_test, y_test)
print("Accuracy:", score)

# Load new data
#new_data = pd.read_csv("new_data.csv")

# Extract the independent variables from the new data
#X_new = new_data.drop(['Date'], axis=1)

# Make predictions on the new data using the trained naive bayes theorem model
#y_pred_new = naive_bayes_model.predict(X_new)


# In[ ]:


from sklearn.neighbors import KNeighborsClassifier

# Load your dataframe
df = pd.read_csv("/Users/qwerg/Desktop/Combined_Classification.csv", index_col = 0)
df = df.iloc[1:]

# Define your features and target
X = df.drop(['Close'], axis=1)
y = df['Close']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a KNN model
knn_model = KNeighborsClassifier(n_neighbors=5)

# Fit the model to the training data
knn_model.fit(X_train, y_train)

# Get predictions for the test set
y_pred = knn_model.predict(X_test)

# Evaluate the model
score = knn_model.score(X_test, y_test)
print("Accuracy:", score)


# In[ ]:


from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense

# Load the data
data = pd.read_csv("/Users/qwerg/Desktop/Combined_Classification.csv", index_col = 0)
print(" [Load the data] - Completed ")

# Prepare the data
X = data.drop(["Close"], axis=1)
y = data["Close"]
scaler = StandardScaler()
X = scaler.fit_transform(X)
print(" [Prepare the data] - Completed ")

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(" [Split the data into training and testing sets] - Completed ")

# Create the neural network
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
print(" [Create the neural network] - Completed ")

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
print(" [Compile the model] - Completed ")

# Fit the model
model.fit(X_train, y_train, epochs=20, batch_size=32)
print(" [Fit the model] - Completed ")

# Evaluate the model
score = model.evaluate(X_test, y_test)
print(f'Test accuracy: {score[1]:.3f}')


# In[ ]:


# Import necessary libraries
from sklearn.ensemble import RandomForestRegressor
#from sklearn.metrics import classification_report # Only for Classification problems.

# Read in the csv document
df = pd.read_csv('/Users/qwerg/Desktop/Combined_C_v2.csv', index_col = 0)
df = df.dropna(axis=1)

# Split the data into independent and dependent variables
X = df.drop(['Close'], axis=1)
y = df['Close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a Random Forest Regressor model
rf = RandomForestRegressor()

# Fit the model to the training data
rf.fit(X_train, y_train)

# Use the model to predict the stock close price on the test data
y_pred = rf.predict(X_test)

# Visualize the results by plotting the predicted values against the actual values
import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Close Price')
plt.ylabel('Predicted Close Price')
plt.show()

# Print testing accuracy for Random Forest
mae = mean_absolute_error(y_test, y_pred)
print("Random Forest testing accuracy: ", mae)


# In[ ]:


# Import necessary libraries
from sklearn import svm

# Read in the csv document
#df = pd.read_csv('financial_data.csv')

# Split the data into independent and dependent variables
#X = df.drop(['close_price'], axis=1)
#y = df['close_price']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a SVM model
svm = svm.SVR()

# Fit the model to the training data
svm.fit(X_train, y_train)

# Use the model to predict the stock close price on the test data
y_pred = svm.predict(X_test)

# Visualize the results by plotting the predicted values against the actual values
import matplotlib.pyplot as plt
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Close Price')
plt.ylabel('Predicted Close Price')
plt.show()

# Print testing accuracy for SVM
mae = mean_absolute_error(y_test, y_pred)
print("SVM testing accuracy: ", mae)


# In[ ]:


from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

# load the dataset
#df = pd.read_csv('/Users/qwerg/Desktop/Combined_C_v2.csv', index_col = 0)
#df = df.dropna(axis=1)

# split the dataset into features and target
#X = df.drop('Close', axis=1)
#y = df['Close']

# split the dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# fit and predict using Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# fit and predict using SVM
svm = SVR(C=1.0, epsilon=0.2)
svm.fit(X_train, y_train)
y_pred_svm = svm.predict(X_test)

# print the performance metric of Random Forest
print("Random Forest MAE: ", mean_absolute_error(y_test, y_pred_rf))
print("Random Forest MSE: ", mean_squared_error(y_test, y_pred_rf))
print("Random Forest R2 score: ", r2_score(y_test, y_pred_rf))

print('')
# print the performance metric of SVM
print("SVM MAE: ", mean_absolute_error(y_test, y_pred_svm))
print("SVM MSE: ", mean_squared_error(y_test, y_pred_svm))
print("SVM R2 score: ", r2_score(y_test, y_pred_svm))

print('')
plt.figure(figsize=(12,6))
plot_tree(rf.estimators_[0], filled=True, feature_names = X_train.columns);
# Save the figure
plt.savefig('/Users/qwerg/Desktop/Random_Forest.jpg', dpi=1000)
print(y_pred_rf)


# In[ ]:


#new_sample = [[2, 3, 4]]
#predicted_value = rf.predict(new_sample)
#print(predicted_value)


# In[ ]:





# In[ ]:


import math
from sklearn.preprocessing import MinMaxScaler
from keras.layers.core import Dense, Dropout
from keras.layers import LSTM
from keras.models import Sequential

df = pd.read_csv('/Users/qwerg/Desktop/Combined_C_v2.csv', index_col = 0)
data = df.filter(['Close'])
dataset = data.values
#print(dataset)
training_data_len = math.ceil(len(dataset) * 0.8) # LOWER PARAMETER '0.8' TO PREDICT FOR LONGER PERIOD UP TO NOW
#print(training_data_len)
scaler = MinMaxScaler(feature_range = (0,1))
scaled_data = scaler.fit_transform(dataset)
train_data = scaled_data[0:training_data_len,:]
x_train = []
y_train = []
# '5', '10', '15'? Starting with 5. # INCREASE PARAMETER '5' TO TRAIN DATA OVER MORE INSTANCES AT ONCE
for i in range(5, len(train_data)):
    x_train.append(train_data[i-5:i, 0])
    y_train.append(train_data[i, 0])
    if i <= 5:
        print(x_train)
        print(y_train)
        print()
#    
x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
model = Sequential()
model.add(LSTM(50, return_sequences = True,input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences = False))
model.add(Dense(25))
model.add(Dense(1))
model.compile(optimizer = 'adam', loss = 'mean_squared_error')
model.fit(x_train, y_train, batch_size = 1, epochs = 10)
test_data = scaled_data[training_data_len - 5:, :]
x_test = []
y_test = dataset[training_data_len:, :]
#
for i in range(5, len(test_data)):
    x_test.append(test_data[i-5:i, 0])
#
x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)
rmse = np.sqrt(np.mean(predictions - y_test)**2)
print(rmse)
train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions
#
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc = 'lower right')
plt.show()


# In[ ]:


# CONDUCT SENTIMENTAL ANALYSIS TO STUDY HUMAN INCENTIVES, POTENTIAL SPECULATION IN THE MARKET AS THE RESULT OF
#MEDIA AND NEWS COVERAGE AND SHARE OF INFORMATION GIVEN A SPECIFIC CORPORATION OR INDUSTRY.
# ALSO POSSIBLE TO INTERPRET SOME EFFECTS FROM A MACRO AND MICRO-ECONOMICS STANDPOINT
# USE NATURAL LANGUAGE PROCESSING (NLP) ALGORITHM TO DETERMINE 'GOOD' OR 'BAD' CONNOTATIONS


# In[ ]:


# WORK ON KNIME


# In[ ]:


# OTHER PREDICTIVE ALGORITHMS TO CONSIDER: XGBoost, Prophet, DeepAR, N-Beats.


# In[ ]:





# In[ ]:




