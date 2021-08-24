def recMC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] >0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1+ recMC(coinValueList,change-i,knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

def dpMakeChange(coinValueList, change, minCoins, coinUsed):
    for cents in range(change + 1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1< coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin =change
    while coin >0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin


# coinUsed = [0]*64
# coinCount = [0]*64
# cl  = [1,5,10,21,25]
# print(dpMakeChange(cl, 63, coinCount, coinUsed))
# printCoins(coinUsed, 63)


def Factorial(n):
    if n ==0:
        return 1
    elif not isinstance(n,int):
        return "请输入正整数"
    else:
        return n*Factorial(n-1)

# print(Factorial(5))
newList = []
def Reversal(List):
    if len(List) > 0:
        temp = List.pop()
        newList.append(temp)
        Reversal(List)
    return newList

print(Reversal([1,2,5,7,9,8,3,6,9,0,4,6,9]))



