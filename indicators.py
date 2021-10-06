'''
Simple Moving Average
data: A DataFrame object containing the data get to get the rolling average from.
window: Time period over which to get average
'''
def sma(data, window=20):
    return data.rolling(window=window).mean()