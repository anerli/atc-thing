'''
Simple Moving Average
data: A DataFrame object containing the data get to get the rolling average from.
window: Time period over which to get average
'''
def sma(data, window=20):
    return data.rolling(window=window).mean()

'''
data: Price data for the stock we want to calculate performance on.
weights: How much of the stock is owned at any point in time.
'''
def calculate_performance(data, weights):
    daily_changes = []
    for i in range(1,len(data)):
        daily_changes.append(data[i] / data[i-1] -1)

    performance = [100]

    for i in range(1, len(data)-2):
        weight = weights[i]
        if weight == 1:
            performance.append(performance[i-1] * (1 + daily_changes[i+1]))
        else:
            performance.append(performance[i-1])

    return performance
    