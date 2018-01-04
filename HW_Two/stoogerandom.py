import random
import time

def load_file(fname):
    with open(fname) as inf:
        data = [[int(i) for i in line.split()] for line in inf]
    return data

# stoogesort algorithm sourced and modified from ispycode.com

def stoogeSort(L):
    stoogeSortRec(L, 0, len(L))

def stoogeSortRec(L, i, j):
    if L[j-1] < L[i]:
        tmp = L[i]
        L[i] = L[j-1]
        L[j-1] = tmp
    if j-i >= 3:
        t = (j-i) // 3
        stoogeSortRec(L, i, j-t)
        stoogeSortRec(L, i+t, j)
        stoogeSortRec(L, i, j-t)


def sample_wr(population, k):
    n = len(population)
    _random, _int = random.random, int
    result = [None] * k
    for i in xrange(k):
        j = _int(_random() * n)
        result[i] = population[j]
    return result

def main():

    sizes = [10,20,30,40,50,60,70,80,90,100]
    for index in range(0,len(sizes)):
        print sizes[index]
        numbers = sample_wr(xrange(0,10000),sizes[index])
        start_time = time.clock()
        stoogeSort(numbers)
        print("---%s seconds---" % (time.clock() - start_time))

main()