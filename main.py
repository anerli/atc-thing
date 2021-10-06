# Hello
#hi

# https://pypi.org/project/yfinance/
import yfinance as yf
import json


msft = yf.Ticker('MSFT')

#print(msft.info)

#with open('msft_info.json', 'w') as f:
#    json.dump(msft.info, f, indent=2)

#
data = msft.history(period = '1d')

#data = msft.history(interval=('01-01-2019', '01-01-2020'))

#print(data)

data = yf.download('MSFT','2020-01-01','2021-06-01')
#6 month chart
#print(data)

'''
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html?highlight=dataframe#pandas.DataFrame
'''

#for row in data[0,:]:
#    print(row)
#    print(data.to_string())
#print(data.to_string())

#print(data)

close = data['Adj Close']

#print(close)

#.plot()

import matplotlib.pyplot as plt

ma = close.rolling(window=50).mean()

#plt.plot(close)
#plt.plot(ma)
#plt.show()

daily_changes = []
for i in range(1,len(close)):
  daily_changes.append(close[i] / close[i-1] -1)

print(daily_changes)



performance = [100]
