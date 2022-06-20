def min_line(stockPrices):
    if len(stockPrices) <= 1:
        return 0
    if len(stockPrices) == 1:
        return 1
    count = 1
    stockPrices.sort()
    for item in range(len(stockPrices) - 2):
        y1 = stockPrices[item + 2][1] - stockPrices[item + 1][1]
        x1 = stockPrices[item + 2][0] - stockPrices[item + 1][0]
        y = stockPrices[item + 1][1] - stockPrices[item][1]
        x = stockPrices[item + 1][0] - stockPrices[item][0]
        if y1 * x == y * x1:
            continue
        else:
            count = count + 1
    return count
arr=[[100000001,99999999],[100000002,199999998],[100000003,299999998]] # Take your own input array
result=min_line(arr)
print(result)
