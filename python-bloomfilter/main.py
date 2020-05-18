import random
from datetime import datetime
from sortedcontainers import SortedList
from pybloom import BloomFilter

def readData(fileName): 
    f = open(fileName, "r")
    if f.mode == "r": 
        contents = f.read()
        # print(contents)
        return contents
    f.close()
 
def generateTestData(queryPositivePercentage, querySize, sampleSize, maxUniverse): 
    uncompressedList = []
    queryList = SortedList([])
    negativeList = []
    samplePercentage = sampleSize * 100 / maxUniverse
    queryPercentage = querySize * 100 / sampleSize
    random.seed(datetime.now())
    for x in range(1, maxUniverse): 
        if (random.randint(1, 100) <= samplePercentage): 
            uncompressedList.append(x)
            if (random.randint(1, 100) <= queryPercentage): 

                if (random.randint(1, 100) <= queryPositivePercentage): 
                    queryList.add(x)
                elif (len(negativeList) > 0): 
                    # you add some random element from the negative list
                    randomIndex = random.randrange(len(negativeList))
                    queryList.add(negativeList.pop(randomIndex))
        else: 
            negativeList.append(x)
    return (uncompressedList, list(queryList.islice(0, len(queryList))))

def main(): 
    uncompressedList, queryList = generateTestData(20, 1000, 100000, 10000000)
    # print(uncompressedList)
    # print("\n\n\n\n\n\n")
    # print(queryList)
    print(len(uncompressedList), len(queryList))
    f = BloomFilter(capacity=1000, error_rate=0.001)
    for x in range(10): 
        f.add(x)
    print(10 in f)
    print(5 in f)

if __name__ == '__main__':
    main()