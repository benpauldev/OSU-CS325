import time

def MakeChange(coinValueList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

def changeCounter(coins,currency,result):
    used = [0]*(result)
    index = len(coins)
    usedCurrency = [0]*(len(currency))
    i = 0
    while index > 1:
        used[i] = coins[index - 1]
        index = index - coins[index -1]
        i = i + 1
    index = 0
    for i in used:

        for j in currency:
            if i == j:
                usedCurrency[index] += 1
            index = index + 1
        index = 0
    return usedCurrency

def saveFile(numbers):
    data = open('change.txt', 'a')
    line = (" ".join(str(i) for i in numbers))
    data.write("%s\n" % line)

def saveRunTime(number):
    timeData = open('runtimeNxA.txt', 'a')
    timeData.write("%s\n" % number)

def saveFileInt(number):
    data = open('change.txt', 'a')
    data.write("%s\n" % number)

def main():
    data = open("functionofNxA.txt","r")
    count = 1
    for index, line in enumerate(data.readlines()):
        value = 0
        if (index +1) %2 == 1:
                denominations = [int(i) for i in line.split()]
        if (index +1) %2 == 0:
            value = int(line)
        if value != 0:
            saveFile(denominations)
            saveFileInt(value)


            coinsUsed = [0]*(value+1)
            minCoins = [0]*(value+1)
            start_time = time.clock()
            result = MakeChange(denominations,value,minCoins,coinsUsed)
            runtime =time.clock() - start_time
            saveRunTime(runtime)
            usedCurrency=changeCounter(coinsUsed,denominations,result)
            saveFile(usedCurrency)
            saveFileInt(result)


main()