import pandas as pd
import pandas_ta as ta 


df = pd.read_csv('https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&outputsize=full&apikey=XG4BIIT0YH3PF5GG&datatype=csv')  #imporitng the file
# print(df) #checking if the file is correct or not


ta.supertrend(high=df['high'],low=df['low'],close=df['close'],period = 7,multiplier= 3)  #applying supertrend algo

df['sup'] = ta.supertrend(high=df['high'],low=df['low'],close=df['close'],period = 7,multiplier= 3)['SUPERT_7_3.0'] #making a new column in df for sup
# print(df.head(7)) #this will not print the sup as we give period 7
# print(df)

df['Buy_signal'] = 0  #making signals for buying
df['Sell_signal'] = 0 #making signals for selling
n = 7  #defining the lower limit
# print(df) #checking columns
for i in range(n,len(df)):
    if df['close'][i-1]<=df['sup'][i-1] and df['close'][i] > df['sup'][i]: #conditions for buying 
        df['Buy_signal'][i] = 1 #changing signals
    if df['close'][i-1]>=df['sup'][i-1] and df['close'][i] < df['sup'][i]: #conditions for selling
        df['Sell_signal'][i] = 1  #changing signals

print(df)  #print all the data
print(df[(df['Buy_signal'] > 0) | (df['Sell_signal'] > 0)]) #print all the places where signal changed