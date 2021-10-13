'''
This crappy code is saved as a repository here:
https://github.com/anerli/atc-thing
'''
# 

# https://pypi.org/project/yfinance/
import yfinance as yf
import json
import indicators


msft = yf.Ticker('MSFT')

data = msft.history(period = '1d')

#data = msft.history(interval=('01-01-2019', '01-01-2020'))

#print(data)

data = yf.download('MSFT','2020-01-01','2021-06-01')
#6 month chart
#print(data)

'''
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame
'''

close = data['Adj Close']

#print(close)

#.plot()

import matplotlib.pyplot as plt

ma = indicators.sma(close, 20)

# plt.plot(close)
# plt.plot(ma)
# plt.ylabel("Price of Stock")
# plt.xlabel("Date")
# plt.show()

'''
daily_changes = []
for i in range(1,len(close)):
  daily_changes.append(close[i] / close[i-1] -1)
'''

weights = close.copy()
#.loc[:] = 0 is an indicator "where" something is will be equal to 0
#creates new empty data frame with 1 column and the same number of rows as the close data
weights.loc[:] = 0 #sets all values to 0

weights.loc[close > ma] = 1 #where close is greater than the moving average, set value = 1, others will stay 0
#print(weights)

print(weights[0])


print(indicators.calculate_performance(close, weights))
'''
performance = [100]*50 

#when we are holding the asset, we want to know the percent change in how much money we've made
for i in range(50,len(close)-2):
    weight = weights[i]
    if weight == 1:
        performance.append(performance[i-1] * (1 + daily_changes[i+1]))
    else:
        performance.append(performance[i-1])

print(performance)
'''