import random
from datetime import datetime
from sortedcontainers import SortedList

# generate test data: 
def generateTestData(queryPositivePercentage, sampleSize, maxUniverse): 
    uncompressedList = []
    queryList = SortedList([])
    negativeList = []
    samplePercentage = sampleSize / maxUniverse * 100
    random.seed(datetime.now())
    for x in range(1, maxUniverse): 
        if (random.randint(1, 100) <= samplePercentage): 
            uncompressedList.append(x)
            if (random.randint(1, 100) <= queryPositivePercentage): 
                queryList.append(x)
            elif (len(negativeList) > 0): 
                # you add some random element from the negative list
                randomIndex = random.randrange(len(negativeList))
                queryList.add(negativeList.pop(randomIndex))
        else: 
            negativeList.append(x)
    return (uncompressedList, list(queryList.islice(0, len(queryList))))

            