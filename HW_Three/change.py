
# Change Making Dynamic Programming Algorithm
#minCoins and coinsUsed maintains list of coins and minimum number
# of coins as algorith progresses from 0...value (change)

def changeDP(coinList,change,minCoins,coinsUsed):
   for cents in range(change+1):
      coinCount = cents
      newCoin = 1
      for j in [c for c in coinList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      minCoins[cents] = coinCount
      coinsUsed[cents] = newCoin
   return minCoins[change]

#This is a function that tracks back through the list of
# coins used in the change algorithm and produces the coins needed to
# make change for that value
# also counts occurences of a particular denomination as suggested by the
# assignment and stores this list of occurences and returns it in usedCurrency.
#This function is a little hacky and could be implemented as a helper function for
# greater readability and encapsulation

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

# function for saving a list of number to an output file
def saveFile(numbers):
    data = open('change.txt', 'a')
    line = (" ".join(str(i) for i in numbers))
    data.write("%s\n" % line)

#function for saving a single integer to an output file
def saveFileInt(number):
    data = open('change.txt', 'a')
    data.write("%s\n" % number)

def main():
    data = open("amount.txt","r")
    for index, line in enumerate(data.readlines()):             #enumerate formatted lines in input txt file
        value = 0
        if (index +1) %2 == 1:                                  #if first line or odd line process as a list of denominations
                denominations = [int(i) for i in line.split()]
        if (index +1) %2 == 0:                                  #if second line or even line process single amount value
            value = int(line)
        if value != 0:                                          #if a value has been found process that value with the denominations list
                                                                # with the change function. save results to file

            saveFile(denominations)
            saveFileInt(value)

            coinsUsed = [0]*(value+1)
            minCoins = [0]*(value+1)

            result = changeDP(denominations,value,minCoins,coinsUsed)
            usedCurrency=changeCounter(coinsUsed,denominations,result)

            saveFile(usedCurrency)
            saveFileInt(result)


main()